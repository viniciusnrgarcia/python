"""
Operador ternário
"""

logged_user = False

if logged_user:
    message = 'user allowed'
else:
    message = 'user not allowed'

print(message)

logged_user = True

message = 'user allowed' if logged_user else 'user not allowed'

print(message)


