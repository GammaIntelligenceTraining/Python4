user_number = input('Please enter some number: ')
user_number_len = len(user_number)
if int(user_number) % 2 == 0:
    print('number is even')
else:
    print('Number is odd')

print(int(user_number) ** 2)
if user_number_len == 1:
    print('There is ' + str(user_number_len) + ' digits in number ' + user_number)
elif user_number_len > 1:
    print('There are ' + str(user_number_len) + ' digits in number ' + user_number)
