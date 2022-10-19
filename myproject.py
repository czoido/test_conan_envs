import os

from conan import ConanFile

class ConanRecipe(ConanFile):
    name = "myproject"
    version = "1.0"

    def build_requirements(self):
        self.build_requires("mybin/1.0")
    
    def build(self):
        self.run("which -a mybin")
        self.run("mybin")
