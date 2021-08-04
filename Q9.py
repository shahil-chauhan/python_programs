''' 
Write a program that computes the net amount of a bank account
based a transaction log from console input. The transaction 
log format is shown as following:
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
D means deposit while W means withdrawal.
Then, the output should be:
500
'''
total_amt = 0

while True:
    tran = input("Enter the transactions: ")
    if tran == '':
        break
    else:
        tran = tran.split()
        if tran[0].upper() == 'D':
            total_amt = total_amt + int(tran[1])
        elif tran[0].upper() == 'W':
            total_amt = total_amt - int(tran[1])

print(total_amt)
