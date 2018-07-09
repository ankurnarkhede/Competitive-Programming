#!/usr/bin/python
# main script for solving "Tourist" problem
import sys

"""
T: Number of campuses
K: Attractions to visit
N: Attractions in campus
V: Number of visits to a campus 
Default list: Ordered from most popular to non-popular
1 < T < 80 
1 < K < N < 50 
1 < V < 10^12
"""


def main():
    """
    Opens text file and reads through it, while executing logic for every campus (block)
    We only iterate once through the .txt file
    """
    total_campuses = 0
    campus_count = 0

    with open ('temp.txt', 'r') as fh:
        # print("File successfully opened")
        analyzing_block = False
        popularity_list = []
        attractions, attractions_to_visit, total_visits = 0, 0, 0  # N,K,V

        for i, line in enumerate (fh):
            if " " in line:
                if analyzing_block and (len (popularity_list) == attractions):
                    campus_count += 1
                    visit (attractions, attractions_to_visit, total_visits, popularity_list, campus_count)
                    analyzing_block = False
                    popularity_list = []
                    attractions, attractions_to_visit, total_visits = 0, 0, 0  # N,K,V

                analyzing_block = True

                s_list = line.split (' ')
                attractions, attractions_to_visit, total_visits = [int (i) for i in s_list]
                continue

            if analyzing_block:
                popularity_list.append (line.strip ())
                continue
            elif (i == 0):
                total_campuses = int (line)
                continue

        # One additional visit (last case, undetected by ending check)
        # TODO Improve useless duplication here
        if analyzing_block and (len (popularity_list) == attractions):
            campus_count += 1
            visit (attractions, attractions_to_visit, total_visits, popularity_list, campus_count)
    return


def visit(N, K, V, p_list, campus):
    """
    Executes the logic for the series of visits for each single campus
    Logic:
        - Follow circular array concept
        - Use modulo operator to determine indices
    """
    last_index = ((
                  K * V)) % N - 1  # index at which we will end up after visiting many times (takes in consideration times visited)
    last_run_visited = []
    ordered_last_run = []

    for i in range (0, K):
        # use negative indexing
        last_run_visited.append (p_list[last_index - i])

    # print(last_run_visited)

    # now order them in popularity
    if (len (last_run_visited) == 1):
        ordered_last_run = last_run_visited
    else:
        for attraction in p_list:
            # can only do this because the attractions are unique
            if attraction in last_run_visited:
                ordered_last_run.append (attraction)

    print_to_file (ordered_last_run, campus)
    return


def print_to_file(final_list, campus):
    """
    Prints the output in correct format
    """
    attractions_str = ' '.join (str (e) for e in final_list)
    print ("Case #{}: {}".format (campus, attractions_str))


    # with open ("output.txt", "a") as text_file:
    #     text_file.write ("Case #{}: {}\n".format (campus, attractions_str))

    return


if __name__ == "__main__":
    main ()