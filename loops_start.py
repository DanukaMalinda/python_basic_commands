#loops
def main():
    x = 0

    #define while loop
    #while (x<5):
    #    print(x)
    #    x = x +1

    # define for loop
    # for x in range(5, 10):
    #     print(x)

    # for loop over things
    # Days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    # for d in Days:
    #     print(d)

    # use the break and continue statements
    # for x in range(5, 10):
    #     #if (x==7): break # break the loop at conditions met
    #     if (x%2 == 0): continue  # if condition is met, that item will be skiped and itterate to next item
    #     print(x)

    #using the enumerate() function to get index
    Days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i,d in enumerate(Days):
        print(i, d)


if __name__ == "__main__":
    main()