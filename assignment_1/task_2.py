import random


def MyFunc(s, n):
    formula = eval(f"lambda A, B, C: {s}")
    for i in range(n):
        A, B, C = [random.randint(1, 100) for i in range(3)]
        print(s.replace('A', str(A)).replace('B', str(B)).replace('C', str(C)), '=', formula(A, B, C))
 

if __name__ == '__main__':
    MyFunc('A+B/C', 25)