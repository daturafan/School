print("Inserite il primo numero, poi il segno (*, /, ^) e infine il secondo numero. Separate da spazi")
print("")
x,s,y=(input("log")). split()
x=int(x)
y=int(y)

def prodotto(): 
  print("log", x, "", "+", "", "log", y)
def quoziente(): 
  print("log", x, "", "-", "", "log", y)
def potenza(): 
  print(y, "*", "log", x)

if s=="*":
  prodotto()

if s=="/":
  quoziente()

if s=="^": 
  potenza()
