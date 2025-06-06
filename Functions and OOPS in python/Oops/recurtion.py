## recurtion -> function call itself


def func(num):
    print(num)
    if num == 1:
        return
    func(num - 1)


func(10)
