

import sys
from Crypto.Util.number import getRandomNBitInteger

def ModDiv(A,B,C) :
   return (A % B ) // C



l = 4992
m = 2432
p = 4992
q = 2432
r = 28

" Size in bits of public pararameter A is l "
A = getRandomNBitInteger(l,randfunc=None)

" Size in bits of private parameters X and Y is m "
X = getRandomNBitInteger(m,randfunc=None)
Y = getRandomNBitInteger(m,randfunc=None)

M = pow(2,p)

M1 = pow(2,p-q)

D = pow(2,q)

D1 = pow(2,m + r)

" If r = 0,  In 50 \% percents, the keys computed by Alice and Bob are not identical : " 
" $W_a = W_b \pm 1$, this is due to bit carry propagation, if r is increased by one " 
" the probability that Wx is diffrent to Wy is devided by two.  " 

U =  ModDiv(A*X,M,D) 

V = ModDiv(A*Y,M,D)
   
Wa = ModDiv(U*Y,M1,D1)

Wb = ModDiv(V*X,M1,D1)

print("")  
print("Public Parameters :")
print("===================")
print("")      
         
print("Public Parameter l = %d" %l)
print("") 
print("Public Parameter m = %d" %m)
print("") 
print("Public Parameter p = %d" %p)
print("") 
print("Public Parameter q = %d" %q)
print("") 
print("Public Parameter r = %d" %r)
print("") 
print("Public Parameter A = %d" %A)
print("")   

print("Private Parameters :")
print("====================")
print("")            

print("Alice Private Parameter X = %d" %X)
print("") 
print("Bob Private Parameter   Y = %d" %Y)
   
print("")   

print("Shared Parameters :")
print("=============")
print("")         

print("Parameter shared with Bob by Alice U = %d" %U)
print("") 
print("Parameter shared with Alice by Bob V = %d" %V)
   
print("")

print("Exchanged Secret Key :")
print("======================")
print("")

print("Secret key computed by Alice Wa = %d" %Wa)
print("") 
print("Secret key computed by Bob   Wb = %d" %Wb)

print("")

sys.exit
