#table elimination method

def set_n(x="donkeys"):
    global n
    if x == "donkeys":
        n = int(input("Enter upper bound for prime search: \n>>> "))
        print() #newline
    else:
        n = x
    return n

def sqrt(x):
    return int((x**0.5)+1)

def gen_nonprime_list():
    global nonprime_list
    nonprime_list = []
    global n
    
    for i in range(2, sqrt(n)):
        if i % 10 == 0:
            print("Filling multiples of", i)
        for j in range(2, n):
            nonprime_list.append(i*j)
    print("Removing duplicates")
    nonprime_list = list(set(nonprime_list)) #remove duplicates
    print("Sorting")
    nonprime_list.sort()
    return nonprime_list

def gen_prime_list():
    global n
    global nonprime_list
    global prime_list
    global prime_count
    prime_count = 0
    gen_nonprime_list()
    print("Generating prime list.")
    prime_list = []
    nonprime_count = 0
    next_nonprime = nonprime_list[nonprime_count]
    for i in range(2, n+1):
        if i % 10000 == 0:
            print("Filled primes up till", i)
        if i == next_nonprime:
            nonprime_count += 1
            next_nonprime = nonprime_list[nonprime_count]
        elif i != next_nonprime:
            prime_list.append(i)
            prime_count += 1
    return n

def results():
    global n
    global prime_count
    if prime_count == 1:
        return "There is only 1 prime between 1 and " + str(n) + "."
    else:
        return "There are " + str(prime_count) + " primes between 1 and " + str(n) + ".\n"

def print_prime_list():
    global prime_list
    result = ""
    for i in prime_list:
        result += str(i) + "\n"
    return result

def get(x = "donkeys"):
    set_n(x)
    gen_prime_list()
    #print(print_prime_list())
    print(results())
    

