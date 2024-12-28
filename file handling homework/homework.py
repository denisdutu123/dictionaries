# while true is a forever loop
while True:
    print("Menu:\n 1.Read\n 2.Write\n 3.Append\n 4.Exit")
    use = input("Select one from the menu:")
    if use == "1":
        print("Read")
        fil = open("file2.txt", "r")
        print(fil.read())
        fil.close()
    elif use == "2":
        print("Write")
        us = input("What text would you like to add?")
        fil = open("file2.txt", "w")
        fil.write(us)
        fil.close()
    elif use == "3":
        print("Append")
        fil = open("file2.txt", "a")
        u = input("What text would you like to append?")
        fil.write(u)
        fil.close()
    elif use == "4":
        print("Exit")
        break
    else:
        print("Invalid value")


