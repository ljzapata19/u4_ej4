class Imaginario:
    __real = float 
    __imag = float
    
    def __init__(self, r, i):
        self.__real = r
        self.__imag = i
        
    def __str__(self):
        if self.__imag >=0:
            return f'{self.__real} + {self.__imag} i'
        else:
            return f'{self.__real} - {abs(self.__imag)} i'
        
    def getReal(self):
        return self.__real
    
    def getImag(self):
        return self.__imag
    
    def __add__(self, otro):
        r = self.__real + otro.getReal()
        i = self.__imag + otro.getImag()
        return Imaginario(r, i)
    
    def __sub__(self, otro):
        r = self.__real - otro.getReal()
        i = self.__imag - otro.getImag()
        return Imaginario(r, i)
    
    def __mul__(self, otro):
        r = (self.__real * otro.getReal()) - (self.__imag * otro.getImag())
        i = (self.__real * otro.getImag()) + (self.__imag * otro.getReal())
        return Imaginario(r, i)
    
    def __truediv__(self, otro):
        conjugado = Imaginario(otro.getReal(), otro.getImag() * -1)
        n = self * conjugado
        d = otro * conjugado
        d= d.getReal()
        return Imaginario(round(n.getReal()/d,2), round(n.getImag()/d,2))
    
    