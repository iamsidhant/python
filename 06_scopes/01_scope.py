
username = "sidhant"
def func():
    # username = "software developer"
    print(username)

print(username)
func()    


x = 99
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x           # avoid this bad practice to manipulate the global variable
#     x = 12

# func3()
# print(x)    

                #  Closure

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()


def coder(num):
    def actual(x):
        return x ** num
    return actual

f = coder(2)
g = coder(3)

print(f(3))
print(g(3))
