#! /usr/bin/python3
import sys

#Vegenere Cipher: Encryption + Decryption

def errorm():
  print('Usage: vegenere [key] [plaintext/ciphertext]')
  
def errorm2():
  print('please put in "e"(encryption) or "d"(decryption) to operate!')
  

def get_key(val):
    for key, value in rot_list.items():
         if val == value:
             return key
 
    return "key doesn't exist"

key = sys.argv[1]
message = sys.argv[2]

print('Do you want to encrypt or decrypt a message? (e/d):')
answer = input()

#Dictionary für Verschiebung
rot_list = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,
'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,
'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,
'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

keylen = len(key)
messlen = len(message)

#Buchstaben in Zahlen umwandeln 
keylist = []             
for a in range(0, keylen):
  keylist.append(rot_list[key[a]])

#Fehler !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
messlist = []
for b in range(0, messlen):
  messlist.append(rot_list[message[b]])

    
#Verrechnung der beiden Listen miteinander

#wie oft wird der Schlüssel angewendet
fest = keylist
if (messlen/keylen) >= 1:
  iteration = int(messlen/keylen)
else:
  iteration = int(keylen/messlen)
for c in range(0, iteration):
  keylist = keylist + fest

#Encryption
if answer == 'e':
  
  #key > text 
  result = []
  if (messlen/keylen) >= 1:
    for d in range(0,messlen):
      result.append(messlist[d] + keylist[d])
  #key < text
  elif (messlen/keylen) <= 1:
    for e in range(0,keylen):
      result.append(messlist[e] + keylist[e])
  #key == text
  else:
    for f in range(0,keylen):
      result.append(messlist[f] + keylist[f])
  
  #Zahlen auf 26 begrenzen
  for g in range(0,len(result)):
    if (result[g]/26) > 1:
      result[g] = result[g]%26
  
  Cryptmess = []
  result_list = list(result)
  for h in range(0,len(result)):
    Cryptmess.append(get_key(result[h]))
  res_string=""
  for i in Cryptmess:
    res_string=res_string+i
  print(res_string)


  #Zahlen in Buchstaben umwandeln

#Decryption
elif answer == 'd':
    
  #key > text 
  result = []
  if (messlen/keylen) >= 1:
    for d in range(0,messlen):
      result.append(messlist[d] - keylist[d])
      if result[d] <= 0:
        result[d] = result[d] + 26
  #key < text
  elif (messlen/keylen) <= 1:
    for e in range(0,keylen):
      result.append(messlist[e] - keylist[e])
      if result[d] <= 0:
        result[d] = result[d] + 26
  #key == text
  else:
    for f in range(0,keylen):
      result.append(messlist[f] - keylist[f])
      if result[d] <= 0:
        result[d] = result[d] + 26
  
  #Zahlen auf 26 begrenzen
  for g in range(0,len(result)):
    if (result[g]/26) > 1:
      result[g] = result[g]%26

  Cryptmess = []
  result_list = list(result)
  for h in range(0,len(result)):
    Cryptmess.append(get_key(result[h]))
  res_string=""
  for i in Cryptmess:
    res_string=res_string+i
  print(res_string)

else:
  errorm2()

#Zahlen in Buchstaben umwandeln


