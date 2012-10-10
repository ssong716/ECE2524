#ECE2524 Homework 2 Problem 2

from sys import argv

script, name = argv

file = open(name+'.txt')
f = file.read()

firstname1 = f.split()[0]
lastname1 = f.split()[1]
moneyOwed1 = float(f.split()[2])
city1 = f.split()[3]
phoneNumber1 = f.split()[4]
    
firstname2 = f.split()[5]
lastname2 = f.split()[6]
moneyOwed2 = float(f.split()[7])
city2 = f.split()[8]
phoneNumber2 = f.split()[9]
    
firstname3 = f.split()[10]
lastname3 = f.split()[11]
moneyOwed3 = float(f.split()[12])
city3 = f.split()[13]
phoneNumber3 = f.split()[14]
	
firstname4 = f.split()[15]
lastname4 = f.split()[16]
moneyOwed4 = float(f.split()[17])
city4 = f.split()[18]
phoneNumber4 = f.split()[19]

firstname5 = f.split()[20]
lastname5 = f.split()[21]
moneyOwed5 = float(f.split()[22])
city5 = f.split()[23]
phoneNumber5 = f.split()[24]

firstname6 = f.split()[25]
lastname6 = f.split()[26]
moneyOwed6 = float(f.split()[27])
city6 = f.split()[28]
phoneNumber6 = f.split()[29]


total = (moneyOwed1+moneyOwed2+moneyOwed3+moneyOwed4+moneyOwed5+moneyOwed6)
average = total/6
maximum = moneyOwed3
minimum = moneyOwed2

print "ACCOUNT SUMMARY"
print "Total amount owed =", ("%.2f" %total)
print "Average amount owed=", ("%.2f" %average)
print "Maximum amount owed=", ("%.2f" %maximum)
print "Minimum amount owed=", ("%.2f" %minimum)

	
