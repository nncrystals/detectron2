# generate the input and output file based on timestamp check
import os
import logging
import pickle


class DependenceGenerator:
    def __init__(self, input_file, output_file):
        self.output_file = output_file
        self.input_file = input_file

    def make(self):
        """
        User entry
        :return:
        """
        if self.is_newer(self.input_file, self.output_file):
            self.generate()
            logging.info(f"Generate {self.input_file}")
        else:
            logging.info(f"Skip {self.input_file}")

    def is_newer(self, new, old):
        """
        Determine whether `generate` should be executed.
        :param new: path to a file
        :param old: path to a file
        :return:
        """
        if not os.path.exists(new):
            raise FileNotFoundError(new)
        if not os.path.exists(old):
            return True

        return os.path.getctime(new) > os.path.getctime(old)

    def generate(self):
        """
        Actual file generation function
        :return:
        """
        pass


class RegistryDependenceGenerator(DependenceGenerator):

    def __init__(self, input_file, registry_path="/tmp/dependency_registry.pkl"):
        self.registry_path = registry_path
        self.input_file = input_file
        if not os.path.exists(registry_path):
            with open(self.registry_path, "wb") as f:
                pickle.dump({}, f)
        super().__init__(input_file, None)

    def is_newer_than_registry(self, new):
        with open(self.registry_path, "rb") as f:
            r = pickle.load(f)
        ret = False
        if new in r:
            if os.path.getmtime(new) > r[new]:
                ret = True
        else:
            ret = True

        if ret:
            r[new] = os.path.getmtime(new)
            with open(self.registry_path, "wb") as f:
                pickle.dump(r, f)
        return ret

    def make(self):
        if self.is_newer_than_registry(self.input_file):
            logging.info(f"Generate {self.input_file}")
            self.generate()
        else:
            logging.info(f"Skip {self.input_file}")


class PySide2ResourceGenerator(DependenceGenerator):
    RCC = "pyside2-rcc"

    def __init__(self, input_file, output_file=None):
        if output_file is None:
            output_file, _ = os.path.splitext(input_file)
            output_file += "_rc.py"
        super().__init__(input_file, output_file)

    def generate(self):
        import subprocess as sp
        try:
            sp.check_output([self.RCC, self.input_file, "-o", self.output_file])
        except sp.CalledProcessError as exc:
            raise RuntimeWarning(f"Error {exc.returncode}: {exc.stderr}")


class PySide2FormGenerator(DependenceGenerator):
    UIC = "pyside2-uic"

    def __init__(self, input_file, output_file=None):
        if output_file is None:
            output_file, _ = os.path.splitext(input_file)
            output_file += ".py"
        super().__init__(input_file, output_file)

    def generate(self):
        import subprocess as sp
        try:
            sp.check_output([self.UIC, self.input_file, "-o", self.output_file])
        except sp.CalledProcessError as exc:
            raise RuntimeWarning(f"Error {exc.returncode}: {exc.stderr}")


class FlatbuffersGenerator(RegistryDependenceGenerator):
    flatc = "flatc"

    def __init__(self, input_file, output_dir=None):
        if output_dir is None:
            output_dir = os.path.dirname(input_file)
        self.output_dir = output_dir
        super().__init__(input_file)

    def generate(self):
        import subprocess as sp
        import sys
        try:
            sp.check_output([self.flatc, "--python", "-o", os.path.dirname(self.output_dir), self.input_file],
                            stderr=sp.PIPE)
        except sp.CalledProcessError as exc:
            raise RuntimeWarning(f"Error {exc.returncode}: {exc.stdout.decode(sys.getfilesystemencoding())}")
