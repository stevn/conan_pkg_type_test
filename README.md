# conan_pkg_type_test

## Build

Conan build is broken because this package holds a library (static or shared) + a tool:

- When I set `package_type` in root `conanfile.py` to `library`, the header include _works_, but the tool run _doesn't work_.
- When I set `package_type` in root `conanfile.py` to `application`, the header include _doesn't work_, but the tool run _does work_.

```text
$ git clone https://github.com/stevn/conan_pkg_type_test
$ cd conan_pkg_type_test
$ conan create .
...
[100%] Built target stufftestpkg

======== Testing the package: Executing test ========
stuff/1.0.0 (test package): Running test()
stuff/1.0.0 (test package): RUN: ./stufftestpkg
stufftestpkg: It works!

stuff/1.0.0 (test package): RUN: stufftool
/bin/sh: stufftool: command not found

ERROR: stuff/1.0.0 (test package): Error in test() method, line 28
        self.run("stufftool", env="conanrun")
        ConanException: Error 127 while executing
```

Solved by adding run=True to the self.requires() call:

<https://github.com/stevn/conan_pkg_type_test/commit/bd781f1aa229f1c66fd3900c85dd6db5392f2018>
