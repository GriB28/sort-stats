<div align="center">

# [sort-stats](https://github.com/GriB28/sort-stats)
## Исследование алгоритмов сортировки массивов разной асимптотики
#### 1 курс ФАКТ МФТИ

</div>

#
### ✅ Запуск проекта (Linux)
1. Установка библиотек: `python3 -m pip install -r .req`
2. `python3 main.py`
3. Скрипт проверит наличие скомпилированных скриптов в папке [`bin`](./bin)
### ☑️ Запуск проекта (Windows)
1. Установка библиотек: `python -m pip install -r .req`
2. `python main.py`
3. Скрипт так же проверит наличие бинарных скриптов ([`bin`](./bin))

#
### ⚙️ Собственная компиляция бинарных файлов (Linux)
Собственноручно скомпилировать бинарные файлы можно при помощи [`makefile`](./makefile):
`make <name>` создаст бинарный файл в папке [`bin`](./bin)

Доступные сортировки (аргумент `name`): `bubble_0`, `bubble_1`, `bubble_2`, `insertion`, `selection`, `merge`, `heap`, `quick`


#
### ❓ Команды меню
* `exit` - выход
* `menu` - меню
* `call <call-string>` - вызов основного функционала (см. подсказки в меню)

#
#### |GriB28|, 2025
[`github.com/GriB28`](https://github.com/GriB28)