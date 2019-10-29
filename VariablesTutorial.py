PrintString = False
PrintNum = False
PrintList = False
PrintVars = False
PrintIf = False
PrintBool = False
PrintDict = False
PrintNone = True

if PrintVars:
    # boolean
    a = True
    b = False
    # integer
    c = 1
    d = -23
    # float
    e = 1.23
    d = -20.3
    # complex numbers
    f = 3+2j
    g = -2.3+4.99j
    # string
    h = "Howdy"
    i = 'there'
    j = str(d)
    k = "use + to concatenate " + str(f) + " a variable"
    l = f"or 'f' and brackets to {c} interpolate a variable"
    # list
    m = [0, 1, 2.44, -3.3]
    n = list(range(10))
    o = [[1, 3, 2], ["a", "b", 3, 2+1j], list(range(3)), "woah", True]
    # dictionary
    p = {
        "name": "cole",
        "role": "author",
        "birthday": "3/21/98",
        "numToes": 10,
        "listOfStuff": [1, "a", 3+2j, False]
    }
    # None
    q = None

    #print all our variables separated by a newline (sep="\n")
    print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, sep="\n")

if PrintBool:
    # Or operator
    a = True or False       # True!
    # And operator
    b = True and False      # False!
    # Equality operator
    c = True is False       # False!
    d = True == False       # False!
    e = True != False       # True!
    # Negation operator
    f = not True is False   # True!
    # Exclusive or operator
    g = not True ^ False    # False! 
    # Inequalities
    h = 2 < 2               # False!
    i = 1 <= 1              # True!
    j = 3 > 2               # True!
    k = 1 >= 2              # False!
    # Set membership
    l = 1 in [1, 2, 3]      # True!
    m = 4 in [1, 2, 3]      # False!
    n = 4 not in [1, 2, 3]  # True!

    print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, sep="\n")

if PrintIf:
    # basic if statement
    if 1 < 2:
        print("1 is less than 2")
    else:
        print("1 is not less than 2")

    # basic while loop
    i = 0
    while i < 10:
        print(i)
        i+=1

if PrintNum:
    a = 1 + 1   # addition: 2
    b = 1 - 1   # subtraction: 0
    c = 2 * 2   # multiplication: 4
    d = 2 ** 4  # exponentiation: 16
    e = 4 / 2   # division: 2.0
    f = 4 // 5  # floor division: 0
    g = 5 % 3   # modulus: 2
    h = 3 & 2   # bitwise and: 2
    i = 7 | 15  # bitwise or: 15
    j = 5 ^ 7   # bitwise xor: 2
    k = ~3      # bitwise not: -4
    l = 15<<1   # shift left: 30
    m = 15>>1   # shift right: 7

    print(a, b, c, d, e, f, g, h, i, j, k, l, m, sep="\n")

    a = b = c = d = e = f = g = h = i = j = k = l = m = 10
    a = 12  # reassignment: 12
    b += 1   # addition: 11
    c -= 1   # subtraction: 9
    d *= 2   # multiplication: 20
    e **= 3  # exponentiation: 1000
    f /= 2   # division: 5.0
    g //= 5  # floor division: 2
    h %= 3   # modulus: 1
    i &= 2   # bitwise and: 2
    j |= 15  # bitwise or: 15
    k ^= 7   # bitwise xor: 13
    l <<=1   # shift left: 20
    m >>=1   # shift right: 5


    print(a, b, c, d, e, f, g, h, i, j, k, l, m, sep="\n")



if PrintString:
    a = "This is a string"
    b = a[0:7]          # Slice: "This is"
    c = len(a)          # Length: 16
    d = a[3]            # Index: "s"
    e = a[-1]           # End index: "g"
    f = a.split(" ")    # Splits on character: ['This', 'is', 'a', 'string']
    g = "   this has whack whitespace    ".strip()  # Removes leading and trailing whitespace
    print(a, b, c, d, e, f, g, sep="\n")

if PrintList:
    a = [] # makes an empty list: []
    print(a)
    b = [9, 8, 7] # makes a list with stuff in it: [9, 8, 7]
    print(b)
    a.append(1) # add 1 to the list: [1]
    print(a)
    a.extend([2, 3, 4]) # add multiple things: [1, 2, 3, 4]
    print(a)
    a.append(b) # append a different list: [1, 2, 3, 4, [9, 8, 7]]
    print(a)
    c = a.pop() # remove last element of list: a=[1, 2, 3, 4], c=[9, 8, 7]
    print(a, c)
    b.sort()    # sorts list: [7, 8, 9]
    print(b)    
    a.sort(reverse=True)    # sorts in reverse: [4, 3, 2, 1]
    print(a)    
    d = a[3]   # gets index from start: 1
    e = a[-2]  # gets index from end: 2
    f = a[2:]  # gets slice from index to end: [2, 1]
    g = a[:3] # gets slice from start to index: [4, 3, 2]
    print(d, e, f, g, sep="\n")

if PrintDict:
    import pprint
    pp = pprint.PrettyPrinter(indent=3)
    a = {} # makes an empty dictionary
    pp.pprint(a)
    b = {
        "Name": "Cole",
        "Birthday": "3/21/1998",
        "Age": 21,
        "Favorite foods": ["Popeyes", "Louisiana Fast", "Number 7", "Spicy Chicken"]
    }
    pp.pprint(b)
    # Add items
    print(len(b), len(a))   #number of key-value pairs: 4, 0
    b["Favorite Kernel"] = "Linux"
    b.update({"Python version": "3.6.7", "Donut preference": "Glazed"})
    pp.pprint(b)
    # Delete items
    b.pop("Birthday")
    del b["Age"]
    pp.pprint(b)
    b.clear()
    pp.pprint(b)

if PrintNone:
    a = None
    if a is not None:
        print(a)
    else:
        print("No object 'a' exists")