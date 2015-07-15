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

if l + q + r >= p :
   print("")
   print("Public Parameter l = %d" %l)
   print("Public Parameter m = %d" %m)
   print("Public Parameter p = %d" %p)
   print("Public Parameter q = %d" %q)
   print("Public Parameter r = %d" %r)
   print("")
   print('Condition (p > l + q + r) is not fulfilled !')

else :

   " Size in bits of public pararameter Z is l "
   Z = getRandomNBitInteger(l,randfunc=None)

   " a hash value of a hypothetical file "
   H = getRandomNBitInteger(l,randfunc=None)

   " Size in bits of private parameters X and Y is m "
   X = getRandomNBitInteger(m,randfunc=None)
   Y = getRandomNBitInteger(m,randfunc=None)

   M = pow(2,p)

   M1 = pow(2,p-q)

   D = pow(2,q)

   D1 = pow(2,l + r)
   
   U =  ModDiv(Z*X,M,D) 

   S1 = ModDiv(Z*Y,M,D)

   S2 = ModDiv(H*(X+Y) ,M,D)

   Wa = ModDiv(H*(S1+U),M1,D1)

   Wb = ModDiv(Z*S2,M1,D1)

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

   print("Public Parameter H = %d" %H)
   print("")   

   print("Private Parameters :")
   print("====================")
   print("")            

   print("Private Key X = %d" %X)
   print("Ephemeral Key   Y = %d" %Y)
   
   print("")   

   print("Signature:")
   print("==========")
   print("")         

   print("S1 = %d" %S1)
   print("S2 = %d" %S2)
   
   print("")

   print("Verification :")
   print("==============")
   print("")

   print("Wa = %d" %Wa)
   print("Wb = %d" %Wb)

   print("")

sys.exit





