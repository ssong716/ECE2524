#ECE2524 Homework 2 Problem 2

from sys import argv

script, name = argv

file = open(name+'.txt')
f = file.read()

firstname1 = f.split()[0]
lastname1 = f.split()[1]
moneyOwed1 = f.split()[2]
city1 = f.split()[3]
phoneNumber1 = f.split()[4]
    
firstname2 = f.split()[5]
lastname2 = f.split()[6]
moneyOwed2 = f.split()[7]
city2 = f.split()[8]
phoneNumber2 = f.split()[9]
    
firstname3 = f.split()[10]
lastname3 = f.split()[11]
moneyOwed3 = f.split()[12]
city3 = f.split()[13]
phoneNumber3 = f.split()[14]
	
firstname4 = f.split()[15]
lastname4 = f.split()[16]
moneyOwed4 = f.split()[17]
city4 = f.split()[18]
phoneNumber4 = f.split()[19]
 
print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
print phoneNumber1+ ',',  lastname1+ ',', firstname1+ ',', moneyOwed1
print phoneNumber2+ ',',  lastname2+ ',', firstname2+ ',', moneyOwed2
print phoneNumber3+ ',',  lastname3+ ',', firstname3+ ',', moneyOwed3
print phoneNumber4+ ',',  lastname4+ ',', firstname4+ ',', moneyOwed4

	
