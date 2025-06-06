def make_pretty(func):
    def inner():
        print("I am Pretty")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am Ordinary")


ordinary()

## Decorator are use to decorate page. in which when we go on website the we have use website before we are login the page the access the website
