from colorama import Fore as F, Style as S
from os import system, listdir
from os.path import exists
from time import time
from platform import system as platform_name
import matplotlib.pyplot as plt
import numpy as np

from config import cfg, j2


def lin_ls(x, y) -> tuple:
    xy = np.mean(x * y)
    x1y = np.mean(x) * np.mean(y)
    x2 = np.mean(x * x)
    x12 = np.mean(x) ** 2
    y2 = np.mean(y * y)
    y12 = np.mean(y) ** 2
    k = (xy - x1y) / (x2 - x12)
    b = np.mean(y) - k * np.mean(x)
    s_k = np.sqrt(1 / x.size) * np.sqrt((y2 - y12) / (x2 - x12) - k ** 2)
    s_b = s_k * np.sqrt(x2 - x12)
    return k, s_k, b, s_b


def handle(c: list[str], settings_link: dict[str, ...]):
    try:
        if len(c) == 0:
            return


        if c[0] == 'menu':
            print(F.CYAN + "== MENU ==")
            print(F.LIGHTBLUE_EX + "exit")
            print(F.LIGHTBLUE_EX + "menu")
            print(F.LIGHTBLUE_EX + "help [<command>]")
            print(F.LIGHTBLUE_EX + "settings read | set <key> <value>")
            print(F.LIGHTBLUE_EX + "filter <filename> [<coefficient>]")
            print(F.LIGHTBLUE_EX + "call <call-string>")
            print(F.LIGHTBLUE_EX + " > sort <name> <filename> <array_type> <graph_name>")
            print(F.LIGHTBLUE_EX + " > render <filename> <scale_type> [<color>]")
            print(F.LIGHTBLUE_EX + " > combine {<filename_1> <filename_2> ...} <scale_type> {<color_1> <color_2> ...}")
            print(F.LIGHTBLUE_EX + " > approx_log_2 <filename> [<color>]")
            print(F.LIGHTBLUE_EX + " > script <filename>")
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

        elif c[0] == 'help':
            if len(c) > 1:
                command = ' '.join(c[1:])
                if command == 'exit':
                    print(F.CYAN + S.NORMAL + "turns off the program")
                elif command == 'menu':
                    print(F.CYAN + S.NORMAL + "prints a menu (as above)")
                elif command == 'help':
                    print(F.YELLOW + S.BRIGHT + "this", F.CYAN + S.NORMAL + "page")
                elif command == 'settings':
                    print(F.CYAN + S.NORMAL + "operations with project settings: reading/rewriting values")
                elif command == 'filter':
                    print(F.CYAN + S.NORMAL + "clears noise in the selected datafile by the cleaning coefficient (default: in settings)")
                elif command == 'call':
                    print(F.CYAN + S.NORMAL + "calls a script or a command:")
                    print(F.CYAN + S.DIM + " >", F.CYAN + S.BRIGHT + "sort")
                    print(
                        F.GREEN + S.DIM + "  > " + S.NORMAL + "launches sorting algorithm with following parameters (delta length is max additional value that",
                        F.GREEN + S.NORMAL + "forms an array of lengths for generated int arrays: checked length with L and dL will be " +\
                        F.BLUE + "[L, L+dL)" + F.GREEN + ")",
                        sep='\n'
                    )

                    print(F.CYAN + S.DIM + " >", F.CYAN + S.BRIGHT + "render")
                    print(F.GREEN + S.DIM + "  > " + S.NORMAL + "renders a plot from a datafile with given name and parameters")

                    print(F.CYAN + S.DIM + " >", F.CYAN + S.BRIGHT + "combine")
                    print(F.GREEN + S.DIM + "  > " + S.NORMAL + "renders a plot from 2 or more datafile with given names and parameters")

                    print(F.CYAN + S.DIM + " >", F.CYAN + S.BRIGHT + "approx_log_2")
                    print(F.GREEN + S.DIM + "  > " + S.NORMAL + "approximates data from file and counts coeffs of poly-2")

                    print(F.CYAN + S.DIM + " >", F.CYAN + S.BRIGHT + "script")
                    print(F.GREEN + S.DIM + "  > " + S.NORMAL + "loads prepared script from a file")
            else:
                print(F.CYAN + S.NORMAL + "use", F.YELLOW + S.BRIGHT + "help <command>", F.CYAN + S.NORMAL + "to see info")

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

        elif c[0] == 'filter':
            filename = c[1]
            if len(c) > 2:
                k = c[2]
                k = float(k) if k.find('%') == -1 else float(k[:-1]) / 100
            else:
                k = settings_link["filter_coefficient"]

            with open(filename) as csv:
                first_line = csv.readline()
                x, y = list(), list()
                for line in csv.readlines():
                    line = line.split(',')
                    x.append(int(line[0]))
                    y.append(int(line[1]))

            print(F.LIGHTBLACK_EX + f"before filtration: length   = {len(y)}")
            print(F.LIGHTBLACK_EX + f"                   mean     = {np.mean(y)}")
            print(F.LIGHTBLACK_EX + f"                   variance = {np.var(y)}")
            print(F.LIGHTBLACK_EX + f"                   max      = {max(y)}")
            print(F.LIGHTBLACK_EX + f"                   min      = {min(y)}")

            i = 0
            while y[i] == 0:
                i += 1
            i = max(100, i < len(x) / 20, i + 1)
            y_filtered = list()
            while i < len(x):
                if y[i] != 0 and y[i - 1] / y[i] >= k:
                    x.pop(i)
                    y_filtered.append(y.pop(i))
                    i -= 1
                i += 1

            print(F.LIGHTBLACK_EX + f"after filtration:  length   = {len(y)}")
            print(F.LIGHTBLACK_EX + f"                   mean     = {np.mean(y)}")
            print(F.LIGHTBLACK_EX + f"                   variance = {np.var(y)}")
            print(F.LIGHTBLACK_EX + f"                   max      = {max(y)}")
            print(F.LIGHTBLACK_EX + f"                   min      = {min(y)}")
            print(F.LIGHTBLACK_EX + f"filtered values: {', '.join(map(str, [_ for _ in y_filtered][:10]))}"
                                    f"{', ...' if len(y_filtered) > 10 else ('' if len(y_filtered) > 0
                                                                             else '<nothing>')}")

            slash_position = filename.rfind("/")
            dir_path, filename = filename[:slash_position + 1], filename[slash_position + 1:]
            filename = dir_path + "filtered_" + filename
            with open(filename, 'w') as csv:
                csv.write(first_line)
                for i in range(len(x)):
                    print(x[i], y[i], file=csv, sep=',')
            print(F.GREEN + "Successfully saved at", F.YELLOW + S.DIM + filename)

        elif c[0] == 'call':
            if len(c) < 2:
                raise IndexError("not enough args")

            if c[1] == 'sort':
                sort = c[2]
                if sort not in listdir(cfg.PATH.BIN_local):
                    raise ValueError("bad sort name")

                print(F.LIGHTBLACK_EX + "> generating starting config...")

                output_file_name = c[3]
                right_dot_marker = output_file_name.rfind('.')
                if output_file_name[right_dot_marker:] == '.csv':
                    output_file_name = output_file_name[right_dot_marker:]

                array_type = int(c[4])
                graph_name = ' '.join(c[5:]).replace(' ', '_')  # энкодим пробелы, чтобы не думать сильно
                if len(graph_name) == 0:
                    raise IndexError("not enough iterations provided: 0")

                x_axis = 'length,_elements'    # аналогичный энкодинг
                y_axis = 'time,_ns'

                with open("data/input.csv", 'w', encoding='utf8') as input_file:
                    print(output_file_name, graph_name, x_axis, y_axis,
                          settings_link['length'], settings_link["max"], settings_link["min"],
                          array_type, settings_link["delta"],
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
                filename = c[2]
                scale = c[3].lower()
                color = c[4] if len(c) > 4 else '#fa8072'

                print(F.LIGHTBLACK_EX + "reading a datafile...")
                with open(filename) as csv:
                    legend = list(map(lambda s: s.replace('_', ' '), csv.readline().strip()[1:].split('\t')))
                    x, y = list(), list()
                    for line in csv.readlines():
                        line = line.split(',')
                        x.append(int(line[0]))
                        y.append(int(line[1]))

                print(F.LIGHTBLACK_EX + "rendering...")
                plt.figure(figsize=(settings_link["plot_fig_x"], settings_link["plot_fig_y"]))
                plt.scatter(x, y, color=color, s=settings_link["plot_dot_size"])
                plt.xscale(scale)
                plt.yscale(scale)
                plt.title(legend[0])
                plt.xlabel(legend[1])
                plt.ylabel(legend[2])
                plt.grid(True, alpha=.3)
                save_file = filename.replace('.csv', '.png')
                plt.savefig(save_file)
                plt.close()
                print(F.GREEN + "Successfully saved at", F.YELLOW + S.DIM + save_file)

            elif c[1] == 'combine':
                i = 2
                filenames = [c[i][1:]]
                i += 1
                while i < len(c) and c[i].count('}') == 0:
                    filenames.append(c[i])
                    i += 1
                filenames.append(c[i][:-1])
                if len(filenames) < 2:
                    raise IndexError("less then 2 subplots")

                i += 1
                scale = c[i].lower()
                i += 1
                colors = [c[i][1:]]+ c[i+1:i+len(filenames)-1] + [c[i+len(filenames)-1][:-1]]

                plt.figure(figsize=(settings_link["plot_fig_x"], settings_link["plot_fig_y"]))

                with open(filenames[0]) as csv:
                    global_legend = list(map(lambda s: s.replace('_', ' '), csv.readline().strip()[1:].split('\t')))
                    x_global, y = list(), list()
                    for line in csv.readlines():
                        line = line.split(',')
                        x_global.append(int(line[0]))
                        y.append(int(line[1]))
                print(F.LIGHTBLACK_EX + f"rendering #{0}: x_global={len(x_global)}, y={len(y)}")
                plt.scatter(x_global, y, color=colors[0], s=settings_link["plot_dot_size"], label=global_legend[0])

                for j in range(1, len(filenames)):
                    with open(filenames[j]) as csv:
                        legend = list(map(lambda s: s.replace('_', ' '), csv.readline().strip()[1:].split('\t')))
                        y = list()
                        for line in csv.readlines():
                            line = line.split(',')
                            y.append(int(line[1]))
                    print(F.LIGHTBLACK_EX + f"rendering #{j}: [x_global], y={len(y)}")
                    plt.scatter(x_global, y, color=colors[j], s=settings_link["plot_dot_size"], label=legend[0])
                plt.xscale(scale)
                plt.yscale(scale)
                plt.title("merged plots")
                plt.legend()
                plt.xlabel(global_legend[1])
                plt.ylabel(global_legend[2])
                plt.grid(True, alpha=.3)
                save_file = f"combined_{int(time())}.png"
                plt.savefig(save_file)
                plt.close()
                print(F.GREEN + "Successfully saved at", F.YELLOW + S.DIM + save_file)

            elif c[1] == 'approx_log_2':
                filename = c[2]
                color = c[3] if len(c) > 3 else '#fa8072'

                print(F.LIGHTBLACK_EX + "reading a datafile...")
                with open(filename) as csv:
                    legend = list(map(lambda s: s.replace('_', ' '), csv.readline().strip()[1:].split('\t')))
                    x, y = list(), list()
                    for line in csv.readlines():
                        line = line.split(',')
                        current_x, current_y = int(line[0]), int(line[1])
                        if current_x > 1 and current_y > 1:
                            x.append(current_x)
                            y.append(current_y)
                x_ln = np.log(np.array(x))
                y_ln = np.log(np.array(y))
                x_label = "ln(" + legend[1][:legend[1].rfind(',')] + ")"
                y_label = "ln(" + legend[2][:legend[2].rfind(',')] + ")"

                k, s_k, b, s_b = lin_ls(x_ln, y_ln)
                x_fit = np.linspace(x_ln.min(), x_ln.max(), 100)
                y_fit = k * x_fit + b

                print(F.LIGHTBLACK_EX + "rendering...")
                plt.figure(figsize=(settings_link["plot_fig_x"], settings_link["plot_fig_y"]))
                plt.scatter(x_ln, y_ln, color=color, s=settings_link["plot_dot_size"])
                plt.plot(x_fit, y_fit, color='black', ms=15, label=f'LLS: k = {k:.3f}, σ = {s_k:.3f}')
                plt.xscale('linear')
                plt.yscale('linear')
                plt.title(legend[0])
                plt.legend()
                plt.xlabel(x_label)
                plt.ylabel(y_label)
                plt.grid(True, alpha=.3)
                save_file = filename.replace('.csv', '') + "_approximated.png"
                plt.savefig(save_file)
                plt.close()
                print(F.GREEN + "Successfully saved at", F.YELLOW + S.DIM + save_file)

            elif c[1] == 'script':
                filename = ' '.join(c[2:])
                if not exists(filename):
                    filename += '.scrpt'
                with open(filename, encoding='utf8') as script:
                    for line in script.readlines():
                        line = line.strip()
                        print(F.LIGHTBLACK_EX + "$ received:", line)
                        handle(line.split(), settings_link)

        else:
            raise ValueError("parsing failed")

        print()
    except Exception as e:
        args = list(e.args)
        print(
            F.RED + S.DIM + "something went wrong:",
            F.YELLOW + S.NORMAL + f"[{e.__class__.__name__}]: \"{', '.join(list(map(str, args))) if len(args) > 0 else '<no args>'}\""
        )
