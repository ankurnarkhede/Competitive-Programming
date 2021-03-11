def main():
    total_campuses = 0
    campus_count = 0

    with open('temp.txt', 'r') as fh:
        analyze = False
        lst = []
        attractions, to_visit, totl = 0, 0, 0  # N,K,V

        for i, line in enumerate(fh):
            if " " in line:
                if analyze and (len(lst) == attractions):
                    campus_count += 1
                    visit(attractions, to_visit, totl, lst, campus_count)
                    analyze = False
                    lst = []
                    attractions, to_visit, totl = 0, 0, 0  # N,K,V

                analyze = True

                s_list = line.split(' ')
                attractions, to_visit, totl = [int(i) for i in s_list]
                continue

            if analyze:
                lst.append(line.strip())
                continue
            elif (i == 0):
                total_campuses = int(line)
                continue

        if analyze and (len(lst) == attractions):
            campus_count += 1
            visit(attractions, to_visit, totl, lst, campus_count)
    return


def visit(N, K, V, p_list, campus):
    lastt = ((
            K * V)) % N - 1
    last_run = []
    ordered_last_run = []

    for i in range(0, K):
        last_run.append(p_list[lastt - i])

    if (len(last_run) == 1):
        ordered_last_run = last_run
    else:
        for attraction in p_list:
            if attraction in last_run:
                ordered_last_run.append(attraction)

    print_to_file(ordered_last_run, campus)
    return


def print_to_file(final, campus):
    attract_str = ' '.join(str(e) for e in final)

    with open("output.txt", "a") as text_file:
        text_file.write("Case #{}: {}\n".format(campus, attract_str))

    return


if __name__ == "__main__":
    main()
