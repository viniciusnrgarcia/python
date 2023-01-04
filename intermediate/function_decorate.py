def create_function(function):
    def internal_function(*args, **kwargs):
        print('init decorate')
        for arg in args:
            is_string(arg)
        result = function(*args, **kwargs)
        print('OK decorate')
        print(result)
        return result
    return internal_function

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser string')

def string_reverse(string):
    print(f'{string_reverse.__name__}')
    return string[::-1]

reverse = string_reverse('012')
print(reverse)

print('-----------')


reverse_string_check_param = create_function(string_reverse)
reverse = reverse_string_check_param('123')
print(reverse)

print('-----------')


@create_function
def string_reverse_annotation(string):
    print(f'{string_reverse_annotation.__name__}')
    return string[::-1]


reverse = string_reverse_annotation('456')
print(reverse)