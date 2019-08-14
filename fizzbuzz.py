#Fizz and Buzz refer to any number that's a multiple of 3 and 5 respectively. In other words, if a number is divisible
#by 3, it is substituted with fizz; if a number is divisible by 5, it is substituted with buzz. If a number is simultaneously
#a multiple of 3 AND 5, the number is replaced with "fizz buzz." In essence, it emulates the famous children game
#"fizz buzz".
for fizzbuzz in range(50):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
