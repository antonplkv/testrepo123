
def arguments_decorator(num_of_repeats):
    def decorator(func_to_decorate):

        def wrapper(*args):
            results = []
            for repeat in range(num_of_repeats):
                print("STARTED WRAPPING!")
                result = func_to_decorate(*args)
                print("STOPPED WRAPPING")
                results.append(result)
            return results

        return wrapper
    return decorator

@arguments_decorator(100)
def hello(name, surname, arg1):
    print(f"Hello world. My name is {name}")
    return 123

# result = decorator(hello)
# result()
#
# print(result())

result = hello("John", "Lehnon", 100)
print(result)