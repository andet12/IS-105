# -*- coding: latin-1 -*-

#
#  IS-105 LAB4
#
#  lab4.py - kildekode som inneholder studentenes løsning.
#         
#
#
import sys
import os
import subprocess
import re
import psutil # Kan installeres med "pip2.7 install psutil"

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Anders Thingelstad', \
			'student2': 'Fredrik Sjulstad', \
            'student3': 'Fredrik Sverdrup Lilleeng', \
}

# Oppgave 1
# 	Funksjonen lager en strukturert utskrift av resultater fra
#   kallet psutil.cpu_times(). 
#	Modulen psutil må være installert.
#
#   Utskriften skal være følgende (verdiene skal selvsagt være forskjellige):
#		user = 3088.16
#		nice = 0.99
#		system = 897.37
#		idle = 72353.81
#		iowait = 19.29
#		irq = 6.82
#		softirq = 3.07
#		steal = 0.00
#		guest = 0.00
#

def psutils_use():

    """
	Henter lister med systeminformasjon fra /proc og bearbeider disse
	"""

    namedtuple = psutil.cpu_times()
    
    fieldsList = namedtuple._fields
    
    tupleList = tuple(namedtuple)

    zipList = zip( fieldsList,tupleList )
    
    for linje in zipList:
        print "{} = {}".format(linje[0], linje[1]) 

psutils_use()


# Oppgave 2
#	Gitt følgende liste (inn-data):
# 	proglangs = [('Python', '1989', 'Guido van Rossum'), ('C', '1969', 'Dennis Ritchie'), ('Java/Oak', '1991', 'James Gosling'), ('C++', '1979', 'Bjarne Stroustrup'), ('Ruby', '1991', 'Yukihiro "Matz" Matsumoto'), ('Perl', '1987' , 'Larry Wall'), ('Go/golang', '2007', 'Robert Griesemer, Rob Pike, and Ken Thompson')]
#
#	skal funksjonen produsere følgende ut-data:
#
#		C ble startet 1969 av Dennis Ritchie.
#		C++ ble startet 1979 av Bjarne Stroustrup.
#		Perl ble startet 1987 av Larry Wall.
#		Python ble startet 1989 av Guido van Rossum.
#		Java/Oak ble startet 1991 av James Gosling.
#		Ruby ble startet 1991 av Yukihiro "Matz" Matsumoto.
#		Go/golang ble startet 2007 av Robert Griesemer, Rob Pike, and Ken Thompson.
#		
	
def print_history():

    proglangs = [('Python', '1989', 'Guido van Rossum'), ('C', '1969', 'Dennis Ritchie'), ('Java/Oak', '1991', 'James Gosling'), ('C++', '1979', 'Bjarne Stroustrup'), ('Ruby', '1991', 'Yukihiro "Matz" Matsumoto'), ('Perl', '1987' , 'Larry Wall'), ('Go/golang', '2007', 'Robert Griesemer, Rob Pike, and Ken Thompson')]

    sorted_liste = sorted(proglangs, key=lambda proglangs: proglangs[1])
    
    for tegn in sorted_liste:
        print "{} ble startet {} av {}" .format(tegn[0], tegn[1], tegn[2])
    
print_history()


# Standardkall for evalueringen
print 5*"-" + " Studenter: " + 5*"-"
for s in gruppe.values():
	if s is not "-":
		print s





