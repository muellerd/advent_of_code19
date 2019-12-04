input_min = 152085
input_max = 670283

current = input_min
count = 0
while current <= input_max:

    current_list = list(str(current))
    i = 1
    cond1 = False
    cond2 = True
    while i < len(current_list):
        if current_list[i-1] == current_list[i]:
            cond1 = True

        if int(current_list[i-1]) > int(current_list[i]):
            cond2 = False

        i += 1

    if cond1 and cond2:
        print(str(current))
        count += 1

    current += 1

print("Count: " + str(count))