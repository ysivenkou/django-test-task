def reverse_func(func):
    def wrapper(*args, **kwargs):
        args = args[::-1]
        return func(*args, **kwargs)
    return wrapper


@reverse_func
def sub(a, b):
    return a - b


if __name__ == '__main__':
    a = 3
    b = 5
    print(sub(a, b))