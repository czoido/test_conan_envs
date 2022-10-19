import os

from conans import ConanFile


class ConanRecipe(ConanFile):
    name = "mybin"
    version = "1.0"

    def build(self):
        pass

    def package(self):
        os.makedirs(os.path.join(self.package_folder, "bin"), exist_ok=True)
        self.run("cd %s/bin && echo 'echo ---------- mybin -----------' > mybin; chmod +x mybin" %
                 self.package_folder)

    def package_info(self):
        bindir = os.path.join(self.package_folder, "bin")
        self.buildenv_info.prepend_path("PATH", bindir)
        self.cpp_info.bindirs = []
