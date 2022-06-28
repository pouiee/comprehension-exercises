# FizzBuzz list for loop
for i in range(1, 101):
    # Check if a number satisfies both divisible by 3 and 5
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    # Check if divisible by 3
    elif i % 3 == 0:
        print("Fizz")
    # Check if divisible by 5
    elif i % 5 == 0:
        print("Buzz")
    # If not divisible by 3 or 5, print number
    else:
        print(i)

# FizzBuzz list comprehension
# check for conditions and add fizz, buzz, both, or number to list
num_list = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
            ("Fizz" if i % 3 == 0 else
             ("Buzz" if i % 5 == 0 else i))
            for i in range(1, 101)]
# print out list
for num in num_list:
    print(num)
