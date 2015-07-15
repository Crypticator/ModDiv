" https://eprint.iacr.org/2014/946.pdf "


import sys
from Crypto.Util.number import getRandomNBitInteger

def ModDiv(A,B,C) :
   return (A % B ) // C

l = sys.argv[1]
m = sys.argv[2]
p = sys.argv[3]
q = sys.argv[4]
r = sys.argv[5]

try:

  l = int(l)
  m = int(m)
  p = int(p)
  q = int(q)
  r = int(r)
except ValueError:
  print('Invalid Arguments')

if m + q + r >= p :
   print("")
   print("Public Parameter l = %d" %l)
   print("Public Parameter m = %d" %m)
   print("Public Parameter p = %d" %p)
   print("Public Parameter q = %d" %q)
   print("Public Parameter r = %d" %r)
   print("")
   print('Condition (p > m + q + r) is not fulfilled !')

else :

   " Size in bits of public pararameter Z is l "
   Z = getRandomNBitInteger(l,randfunc=None)

   " Size in bits of private parameters X and Y is m "
   X = getRandomNBitInteger(m,randfunc=None)
   Y = getRandomNBitInteger(m,randfunc=None)

   M = pow(2,p)

   M1 = pow(2,p-q)

   D = pow(2,q)

   D1 = pow(2,m + r)

   " If r = 0,  In 30 \% percents, the keys computed by Alice and Bob are not identical : " 
   " $W_a = W_b \pm 1$, this is due to bit carry propagation, if r is increased by one " 
   " the probability that Wx is diffrent to Wy is devided by two.  " 

   U =  ModDiv(Z*X,M,D) 

   V = ModDiv(Z*Y,M,D)
   
   Wa = ModDiv(U*Y,M1,D1)

   Wb = ModDiv(V*X,M1,D1)

   print("")  
   print("Public Parameters :")
   print("===================")
   print("")      
         
   print("Public Parameter l = %d" %l)

   print("Public Parameter m = %d" %m)

   print("Public Parameter p = %d" %p)

   print("Public Parameter q = %d" %q)

   print("Public Parameter r = %d" %r)

   print("Public Parameter Z = %d" %Z)
   print("")   

   print("Private Parameters :")
   print("====================")
   print("")            

   print("Alice Private Parameter X = %d" %X)
   print("Bob Private Parameter   Y = %d" %Y)
   
   print("")   

   print("Shared Parameters :")
   print("=============")
   print("")         

   print("Parameter shared with Bob by Alice U = %d" %U)
   print("Parameter shared with Alice by Bob V = %d" %V)
   
   print("")

   print("Exchanged Secret Key :")
   print("======================")
   print("")

   print("Secret key computed by Alice Wa = %d" %Wa)
   print("Secret key computed by Bob   Wb = %d" %Wb)

   print("")

sys.exit
