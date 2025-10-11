from random import randint


def generate_array(type_: int, min_: int, max_: int, length: int):
    if type_ == 0:
        return random_array(min_, max_, length)
    elif type_ == 1:
        return ascending_array(min_, max_, length)
    elif type_ == 2:
        return descending_array(min_, max_, length)
    else:
        return None

def random_array(min_: int, max_: int, length: int) -> list[int]:
    return [randint(min_, max_) for _ in range(length)]

def ascending_array(min_: int, max_: int, length: int) -> list[int]:
    return sorted(random_array(min_, max_, length))

def descending_array(min_: int, max_: int, length: int) -> list[int]:
    return sorted(random_array(min_, max_, length), reverse=True)
