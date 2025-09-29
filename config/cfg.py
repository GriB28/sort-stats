from os import getcwd


class PATH:
    CWD = getcwd()

    CONFIG = CWD + "/config/"
    SETTINGS = CONFIG + "settings.json"

    IMAGE = CWD + "/img/"

    BIN = CWD + "/bin/"
    BIN_local = "bin/"


BINARIES = (
    PATH.BIN + "bubble_0",
    #PATH.BIN + "insertion",
    #PATH.BIN + "selection",
    #PATH.BIN + "merge",
    #PATH.BIN + "hoar",
    #PATH.BIN + "quick"
)
POSSIBLE_SORTS = ("bubble_0", "bubble_1", "bubble_2", "insertion", "selection", "merge", "hoar", "quick")
