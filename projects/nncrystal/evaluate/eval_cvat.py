import argparse
import json
import os

from detectron2.config import get_cfg
from detectron2.data.datasets import register_coco_instances
from cvat.api import CVATAPI
from training.train_cvat import strip_annotation
from evaluate.performance import evaluate_on_dataset

def remap_annotation(coco_json, remap_map):
    for ann in coco_json["annotations"]:
        ann["category_id"] = remap_map[ann["category_id"]]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--job_id", action="append")
    parser.add_argument("--config", required=True)
    parser.add_argument("--cvat_host", default="http://localhost:8080")
    parser.add_argument("--cvat_username")
    parser.add_argument("--cvat_password")
    parser.add_argument("--output_dir", default="./eval_output")
    parser.add_argument("--cvat_base")
    parser.add_argument("--weights")
    parser.add_argument("--mapping", help="[old_id, new_id]")
    args = parser.parse_args()

    cfg = get_cfg()
    cfg.merge_from_file(args.config)

    api = CVATAPI(args.cvat_host)
    api.login(args.cvat_username, args.cvat_password)

    eval_tasks = []
    for job_id in args.job_id:
        job = api.get_job(job_id).json()
        task_id = job["task_id"]

        data = api.export_data(task_id).json()
        if args.mapping is not None:
            mapping = json.loads(args.mapping)
            mapping = {mapping[0]: mapping[1]}
            remap_annotation(data, mapping)


        coco_json = f"datasets/eval_cvat_{task_id}.coco.json"
        with open(coco_json, "w") as f:
            json.dump(data, f)
        eval_task = f"cvat/eval_{task_id}"
        register_coco_instances(eval_task, {}, coco_json, args.cvat_base)
        eval_tasks.append(eval_task)

    for eval_task in eval_tasks:
        os.makedirs(args.output_dir, exist_ok=True)

    evaluate_on_dataset(args.config, ['MODEL.WEIGHTS', args.weights], eval_tasks)
