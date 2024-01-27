# some dictionary for defining registers memories and instruction opcode
import re

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
memory_32bit = {
    "[eax]": "000",
    "[ecx]": "001",
    "[edx]": "010",
    "[ebx]": "011",
    "[esp]": "100",
    "[esi]": "110",
    "[edi]": "111",
    "[ebp]": "101"
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
memory_16bit = {
    "[ax]": "000",
    "[cx]": "001",
    "[dx]": "010",
    "[bx]": "011",
    "[sp]": "100",
    "[si]": "110",
    "[di]": "111",
    "[bp]": "101"
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
memory_8bit = {
    "[al]": "000",
    "[cl]": "001",
    "[dl]": "010",
    "[bl]": "011",
    "[ah]": "100",
    "[ch]": "101",
    "[dh]": "110",
    "[bh]": "111"
}

InstructionOpCode = {
    "add": "000000",
    "sub": "001010",
    "and": "001000",
    "or": "000010",
    "xor": "001100",
    "push": "01010",
    "pop": "01011",
    "inc": "01000",
    "dec": "01001"
}


# this is a 16 complement for neg hexa numbers
def complement16(num):
    hexnum = [*num]
    for i in range(len(hexnum)):
        hexnum[i] = hex(15 - int(hexnum[i], 16))[2:]
    temp = "".join(hexnum)
    if len(hexnum) < 2:
        temp = "f" + temp
    return hex((int(temp, 16)) + 1)[2:]


# this function set offset(address) for instruction
def findCounterAddress(output):
    index = 0
    for i in range(len(output)):
        if (output[i]) == ":":
            index = i
            break
    index += 2
    out = ""
    for i in range(index, len(output)):
        out += output[i]
    cnt = len(out.split(" "))
    return cnt


def createStrIndexMemory(index):
    if index < 10:
        return "00" + str(index)
    elif index < 100:
        return "0" + str(index)
    else:
        return str(index)


# this is assembler function
def assembler(instruction, first_arg, second_arg, addressCounter):
    # define local vars
    number = []
    index = 0
    output = ""

    # if for reg reg mode
    if first_arg in registers_32bit and second_arg in registers_32bit:

        number.append(
            InstructionOpCode[instruction] + "01" + '11' + registers_32bit[second_arg] + registers_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")
        x = findCounterAddress(output)
        return x

    # if for reg/reg16
    elif first_arg in registers_16bit and second_arg in registers_16bit:

        number.append(
            InstructionOpCode[instruction] + "01" + '11' + registers_16bit[second_arg] + registers_16bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
        output += "66 "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")
        x = findCounterAddress(output)
        return x

    # if reg/reg8
    elif first_arg in registers_8bit and second_arg in registers_8bit:

        number.append(
            InstructionOpCode[instruction] + "00" + '11' + registers_8bit[second_arg] + registers_8bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")
        x = findCounterAddress(output)
        return x

    # if for memory/reg32
    elif first_arg in memory_32bit and second_arg in registers_32bit:

        number.append(
            InstructionOpCode[instruction] + "01" + '00' + registers_32bit[second_arg] + memory_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]

        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")
        x = findCounterAddress(output)
        return x
    # if for memory/reg16
    elif first_arg in memory_32bit and second_arg in registers_16bit:

        number.append(
            InstructionOpCode[instruction] + "01" + '00' + registers_16bit[second_arg] + memory_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
        output += "66 "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")
        x = findCounterAddress(output)
        return x
    # if for memory/reg8
    elif first_arg in memory_32bit and second_arg in registers_8bit:

        number.append(
            InstructionOpCode[instruction] + "00" + '00' + registers_8bit[second_arg] + memory_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]

        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")
        x = findCounterAddress(output)
        return x

    # if for reg32/memory
    elif first_arg in registers_32bit and second_arg in memory_32bit:

        number.append(
            InstructionOpCode[instruction] + "11" + '00' + registers_32bit[first_arg] + memory_32bit[second_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]

        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")
        x = findCounterAddress(output)
        return x

    # if for reg16/memory
    elif first_arg in registers_16bit and second_arg in memory_32bit:

        number.append(
            InstructionOpCode[instruction] + "11" + '00' + registers_16bit[first_arg] + memory_32bit[second_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
        output += "66 "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")
        x = findCounterAddress(output)
        return x

    # if for reg8/memory
    elif first_arg in registers_8bit and second_arg in memory_32bit:

        number.append(
            InstructionOpCode[instruction] + "10" + '00' + registers_8bit[first_arg] + memory_32bit[second_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]

        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        output += " "
        if len(second_print) == 1:
            output += "0" + second_print
        else:
            output += second_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")
        x = findCounterAddress(output)
        return x

    # if for one args mode reg32
    elif first_arg in registers_32bit:

        number.append(InstructionOpCode[instruction] + registers_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]

        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")
        x = findCounterAddress(output)
        return x

    # if for one args mode reg16
    elif first_arg in registers_16bit:

        number.append(InstructionOpCode[instruction] + registers_16bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        output += "66 "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")

        x = findCounterAddress(output)
        return x

    # if for inc
    elif first_arg in registers_8bit and instruction == "inc":

        number.append("11000" + registers_8bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        output += "fe "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")

        x = findCounterAddress(output)
        return x

    # if for reg8 and dec instruction
    elif first_arg in registers_8bit and instruction == "dec":

        number.append("11001" + registers_8bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]

        output += "fe"
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")

        x = findCounterAddress(output)
        return x


    # if for label
    elif first_arg == None and second_arg == None:
        output += instructions.upper() + " <====> "
        output += "0x"
        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": NOTHING "
        codePrinted.append(output.upper())
        x = 0
        return x

    # if for jmp
    elif instruction == "jmp":
        output = ""
        codePrinted.append(output.upper())
        jmps.append([first_arg, addressCounter, len(codePrinted) - 1])
        x = 2
        return x

    # if for push imm in this range
    elif ((int(first_arg)) <= 127) and (int(first_arg) >= -128) and instruction == "push":

        if int(first_arg) > 0:
            first_print = hex(int(first_arg))[2:]
        else:
            first_print = str(complement16(hex(int(first_arg))[3:]))

        output += "6a "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")

        x = findCounterAddress(output)
        return x

    # if for push imm in this range
    elif ((int(first_arg)) <= -129) or (int(first_arg) >= 128) and instruction == "push":

        if int(first_arg) > 0:
            first_print = hex(int(first_arg))[2:]
            first_print = ("0" * (8 - len(str(first_print)))) + first_print
            temp = ""
            for i in range(len(first_print) - 2, -1, -2):
                temp += first_print[i] + first_print[i + 1] + " "
        else:
            first_print = str(complement16(hex(int(first_arg))[3:]))
            first_print = ("f" * (8 - len(str(first_print)))) + first_print
            temp = ""
            for i in range(len(first_print) - 2, -1, -2):
                temp += first_print[i] + first_print[i + 1] + " "

        first_print = temp

        output += "68 "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print
        output = output[:len(output)-1]
        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")

        x = findCounterAddress(output)
        return x

    # if for memory and one args
    elif first_arg in memory_32bit:

        number.append(InstructionOpCode[instruction] + memory_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]

        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")

        x = findCounterAddress(output)
        return x

    # if for push imm in this range
    elif first_arg in memory_16bit:

        number.append(InstructionOpCode[instruction] + memory_16bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]

        output += "66 "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")

        x = findCounterAddress(output)
        return x

    # if for push imm in this range
    elif first_arg in memory_8bit:

        number.append(InstructionOpCode[instruction] + memory_8bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]

        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())

        codePrinted.append(" ")

        x = findCounterAddress(output)
        return x

    # if for push imm in this range
    elif instruction in memory_8bit:

        number.append(InstructionOpCode[instruction] + memory_8bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]

        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        outputReverseArray = output.split(" ")
        outputReverseArray = outputReverseArray[::-1]
        for i in outputReverseArray:
            codePrinted.append(i.upper())
        codePrinted.append(" ")

        x = findCounterAddress(output)
        return x



    # error handler
    else:
        print("Invalid Instruction or reg/m/imm")
        return 0


# this function create jmp output and opcode
def jmp(first_arg, addressCounter, index):
    output = ""
    number = []

    labelAddress = labels[first_arg]  # label's address
    processedNum = labelAddress - (addressCounter + 2)  # the number that should print after eb
    if processedNum < 0:
        first_print = str(complement16(hex(int(processedNum))[3:]))
    else:
        first_print = hex(int(processedNum))[2:]
    number.append(first_print)
    output += "eb "
    if len(first_print) == 1:
        output += "0" + first_print
    else:
        output += first_print

    outputReverseArray = output.split(" ")
    outputReverseArray = outputReverseArray[::-1]
    for i in outputReverseArray:
        codePrinted.append(i.upper())
    codePrinted.append(" ")
    return


# file path
file_path = "AssemblyProject1.txt"

# open file for reading it
with open(file_path, 'r') as file:
    code = file.read()

lines = code.splitlines()
addressCounter = 0
labels = {}
jmps = []
codePrinted = []
dataPrinted = []
stackPrinted = []
memory = ["XX"] * 256
cp = 0
sp = 0
dp = 0
flagCode = 0
flagDataBreak = 0
printLabelForStartASegment = 0

try:
    # iterate the input file
    for line in lines:
        flagDataBreak = 0
        splitT = line.split(" ")
        # set instruction
        instructions = splitT[0].lower()
        if instructions == "":
            continue
        if ".stack" in instructions:
            sp = int(re.search(r'\((\d+)\)', line).group(1))
            continue
        if ".data" in instructions:
            dp = int(re.search(r'\((\d+)\)', line).group(1))
            continue
        while (True and flagCode == 0):
            if ".code" in instructions:
                flagCode = 1
                break
            else:
                dataType = splitT[1].lower()
                instructions = instructions.upper()
                if dataType == "byte":
                    dataPrinted.append(instructions)
                elif dataType == "word":
                    dataPrinted.append(instructions)
                    dataPrinted.append(instructions)
                elif dataType == "dword":
                    dataPrinted.append(instructions)
                    dataPrinted.append(instructions)
                    dataPrinted.append(instructions)
                    dataPrinted.append(instructions)
                flagDataBreak = 1
                break
        if flagDataBreak == 1:
            continue
        if ".code" in instructions:
            cp = int(re.search(r'\((\d+)\)', line).group(1))
            continue
        # if instruction is label
        if ":" in line:
            first_arg = None
            second_arg = None
        else:
            regs = splitT[1].split(",")
            if len(regs) == 2:
                # instructions like add reg/reg
                first_arg = regs[0].lower()
                second_arg = regs[1].lower()
            # instructions like push imm or inc
            elif len(regs) == 1:
                first_arg = regs[0].lower()
                second_arg = None

        # call assembler function
        counterAdding = assembler(instructions, first_arg, second_arg, addressCounter)
        addressCounter += counterAdding

        # add label to labels dict if instruction is label
        if ":" in instructions:
            labels[instructions[0:len(instructions) - 1]] = addressCounter
        if "push" in instructions:
            pushArg = splitT[1].lower()
            instructions = instructions.upper()

            if pushArg in registers_8bit:
                pushArg = splitT[1].upper()
                stackPrinted.append(pushArg)
                stackPrinted.append("MM")
                stackPrinted.append("MM")
                stackPrinted.append("MM")
            elif pushArg in registers_16bit:
                pushArg = splitT[1].upper()
                stackPrinted.append(pushArg)
                stackPrinted.append(pushArg)
                stackPrinted.append("MM")
                stackPrinted.append("MM")
            elif pushArg in registers_32bit:
                pushArg = splitT[1].upper()
                stackPrinted.append(pushArg)
                stackPrinted.append(pushArg)
                stackPrinted.append(pushArg)
                stackPrinted.append(pushArg)
            elif int(pushArg) >= -128 and int(pushArg) <= 127:
                pushArg = splitT[1].upper()
                stackPrinted.append(pushArg)
                stackPrinted.append("MM")
                stackPrinted.append("MM")
                stackPrinted.append("MM")
            elif int(pushArg) <= -128 or int(pushArg) >= 127:
                if int(pushArg) >= -32768 and int(pushArg) <= 32767:
                    pushArg = splitT[1].upper()
                    stackPrinted.append(pushArg)
                    stackPrinted.append(pushArg)
                    stackPrinted.append("MM")
                    stackPrinted.append("MM")
                else:
                    pushArg = splitT[1].upper()
                    stackPrinted.append(pushArg)
                    stackPrinted.append(pushArg)
                    stackPrinted.append(pushArg)
                    stackPrinted.append(pushArg)
        if "pop" in instructions:
            popArg = splitT[1].upper()
            for i in range(0, len(stackPrinted)):
                if stackPrinted[i] == popArg:
                    stackPrinted[i] = "MM"

except:
    print("invalid input")

# iterate jumps array for modify jmps and create output for it
for i in jmps:
    jmp(i[0], i[1], i[2])

# print all elements in printed array
cpiterate = cp
for i in range(cp, cp + 32):
    memory[i] = "MM"
for i in codePrinted:
    if i == " " and cpiterate % 2 != 0:
        cpiterate += 1
        continue
    if i == " " and cpiterate % 2 == 0:
        continue
    memory[cpiterate] = i
    cpiterate += 1

dpIterate = dp
for i in range(dp, dp + 32):
    memory[i] = "MM"
for i in dataPrinted:
    memory[dpIterate] = i
    dpIterate += 1

spIterate = sp
for i in range(sp, sp + 32):
    memory[i] = "MM"
for i in stackPrinted:
    memory[spIterate] = i
    spIterate += 1

def colorize(text, color):
    colors = {
        'RESET': '\033[0m',
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'BLUE': '\033[94m',  # ANSI escape code for blue
        'PURPLE': '\033[95m',
        'CYAN': '\033[96m',
        'WHITE': '\033[97m'
    }
    return colors[color] + text + colors['RESET']

# Your existing code

for i in range(0, len(memory)):
    if i == cp or i == dp or i == sp:
        if i == cp:
            printLabelForStartASegment = "CP"
        elif i == dp:
            printLabelForStartASegment = "DP"
        elif i == sp:
            printLabelForStartASegment = "SP"
        print("          ------      ")
        print(colorize(printLabelForStartASegment + " " + createStrIndexMemory(i) + " : |  " + colorize(memory[i], 'GREEN') + colorize("  |","GREEN"), 'GREEN'))

    else:
        print("          ------      ")
        print("   " + colorize(createStrIndexMemory(i),"PURPLE") + " : |  " + colorize(memory[i], 'BLUE') + "  |")

print("          ------      ")
