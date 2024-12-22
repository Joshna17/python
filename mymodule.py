# def greeting(name):
#     print("Hello, " +name)

# def sum(a,b):
#     result=a+b
#     print("result",result)
#     return result
# def diff (a,b):
#     result=a-b
#     print("result",result)
#     return result
# def mul (a,b):
#     result=a*b
#     print("result",result)
#     return result
# if __name__ == "__main__":
#    print("my module")


def sum(a,b):
    result=a+b
    print("result for sum",result)
    return result
def diff (a,b):
    result=a-b
    print("result for diff",result)
    return result
def mul (a,b):
    result=a*b
    print("result for mul",result)
    return result
def div (a,b):
    result=a/b
    print("result for div",result)
    return result
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        print("result for fact",result)
    return result
def floor(a,b):
    result = a//b
    print("result for floor",result)
    return result
def mod(a,b):
    result = a%b
    print("result for fact",result)
    return result


