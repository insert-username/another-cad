from conans import ConanFile, CMake, tools


class AnotherCadConan(ConanFile):
    name = "another-cad"
    version = "0.0.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of AnotherCad here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    scm = {
        "type": "git",  # Use "type": "svn", if local repo is managed using SVN
         "url": "auto",
        "revision": "auto",
    } 

    def requirements(self):
        self.requires("sfml/2.5.1@bincrafters/stable")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("*", dst="bin", src="bin")

