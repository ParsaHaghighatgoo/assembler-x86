import easygui

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


def complement16(num):
    hexnum = [*num]
    for i in range(len(hexnum)):
        hexnum[i] = hex(15 - int(hexnum[i], 16))[2:]
    temp = "".join(hexnum)
    if len(hexnum) < 2:
        temp = "f" + temp
    return hex((int(temp, 16)) + 1)[2:]


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


def assembler(instruction, first_arg, second_arg, addressCounter):
    number = []
    index = 0
    output = ""
    if first_arg in registers_32bit and second_arg in registers_32bit:
        output += instruction.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(
            InstructionOpCode[instruction] + "01" + '11' + registers_32bit[second_arg] + registers_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
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

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in registers_16bit and second_arg in registers_16bit:
        output += instruction.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(
            InstructionOpCode[instruction] + "01" + '11' + registers_16bit[second_arg] + registers_16bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
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

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in registers_8bit and second_arg in registers_8bit:
        output += instruction.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(
            InstructionOpCode[instruction] + "00" + '11' + registers_8bit[second_arg] + registers_8bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
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

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in memory_32bit and second_arg in registers_32bit:
        output += instruction.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(
            InstructionOpCode[instruction] + "01" + '00' + registers_32bit[second_arg] + memory_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
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

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in memory_32bit and second_arg in registers_16bit:
        output += instruction.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(
            InstructionOpCode[instruction] + "01" + '00' + registers_16bit[second_arg] + memory_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
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

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in memory_32bit and second_arg in registers_8bit:
        output += instruction.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(
            InstructionOpCode[instruction] + "00" + '00' + registers_8bit[second_arg] + memory_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
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

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in registers_32bit and second_arg in memory_32bit:
        output += instruction.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(
            InstructionOpCode[instruction] + "11" + '00' + registers_32bit[first_arg] + memory_32bit[second_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
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

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in registers_16bit and second_arg in memory_32bit:
        output += instruction.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(
            InstructionOpCode[instruction] + "11" + '00' + registers_16bit[first_arg] + memory_32bit[second_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
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

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in registers_8bit and second_arg in memory_32bit:
        output += instruction.upper() + " " + first_arg + "," + second_arg + " <====> "
        output += "0x"
        number.append(
            InstructionOpCode[instruction] + "10" + '00' + registers_8bit[first_arg] + memory_32bit[second_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        second_print = hex(int(number[index][8:], 2))[2:]
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

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in registers_32bit:
        output += instruction.upper() + " " + first_arg + " <====> "
        output += "0x"
        number.append(InstructionOpCode[instruction] + registers_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in registers_16bit:
        output += instruction.upper() + " " + first_arg + " <====> "
        output += "0x"
        number.append(InstructionOpCode[instruction] + registers_16bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": 66 "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in registers_8bit and instruction == "inc":
        output += instruction.upper() + " " + first_arg + " <====> "
        output += "0x"
        number.append("11000" + registers_8bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]
        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": fe "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in registers_8bit and instruction == "dec":
        output += instruction.upper() + " " + first_arg + " <====> "
        output += "0x"
        number.append("11001" + registers_8bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]

        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": fe "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg == None and second_arg == None:
        output += instruction.upper() + " <====> "
        output += "0x"
        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": NOTHING "
        printed.append(output.upper())
        x = 0
        return x

    elif instruction == "jmp":
        output = ""
        printed.append(output.upper())
        jmps.append([first_arg, addressCounter, len(printed) - 1])
        x = 2
        return x

    elif ((int(first_arg)) <= 127) and (int(first_arg) >= -128) and instruction == "push":
        output += instruction.upper() + " " + first_arg + " <====> "
        output += "0x"

        if int(first_arg) > 0:
            first_print = hex(int(first_arg))[2:]
        else:
            first_print = str(complement16(hex(int(first_arg))[3:]))

        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": 6a "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x


    elif ((int(first_arg)) <= -129) or (int(first_arg) >= 128) and instruction == "push":
        output += instruction.upper() + " " + first_arg + " <====> "
        output += "0x"

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

        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": 68 "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x


    elif first_arg in memory_32bit:
        output += instruction.upper() + " " + first_arg + " <====> "
        output += "0x"
        number.append(InstructionOpCode[instruction] + memory_32bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]

        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in memory_16bit:
        output += instruction.upper() + " " + first_arg + " <====> "
        output += "0x"
        number.append(InstructionOpCode[instruction] + memory_16bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]

        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": 66 "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif first_arg in memory_8bit:
        output += instruction.upper() + " " + first_arg + " <====> "
        output += "0x"
        number.append(InstructionOpCode[instruction] + memory_8bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]

        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x

    elif instruction in memory_8bit:
        output += instruction.upper() + " " + first_arg + " <====> "
        output += "0x"
        number.append(InstructionOpCode[instruction] + memory_8bit[first_arg])
        first_print = hex(int(number[index][:8], 2))[2:]

        output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
        output += ": "
        if len(first_print) == 1:
            output += "0" + first_print
        else:
            output += first_print

        printed.append(output.upper())
        x = findCounterAddress(output)
        return x


    else:
        print("Invalid Instruction or reg/m/imm")
        return 0


def jmp(first_arg, addressCounter, index):
    output = ""
    number = []
    output += "jmp" + " " + first_arg + " <====> "
    output += "0x"
    labelAddress = labels[first_arg]
    processedNum = labelAddress - (addressCounter + 2)
    if processedNum < 0:
        first_print = str(complement16(hex(int(processedNum))[3:]))
    else:
        first_print = hex(int(processedNum))[2:]
    number.append(first_print)
    output += ("0" * (16 - len(str(addressCounter)))) + str(addressCounter)
    output += ": eb "
    if len(first_print) == 1:
        output += "0" + first_print
    else:
        output += first_print

    printed[index] = output.upper()
    return


addressCounter = 0
labels = {}
jmps = []
printed = []


def main(addressCounter=0):
    msg = "Enter your x86 assembly code:"
    title = "x86 Assembler"

    # Use codebox for multi-line input
    user_input = easygui.codebox(msg, title, "")

    if user_input:
        output_file_path = easygui.filesavebox("Save Input to File", "x86 Assembler", filetypes=["*.txt"])

        if output_file_path:
            with open(output_file_path, "w") as file:
                file.write(user_input)

            file_path = output_file_path

            with open(output_file_path, 'r') as file:
                code = file.read()

            lines = code.splitlines()

            for line in lines:
                splitT = line.split(" ")
                instructions = splitT[0].lower()
                if ":" in line:
                    first_arg = None
                    second_arg = None
                else:
                    regs = splitT[1].split(",")
                    if len(regs) == 2:
                        first_arg = regs[0].lower()
                        second_arg = regs[1].lower()
                    elif len(regs) == 1:
                        first_arg = regs[0].lower()
                        second_arg = None

                counterAdding = assembler(instructions, first_arg, second_arg, addressCounter)
                addressCounter += counterAdding
                if ":" in instructions:
                    labels[instructions[0:len(instructions) - 1]] = addressCounter

            for i in jmps:
                jmp(i[0], i[1], i[2])

            for i in printed:
                print(i)

            output = "\n".join(printed)
            easygui.msgbox("Assembled Code:\n\n{}".format(output), "Assembler Output")
        else:
            easygui.msgbox("Output file not selected.", "x86 Assembler")


if __name__ == "__main__":
    main()

