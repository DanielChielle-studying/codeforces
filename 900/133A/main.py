program = input()

instruction_h = program.find("H")
instruction_q = program.find("Q")
instruction_9 = program.find("9")

if instruction_h != -1 or instruction_q != -1 or instruction_9 != -1:
    print("YES")
else:
    print("NO")