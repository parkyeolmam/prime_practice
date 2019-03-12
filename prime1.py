def set_n(x="donkeys"):
    global n
    if x == "donkeys":
        n = int(input("Enter upper bound for prime search: \n>>> "))
        print() #newline
    else:
        n = x

def isPrime(x):
    result = True #innocent until proven guilty
    divisor = x - 1
    if x % 1000 == 0:
        print("Checked up till", x)
    while divisor > 1:
        if x % divisor == 0:
            result = False
            break
        divisor -= 1
    return result

def gen_prime_list(x = "donkeys"):
    global prime_list
    global n
    if x != "donkeys":
        n = x
    prime_list = []
    for i in range(2, n):
        if isPrime(i):
            prime_list.append(i)
    global prime_count
    prime_count = len(prime_list)
    return prime_list

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

