#Oppgave 1
def ascii_fugl():
    print """      \/_
  \,   /( ,/
   \\\\\\' ///
    \_ /_/
    (./
     '` """
    return
ascii_fugl();

#Oppgave 2
def bitAnd(x, y):
    return x & y
    
print bitAnd (5, 6)

#Oppgave 3
def bitXor(x, y):
    return x ^ y
    
print bitXor (4, 5)

#Oppgave 4
def bitOr(x, y):
    return x|y
    
print bitOr(0, 1)

#Oppgave 5
def ascii8Bin(x):
    bin1 = ord(x)    
    toBin = "{0:08b}".format(bin1)
    return toBin
    
print ascii8Bin('A')

#Oppgave 6
def transferBin(string):
    l = list(string)
    for c in l: 
           print ascii8Bin(c)

	
transferBin("Hi")

#Oppgave 7
def ascii2Hex(x):
    hex1 = ord(x)
    toHex = "{0:08x}".format(hex1)
    return toHex

def transferHex(string):
    l = list(string)
    for c in l:
            print ascii2Hex(c)
            
transferHex("Hi")



