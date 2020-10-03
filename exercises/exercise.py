# Constants
MIN_DRIVING_AGE = 18


def min_age(name: str, age: int):
    try:
        if age >= MIN_DRIVING_AGE:
            print(f"{name} is allowed to drive")
        else:
            print(f"{name} is not allowed to drive")
    except TypeError:
        raise TypeError("Only integers are allowed")


if __name__ == "__main__":
    min_age(input("Type your name"), int(input("Type your age")))
