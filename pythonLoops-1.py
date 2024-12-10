# Declare list of 15 different numbers ranging from 2 to 16
listName = [1, 2, 3, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 22, 139]

# Perform loop on all numbers in list 
for number in listName:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
