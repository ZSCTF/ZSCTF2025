#Try to read file /flag
BANLIST = ['__loader__', '__import__', 'compile', 'eval', 'exec', 'chr']
eval_func = eval
for m in BANLIST:
    del __builtins__.__dict__[m]
del __loader__, __builtins__
def filter(s):
    not_allowed = set('"\'`')
    print(not_allowed)
    return any(c in not_allowed for c in s)
WELCOME = '''
 _____       _                     _   _             
|_   _|     | |                   | | (_)            
  | |  _ __ | |_ ___ _ __ ___  ___| |_ _ _ __   __ _ 
  | | | '_ \| __/ _ \ '__/ _ \/ __| __| | '_ \ / _` |
 _| |_| | | | ||  __/ | |  __/\__ \ |_| | | | | (_| |
|_____|_| |_|\__\___|_|  \___||___/\__|_|_| |_|\__, |
                                                __/ |
                                               |___/ 
 _____        _       _ _ 
|  __ \      (_)     (_) |
| |__) |   _  _  __ _ _| |
|  ___/ | | || |/ _` | | |
| |   | |_| || | (_| | | |
|_|    \__, || |\__,_|_|_|
        __/ |/ |          
       |___/__/                                                                                                                                            
'''
print(WELCOME)
print("Welcome to the python jail")
print("Let's have an beginner jail of calc")
print("Enter your expression and I will evaluate it for you.")
while True:
    try:
        input_data = input("> ")
        if filter(input_data):
            print("Oh hacker!")
        print('Answer: {}'.format(eval_func(input_data)))
    except Exception as e:
        print(e)