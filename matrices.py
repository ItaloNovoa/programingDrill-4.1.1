
import unittest

"""
C ->  Numeros Complejos
m1,m2 E C^(n*m) ^ m1,m2 E C^(n)
c,c1,c2 E C
"""


#ejemplo
#sumaMatrices([[[3,2],[4,-2]],[[1,2],[3,2]]],[[[5,-6],[7,2]],[[2,5],[-12,-9]]])
def sumaMatrices(m1,m2):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0]+m2[i][j][0],m1[i][j][1]+m2[i][j][1]))
        matriz.append(vector)
    return matriz



#ejemplo
#negativaMatriz([[[5,-6],[7,2]],[[2,5],[-12,-9]]])
def negativaMatriz(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0]*-1,m1[i][j][1]*-1))
        matriz.append(vector)
    return matriz

#ejemplo
#complejoPorMatriz((3,1),[[(1,0),(1,0),(1,0)]])
def complejoPorMatriz(c1,m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append(producto(m1[i][j],c1))
        matriz.append(vector)
    return matriz

#ejemplo
#transpuesta([[(3,2),(4,2)],[(5,1),(6,3)]])
def transpuesta(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append(m1[j][i])
        matriz.append(vector)
    return matriz

#ejemplo
#conjugada([[(3,2),(4,2)],[(5,1),(6,3)]])
def conjugada(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0],m1[i][j][1]*-1))        
        matriz.append(vector)
    return matriz

#ejemplo
#adjunta([[(3,2),(4,2)],[(5,1),(6,3)]])
def adjunta(m1):
    matriz=transpuesta(m1)
    matriz=conjugada(matriz)
    return matriz


#Ejemplos
#m1=[[(1,0),(2,0),(-3,0)],[(4,0),(0,0),(-2,0)]]
#m2=[[(3,0),(1,0)],[(2,0),(4,0)],[(-1,0),(5,0)]]
#m2=[[(1,0)],[(1,-2)],[(0,-1)]]
#m1=[[(3,0),(1,2),(0,-1)],[(2,-1),(0,0),(1,0)],[(0,0),(4,3),(0,1)]]
def multiplicacionDeMatrices(m1,m2):
    matriz=[]
    for i in range(len(m1)):
        vector=[]        
        for j in range(len(m2[i])):
            suma=(0,0)
            for k in range (len(m2)):                
                if(len(m1[i])!=len(m2)):
                    return "mala entrada"
                else:
                    suma=sumas(suma,producto(m1[i][k],m2[k][j]))
            vector.append(suma)
        matriz.append(vector)

    return matriz

#Ejemplo
#m1=[[(2.8,5.8),(3.4,-8.4)]]
#Norma(m1)
def Norma(m1):
    resultado=(0,0)
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            resultado=sumas(producto(m1[i][j],conjugado(m1[i][j])),resultado)
    return resultado[0]**0.5

#EJEMPLO
#m1=[[(2.8,5.8),(3.4,-8.4)]]
#distancia(m1,m1)
def distancia(m1,m2):
    resultado=(0,0)
    if(len(m1)-len(m2)!=0):
        return "las dimensiones deben ser iguales"
    else:
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                resultado=sumas(producto(resta(m1[i][j],m2[i][j]),resta(conjugado(m1[i][j]),conjugado(m2[i][j]))),resultado)
        return resultado[0]**0.5

#EJEMPLO
#m1=[[(1,0),(0,0),(0,0)],[(0,0),(0,0),(1,0)],[(0,0),(1,0),(0,0)]]
#Unitario(m1)
def Unitaria(m1):
    MatrizIdentidad=[[(1,0) if j == i else (0,0) for j in range(len(m1))] for i in range(len(m1))]
    for i in range(len(m1)):
        if(len(m1)!=len(m1[i])):
            return "la matriz debe ser de mXm"        

    if(multiplicacionDeMatrices(m1,adjunta(m1))==MatrizIdentidad):
        return True
    else:
        return False
    
    

