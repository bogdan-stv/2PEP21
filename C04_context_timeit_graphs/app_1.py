import os
from contextlib import contextmanager

@contextmanager
def ip_information(ostype):
    if ostype == "nt":
        print("ceva")
        ip_command = "ipconfig"
    elif ostype == "posix":
        ip_command = "python3 --version"
    obj = os.popen(ip_command)

    try:
        yield obj
    except Exception as e:
        print(e.args)
    finally:
        print("end")

with ip_information("nt") as ip1:
    print(ip1.read())
    raise AttributeError("arg1", "arg2")




