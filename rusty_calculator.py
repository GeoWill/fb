# -*- coding: utf-8 -*-
"""
Created on Thu May 12 13:54:16 2016

@author: s0568630
"""

def answer(mystr):
    output = []
    opstack =[]
    precedence = {"*":2,"+":1}
    for char in mystr:
        print '\nstart loop'
        print 'char: ',char
        print 'output: ',output
        print 'opstack: ',opstack
        if char.isdigit():
            output.append(char)
        else:
            if len(opstack) == 0:
                opstack.append(char)
            elif precedence[char] >= precedence[opstack[-1]]:
                opstack.append(char)
            else:
                while len(opstack) != 0 and precedence[char] < precedence[opstack[-1]]:
                    output.append(opstack.pop())
                opstack.append(char)
        print 'output: ',output
        print 'opstack: ',opstack
        print 'end loop\n'
            
    print 'output: ',output
    print 'opstack[::-1]: ',opstack[::-1]
    output = output + opstack[::-1]
    
    return ''.join(output)
            
    
    
print answer("2+3*2")
print answer("2*4*3+9*3+5")


#2 3 * => 6
#4 9 + 2 * 3 + => 13 2 * 3 + => 26 3 + => 29
#
#Inputs:
#    (string) str = "2+3*2"
#Output:
#    (string) "232*+"
#
#Inputs:
#    (string) str = "2*4*3+9*3+5"
#Output:
#    (string) "243**93*5++"