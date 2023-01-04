# mac m1 install greenlet

## error
```
      clang -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -iwithsysroot/System/Library/Frameworks/System.framework/PrivateHeaders -iwithsysroot/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/Headers -arch arm64 -arch x86_64 -Werror=implicit-function-declaration -I/opt/homebrew/opt/openssl@1.1/include -I/opt/homebrew/opt/openssl@3/include -I/Users/rey/.virtualenvs/dxwatch-api/include -I/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/Headers -c src/greenlet/greenlet.cpp -o build/temp.macosx-10.9-universal2-cpython-39/src/greenlet/greenlet.o --std=gnu++11
      src/greenlet/greenlet.cpp:16:10: fatal error: 'Python.h' file not found
      #include <Python.h>
               ^~~~~~~~~~
      1 error generated.
      error: command '/usr/bin/clang' failed with exit code 1
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure

× Encountered error while trying to install package.
╰─> greenlet
```

## solution
```
export CPLUS_INCLUDE_PATH=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Headers
export C_INCLUDE_PATH=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Headers

```