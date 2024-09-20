import os

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.tools.files import copy
from conan.tools.build import can_run


COMPONENT_STUFF_LIB = "stuff"
COMPONENT_STUFF_TOOL = "stufftool"


class TestEnvPrj(ConanFile):

    name = "stuff"
    version = "1.0.0"
    # package_type = "application"
    # package_type = "library"
    package_type = "unknown"
    settings = "os", "compiler", "build_type", "arch"

    options = {"shared": [True, False]}
    default_options = {"shared": False}

    exports_sources = "CMakeLists.txt", "src/*"

    tool_requires = "cmake/[^3]"

    generators = [
        "CMakeToolchain",
        "VirtualBuildEnv",
        "VirtualRunEnv",
    ]

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if can_run(self):
            cmake.test()

    def package(self):
        copy(self,
            pattern="*",
            src=os.path.join(self.source_folder, 'src/lib/stuff/include'),
            dst=os.path.join(self.package_folder, 'include'),
        )
        copy(self,
            pattern="*/stuff_export.h",
            src=os.path.join(self.build_folder),
            dst=os.path.join(self.package_folder, 'include'),
            keep_path=False,
        )
        if self.settings.os == "Windows":
            copy(self,
                pattern="*/stuff.lib",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'lib'),
                keep_path=False,
            )
            copy(self,
                pattern="*/stuff.dll",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'bin'),
                keep_path=False,
            )
            copy(self,
                pattern="*/stuff.pdb",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'bin'),
                keep_path=False,
            )
            copy(self,
                pattern="*/stufftool.exe",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'bin'),
                keep_path=False,
            )
            copy(self,
                pattern="*/stufftool.pdb",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'bin'),
                keep_path=False,
            )
        else:
            copy(self,
                pattern="*/libstuff.a",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'lib'),
                keep_path=False,
            )
            copy(self,
                pattern="*/libstuff.dylib",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'lib'),
                keep_path=False,
            )
            copy(self,
                pattern="*/stufftool",
                src=self.build_folder,
                dst=os.path.join(self.package_folder, 'bin'),
                keep_path=False,
            )

    def package_info(self):
        self.cpp_info.components[COMPONENT_STUFF_LIB].libs = [COMPONENT_STUFF_LIB]
        self.cpp_info.components[COMPONENT_STUFF_LIB].includedirs = ['include']

        self.cpp_info.components[COMPONENT_STUFF_TOOL].bindirs = ['bin']
        self.cpp_info.components[COMPONENT_STUFF_TOOL].requires = [COMPONENT_STUFF_LIB]

        self.cpp_info.bindirs = ['bin']

        # self.runenv_info.append_path("PATH", os.path.join(self.package_folder, 'bin'))
