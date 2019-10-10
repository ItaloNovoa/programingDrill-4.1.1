# programingDrill-4.1.1

en este laboratorio miraremos  la probabilidad de que una particula este en un punto dado un vector ket de probailidad  y la amplitud de transicion de un ket a otro

### programingDrill-4.1.1
Write a program that simulates the first quantum system described
in this section. The user should be able to specify how many points the particle
can occupy (warning: keep the max number low, or you will fairly quickly run out of
memory). The user will also specify a ket state vector by assigning its amplitudes.
The program, when asked the likelihood of finding the particle at a given point, will
perform the calculations described in Example 4.1.1. If the user enters two kets, the
system will calculate the probability of transitioning from the first ket to the second,
after an observation has been made.


- Probabilidad
  - Descripcion entrada 
    - Vector -> ket
    - Entero -> Posicion de la cual se quiere ver la probabilidad de la particula
   - Entrada
   ~~~~
    probabilidad([(-3,-1),(0,-2),(0,1),(2,0)],2)
   ~~~~

- Amplitud
  - Descripcion entrada 
    - Vector -> ket1
    - Vector -> ket2
   - Entrada
   ~~~~
    ket1=[[((2**0.5/2),0),(0,(2**0.5/2))]]
     ket2=[[(0,(2**0.5/2)),(-(2**0.5/2),0)]]
    amplitudTransicion(ket1,ket2)
   ~~~~




# Pruebas
#### Al compilar el archivo automaticamente se ejecutan 15 pruebas que verifican todas las operaciones especificadas anteriormente.
#### para ejecutar el archivo matrices.py sigua las siguientes intrucciones:

1. Descargue el repositorio
~~~~
git clone https://github.com/ItaloNovoa/lab2-CNYT.git
~~~~
2. Ingrese al cmd/Terminal o simbolo del sistema
3. Ingresar a la carpeta de archivo 
4. digitar (Windows):
~~~~
python  lab4CNYT.py 
~~~~ 
4.digitar (Ubuntu, Mac)
~~~~
python3 lab4CNYT.py
~~~~
