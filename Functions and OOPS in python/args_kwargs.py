def add(*args):
    # print(sum(args))
    print(args)


add(2342, 4, 4, 2)  # *args give output in tuple
add()


#


def add(**kwargs):
    print(kwargs)  # kwaregs give output in dictionary

    for k, v in kwargs.items():
        print(k, v)


add(name="Dinesh", age=23)


def add(n1, n2, n3, *addd, **kwaddd) -> int:
    print(f"{n1= }")
    print(f"{n2= }")
    print(f"{n3= }")
    print(f"{addd = }")
    print(f"{kwaddd = }")


add(1, 2, 3)

add([12, 34, 56, 6], 4, 5, 6, 7, name="dinesh")
