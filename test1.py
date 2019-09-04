import functools

def log(text):
    def derector(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return derector

@log('excute')
def now():
    print('2015-3-25')
now()

