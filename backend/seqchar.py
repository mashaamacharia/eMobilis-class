ch=str(input("Enter the extent of a letter"))
a=ord(ch)
for x in range(65,a+1):
    for c in range(65,x+1):
        print(chr(c),end="")
    print("")   