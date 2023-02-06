print("Welcome to Chase bank.")
print("Have a nice day!")

# age = input('How old are you? \n')
# age = int(age)
balance = 4000
print('Your current balance is \n' f'{balance}')

decision = input('What would you like to do? (deposit, withdraw, check_balance) \n' )

if decision == 'check_balance':
    print(balance)
elif decision == 'withdraw':
    amount = input('How much would you like? \n')
    amount = 4000 - int(amount)
    print(amount)
else: 
    deposit = input('How much would you like to deposit? \n')
    deposit = balance + int(deposit)
    print(deposit)

finishded = input('Are you done? \n')

if (finishded == 'yes'):
    print('Thank you!')
elif (finishded == 'no'): 
    print(decision)

# one = 1
# two = 2
# three = one + two
# print(int(f'{one}') + int (f'{two}'))
# print(three)


