def change_base(n, base: int) -> str:
    n_base = []
    while n > 0:
        n_base.insert(0, str(n % base))
        n = n // base
    return ''.join(n_base)
        
        
def is_esthetic(n_base: str) -> bool:
    last = None
    for item in n_base:
        if not(last == None or abs(int(item) - int(last))  == 1):
            return False
        last = item 
    return True

            

def esthetic(n):
    bases = []
    for i in range(2, 11):                      #only need to change base for 2 to 9, base 10 is equal to n
        if i <= 10:
            n_base = change_base(n, i)
        else:
            n_base = str(n)
        if is_esthetic(n_base):
            bases.append(i)
    if bases: 
        return bases
    else:
        return 'non-ethetic'



# final answer

n = int(input('Enter num: '))
print(esthetic(n))


# Check answer
'''
    for n in range(2, 10001):
        out = esthetic(n)
        if type(out) == list:
            print(n, out)
'''