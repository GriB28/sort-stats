from os import getcwd


class PATH:
    CWD = getcwd()

    CONFIG = CWD + "/config/"
    SETTINGS = CONFIG + "settings.json"

    IMAGE = CWD + "/img/"

    BIN = CWD + "/bin/"
    BIN_local = "bin/"


BINARIES_LINUX = (
    PATH.BIN + "bubble_0",
    PATH.BIN + "bubble_1",
    PATH.BIN + "bubble_2",
    PATH.BIN + "insertion",
    PATH.BIN + "selection",
    PATH.BIN + "merge",
    PATH.BIN + "heap",
    PATH.BIN + "quick"
)
BINARIES_WINDOWS = (
    PATH.BIN + "bubble_0.exe",
    PATH.BIN + "bubble_1.exe",
    PATH.BIN + "bubble_2.exe",
    PATH.BIN + "insertion.exe",
    PATH.BIN + "selection.exe",
    PATH.BIN + "merge.exe",
    PATH.BIN + "heap.exe",
    PATH.BIN + "quick.exe"
)
POSSIBLE_SORTS = ("bubble_0", "bubble_1", "bubble_2", "insertion", "selection", "merge", "heap", "quick")
