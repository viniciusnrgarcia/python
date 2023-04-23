"""
    chamando método super da super class
"""
class Customer(str):

    def upper(self):
        print('upper')
        # super().upper() == super(Customer, self).upper()
        s = super(Customer, self).upper()
        if s == super().upper():
            print (s) 
        return super().upper()


s = Customer('Vinicius')
print(s.upper())


class A:
    a = 'A'
    def m(self):
        print('A')


class B(A):
    b = 'B'
    def m(self):
        print('B')


class C(B):
    c = 'C'
    def m(self):
        super(C, self).m()
        print('C')


class D():
    d = 'D'
    def m(self):
        print('D')


class E(A, D):
    d = 'E'
    def m(self):
        print('D')




c = C()
#print(c.a)
#print(c.b)
print(c.c)

c.m()