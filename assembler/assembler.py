registers_32bit = {
    "eax": "000",
    "ecx": "001",
    "edx": "010",
    "ebx": "011",
    "esp": "100",
    "esi": "110",
    "edi": "111",
    "ebp": "101"
}
registers_16bit = {
    "ax": "000",
    "cx": "001",
    "dx": "010",
    "bx": "011",
    "sp": "100",
    "si": "110",
    "di": "111",
    "bp": "101"
}
registers_8bit = {
    "al": "000",
    "cl": "001",
    "dl": "010",
    "bl": "011",
    "ah": "100",
    "ch": "101",
    "dh": "110",
    "bh": "111"
}
reg8b = ["al", "cl", "dl", "ah", "ch", "dh", "bh"]
reg16b = ["ax", "cx", "dx", "bx", "sp", "si", "di", "bp"]
reg32b = ["eax", "ecx", "edx", "ebx", "esp", "esi", "edi"]
registers = ["al", "cl", "dl", "ah", "ch", "dh", "bh", "ax", "cx", "dx", "bx", "sp", "si", "di", "bp", "eax", "ecx",
             "edx", "ebx", "esp", "esi", "edi"]

InstructionOpCode = {
    "add": "000000",
    "sub": "001010",
    "and": "001000",
    "or": "000010",
    "xor": "001100",
    "push": "110010",
    "pop": "110110",
}

file_path = "AssemblyProject1.txt"

with open(file_path, 'r') as file:
    code = file.read()

lines = code.splitlines()
addressCounter = 0

for line in lines:
    number = []
    index = 0
    output = ""

    splitT = line.split(" ")
    instructions = splitT[0].lower()
    regs = splitT[1].split(",")
    if len(regs) == 2:
        first_arg = regs[0].lower()
        second_arg = regs[1].lower()
    elif len(regs) == 1:
        first_arg = regs[0].lower()

    if instructions == "add" and first_arg in registers_32bit and second_arg in registers_32bit:
        output += instructions.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(InstructionOpCode["add"] + "01" + '11' + registers_32bit[second_arg] + registers_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
        addressCounter += 2
        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        print(output.upper())
        index += 1
        output = ""

    elif instructions == "add" and first_arg in registers_16bit and second_arg in registers_16bit:
        output += instructions.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(InstructionOpCode["add"] + "01" + '11' + registers_16bit[second_arg] + registers_16bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
        addressCounter += 2
        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": 66 "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        print(output.upper())
        index += 1
        output = ""

    elif instructions == "add" and first_arg in registers_8bit and second_arg in registers_8bit:
        output += instructions.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(InstructionOpCode["add"] + "00" + '11' + registers_8bit[second_arg] + registers_8bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
        addressCounter += 2
        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        print(output.upper())
        index += 1
        output = ""

    elif instructions == "sub" and first_arg in registers_32bit and second_arg in registers_32bit:
        output += instructions.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(InstructionOpCode["sub"] + "01" + '11' + registers_32bit[second_arg] + registers_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
        addressCounter += 2
        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        print(output.upper())
        index += 1
        output = ""

    elif instructions == "sub" and first_arg in registers_16bit and second_arg in registers_16bit:
        output += instructions.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(InstructionOpCode["sub"] + "01" + '11' + registers_16bit[second_arg] + registers_16bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
        addressCounter += 2
        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": 66 "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        print(output.upper())
        index += 1
        output = ""

    elif instructions == "sub" and first_arg in registers_8bit and second_arg in registers_8bit:
        output += instructions.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(InstructionOpCode["sub"] + "00" + '11' + registers_8bit[second_arg] + registers_8bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
        addressCounter += 2
        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        print(output.upper())
        index += 1
        output = ""


