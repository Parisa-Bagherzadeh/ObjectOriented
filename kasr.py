class Fraction:

    def __init__(self,n,d):
        self.num=n
        self.denom=d
    

    def mul(self,b):
        result=Fraction(None,None)
        result.num=self.num*b.num
        result.denom=self.denom*b.denom
        return result

    def sum(self,b):
        result=Fraction(None,None)
        result.num=self.num+b.num
        result.denom=self.denom+b.denom
        return result

    def subtract(self,b):
        result=Fraction(None,None)
        result.num=self.num-b.num
        result.denom=self.denom-b.denom
        return result   

    def div(self,b):
        result=Fraction(None,None)
        result.num=self.num/b.num
        result.denom=self.denom/b.denom
        return result




    def show(self):
        print(self.num,"/",self.denom)

num=int(input("Numerator: "))
denom=int(input("Denominator")) 
fraction=Fraction(num,denom)
fraction.show()
a=Fraction(2,5)
b=Fraction(4,9)
m=a.mul(b)
m.show()

s=a.sum(b)
s.show()

sub=a.subtract(b)
sub.show()

div=a.div(b)
div.show()






