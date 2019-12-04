input_min = 152085
input_max = 670283

current = input_min
count = 0
while current <= input_max:
    current_list = list(str(current))
    i = 1
    cond1 = False
    cond2 = True
    max_counter = 0
    while i < len(current_list):
        if current_list[i-1] == current_list[i]:
            if max_counter == 0:
                max_counter = 2
            else:
                max_counter += 1
        else:
            if max_counter == 2:
                cond1 = True
            max_counter = 0

        if int(current_list[i-1]) > int(current_list[i]):
            cond2 = False

        i += 1

    if not cond1 and max_counter == 2:
        cond1 = True

    if cond1 and cond2:
        print(str(current))
        count += 1

    current += 1

print("Count: " + str(count))