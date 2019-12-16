import io
import os
import pickle
import zipfile

import typing

PROJECT_FILE_NAME = "project.pkl"


class Configuration:
    def __init__(self):
        self.name = ""
        self.fd = ""
        self.description = ""


class ConfigurationManager:
    def __init__(self, runtime):
        self.configurations = []
        self.runtime = runtime

    def check_integrity(self):
        return True

    def append(self, config: Configuration):
        pass



class RuntimeData:
    zipfile: zipfile.ZipFile

    def __init__(self):
        self.project_fd = None
        self.zipfile = None
        self.meta_updated = False
        self.image_updated = False
        self.annotation_updated = False
        self.weights_updated = False


class Project(object):
    PROJECT_FILE_NAME = "project.pkl"

    def __init__(self):
        self.runtime = RuntimeData()

    def save_project(self):
        with self.runtime.zipfile.open(self.PROJECT_FILE_NAME, "w") as f:
            pickle.dump(self, f)
        self.runtime.meta_updated = False

    def save(self):
        if self.runtime.meta_updated:
            self.save_project()

    @staticmethod
    def load(self, project_path):
        if not os.path.exists(project_path):
            raise FileNotFoundError(f"{project_path} does not exist")

        fd = open(project_path, "r+")
        zf = zipfile.ZipFile(fd)

        with zf.open(self.PROJECT_FILE_NAME, "r") as f:
            obj: Project = pickle.load(f)
        obj.runtime.zipfile = zf
        obj.runtime.project_fd = fd

        return obj

    def check_integrity(self):
        return True

    def __getstate__(self):
        state = self.__dict__.copy()
        state.pop("runtime")
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__ = state
        self.runtime = RuntimeData()

    def __del__(self):
        try:
            self.runtime.project_fd.close()
        except:
            pass
