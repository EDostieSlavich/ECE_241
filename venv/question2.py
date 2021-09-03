class HW1Q2():
    def __int__(self, a= None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def monomial(self):
        if self.a == None or self.b == None or self.c == None:
            self.a = input("Please enter an integer for a: ")
            self.b = input("Please enter an integer for b: ")
            self.c = input("Please enter an integer for c: ")
        x = (self.c + 2*self.b)/self.a
        return x





