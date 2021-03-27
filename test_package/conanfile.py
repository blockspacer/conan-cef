from conans import ConanFile, CMake, tools
import os


class CefTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["NO_BROWSER_WORKING_TEST"] = "1"
        cmake.configure()
        cmake.build()

    #    if self.settings.os == "Macos":
    #        self.run("cd bin; for LINK_DESTINATION in $(otool -L client | grep libproto | cut -f 1 -d' '); do install_name_tool -change \"$LINK_DESTINATION\" \"@executable_path/$(basename $LINK_DESTINATION)\" client; done")

    #def imports(self):
        #self.copy("*", "bin", "bin")

    def test(self):
        if not tools.cross_building(self.settings):
            bin_path = os.path.join("bin", "cefsimple")
            # TODO: requires data files to run
            # cp -r ~/.conan/data/cef/3.3683.1920.g9f41a27/master/stable/build/xxx/source_subfolder/Resources/* ~/conan-cef/test_package/build/xxx/bin/
            # self.run(bin_path, run_environment=True)
