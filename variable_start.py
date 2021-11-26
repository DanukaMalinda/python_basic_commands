#declare variables
f = 0
print(f)

#re-declaring same variable
f = "abc"
print(f)

#only can concatenate sane type of variables
print("this is a string " + str(123))

#global and local variable different (global variables and local variables can have same name but hold different values)
def someFunction():
    global f #if we want to have gloabl f inside of this function, we have to say this global f
    f = "this is different f"
    print(f)

someFunction()
print(f)

#delete variables
del f