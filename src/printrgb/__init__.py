import sys
from .printrgb import print_rgb # type: ignore

__all__ = ["print_rgb", "printrgb"]
__version__ = "1.2.4"

printrgb = print_rgb()

if __name__ == "__main__":
    printrgb("".join(map(str, sys.argv[1:])), rainbow=1)
    printrgb(sys.stdin.read(), rainbow=1)