# Enter your code here. Read input from STDIN. Print output to STDOUT
c ='.|.'
x = input().split()
M=int(x[1])
w=int(x[0])
m = (M-3)//2
for i in range(1,w-1,2):
    print(('-'*m).rjust(m)+c*(i)+('-'*m).ljust(m))
    m -=3
m=3
print('WELCOME'.center(M,'-'))
for i in range(w-2,0,-2):
    print(('-'*m).rjust(m)+c*(i)+('-'*m).ljust(m))
    m+=3
