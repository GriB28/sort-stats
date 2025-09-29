from sys import argv
from colorama import Fore as F, Style as S, init as c_init
c_init(autoreset=False)
print(end=F.LIGHTBLACK_EX + S.DIM)


if argv[1] != "auto":
    print("this script can only be launched from C++ project shell")
    exit()

try:
    legend_file = argv[2]
    data_file = argv[3]
    print("> entered plotmaker")
    print(f"> given args: {argv[1:]}")

    with open(legend_file, encoding='utf8') as legend:
        x_axis_title = legend.readline().strip()
        y_asix_title = legend.readline().strip()
    with open(data_file, encoding='utf8') as data:
        plot_data = data
except IndexError:
    print(
        S.RESET_ALL + F.RED + S.NORMAL + "something went wrong:",
        F.YELLOW + "caught an",
        F.CYAN + "[IndexError]",
        F.YELLOW + "while parsing arguments"
    )
