def start():
    keep_going = True
    while keep_going:
        n = input("Please select which prime algorithm to use, or type 'q' to quit.\n>>> ")
        print() #newline
        try:
            int(n)
        except ValueError:
            if n == "quit" or n == "q":
                print("Bye!")
                break
            else:
                print("Input not recognized, please try again.\n")
                continue
        exec("prime" + str(n) + ".get()")


number_of_algorithms = 2 #manually update
for i in range(1, number_of_algorithms + 1):
    exec("import prime" + str(i))
    
start()
