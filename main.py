# python3

n = int(input())
phbook = {}

for i in range(n):
    
    query = input().split()
    command = query[0]
    number  = query[1]
    
    if command == "add":
        name = query[2]
        phbook[number] = name
    
    if command == "del":
        if number in phbook:
            phbook.pop(number)

    if command == "find":
        if number in phbook:
            print(phbook[number])
        else:
            print("not found")
            
