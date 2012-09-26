import sys
import argparse


parser = argparse.ArgumentParser(description='')
parser.parse_args()
arg = parser.parse_args()
#parser.print_help()

total = 1.0
sys.stdout.write("Input Numbers to Multiply!!!\n")
try:
    while 1:        
        c = raw_input()
        if c.isspace():
            print total
            total = 1
            
        else:
            c = float(c)   
            total = total * c

except EOFError:
    print "^D"
    
except ValueError:
    print "Could not convert string to float: ", c
    exit(1)
    
       
print "Total: %r" %total
