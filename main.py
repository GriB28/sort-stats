from colorama import Fore as F, Style as S, init as c_init
from os import mkdir
from os.path import exists
from platform import system as platform_name

from config import cfg, j2
from handler import handle

c_init(autoreset=True)

if platform_name() == 'Windows':
    from colorama import just_fix_windows_console
    just_fix_windows_console()


print(F.LIGHTBLACK_EX + S.DIM + "checking for binaries...", end=' ')
if platform_name() == "Linux":
    bins = cfg.BINARIES_LINUX
elif platform_name() == "Windows":
    bins = cfg.BINARIES_WINDOWS
else:
    bins = tuple()
if all(exists(path) for path in bins):
    print(F.GREEN + "[OK]")
else:
    print(F.RED + "[NOT BUILT]")
    exit()

print(F.LIGHTBLACK_EX + S.DIM + "checking for directories...", end=' ')
if exists("data/"):
    print(F.GREEN + "[OK]")
else:
    print(F.RED + "[RESTORED]")
    mkdir("data/")


print("\n\n")
c = ['menu']
settings = j2.fromfile(cfg.PATH.SETTINGS)
while c[0] != 'exit':
    handle(c, settings)
    c = list()
    while len(c) == 0:
        c = input(F.GREEN + ">>> " + S.RESET_ALL).strip().split()

print(F.LIGHTBLACK_EX + "finishing...")
