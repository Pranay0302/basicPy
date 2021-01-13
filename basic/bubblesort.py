def bubblesort(str):
    length = len(str)
    str = list(str)

    for i in range(length - 1):
        for j in range(i + 1, length):
            if str[i] > str[j]:
                str[j], str[i] = str[i], str[j]
    
    return str


print("enter a string")
ip = input()
print(bubblesort(ip))
