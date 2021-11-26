#defining a function
def function1():
    print("I am a function") #arguments in a function should be intended

#functions that takes arguments
def function2(arg1,arg2):
    print(arg1," ",arg2)

#functions that return values
def function3(x):
    return x*x*x

#function with arguments which have default value
def power(num,x=1):
    result = 1
    for i in range(x):
        result = result*num
    return result

#functions with variable number of arguments
def varArgFunc(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print("Function1")
function1()
print("Function2")
function2("Danuka","Malinda")
print("Function3")
print(function3(5))
print(power(2))
print(power(2,3))
print(varArgFunc(1,2,3,4))
print(varArgFunc(1,2,3,4,5))