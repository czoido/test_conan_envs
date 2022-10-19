from io import StringIO
import os

from conan import ConanFile

class ConanRecipe(ConanFile):
    name = "myproject"
    version = "1.0"

    def build_requirements(self):
        self.build_requires("mybin/1.0")
    
    def build(self):
        mybuf = StringIO()
        self.run("mybin", output=mybuf)
        print(mybuf.getvalue())
        assert "---------- mybin -----------" in mybuf.getvalue()