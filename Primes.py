#!/usr/bin/python3
import sys
import json
import random

primes = [2]
composites = {}

def primesComposites(n):
    # Loop from 2 to n (range is not inclusive)
    for i in range(2, n+1):
        divisors = lambda a :  [[p,int(i/p)] for p in primes if (i/p).is_integer()]
        # add to primes if no divisors, otherwise add to composites
        if not divisors(i):
            primes.append(i)
        else:
            composites[str(i)] = divisors(i)

def primeFact(n):
    primeFactorization = [] # start with empty list
    if isPrime(n) or n == 1:
        # add to list if prime or 1
        primeFactorization.append(n)
    else:
        # otherwise, recurse on the composite num
        c = composites[str(n)]
        firstFactor = c[0][0]
        secondFactor = c[0][1]
        primeFactorization.append(firstFactor)
        # add prime factorization of the composite num
        primeFactorization.extend(primeFact(secondFactor))
    return primeFactorization

def isPrime(n):
    for p in primes:
        if p == n: # if we called using a prime
            return True
        if p > n: # if no divisors up to n
            return False
        if (n/p).is_integer(): # if a prime is a divisor, n is not prime
            return False
    return True # otherwise, no divisors exist!

def getPrimesLambda(n):
    # Loop from 2 to n, add prime if it has no divisors
    divisors = lambda a : [p for p in primes if (i/p).is_integer()]
    for i in range(2, n+1):
        if not divisors(i):
            primes.append(i)

def readPrimes(filename):
    # use the global scoped vars
    global primes
    global composites
    with open(filename, "r") as f:
        data = json.load(f)
        primes = data["primes"]
        composites = data["composites"]

def writePrimes(filename):
    # construct data dict to write
    data = {
        "primes": primes,
        "composites": composites
    }
    with open(filename, "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    verbose = False # print more stuff!
    write = False   # write to file
    read = False    # read from file
    factorization = False   # print prime factorization
    getComposites = False   # collect composite numbers
    readFile = None     # filename to read from
    writeFile = None    # filename to write to
    batchFactorizationList = None   # tuple to factor
    maxOfBatch = 2 # max int of batch
    numPrimes = None # number passed

    # checkArgs: is the argument present
    checkArgs = lambda toCheck: any([any(arg.startswith(s) for arg in sys.argv) for s in toCheck])
    # removeArgs: sublist without the argument
    removeArgs = lambda toRemove: [arg for arg in sys.argv if not any([arg.startswith(s) for s in toRemove])]
    # getString: extract string with arg
    getString = lambda toRemove: str(set(sys.argv).difference(removeArgs(toRemove)).pop()).split('=', 1)[1]


    if checkArgs(["-h", "--help"]) or len(sys.argv) is 1:
        print("To run:\n\tprimes.py (options) NUMBER")
        print("""Options:
        -h || --help                          Prints this help message
        -v || --verbose                       Gives additional output
        -r=<FILE> || --read=<FILE>            Reads in primes list from specified file (JSON)
        -w=<FILE> || --write=<FILE>           Writes primes list to specified file (JSON)
        -c || --composite                     Collects composite numbers also
        -f || --factorization                 Prints prime factorization of NUMBER
        -b=num,num... || --batch=num,num...   Prints prime factorization of num,num,num...""")
        sys.exit()

    if checkArgs(["-v", "--verbose"]):
        sys.argv = removeArgs(["-v", "--verbose"])
        verbose = True

    if checkArgs(["-r", "--read"]):
        # get file attached to arg
        readFile = getString(["-r", "--read"])
        sys.argv = removeArgs(["-r", "--read"])
        # read in file, print max prime if verbose
        readPrimes(readFile)
        read = True
        if verbose:
            print("Read file:", readFile, "max num:", primes[-1])

    if checkArgs(["-w", "--write"]):
        # get file attached to arg
        writeFile = getString(["-w", "--write"])
        sys.argv = removeArgs(["-w", "--write"])
        if verbose:
            print("Write file:", writeFile)

    if checkArgs(["-f", "--factorization"]):
        sys.argv = removeArgs(["-f", "--factorization"])
        factorization = True
    
    if checkArgs(["-c", "--composite"]):
        sys.argv = removeArgs(["-c", "--composite"])
        getComposites = True

    if checkArgs(["-b", "--batch"]):
        # get tuple attached to arg, put into int list, save max
        batchFactorizationList = getString(["-b", "--batch"])
        batchFactorizationList = [int(n) for n in batchFactorizationList.split(",")]
        maxOfBatch = max(batchFactorizationList)
        sys.argv = removeArgs(["-b", "--batch"])
    
    if len(sys.argv) > 1:
        # get number passed in
        numPrimes = int(sys.argv[1])
        # collect composites if necessary
        if getComposites or factorization or batchFactorizationList:
            primesComposites(max(maxOfBatch,numPrimes))
        else:
            getPrimesLambda(numPrimes)
        # print all primes up to number passed if verbose
        if verbose:
            print([prime for prime in primes if prime <= numPrimes])
        # print factorization
        if factorization:
            print(numPrimes, ":", primeFact(numPrimes))
    # if no number passed, print all primes of file
    elif verbose and read:
        print(primes)
    
    if batchFactorizationList:
        # if no number passed, get composites to max
        if not numPrimes:
            primesComposites(maxOfBatch)
        print("Factorization Batch:")
        for num in batchFactorizationList:
            print("-->  ",num, ":", primeFact(num))

    # print whether num passed is prime or not
    if numPrimes:
        print(numPrimes, "is prime" if isPrime(numPrimes) else "is not prime")

    # save to file
    if writeFile is not None:
        writePrimes(writeFile)