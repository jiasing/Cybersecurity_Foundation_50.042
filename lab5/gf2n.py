# 50.042 FCS Lab 5 Modular Arithmetic
# Year 2023

import copy
class Polynomial2:
    def __init__(self,coeffs): #coeffs is a list. 
        self.coeff = coeffs

    def add(self,p2):
        new_power = []
        power1 = self.coeff
        power2 = p2.coeff
        
        if len(power1) > len(power2):
            longer = power1
        else:
            longer=power2

        for i in range(max(len(power1), len(power2))):
            if i < min(len(power1), len(power2)) :
                new_power.append(power1[i] ^ power2[i])
            else:
                new_power.append(longer[i])
        return Polynomial2(new_power)

    def sub(self,p2):
        return self.add(p2)
    
    def mul(self,p2,modp=None):
        partial = [] #first element means multiply by 1.
        final = Polynomial2([0])

        for val in range(len(self.coeff)):
            if self.coeff[val] == 1:
                partial.append(Polynomial2([0]*val + p2.coeff))
               
        for poly in partial:
            final = final.add(poly)

        if modp != None:
            q, final = final.div(modp)
        
        return final
    
    
    def div(self,p2):
        q = Polynomial2([0])                   
        r = Polynomial2(self.coeff)            
        d = self.deg(p2)                   
        while (self.deg(r)) >= d:
            newpower = self.deg(r) - d
            s = Polynomial2([0] * (newpower) + [1])
            q = q.add(s)   
            to_subtract = Polynomial2([0] * (newpower) +p2.coeff)    
            r = r.sub(to_subtract)    
        return q, r

    def deg(self, poly):
        for i in range(len(poly.coeff) - 1, -1, -1):
            if poly.coeff[i] == 1:
                return i
        # Return -1 if 1 is not found in the list
        print("THIS IS A ZERO POLYNOMIAL")
        return -1

    def __str__(self):
        power = len(self.coeff) - 1
        text = ''
        for i in range(power, -1, -1):
            if self.coeff[i] == 1:
                text += f'x^{i}+'
        text = text[:-1] + '.'
        return text

    def getInt(p):
        coeff = p.coeff
        value = 0
        for i in range(len(coeff)):
            if coeff[i] == 1:
                value += 2**i
        return value


class GF2N:
    affinemat=[[1,0,0,0,1,1,1,1],
               [1,1,0,0,0,1,1,1],
               [1,1,1,0,0,0,1,1],
               [1,1,1,1,0,0,0,1],
               [1,1,1,1,1,0,0,0],
               [0,1,1,1,1,1,0,0],
               [0,0,1,1,1,1,1,0],
               [0,0,0,1,1,1,1,1]]

    def __init__(self,x,n=8,ip=Polynomial2([1,1,0,1,1,0,0,0,1])):
        self.x = x
        self.n = n
        self.ip = ip
        self.poly = self.getPolynomial2()

    def add(self,g2):
        final = self.poly.add(g2.poly)
        return GF2N(final.getInt(), self.n, self.ip)

    def sub(self,g2):
        return self.add(g2)
    
    def mul(self,g2):
        final = self.poly.mul(g2.poly, self.ip)
        return GF2N(final.getInt(), self.n, self.ip)

    def div(self,g2):
        q,r = self.poly.div(g2.poly)
        return GF2N(q.toInt(), self.n, self.ip), GF2N(r.toInt(), self.n, self.ip)

    def getPolynomial2(self):
        bin_str = (bin(self.x)[2:].zfill(self.n))[::-1] #reverse is cause first element is power 0.
        return Polynomial2([int(bit) for bit in bin_str])

    def __str__(self):
        return str(self.getInt())

    def getInt(self):
        value = self.poly.getInt()
        return value

    def mulInv(self):
        pass

    def affineMap(self):
        pass


# print('\nTest 1')
# print('======')
# print('p1=x^5+x^2+x')
# print('p2=x^3+x^2+1')
# p1=Polynomial2([0,1,1,0,0,1])
# p2=Polynomial2([1,0,1,1])
# p3=p1.add(p2)
# print('p3= p1+p2 = ',p3)

# print('\nTest 2')
# print('======')
# print('p4=x^7+x^4+x^3+x^2+x')
# print('modp=x^8+x^7+x^5+x^4+1')
# p4=Polynomial2([0,1,1,1,1,0,0,1])
# modp=Polynomial2([1,0,0,0,1,1,0,1,1])
# p5=p1.mul(p4,modp)
# print('p5=p1*p4 mod (modp)=',p5)

# print('\nTest 3')
# print('======')
# print('p6=x^12+x^7+x^2')
# print('p7=x^8+x^4+x^3+x+1')
# p6=Polynomial2([0,0,1,0,0,0,0,1,0,0,0,0,1])    
# p7=Polynomial2([1,1,0,1,1,0,0,0,1])
# p8q,p8r=p6.div(p7)
# print('q for p6/p7=',p8q)
# print('r for p6/p7=',p8r)


# print('\nTest 4')
# print('======')
# g1=GF2N(100)
# g2=GF2N(5)
# print('g1 = ',g1.getPolynomial2())
# print('g2 = ',g2.getPolynomial2())
# g3=g1.add(g2)
# print('g1+g2 = ',g3)

# print('\nTest 5')
# print('======')
# ip=Polynomial2([1,1,0,0,1])
# print('irreducible polynomial',ip)
# g4=GF2N(0b1101,4,ip)
# g5=GF2N(0b110,4,ip)
# print('g4 = ',g4.getPolynomial2())
# print('g5 = ',g5.getPolynomial2())
# g6=g4.mul(g5)
# print('g4 x g5 = ',g6)

# print('\nTest 6')
# print('======')
# g7=GF2N(0b1000010000100,13,None)
# g8=GF2N(0b100011011,13,None)
# print('g7 = ',g7.getPolynomial2())
# print('g8 = ',g8.getPolynomial2())
# q,r=g7.div(g8)
# print('g7/g8 =')
# print('q = ',q.getPolynomial2())
# print('r = ',r.getPolynomial2())

# print('\nTest 7')
# print('======')
# ip=Polynomial2([1,1,0,0,1])
# print('irreducible polynomial',ip)
# g9=GF2N(0b101,4,ip)
# print('g9 = ',g9.getPolynomial2())
# print('inverse of g9 =',g9.mulInv().getPolynomial2())

# print('\nTest 8')
# print('======')
# ip=Polynomial2([1,1,0,1,1,0,0,0,1])
# print('irreducible polynomial',ip)
# g10=GF2N(0xc2,8,ip)
# print('g10 = 0xc2')
# g11=g10.mulInv()
# print('inverse of g10 = g11 =', hex(g11.getInt()))
# g12=g11.affineMap()
# print('affine map of g11 =',hex(g12.getInt()))