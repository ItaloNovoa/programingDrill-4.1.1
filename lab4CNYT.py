from matrices import *
import unittest

#probabilidad([(-3,-1),(0,-2),(0,1),(2,0)],2)
def probabilidad(vector,pos):
    return float("%.6f" % (Norma([[vector[pos]]])**2/Norma([vector])**2))


#Matriz Compleja --> ket
#normKet([[(-3,-1)],[(0,2)],[(0,1)],[(2,0)]])
def normKet(ket):
    normalizada=complejoPorMatriz((1/Norma(ket),0),ket)
    return bonitaCompleja(normalizada)


#Matriz Compleja --> ket    
#Bra([[(-3,-1)],[(0,2)],[(0,1)],[(2,0)]])
def Bra(ket):
    ket=conjugada(ket)
    return transpuestaVector(ket[0]);
    

#Matriz Compleja --> ket1
#Matriz Compleja --> ket2
"""
ket1=[[((2**0.5/2),0),(0,(2**0.5/2))]]
ket2=[[(0,(2**0.5/2)),(-(2**0.5/2),0)]]
amplitudTransicion(ket1,ket2)
"""
def amplitudTransicion(ket1,ket2):    
    rta=multiplicacionDeMatricesComplejas(ket1,Bra(ket2))
    a=0
    b=0
    for i in range(len(rta)):
        a+=float("%.4f" % (rta[0][0][0]))
        b+=float("%.4f" % (rta[0][0][1])) 
    return (a,b)


class TestUM(unittest.TestCase):
    #probabilidad
    def test_caso_probabilidad_1(self):
        self.assertEqual(0.052632,probabilidad([(-3,-1),(0,-2),(0,1),(2,0)],2))
    
    #amplitudTransicion
    def test_caso_amplitudTransicion_1(self):
        ket1=[[((2**0.5/2),0),(0,(2**0.5/2))]]
        ket2=[[(0,(2**0.5/2)),(-(2**0.5/2),0)]]
        self.assertEqual((0.0, -1.0),amplitudTransicion(ket1,ket2))        
    

if __name__ =='__main__':
    unittest.main()


