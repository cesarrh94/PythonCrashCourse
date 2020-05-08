""" WHILE LOOPS:
the FOR loop takes a collection of items and executes a block of code once for each item in the
collection. In contrast, the WHILE loop runs as log as, or while, a certain condition is true. """

current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1


# Letting the user choose when to quit!
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += '\nEnter "quit" to end the program. '

""" For a program that should run only as long as many conditions are true, you can define one
variable that determines whether or not the entire program is active. This variable is called
a FLAG, acts as a signal to the program. We can write our programs so they run while the flag is
set to true and stop running when any of several events set the value of the flag to false. """

active = True # the flag!

message = ''
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)


""" using BREAK to exit a loop:
To exit a while loop immediately without running any remaining code in the loop, regardless of
the results of any conditional test, use the BREAK statement. the break statement directs the flow 
of your program; you can use it to control which lines of code are executed and which are not so
the program only executes code that you want it to, when tou want it to. """

p = '\nPlease enter the name of the city you have visited:'
p += '\n(Enter "quit" when you are finished.) '

while True:
    city = input(p)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")


""" using CONTINUE in a loop: 
Rather than breaking out of a loop entirely without executing the rest of its code, you can use the
CONTINUE statement to return to the beginning of the loop based on the result of a conditional test. """

c_number = 0
while c_number < 10:
    c_number += 1
    if c_number % 2 == 0:
        continue
    
    # prints even numbers!
    print(c_number) 