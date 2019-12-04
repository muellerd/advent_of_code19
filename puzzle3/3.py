# read the input file
file = "input1.txt"

with open(file) as f:

    wires = []

    for line in f:
        current_position = (0, 0)
        print(line.strip())

        # for each cable, create sections
        line_split = line.split(',')
        i = 0
        current_wire = []
        while i < len(line_split):
            next_position = list((current_position[0], current_position[1]))
            if line_split[i].startswith('L'):
                next_position[0] -= int(line_split[i][1:])

            if line_split[i].startswith('R'):
                next_position[0] += int(line_split[i][1:])

            if line_split[i].startswith('U'):
                next_position[1] += int(line_split[i][1:])

            if line_split[i].startswith('D'):
                next_position[1] -= int(line_split[i][1:])

            section = (current_position, tuple(next_position))
            current_wire.append(section)
            i += 1
            current_position = tuple(next_position)
        wires.append(current_wire)

    # compare each section of cable 1 with each section of cable 2 and check for an intersection
    wire1 = wires[0]
    wire2 = wires[1]

    intersections = []
    intersectionToSectionOfWire1 = {}
    intersectionToSectionOfWire2 = {}

    for section1 in wire1:
        for section2 in wire2:
            section1_horizontal = False
            if section1[0][1] == section1[1][1]:
                section1_horizontal = True

            section2_horizontal = False
            if section2[0][1] == section2[1][1]:
                section2_horizontal = True

            intersection = False
            # only compare when orientation of sections is different
            if section1_horizontal != section2_horizontal:
                if section1_horizontal:
                    # section1 is horizontal, section2 is vertical
                    if (min(section1[0][0], section1[1][0]) <= section2[0][0] <= max(section1[0][0], section1[1][0])) \
                            and (min(section2[0][1], section2[1][1]) <= section1[0][1] <= max(section2[0][1], section2[1][1])):
                        # intersection has been found
                        if not (section1[0] == section2[0] or section1[1] == section2[1]):
                            print("INTERSECTION: " + str(section1) + ' & ' + str(section2))
                            position_x = min(max(section1[0][0], section1[1][0]), max(section1[0][0], section2[0][0]), max(section1[1][0], section2[0][0]))
                            positition_y = min(max(section1[0][1], section1[1][1]), max(section1[0][1], section2[0][1]), max(section1[1][1], section2[0][1]))
                            position = (position_x, positition_y)
                            print("Intersection at position: " + str(position))
                            intersections.append(position)
                            intersectionToSectionOfWire1[position] = section1
                            intersectionToSectionOfWire2[position] = section2
                else:
                    # section2 is vertical, section1 is horizontal
                    if (min(section2[0][0], section2[1][0]) <= section1[0][0] <= max(section2[0][0], section2[1][0])) \
                            and (min(section1[0][1], section1[1][1]) <= section2[0][1] <= max(section1[0][1], section1[1][1])):
                        # intersection has been found
                        if not (section1[0] == section2[0] or section1[1] == section2[1]):
                            print("INTERSECTION: " + str(section1) + ' & ' + str(section2))
                            position_x = min(max(section2[0][0], section2[1][0]), max(section2[0][0], section1[0][0]),
                                             max(section2[1][0], section1[0][0]))
                            positition_y = min(max(section2[0][1], section2[1][1]), max(section2[0][1], section1[0][1]),
                                               max(section2[1][1], section1[0][1]))
                            position = (position_x, positition_y)
                            print("Intersection at position: " + str(position))
                            intersections.append(position)
                            intersectionToSectionOfWire1[position] = section1
                            intersectionToSectionOfWire2[position] = section2

    # calculate the manhattan distances of each intersection and find the minimum
    # calculate the minimum number of steps to each intersection and find the minimum
    manhattan = -1
    minSteps = -1
    minPosition = None

    for position in intersections:
        if manhattan == -1:
            manhattan = abs(position[0]) + abs(position[1])
        elif manhattan > abs(position[0]) + abs(position[1]):
            manhattan = abs(position[0]) + abs(position[1])

        stepsOnWire1 = 0
        for section in wire1:
            if section != intersectionToSectionOfWire1[position]:
                stepsOnWire1 += abs(section[0][0] - section[1][0]) + abs(section[0][1] - section[1][1])
            else:
                stepsOnWire1 += abs(section[0][0] - position[0]) + abs(section[0][1] - position[1])
                break

        stepsOnWire2 = 0
        for section in wire2:
            if section != intersectionToSectionOfWire2[position]:
                stepsOnWire2 += abs(section[0][0] - section[1][0]) + abs(section[0][1] - section[1][1])
            else:
                stepsOnWire2 += abs(section[0][0] - position[0]) + abs(section[0][1] - position[1])
                break

        if minSteps == -1:
            minSteps = stepsOnWire1 + stepsOnWire2
            minPosition = position
        elif minSteps > stepsOnWire1 + stepsOnWire2:
            minSteps = stepsOnWire1 + stepsOnWire2
            minPosition = position

    print('Smallest manhattan distance: ' + str(manhattan))
    print('Smallest number of steps for intersection ' + str(minPosition) + ': ' + str(minSteps))