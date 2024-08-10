rows=int(input('How many rows do you want?:'))
columns=int(input(('How many columns do you want?:')))
symbol=input('Enter a symbol:')



for i in range(0,rows):
  for j in range(0,columns-i):
    print(' ',end='')
  for k in range(0,2*i+1):
    print(symbol,end='')
  print('')