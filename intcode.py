def intcode(input_split, input):
    instruction_pointer = 0

    op_code_to_parameter_count = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3}
    valid_op_codes = [1, 2, 3, 4, 5, 6, 7, 8, 99]

    while int(input_split[instruction_pointer]) != 99:
        # modes
        # 0: position mode
        # 1: immediate mode
        parameter_modes = []

        op_code_str = input_split[instruction_pointer]

        instruction_pointer_is_set = False

        # split op code into its digits
        # two right most digits = op code
        op_code = int(op_code_str[-2:])
        # then from right to left => parameters
        k = 2

        while k < len(op_code_str):
            digit = op_code_str[-1-k:-k]
            parameter_modes.append(int(digit))
            k += 1

        j = 0
        while j < op_code_to_parameter_count[op_code] - len(parameter_modes):
            parameter_modes.append(0)

        j = 0
        specific_params = []
        while j < op_code_to_parameter_count[op_code]:
            if j == op_code_to_parameter_count[op_code] - 1:
               if op_code == 5 or op_code == 6:
                   if parameter_modes[j] == 0:
                       specific_params.append(int(input_split[int(input_split[instruction_pointer + j + 1])]))
                   else:
                       specific_params.append(int(input_split[instruction_pointer + j + 1]))
               else:
                   specific_params.append(int(input_split[instruction_pointer + j + 1]))
            if parameter_modes[j] == 0:
                specific_params.append(int(input_split[int(input_split[instruction_pointer + j + 1])]))
            elif parameter_modes[j] == 1:
                specific_params.append(int(input_split[instruction_pointer + j + 1]))
            j += 1

        if op_code == 1:     # add two numbers and store it at a position, three parameters
            first_val = specific_params[0]
            second_val = specific_params[1]
            third_val = specific_params[2]
            input_split[third_val] = str(first_val + second_val)
            print(str(op_code) + "," + str(first_val) + "," + str(second_val) + ", " + str(third_val))

        if op_code == 2:     # multiply two numbers and store it at a position, three parameters
            first_val = specific_params[0]
            second_val = specific_params[1]
            third_val = specific_params[2]
            input_split[third_val] = str(first_val * second_val)
            print(str(op_code) + "," + str(first_val) + "," + str(second_val) + ", " + str(third_val))

        if op_code == 3:     # take integer as input and save it to position given by parameter, one parameter
            first_val = specific_params[0]
            input_split[first_val] = str(input)
            print(str(op_code) + "," + str(first_val))

        if op_code == 4:     # outputs value of parameter, one parameter
            first_val = specific_params[0]
            print(str(op_code) + "," + str(first_val))
            print("OUTPUT: " + str(input_split[first_val]))

        if op_code == 5:     # jump-if-true:
            first_val = specific_params[0]
            second_val = specific_params[1]
            if first_val != 0:
                instruction_pointer = second_val
                instruction_pointer_is_set = True
            print(str(op_code) + "," + str(first_val) + "," + str(second_val))

        if op_code == 6:     # jump-if-false:
            first_val = specific_params[0]
            second_val = specific_params[1]
            if first_val == 0:
                instruction_pointer = second_val
                instruction_pointer_is_set = True
            print(str(op_code) + "," + str(first_val) + "," + str(second_val))

        if op_code == 7:     # less than
            first_val = specific_params[0]
            second_val = specific_params[1]
            third_val = specific_params[2]
            if first_val < second_val:
                input_split[third_val] = 1
            else:
                input_split[third_val] = 0
            print(str(op_code) + "," + str(first_val) + "," + str(second_val) + ", " + str(third_val))

        if op_code == 8:     # equals
            first_val = specific_params[0]
            second_val = specific_params[1]
            third_val = specific_params[2]
            if first_val == second_val:
                input_split[third_val] = 1
            else:
                input_split[third_val] = 0
            print(str(op_code) + "," + str(first_val) + "," + str(second_val) + ", " + str(third_val))


        if op_code not in valid_op_codes:
            print("Unknown opcode. Something went wrong.")

        if not instruction_pointer_is_set:
            instruction_pointer += op_code_to_parameter_count[op_code] + 1
    return input_split