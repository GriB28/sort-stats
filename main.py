from colorama import Fore as F, Style as S, init as c_init
from os import system, mkdir
from os.path import exists

from config import cfg, j2

c_init(autoreset=True)


print(F.LIGHTBLACK_EX + S.DIM + "checking for binaries...", end=' ')
if all(exists(path) for path in cfg.BINARIES):
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
    try:
        if c[0] == 'menu':
            is_wrong_args = False
            print(F.CYAN + "== MENU ==")
            print(F.LIGHTBLUE_EX + "exit                             ",
                  ">", F.GREEN + S.BRIGHT + "exit")
            print(F.LIGHTBLUE_EX + "menu                             ",
                  ">", F.YELLOW + S.BRIGHT + "this " + F.GREEN + "menu")
            print(F.LIGHTBLUE_EX + "settings read | set <key> <value>",
                  ">", F.GREEN + S.BRIGHT + "settings (literally)")
            print(F.LIGHTBLUE_EX + "sort <name>                      ",
                  ">", F.GREEN + S.BRIGHT + "launch sorting algorithm")
            print(F.LIGHTBLUE_EX + "render <name>                    ",
                  ">", F.GREEN + S.BRIGHT + "render a plot of algorithm with given name")
            print(
                " >",
                F.GREEN + "possible names:",
                (S.RESET_ALL + ', ').join(
                    F.YELLOW + S.BRIGHT + name
                    for name in cfg.POSSIBLE_SORTS
                )
            )
            print(F.LIGHTBLUE_EX + "call <script>                    ",
                  ">", F.GREEN + S.BRIGHT + "script")
            print()


        elif c[0] == 'settings':
            if c[1] == 'read':
                print(F.LIGHTBLACK_EX + S.NORMAL + str(cfg.PATH.SETTINGS))
                print(F.LIGHTBLACK_EX + S.NORMAL + str(settings))
            elif c[1] == 'set':
                key = c[2]
                if key in settings.keys():
                    value = ' '.join(c[3:])
                    if value == 'false':
                        value = False
                    elif value == 'true':
                        value = True
                    elif value == 'none' or value == 'null':
                        value = None
                    else:
                        try:
                            value = int(value)
                        except:
                            try:
                                value = eval(value)
                            except:
                                raise ValueError("parsing error")
                    if type(value) is type(settings[key]) or value is None or settings[key] is None:
                        settings[key] = value
                        with open(cfg.PATH.SETTINGS, 'w', encoding='utf8') as f:
                            f.write(j2.to_(settings))
                        print(F.LIGHTBLACK_EX + S.NORMAL + "> setting updated")
                    else:
                        print(F.RED + S.DIM + "> bad types")
                else:
                    raise KeyError("key was not found")
            else:
                raise ValueError("unknown argument")


        elif c[0] == 'sort':
            if len(c) == 0:
                raise IndexError("no args")
            sort = c[1]
            if sort not in cfg.POSSIBLE_SORTS:
                raise ValueError("bad sort name")

            print(F.LIGHTBLACK_EX + "> generating starting config...")
            with open("data/input.csv", 'w') as input_file:
                print(settings['length'], settings["max_abs"], -settings["max_abs"], file=input_file)

            print(F.LIGHTBLACK_EX + "> calculating...")
            system(f"./{cfg.PATH.BIN_local}{sort}")
            print(F.LIGHTBLACK_EX + "> finished...")

        else:
            raise ValueError("parsing failed")


    except Exception as e:
        args = list(e.args)
        print(
            F.RED + S.DIM + "something went wrong:",
            F.YELLOW + S.NORMAL + f"[{e.__class__.__name__}]: \"{args if len(args) > 0 else '<no args>'}\""
        )
    c = list()
    while len(c) == 0:
        c = input(F.GREEN + ">>> " + S.RESET_ALL).strip().lower().split()

print(F.LIGHTBLACK_EX + "finishing...")
