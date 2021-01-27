def main():
    x = 0

    # While
    # while(x<5):
    #     print(x)
    #     x = x+1

    #For
    # for x in range(5, 10):
    #     print(x)

    # For over a collection
    # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # for d in days:
    #     print(d)

    # Break and continue
    # for x in range(5, 10):
    #     # if(x==7):break
    #     if(x % 2 == 0): continue
    #     print(x)

    #Enumerate
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, d in enumerate(days):
        print(i, d)


if __name__ == "__main__":
    main()