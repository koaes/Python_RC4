#Name: RC4 Encoder/Decoder Program
#Date: 2015/07/15

#Key Info: Capable of using Hex or Ascii key
# Hex Key Format; must be spaced. Make sure you use correct KSA below
#key = '10 20 30 40 50 60 70 80 90 11 12 13 1A FF EE 48'
#key = key.split(" ")

# ASCII Key Format
key = 'YnJiYm90'
key = '0006'


#data = "ea 65 ba f2 a8 64 e9 bf d1 1c 03 60 ba dd 69 e6 14 fa 7b e8"
#data = "75 d6 00 9c 38 04 00 00" 
#data = "b8 9c c3 aa df 98 67 0e 38 b3 e6 68 27 1a"
data = "ea 49 7f 6b d6 55 5b a8 51 27 ce 08 3a 51 3b e8"
#The data above is the plaintext used in the Talos blog.  It should generate
#a key stream of 21 5f 44 38 96 26 1e f1 1f fc 25 e6 46 ce 33 36; ciphertext of
# cb 16 3b 53 40 73 45 59 4e db eb ee 7c 9f 08 de.

data = data.split(" ")

box = range(256)
x = 0

# KSA Generation
for i in range(256):
    #print int(key[i % len(key)],16)

    #Use the ord when the key is ascii
    x = (x + box[i] + ord(key[i % len(key)])) % 256

    #use this one if its hex
    #x = (x + box[i] + int(key[i % len(key)],16)) % 256

    box[i] , box[x] = box[x] , box[i]




x = 0
y = 0 
for char in data:
#for char in range(256):  #if you switch to this for loop, it will display the key cipher

    #print char     
    x = ( x + 1 ) % 256
    y = (y + box[x]) % 256
    box[x] , box[y] = box[y] , box[x]
    #print (chr(int(char,16) ^ box[(box[x] + box[y]) % 256]))

    #Encoder Version; used if Data above is plaintext
    #print (hex(int(char,16) ^ box[(box[x] + box[y]) % 256]))

    #Decoder version; used if Data is encrypted
    keystream = hex(box[(box[x] + box[y]) % 256])
    ciphertext = hex(box[(box[x] + box[y]) % 256] ^ int(char,16))

    print "PT: " + char + "  KS: " + str(keystream) + "   CT: " + ciphertext
