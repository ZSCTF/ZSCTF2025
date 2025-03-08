def filter(s):
    BLACKLIST = ["exec","input","eval"]
    for i in BLACKLIST:
        if i in s:
            print(f'{i!r} has been banned for security reasons')
            exit(0)

WELCOME = '''
 _____        _       _ _    _____ _____ 
|  __ \      (_)     (_) |  |_   _|_   _|
| |__) |   _  _  __ _ _| |    | |   | |  
|  ___/ | | || |/ _` | | |    | |   | |  
| |   | |_| || | (_| | | |   _| |_ _| |_ 
|_|    \__, || |\__,_|_|_|  |_____|_____|
        __/ |/ |                        
       |___/__/                                                                                                              
'''

print(WELCOME)

print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
input_data = input("> ")
filter(input_data)
if len(input_data)>13:
    print("Oh hacker!")
    exit(0)
print('Answer: {}'.format(eval(input_data)))