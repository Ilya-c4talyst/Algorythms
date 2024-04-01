a = 0
def ct(func):
    def wrapper(*args, **kwargs):
        func()
        global a
        a = a + 1
        print(a)
    return wrapper

@ct
def test():
    print("headstart")

for _ in range(5):
    test()