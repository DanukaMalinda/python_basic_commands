#if statements

def main():
    x = input("enter integer for x: ")
    y = input("enter integer for y: ")

    # conditional flow uses if, elif, else
    if (x<y):
        st = "x is less than y"
    elif (x>y):
        st = "x is greater than y"
    else:
        st = "x equals to y"

    print(st)

# if only two argument present(only if and else) we can write it in one line
    st = "x is less than y" if (x<y) else "x is greater than or equal to y"
    print(st)


if __name__ == "__main__":
    main()
