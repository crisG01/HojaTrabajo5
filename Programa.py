import random
import simpy
def programa(N,T,C,P):
    global prom  
    yield T.timeout(C)
    inicio = T.now
    espacio = random.randint(1, 10)
    print (str(N) + ' llego a las ' + str(inicio) + ' y su duracion es de ' + str(espacio) )
    with P.request() as corrida:
        yield corrida
        yield T.timeout(espacio) 
        print (str(N)+' sale de gasolinera a las '+ str(T.now) )  
    duracion = T.now - inicio
    print (str(N)+' se tardo '+str(duracion))
    prom = prom + duracion
T = simpy.Environment() 
P = simpy.Resource(T,capacity = 3)
random.seed(5)
prom = 0
for i in range(150):
    T.process(programa('Programa %d'%i,T,random.expovariate(1.0/10),P))
T.run(until=100)  
print ("El promedio de los programas es: ", prom/150.0)
print("Programas utilizados 150")