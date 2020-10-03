VALID_COLORS = ['azul', 'amarillo', 'rojo']


def colors_decorator(function):
    def wrapper(*args, **kwargs):
        result: bool = function(*args, **kwargs)
        if result:
            return colors_valid(input("\nType a color -> "))
        wrapper._original = function
        return result

    return wrapper


@colors_decorator
def colors_valid(color: str):
    if color == 'exit':
        print("bye")
        return False
    elif color in VALID_COLORS:
        print(f"{color.lower()} is in colors")
        return False
    else:
        print("Not a valid color and continue the loop.")
        return True


if __name__ == '__main__':
    result = colors_valid(input("\nType a color -> "))
    print(result)
