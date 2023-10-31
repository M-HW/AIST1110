def comb(n, r: int) -> int:
    result = dic_int.get((n,r))
    if result:
        return result
    elif n >= r:
        if n==0 or r == 0:
            dic_int[(n, r)] = 1
            return 1
        elif r == 1:
            dic_int[(n, r)] = n
            return n
        else:
            result = comb(n-1, r-1) + comb(n-1, r)
            dic_int[(n, r)] = result
            return result 
    else:
        return 0

def pascal_triangle(n:int) -> str:
    max_entry = comb(n, n // 2)
    max_length = len(str(max_entry))
    max_length_amend = max_length
    if max_length % 2 == 0:
        max_length_amend += 1
    base_length = (max_length_amend+1)  * (n+1) // 2
    for i in range(n + 1):
        base_length -= (max_length//2+1)
        print(' ' * base_length, end = '')
        for j in range(i + 1):
            print_int = comb(i, j)
            diff_length = max_length_amend - len(str(print_int)) 
            front = diff_length // 2
            end = front + diff_length % 2
            print_str = ' '*front + str(print_int) + ' '*end
            print(print_str, end=' ')
        print()
    pass


dic_int = {}
n = int(input("Enter num: "))
pascal_triangle(n)