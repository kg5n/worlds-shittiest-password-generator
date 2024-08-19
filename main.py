import random
 
passwrd = ''
length = 30
for _ in range(length):
  bits = random.getrandbits(8)
  num = (int('{0:b}'.format(bits),2) + 33) % 127
  passwrd+= chr(num)

print(passwrd)
