
import sys

n = int(input ())

for _ in range (n):

    A = int (input ())
    if A < 9:
        A = 9

    if A % 3 != 0:
        A += (3 - (A % 3))

    num_targets = int (A / 3)

    i = 2
    j = 2
    current_dug = set ()
    end_test_case = False  # Flag variable for flow control
    while j != num_targets + 2:
        print ("{} {}".format (i, j))
        sys.stdout.flush ()
        hole_position = tuple ([int (i) for i in input ().strip ().split ()])
        if hole_position == (-1, -1):
            exit ()
        if hole_position == (0, 0):
            end_test_case = True
            break

        current_dug.add (hole_position)
        if len (current_dug) == 9:
            j += 1
            current_dug = set ()

    if end_test_case:
        continue