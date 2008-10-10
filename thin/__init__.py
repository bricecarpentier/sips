import os.path
from ctypes import CDLL

LIB_NAME = 'libsips.so'

LIB_FILE = os.path.normpath(
    "%s%s%s%s%s" % (
        os.path.abspath(os.path.dirname(__file__)),
        os.path.sep,
        os.path.pardir,
        os.path.sep,
        LIB_NAME
    )
)

lib = CDLL(LIB_FILE)