from colorama import Fore as F, Style as S
from os import system
from platform import system as platform_name

from config import cfg, j2


def handle(c: list[str], settings_link: dict[str, ...]):
    print()
    try:
        if c[0] == 'menu':
            print(F.CYAN + "== MENU ==")
            print(F.LIGHTBLUE_EX + "exit                             ",
                  ">", F.GREEN + S.BRIGHT + "exit")
            print(F.LIGHTBLUE_EX + "menu                             ",
                  ">", F.YELLOW + S.BRIGHT + "this " + F.GREEN + "menu")
            print(F.LIGHTBLUE_EX + "settings read | set <key> <value>",
                  ">", F.GREEN + S.BRIGHT + "settings (literally)")
            print(F.LIGHTBLUE_EX + "call <call-string>               ",
                  ">", F.GREEN + S.BRIGHT + "calls one of the following actions:")
            print(F.LIGHTBLUE_EX + " > sort <name> <filename> <array_type> <cycles> <graph_name>",
                  ">", F.GREEN + S.BRIGHT + "launches sorting algorithm with following parameters")
            print(F.LIGHTBLUE_EX + " > render <filename>                                        ",
                  ">", F.GREEN + S.BRIGHT + "renders a plot from a datafile with given name")
            print(F.LIGHTBLUE_EX + " > script <filename>                                        ",
                  ">", F.GREEN + S.BRIGHT + "loads prepared script from a file")
            print()
            print()
            print(
                "|>",
                F.GREEN + "possible sort algorithms' names:",
                (S.RESET_ALL + ', ').join(
                    F.YELLOW + S.BRIGHT + name
                    for name in cfg.POSSIBLE_SORTS
                )
            )
            print()


        elif c[0] == 'settings':
            if c[1] == 'read':
                print(F.LIGHTBLACK_EX + S.NORMAL + str(cfg.PATH.SETTINGS))
                print(F.LIGHTBLACK_EX + S.NORMAL + str(settings_link))
            elif c[1] == 'set':
                key = c[2]
                if key in settings_link.keys():
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
                    if type(value) is type(settings_link[key]) or value is None or settings_link[key] is None:
                        settings_link[key] = value
                        with open(cfg.PATH.SETTINGS, 'w', encoding='utf8') as f:
                            f.write(j2.to_(settings_link))
                        print(F.LIGHTBLACK_EX + S.NORMAL + "> setting updated")
                    else:
                        print(F.RED + S.DIM + "> bad types")
                else:
                    raise KeyError("key was not found")
            else:
                raise ValueError("unknown argument")

        elif c[0] == 'call':
            if len(c) < 2:
                raise IndexError("not enough args")

            if c[1] == 'sort':
                sort = c[2]
                if sort not in cfg.POSSIBLE_SORTS:
                    raise ValueError("bad sort name")

                print(F.LIGHTBLACK_EX + "> generating starting config...")

                output_file_name = c[3]
                right_dot_marker = output_file_name.rfind('.')
                if output_file_name[right_dot_marker:] == '.csv':
                    output_file_name = output_file_name[right_dot_marker:]

                array_type = int(c[4])
                iterations = int(c[5])

                graph_name = ' '.join(c[6:]).replace(' ', '_')  # энкодим пробелы, чтобы не думать сильно
                if len(graph_name) == 0:
                    raise IndexError("not enough iterations provided: 0")

                Ox = 'time,_s'          # аналогичный энкодинг
                Oy = 'length,_elements'

                with open("data/input.csv", 'w', encoding='utf8') as input_file:
                    print(
                        output_file_name, graph_name, Ox, Oy,
                        settings_link['length'], settings_link["max"], settings_link["min"],
                        array_type, iterations,
                        file=input_file)

                print(F.LIGHTBLACK_EX + "> calculating...")
                if platform_name() == 'Linux':
                    system(f"./{cfg.PATH.BIN_local}{sort}")
                elif platform_name() == 'Windows':
                    system(f"{cfg.PATH.BIN_local}{sort}")
                else:
                    print(F.RED + S.DIM + "> current platform is not supported... yet...")
                    exit()
                print(F.LIGHTBLACK_EX + "> finished...")

            elif c[1] == 'render':
                pass

            elif c[1] == 'script':
                filename = ' '.join(c[2:])
                with open(filename, encoding='utf8') as script:
                    for line in script.readlines():
                        line = line.strip()
                        print(F.LIGHTBLACK_EX + "$ received:", line)
                        handle(line.split(), settings_link)

        else:
            raise ValueError("parsing failed")


    except Exception as e:
        args = list(e.args)
        print(
            F.RED + S.DIM + "something went wrong:",
            F.YELLOW + S.NORMAL + f"[{e.__class__.__name__}]: \"{args if len(args) > 0 else '<no args>'}\""
        )
