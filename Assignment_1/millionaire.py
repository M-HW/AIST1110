import random

def gen_q(n,jumped, withdrawed):
    add_sign = '#' if n == 5 or n == 10 else ''
    print(f'Question {n} (${ques_val_table[n]}{add_sign}):')

    
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    op = random.choice(['+', '-', '*', '/'])
    c = random.choice(['A', 'B', 'C', 'D'])

    print(f'{x} {op} {y} = ?')                          #print the question
    if op == '/':
        op = '//'
    soln = eval(str(x) + op + str(y))
                           

    

    for choice in ['A', 'B', 'C', 'D']:                 #print the choice
        print(choice, end='. ')
        if choice == c:
            print(soln, end='  ')
            correct = choice
        else:
            r = None
            while r == None or r == soln:
                r = random.randint(1, 100)
            print(r, end='  ')
    if not jumped and not i == 15:
        print('E. Jump', end='  ')
    print("F. Withdraw")
    return correct


def check_ans(i: int, inp:str, answer:str, jumped:bool, index_jump:int):

    if inp.lower() in 'abcdef':
        if inp.lower() == 'e':                      #use jump
            if jumped or i == 15:                              #already used jump
                print('Wrong!')
                return True, jumped, index_jump, False             #True means game end = true
            else:
                jumped = True
                index_jump = i 
                return False, jumped, index_jump, False
        
        if inp.lower() == 'f':                      #The participant withdraw
            return True, jumped, index_jump, True

        if inp.lower() == answer.lower():           #The Answer is correct
            print("Right!")
            return False, jumped, index_jump, False
        else:                                       #Wrong Answer
            print("Wrong!")
            return True, jumped, index_jump, False 
    else:                                           #Input invaild
        print('Wrong!')
        return True, jumped, index_jump, False                                   #True means game end = true
 

def final_count(i, index_jump, withdraw):
    #print(i, index_jump, withdraw)
    print('Game Over!')
    if index_jump == i-1:
        i -= 2
    if not withdraw:
        if i > 1:
            i -= 1 
        i -= i%5
    print(f'You got ${ques_val_table[i]}')
    if i == 15:
        print('Congrats! You are a millionaire!')


ques_val_table = {0:0, 1:1000, 2:2000, 3:3000, 4:4000, 5:8000, 6:10000, 7:20000, 8:30000, 9:40000, 10:60000, 11:80000, 12:150000, 13:250000, 14:500000, 15:1000000}

se= eval(input('Enter seed: '))
random.seed(se)

i = 1
game_ended = False
jumped = False
index_jump = -1
while i < 16 and not game_ended:
    answer = gen_q(i, jumped, False)
    user_inp = input("Final answer: ")              #get the answer
    game_ended, jumped, index_jump, withdraw = check_ans(i, user_inp, answer, jumped, index_jump)
    if game_ended or i == 15:
        final_count(i, index_jump, withdraw)  
    i += 1
        