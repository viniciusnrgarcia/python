# Try, except, else e finally


try:
    a = 18
    b = 1
    c = a / b
    print('function', c)
except ZeroDivisionError as error:
    print('ZeroDivisionError', error.args, error.with_traceback, error, error.__class__.__name__)
except (NameError, TypeError, ImportError):
    print('NameError + TypeError + ImportError')
except Exception as error:
    print('Generic', error.args, error.with_traceback, error)
else:
    # executado caso não der error
    print('else')
finally:
    print('finally')

