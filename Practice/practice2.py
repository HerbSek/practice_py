# # Guess the number 
# import random 


# def guess(number):
#     global count
#     count = 0
#     num_to_guess = random.randint(1,11)
#     if number == num_to_guess:
#         return f'Number guessed right at {count} guesses'
#     while(number != num_to_guess):
#         count += 1
#         print(f'Number entered is incorrect at {count} tries, Try again !!!')
#         number = eval(input('Enter number to guess :'))
#         if number == num_to_guess:
#             return f'Number guessed right at {count} guesses'


# def main():
#     num = eval(input('Enter number to guess :'))
#     print(guess(num))


# main()



# def divide(num):
#     return 42/ num

# def main():
#     try:
#         number = eval(input('Enter number :'))
#         print(divide(number))
#     except Exception as e:
#         print(f'Error : {e}')

# main()

# Up next : Collatz sequence !!! 


# def collatz(number):
#     while number != 1:
#         if number % 2 == 0 : 
#             answer = number // 2
#             print(answer)
#             return collatz(answer)
#         else: 
#             answer = 3*number + 1
#             print(answer)
#             return collatz(answer)
  
#     if number == 1:
#         return f'Done!!! :)'  

# print(collatz(3))

# Lists 

spam = ['apples', 'bananas', 'tofu', 'cats']

def function(mylist):
   for i in range(0,len(mylist)-1):
    print(f'{mylist[i]}, ', end = '')
   return f'and {mylist[-1]}' 
print(function(spam))
