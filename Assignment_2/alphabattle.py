import random
import string

def alpha_battle(p, pi, q, qi):
    p_list = []
    q_list = []
    result = {"P": 0, "Q": 0}
    for i in range(26):
        if i not in qi:
            p_list.append(int(ord(p[i])))
        if i not in pi:
            q_list.append(int(ord(q[i])))
    for i in range(16):
        diff = p_list[i] - q_list[i]
        #print(diff)
        if diff > 0:
            result["P"] += diff
        else:
            result["Q"] += abs(diff)
        #print(result)
    return result

if __name__ == "__main__":
  

    seed = int(input("Enter seed: "))
    random.seed(seed)
    p_list = random.sample(string.ascii_uppercase, k=26)
    p = ''.join(p_list)
    q_list = random.sample(string.ascii_uppercase, k=26)
    q = ''.join(q_list)
    pi = random.sample(range(26), k=10)
    qi = random.sample(range(26), k=10)
    result = alpha_battle(p, pi, q, qi)
    
   # result = alpha_battle("MZNHUVIOEPTWFJCBXKALSDQGYR", [1, 3, 2, 8, 10, 12, 9, 7, 4, 22] , "YFTUCSQOMGKPXNDWHIVJRABZEL" , [21, 24, 25, 3, 4, 1, 8, 9, 10, 17] )
    print(f"Player P: {p} {pi}")
    print(f"Player Q: {q} {qi}")
    print(f"Score: {result}")
    if result["P"] > result["Q"]:
        print("Player P wins!")
    elif result["Q"] > result["P"]:
        print("Player Q wins!")
    else:
        print("Draw game!")