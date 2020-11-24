class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return (self.a + self.b + self.c)

    def tipo_lado(self):
        if(self.a == self.b and self.a == self.c):
            return 'equilátero'
        elif((self.a == self.b and self.a != self.c) or (self.b == self.c and self.b != self.a) or (self.a == self.c and self.a != self.b)):
            return 'isósceles'
        elif(self.a != self.b and self.a != self.c and self.b != self.c):
            return 'escaleno'

t = Triangulo(4,4,4)
print(t.tipo_lado())

u = Triangulo(5,8,5)
print(u.tipo_lado())
