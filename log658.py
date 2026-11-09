import math 

bas=int(input("base:"))
arg=int(input("argomento:"))

def cambiamento(): 
  x = math.log(arg)/math.log(bas)
  x = round(x,4)
  print("Logaritmo:", x)

if arg > 0: 
  cambiamento()
