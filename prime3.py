#modified sieve to run faster, hopefully

def set_n():
    #print("set_n")
    n = int(input("Enter upper bound for prime search: \n>>> "))
    print()
    return n

def sqrt(x):
    return int((x**0.5)+1)


def get_sieveprime_list(n):
    #calculates the list of primes up till sqrt(n) for use in sieve to avoid duplicates
    prime_list = read_prime_list_from_file()

    if len(prime_list) > sqrt(n):
        sieveprime_list = prime_list[0:sqrt(n)]
    elif len(prime_list) < sqrt(n):
        while len(prime_list) <= sqrt(n):
            x = prime_list[-1]
            
            prime_list = get_prime_list(int(2*x))
            print("Insufficient primes in memory.")
            print("Doubling primes in memory.")
        sieveprime_list = prime_list[0:sqrt(n)]
    else:
        sieveprime_list = prime_list

        
    return sieveprime_list

def get_nonprime_list(n):
    #print("get_nonprime_list(n)")
    sieveprime_list = get_sieveprime_list(n)
    nonprime_list = []
    print("Applying sieve.")
    while sieveprime_list[0] <= sqrt(n):
        i = sieveprime_list.pop(0)
        for j in range(i, int((n/i))+1):
            #print(i, "*", j, "=", i*j)
            nonprime_list.append(i*j)

    print("Removing duplicates.")
    nonprime_list = list(set(nonprime_list))
    print("Sorting sieve.")
    nonprime_list.sort()
    return nonprime_list

def get_prime_list(n):
    #print("get_prime_list(n)")
    nonprime_list = get_nonprime_list(n)
    print("Sieve complete.")
    print("Eliminating non-primes.")
    prime_list = []

    nonprime_count = 0
    next_nonprime = nonprime_list[nonprime_count]
    for i in range(2, n+1):
        try:
            if i == next_nonprime:
                nonprime_count += 1
                next_nonprime = nonprime_list[nonprime_count]
            elif i != next_nonprime:
                prime_list.append(i)
        except IndexError:
            break
    return prime_list

def convert_list_to_text(lima):
    #print("convert_list_to_text(lima)")
    s = [str(i) for i in lima]
    result = "\n".join(s)
    return result

def get(n="donkeys"):
    #print("get(n)")
    if n == "donkeys":
        n = set_n()
    
    initialize()
    prime_list = get_prime_list(n)
    if len(prime_list) > len(read_prime_list_from_file()):
        write_list_to_prime_file(prime_list)
        
    print()
    print(results(len(prime_list), n))

def read_line(n): #buggy so this function is unused, but leaving it in for later
    n += 1
    #print("read_line(n)")
    try:
        prime_list_file = open("prime_list.txt", "r")
        prime_list = []
        for i in range(1, n):
            entry = prime_list_file.readline()[:-1]
            if entry == "":
                break
            else:
                entry = int(entry)
            prime_list.append(entry)
    except FileNotFoundError:
        prime_list = []
    return prime_list


def read_prime_list_from_file():
    #print("read_prime_list_from_file()")
    try:
        prime_list_file = open("prime_list.txt", "r")
        prime_list = [int(s) for s in prime_list_file.read().split("\n")]
    except FileNotFoundError:
        prime_list = []
    return prime_list

def write_to_prime_file_using_prime1(n):
    #print("write_to_prime_file_using_prime1(n)")
    print("Importing 1000 primes from prime1.")
    import prime1
    prime1_list = prime1.gen_prime_list(n)
    write_list_to_prime_file(prime1_list)


def write_list_to_prime_file(lima):
    #lima.append(1) #workaround to the last line missing \n causing line loss
    #print("write_list_to_prime_file(lima)")
    prime_list_write = open("prime_list.txt", "w+")
    prime_list_write.truncate(0)

    prime_list_write.writelines( convert_list_to_text(lima) )
        
def initialize():
    print("Initializing.")
    prime_list = read_prime_list_from_file()
    if len(prime_list) < 168:
        print("Insufficient primes in memory.")
        write_to_prime_file_using_prime1(1000)

def results(prime_count, n):
    if prime_count == 1:
        return "There is only 1 prime between 1 and " + str(n) + "."
    else:
        return "There are " + str(prime_count) + " primes between 1 and " + str(n) + ".\n"