#Ejemplo
#m1=[[(5,0),(4,5),(6,-16)],[(4,-5),(13,0),(7,0)],[(6,16),(7,0),(-2.1,0)]]
#Hermitian(m1):    
def Hermitian(m1):
    if(len(m1[0])!=len(m1[1])):
        return "la matriz debe ser de mXm"
    elif(m1==adjunta(m1)):
        return True
    else:
        return False
# m1=[[(2,0),(3,0)]]
# m2=[[(4,0),(6,0),(3,0)]]
def ProductoTensor(m1,m2):
    LaMegaMatriz=[]
    #[[(0,0)]*(len(m1[0])*len(m2[0]))]*(len(m1)*len(m2))
    for i in range(len(m1)):
        LaMatriz=[[]]*len(m2)
        for j in range(len(m1[i])):            
            m3=complejoPorMatriz(m1[i][j],m2)
            for k in range(len(m2)):
                LaMatriz[k]=LaMatriz[k]+m3[k]
        for k in range(len(m2)):
            LaMegaMatriz.append(LaMatriz[k])
        
    return LaMegaMatriz
                        

            

#------------------------------COMPLEMENTOS------------------------------

       
#recibe dos tuplas con una parte real y otra imaginaria
#EJEMPLO --> (3,-4),(-5,18)
def sumas(c1,c2):
    preal=c1[0]+c2[0]
    pimaginaria=c1[1]+c2[1]
    return (preal,pimaginaria)

#recibe una tupla con una parte real y otra imaginaria
#EJEMPLO --> (3,-4)
def conjugado(c1):
    return (c1[0],(c1[1]*-1))

#recibe dos tuplas con una parte real y otra imaginaria
#EJEMPLO --> (3,-4),(-5,18)
def resta(c1,c2):
    preal=c1[0]-c2[0]
    pimaginaria=c1[1]-c2[1]
    return (preal,pimaginaria)

def multiplicacionDeMatricesComplejas(m1,m2):
    matriz=[]
    for i in range(len(m1)):
        vector=[]        
        for j in range(len(m2[i])):
            suma=(0,0)
            for k in range (len(m2)):                
                if(len(m1[i])!=len(m2)):
                    return "mala entrada"
                else:
                    suma=sumas(suma,producto(m1[i][k],m2[k][j]))
            vector.append(suma)
        matriz.append(vector)

    return matriz


def bonita(mi):
    for i in range(len(mi)):
        for j in range(len(mi[i])):
            print(("%.2f" % mi[i][j]), end= " ") 
        print()

def bonitaCompleja(mi):
    for i in range(len(mi)):
        for j in range(len(mi[i])):
            if((mi[i][j][1])>0):
                print(str(mi[i][j][0])+"+"+str(mi[i][j][1])+"i", end= " "*(7-(len(str(mi[i][j][0])))+len(str(mi[i][j][1]))))
            elif((mi[i][j][1])==0):
                print(str(mi[i][j][0]), end= " "*(7-len(str(mi[i][j][0]))))
            else:
                print(str(mi[i][j][0])+str(mi[i][j][1])+"i", end= " "*(7-(len(str(mi[i][j][0])))+len(str(mi[i][j][1]))))
        print()



def multiplicacionDeMatricesN(m1,m2):
    matriz=[]
    for i in range(len(m1)):
        vector=[]        
        for j in range(len(m2[i])):
            suma=0
            for k in range (len(m2)):                
                if(len(m1[i])!=len(m2)):
                    return "mala entrada 1"
                else:
                    suma+=m1[i][k]*m2[k][j]
            vector.append(suma)
        matriz.append(vector)
    return matriz
    
def transpuestaVector(v1):
    matriz=[]
    for i in range(len(v1)):
        vector=[v1[i]]
        matriz.append(vector)
    return matriz

def producto(c1,c2):
    pr=(c1[0]*c2[0])-(c1[1]*c2[1])
    pi=(c1[0]*c2[1])+(c2[0]*c1[1])
    return (pr,pi)



    

