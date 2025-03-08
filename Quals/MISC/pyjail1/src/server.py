#Your goal is to read ./flag
#You can use these payload liked `__import__('os').system('cat ./flag')` or `print(open('/flag').read())`

WELCOME = '''
 ______                        _       _ _ 
|  ____|                      | |     (_) |
| |__   __ _ ___ _   _        | | __ _ _| |
|  __| / _` / __| | | |   _   | |/ _` | | |
| |___| (_| \__ \ |_| |  | |__| | (_| | | |
|______\__,_|___/\__, |   \____/ \__,_|_|_|
                  __/ |                   
                 |___/                                                             
'''

print(WELCOME)

print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
input_data = input("> ")
print('Answer: {}'.format(eval(input_data)))