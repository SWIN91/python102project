x = int(input("Please enter an integer: "))
if x < 0:
    print ("Negative changed to zero")
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print ('More')


print('\nMeasure some strings:')
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
print("\nFunction Syntax:")
def add_num(num1,num2):
    return num1+num2
print(add_num(4,5))


print('\nUDF function to tests if a given number is a prime number:')
def is_prime(num):
    """
    Naive method of checking for primes.
    """
    for n in range(2,num):
        if num % n == 0:
            print ('not prime')
            break
    else:
        print('prime')
print(is_prime(25))





print("\n\tTask 3 - Coding Questions:" +
      '\nQuestion 1: Write a function to print "hello_USERNAME!"\n\n')
def hello_name(user_name):
    """
    Print "hello USERNAME!"
    """
user_name = input("Username: ")
print('"hello, ' + user_name.upper() + '!"')




print("\n\nQuestion 2: Print the first 100 odd numbers in Python:")
for int in range(0, 100):
    if int % 2:
            print(int)




print("\n\nQuestion 3: Write a function, max_num_list to return the max number of a given list:")
def max_num_in_list(a_list):
    """
    Return the max number of a given list.
    """
    max= a_list[0]
    for number in a_list:
        if number > max:
            max=number
    return max


numbers=[2, 6, 19, 104, 76, 30]
max_num_in_list(numbers)
print(max_num_in_list(numbers))





print(
    "\n\nQuestion 4:"
    "\n\tWrite a function to return if the given year is a leap year."
    "\n\tA leap year is divisible by 4, but not by 100 unless its also divisible by 400."
    "\n\tThe return should be boolean Type:"
    )


def is_leap_year(a_year):
    """
    Return True if the given year is a leap year.
    """
    if (a_year % 400 == 0) or (a_year % 100 != 0) and (a_year % 4 == 0):
        return True
    else:
        return False
print(is_leap_year(1991))




print(
    "\n\nQuestion 5: Write a function to check to see if "
    "all numbers in a list are consecutive numbers."
    "\nThe return should be boolean Type:"
)
def is_consecutive(a_list):
    """
    Check to see if all numbers in list are consecutive numbers.
    Return a boolean Type.
    """
    a_list= [0]
    for number in a_list:
        if number == a_list[0] +1:
            return True
    else:
        return False
growth_inches= [1, 3, 5, 7]
growth_feet= [2, 3, 4, 5]
print(is_consecutive(growth_inches))
print(is_consecutive(growth_feet))


        
