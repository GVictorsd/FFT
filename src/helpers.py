#########
# helper classes and functions
#
######3


class cpxnum:
    '''
        COMPLEX NUMBERS Class
        Class defining attribures and required behaviour of complex numbers
        Python has inbuilt support for complex numbers but where is fun in that? :P
    '''
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        return f'{self.real} + i {self.img}'

    def add(self, other):
        '''
         method to add two complex numbers
        '''
        return cpxnum(self.real + other.real, self.img + other.img)

    def sub(self, other):
        '''
            returns difference of two complex numbers
        '''
        return cpxnum(self.real - other.real, self.img - other.img)

    def mul(self, other):
        '''
        product of two complex numbers
        '''
        a = self.real
        b = self.img
        c = other.real
        d = other.img
        return cpxnum((a*c)-(b*d), (a*d)+(b*c))


