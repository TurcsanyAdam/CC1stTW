def File_List():
    f = open("todolist.txt", "r")
    print("You saved the following to-do items: ")
    print(f.read())
    f.close()

def File_Add():
    with open("todolist.txt", "r+") as f:
        x = len(f.readlines())
        y = input("Add an item: ")
        f.write(str(x+1) + ". [ ] " + y + "\n")
        print("Item added! ")
        f.close()

def File_Mark():
    with open("todolist.txt", "r+") as f:
        line = f.readlines()
        y = int(input("Which line would you like to mark as done? "))
        l = open("todolist.txt", "w")
        r = int(len(str(y)))
        for i in range(len(line)):
            if i == y-1:
                l.write(str(y) + ". [X]" + line[i][(r+5):])
            else:
                l.write(line[i])

def File_Archive():
     with open("todolist.txt", "r+") as l:
        line = l.readlines()
        l = open("todolist.txt", "w+")
        x = 0
        for lines in line:
            if "[X]" in lines:
                pass
            else:
                x += 1
                l.write(str(x) + lines[1:])


        print("Your completed tasks have been archived! ")



while True:
    cmd = input("Please specify a command [list, add, mark, archive]: ")
    if cmd == 'list':
        File_List()
    elif cmd == 'add':
        File_Add()
    elif cmd == 'mark':
        File_Mark()
        File_List()
    elif cmd == 'archive':
        File_Archive()
        File_List()
