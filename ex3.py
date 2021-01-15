def create_list():
    """This function recieves strings from the user, creates and returns a
    list of those strings"""
    list=[]
    x=input()
    while x!="":
        list.append(x)
        x=input()
    return list

def concat_list(str_lst):
    """This function recieves a list and returs a single string
    which is actually all the items of the list stringed together"""
    x=""
    for item in range(len(str_lst)):
        x += str_lst[item]
    return x

def average(num_list):
    """This function receives a list of numbers and returns the average of
    all the numbers put together."""
    if num_list==[]:
        return None
    else:
        x=0
        for i in range(len(num_list)):
            x += num_list[i]
        return x/len(num_list)

def cyclic(lst1,lst2):
    """This function receives two lists and checks if they are alike, only
    formatted by an integer number, and returns True or False accordingly."""
    difference=0
    if lst1==lst2:
        return True
    elif len(lst1)!=len(lst2):
        return False
    else:
        for i in range(len(lst1)):
            if lst1[i] not in lst2:
                return False
            elif lst1[i]==lst2[0]:
                difference=i
        for j in range(len(lst2)):
            if lst2[j]!=lst1[((j+difference)%len(lst2))]:
                return False
        return True

def histogram(n, num_list):
    """This function receives a list of integer numbers and returns a new list
    who's slots are equivalent to the items in the first list, and the value
    of each slot in the new list, is equal to the amount of times
    that number slot showed up as a value in the original list."""
    histo_list=[]
    for i in range(n):
        histo_list.append(0)
    if num_list==[]:
        return histo_list
    else:
        for j in range(len(num_list)):
            histo_list[num_list[j]] +=1
        return histo_list

def prime_factors(n):
    """This function reciceves an integer number and returns a list of all
    it's sources, in their prime values. For instance if '4' is a source of n,
    then in the returned list, it will be shown as two separate values
    of '2'."""
    prime_list=[]
    if n==1:
        return prime_list
    else:
        for i in range(2,n):
            while n%i==0:
                prime_list.append(i)
                n=n/i
        if prime_list==[]:
            prime_list.append(n)
        return prime_list

def cartesian(lst1, lst2):
    """This functions receives two lists and returns a list of dual values,
    as if the original lists were cartesianly multiplied."""
    cart_list=[]
    if lst1==[] or lst2==[]:
        return cart_list
    else:
        for i in range(len(lst1)):
            for j in range(len(lst2)):
                cart_list.append((lst1[i],lst2[j]))
        return cart_list

def pairs(n, num_list):
    """This function receives an integer number and a list of numbers,
    and returns a list of dual values which are made out of pairs the the
    original list's values which sum up to the received integer number."""
    sums_list=[]
    if num_list==[]:
        return sums_list
    else:
        for i in range(len(num_list)):
            if n-num_list[i] in num_list:
                if (num_list[i],n-num_list[i]) not in sums_list:
                    sums_list.append((n-num_list[i],num_list[i]))
        return sums_list






