" https://eprint.iacr.org/2014/946.pdf "

import sys
from Crypto.Util.number import getRandomNBitInteger

def ModDiv(A,B,C) :
   return (A % B ) // C

l = sys.argv[1]
m = sys.argv[2]
p = sys.argv[3]
q = sys.argv[4]

try:

  l = int(l)
  m = int(m)
  p = int(p)
  q = int(q)
except ValueError:
  print('Invalid Arguments')

if m + q >= p :
   print("")
   print("Public Parameter l = %d" %l)
   print("Public Parameter m = %d" %m)
   print("Public Parameter p = %d" %p)
   print("Public Parameter q = %d" %q)
   print("")
   print('Condition (p > m + q) is not fulfilled !')

else :

   " Size in bits of public pararameter Z is l "
   Z = getRandomNBitInteger(l,randfunc=None)

   " Size in bits of private parameters X and Y is m "
   X = getRandomNBitInteger(m,randfunc=None)
   Y = getRandomNBitInteger(m,randfunc=None)

   M = pow(2,p)

   M1 = pow(2,p-q)

   D = pow(2,q)

   D1 = pow(2,m)

   " In approximately 30 % percents, the keys computed by Alice and Bob are not identical "
   " their difference is one, this is due to bit carry propagation, In order that public key "
   " algorithms presented in this paper function properly all the time, some least significant " 
   " bits of the two numbers to compare should be removed : replace the last instruction by the " 
   " following : "

   #D1 = pow(2,m+10)

   U =  ModDiv(Z*X,M,D) 

   V = ModDiv(Z*Y,M,D)
   
   Wx = ModDiv(U*Y,M1,D1)

   Wy = ModDiv(V*X,M1,D1)

   print("")  
   print("Public Parameters :")
   print("===================")
   print("")      
         
   print("Public Parameter l = %d" %l)

   print("Public Parameter m = %d" %m)

   print("Public Parameter p = %d" %p)

   print("Public Parameter q = %d" %q)

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

   " If the actual size of exchanged key is not equal to (p-q)-m , it is because some "
   " most significant bits of exchanged key are zeroes. "

   print("p Size : %d " % p)
   print("q Size : %d " % q)
   print("m Size : %d " % m)
   print("Secret Key Size (p-q)-m : %d " %Wx.bit_length())

   print("") 

   print("Secret key computed by Alice Wx = %d" %Wx)
   print("Secret key computed by Bob   Wy = %d" %Wy)

   print("")

sys.exit





