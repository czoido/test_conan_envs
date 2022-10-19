conan create mybin.py
conan create sysroot.py
conan create myproject.py -pr:h=./profile -pr:b=default -c tools.env.virtualenv:auto_use=True