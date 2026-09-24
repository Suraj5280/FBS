# def demo():
#     print("I am from demo")
# #print(type(demo))
# a=10
# #print(type(a))
# x=demo
# #demo()
# x()



# def fun(a):
#     a()
#     def demo():
#         print("I am from demo")
# x=demo
# fun(x)



# def outer():
#     print("I am form outer")
#     def innerFun():
#         print("I am from inner function")
#     return innerFun
# x=outer()
# x()



def outer():
    a="virat"
    def innerFun():
        print(a)
    return innerFun
x=outer()
x()