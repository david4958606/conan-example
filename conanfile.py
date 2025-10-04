import os
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy, get


class CompressorRecipe(ConanFile):
    
    settings = "os", "compiler", "build_type", "arch"

    options = {"shared": [True, False]}
    default_options = {"shared": True}

    
    def requirements(self):
        self.requires("zlib/1.3.1", options={"shared": self.options.shared})
        self.requires("fmt/11.1.3", options={"shared": self.options.shared})

    def layout(self):
        cmake_layout(self)
    
    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self, generator="Ninja")
        tc.generate()
        if self.settings.get_safe("build_type") == "Debug":
            bin_folder = os.path.join(self.source_folder, "bin", "Debug")
        else:
            bin_folder = os.path.join(self.source_folder, "bin", "Release")
        if self.options.shared:
            print("Option SHARED is enabled")
            if self.settings.get_safe("os") == "Windows":
                for dep in self.dependencies.values():
                    for so in dep.cpp_info.bindirs:
                        print(f"Adding Shared Libraries to bin folder {bin_folder}")
                        copy(self, "*.dll", so, bin_folder)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()