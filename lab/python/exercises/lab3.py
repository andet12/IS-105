# -*- coding: latin-1 -*-

#
#  IS-105 LAB3
#
#  lab3.py - kildekode som inneholder studentenes løsning.
#         
#
#
import sys
import os
import subprocess
import re

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Anders Thingelstad', \
			'student2': 'Fredrik Sverdrup Lilleeng', \
            'student3': 'Fredrik Sjulstad', \
}

#
#  Oppgave 1
#    Skrive test1.sh, test1.pl og test1.py.
#	 Se teksten til LAB3 for mer detaljer.
#    Kalle disse opp fra en funksjon lab3_scripts()
#    vha. Python modulen subprocess
#    Funksjonen kalles opp på slutten av denne filen
#    Eksempel:
#      subprocess.call(["../scripts/test.sh"])
#      som skal returnere
#      1 a
#      1 b
#      1 c
#      ....
#      3 c
#
# Din funksjonsimplementering skrives her ...

def lab3_scripts():
    subprocess.call(["/home/anders/IS-105/lab/scripts/test1.sh"])
    subprocess.call(["/home/anders/IS-105/lab/scripts/test1.pl"])
    subprocess.call(["/home/anders/IS-105/lab/python/test1.py"])

#def lab3_scripts():
    #subprocess.call(["/home/anders/test1.sh"])
    #subprocess.call(["/home/anders/test1.pl"])
    #subprocess.call(["/home/anders/test1.py"])


#
#  Oppgave 2
#    Funksjonen min_sys_info() skriver ut systeminformasjon
#    til det miljøet (maskinen) den blir utført på.
#
#    Kopier resultatet som kjøring av denne funksjonen gir og 
#    lim inn her som kommentar.
#
def min_sys_info():
	"""
	Her er mitt resultat av kjøringen av denne funksjonen:
   
    byteorder: little
    os data: 
    ('Linux', 'localhost.localdomain', '2.6.32-431.el6.i686', '#1 SMP       Fri Nov 22 00:26:36 UTC 2013', 'i686')
    os bruker: anders
	"""
	print "byteorder: " + sys.byteorder
	print "os data: "
	print os.uname()
	print "os bruker: " + os.getlogin()
	



#
#  Oppgave 3
#    Jobbe med symboler (bokstaver og tall)
#	 Utforske str.find funksjon fra Python Standard Library
#    
#    Ved hjelp av str.find funksjonen implementer funksjon
#    initialer(navn), som gjør et personnavn med både
#	 fornavn og etternavn til initialer.
#    
#    Eksempel:
#    initialer("Alf Bogen") returnerer "A.B."
#    initialer("Von Neuman") returnerer "V.N."
#    
#    Anta at inn-data er korrekt (ingen testing nødvendig)
#

def initialer(navn):
    str = navn
    print str[0] + "." + str[str.find(" ")+1] + "."

#
#  Oppgave 4
#    Ditt første møte med regulære uttrykk i Python (Perl stil)
#    Utførsk re.findall funksjonen fra Python modulen re
#    list = re.findall(regexp, str) (funksjon returnere en 
#	 liste av det som matcher regexp)
#    
#    Gitt to regulære uttrykk r"[0-9]+" og r"[+*\-\/] gjør 
#    om en infix-notasjon på et enkelt regnestykke 
#    (kun to operander og en operator) til en prefix-notasjon)
#    
#    Eksempel:
#    infix_to_prefix("2+3") skal gi "+ 2 3"
#    infix_to_prefix("234+6125") skal gi "+ 234 6125"
#    infix_to_prefix("3/4") skal gi "/ 3 4"
#
#    Anta at inn-data er korrekt, dvs. inneholder to 
#    operander (to tall) og en operatør (+, for eksempel).
#

def infix_to_prefix(infix):
    regexp1 = r"[0-9]+" # finner alle tall og holder sifre sammen
    regexp2 = r"[+*\-\/]" # finner alle operander

    operands = re.findall(regexp1, infix) # ['2','3']
    operator = re.findall(regexp2, infix) # +-/*

    print operator[0] + " " + operands[0] + " " + operands[1]

# Kaller opp implementerte funksjoner (pseudo-testing)
# For å teste innleveringen
print 5*"-" + " Studenter: " + 5*"-"
for s in gruppe.values():
	if s is not "-":
		print s

print 5*"-" + " mysysinfo() " + 5*"-"
print min_sys_info.__doc__
min_sys_info()

print 5*"-" + " initialer() " + 5*"-"
initialer("Wolfgang Goethe")

print 5*"-" + " infix_to_prefix() " + 5*"-"
infix_to_prefix("2+3")

# Kalle opp din lab3_scripts() funksjon her
print 5*"-" + " lab3_scripts() " + 5*"-"
lab3_scripts()



