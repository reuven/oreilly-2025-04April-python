if __name__ == '__main__':
    print(f'Hello from {__name__}!')  # only print when running the module; don't print when we import it

x = 100

y = [10, 20, 30]

def hello(name):
    return f'Hello, {name} from mymod!'

if __name__ == '__main__':
    print(f'Goodbye from {__name__}!')   # only print when running the module as a program; don't when we import it
    
