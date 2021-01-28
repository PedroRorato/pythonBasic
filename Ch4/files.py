def main():
    # Open File for writing and create it if it doesn't exist
    # f = open("textfile.txt", "w+")

    # Open the file for appending text to the end
    # f = open("textfile.txt", "a")

    # Write some lines of data to the file
    # for i in range(10):
    #     f.write("This is line " + str(i) + "\r\n")
    
    # Read the file contents
    # f = open("textfile.txt", "r")
    # contents = f.read()
    # print(contents)

    # Read the contents line by line
    f = open("textfile.txt", "r")
    fl = f.readlines()
    for x in fl:
        print(x)
        
    # close the file
    f.close()


if __name__ == "__main__":
    main()