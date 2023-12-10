# # ADD as same as MOV
#
# # MOV reg,reg
# # MOV mem,reg
# # MOV reg,mem
# # MOV mem,imm
# # MOV reg,imm
registers_32bit = {'EAX': "000", 'EBX': "011", 'ECX': '001', 'EDX': '010', 'ESI': '110', 'EDI': '111'}

import re


# Assuming your code is stored in a file named "code.txt"
file_path = "AssemblyProject1.txt"

# Read the content of the file
with open(file_path, 'r') as file:
    code = file.read()

# Split each line into components (operation, operand1, operand2)
lines = code.split('\n')

for line in lines:
    number = []
    components = re.split(r'\s|,\s*', line)
    instructions = components[0].upper()
    first_arg = components[1].upper()
    second_arg = components[2].upper()
    print(instructions, first_arg, second_arg)

    if instructions == "ADD" and first_arg in registers_32bit and second_arg in registers_32bit:
        # Append a specific string to the number list
        number.append('00000001' + '11' + registers_32bit[second_arg]+registers_32bit[first_arg])
        print(number[0])