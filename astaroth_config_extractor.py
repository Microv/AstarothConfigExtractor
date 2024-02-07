import sys
import base64


f = open(sys.argv[1],"r")
content = f.read()
f.close()

to_decrypt = base64.b64decode(content).decode('utf-8')

index = 0
key = ord(to_decrypt[0]) - 0x41
decrypted = ""

while(index < len(to_decrypt) - 2):

	elem = ord(to_decrypt[index+1])
	new_elem = (elem - 0x41) * 0x19
	elem_2 = ord(to_decrypt[index+2])
	new_elem_2 = (elem_2-0x41)
	new_elem = new_elem + new_elem_2 - key - 0x3F2
	decrypted += chr(new_elem)

	index += 2

print(decrypted)