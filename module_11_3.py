import inspect


def introspection_info(obj):
    dict_ = {}
    dict_['type'] = type(obj).__name__
    dict_['attributes'] = dir(obj)
    dict_['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    dict_['module'] = inspect.getmodule(obj)
    return dict_

def function_():
    a = 3
    print(a)

class Class_:
    def __init__(self, a, b):
        self.a = a
        self.b = b


number_info = introspection_info(42)
print(number_info)

string_info = introspection_info('Два')
print(string_info)

list_info = introspection_info([1, 'Два', 3, True])
print(list_info)

function_info = introspection_info(function_)
print(function_info)

cl = Class_(1, 2)
class_info = introspection_info(cl)
print(class_info)
