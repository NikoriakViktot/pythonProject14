# Task 1

# Write a decorator that prints a
# function with arguments passed to it. NOTE! It should print the function, not theresult
# of its execution!
# For example: "add called with 4, 5"


def logger(func):
    def argument(*args):
        print(f' Я декоротор для функції {func.__name__} з атрибутами {args}  ')
        result = func(*args)
        print('результат', result)
        return result
    return argument






@logger
def add(x, y):

    return x + y


@logger
def square_all(*args):

    return [arg ** 2 for arg in args]



# Task 2
#
# Write a decorator that takes a list of stop words and replaces them
# with *inside the decorated function
from functools import wraps
def stop_words(words: list,):
    def stop_word_slogan(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            print(result)
            sp = ' '
            res = []

            for word in result.split():
                clear_word = word.strip("!,.& ")
                if clear_word in words:
                    res.append(word.replace(clear_word, '*'))
                else:
                    res.append(word)
            return " ".join(res)
        return wrap
    return stop_word_slogan

@stop_words(['pepsi', 'BMW' ])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"



# Task 3
# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list
# of symbols that an argument should contain If some of the rules
# ' checks returns False, the function should return False and print the reason it failed;
# otherwise, return the result.

def arg_rules(type_: type, max_length: int, contains: list):
    def stop_slogan(func):
        @wraps(func)
        def stop(*args, **kwargs):
            login = args[0]
            if not isinstance(login, type_):
                raise TypeError("Ви ввели неправильне імя воно має бути строкою")

            if len(login) > max_length:
                raise ValueError("Ви ввели неправильне імя воно не може бути більше 15 символів")
            if any(word not in login for word in contains):
                raise ValueError("Ви ввели неправильне імя воно має містити необхідні символи")

            user = func(*args, **kwargs)
            print(user)
            return user
        return stop
    return stop_slogan




@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogans(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"



if __name__ == '__main__':
    m = add(5,5)
    s = square_all(5)

    slogan = create_slogan( "VW" )
    print(slogan)
    a = create_slogans(1)
    print(a)
    b = create_slogans('joh05@gmail.com')
    print(b)








