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
        for j in range(2, n):
            nonprime_list.append(i*j)
    nonprime_list = list(set(nonprime_list)) #remove duplicates
    nonprime_list.sort()
    return nonprime_list

def gen_prime_list():
    global n
    global nonprime_list
    global prime_list
    global prime_count
    prime_count = 0
    gen_nonprime_list()
    prime_list = []
    for i in range(2, n):
        if i not in nonprime_list:
            prime_list.append(i)
            prime_count += 1
    return n

def results():
    global n
    global prime_count
    if prime_count == 1:
        return "There is only 1 prime between 1 and " + str(n) + "."
    else:
        return "There are " + str(prime_count) + " primes between 1 and " + str(n) + "."

def print_prime_list():
    global prime_list
    result = ""
    for i in prime_list:
        result += str(i) + "\n"
    return result

def get(x = "donkeys"):
    set_n(x)
    gen_prime_list()
    print(results(), "They are: ")
    print(print_prime_list())
