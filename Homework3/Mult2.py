import sys
import argparse
import fileinput
import math

parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='*', type=str,
                    default=sys.stdin)
parser.add_argument("--ignore-blank", action='store_true', dest='ignore_blank', help="ignores the blank line")
parser.add_argument("--ignore-non-numeric", action='store_true', dest='ignore_non_numeric', help='ignore the non-numeric line')
args = parser.parse_args()                

total = 1.0

"""
for line in fileinput.input():
    if fileinput.isstdin():
        if line == '\n':
            if args.ignore_blank:
                continue
            
            else:
                print total
                total = 1 
           
        else:
            try:
                total *= float(line)
            except Exception as err: 
                if args.ignore_non_numeric:
                    continue
                else:
                    sys.stderr.write(str(err))
                    sys.exit(1)        
        print total
    
    else:
        for line in fileinput.input(args.infile):
            if line == '\n':
                if args.ignore_blank:
                   continue
            
                else:
                    print total
                    total = 1 
           
        else:
            try:
                total *= float(line)
            except Exception as err: 
                if args.ignore_non_numeric:
                    continue
                else:
                    sys.stderr.write(str(err))
                    sys.exit(1)        
        print total
"""    
    
if (len(sys.argv) > 1):
    for line in fileinput.input(args.infile):
        if line == '\n':
            if args.ignore_blank:
                continue
            
            else:
                print total
                total = 1 
           
        else:
            try:
                total *= float(line)
            except Exception as err: 
                if args.ignore_non_numeric:
                    continue
                else:
                    sys.stderr.write(str(err))
                    sys.exit(1)        
    print total


else:
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
    
    print total

