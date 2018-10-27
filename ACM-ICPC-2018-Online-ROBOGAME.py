
def main():

    no = int(input())

    for q in range(no):

       seq = input()

       nw = [0] * len(seq)

       for index in range(len(seq)):
           chr = seq[index]
           if chr.isdigit():
               num = int(chr)
               for i in range(max(0, index-num), min(len(seq), index+num+1)):
                   nw[i] += 1

           else:
               continue


       if max(nw) > 1:
           print('unsafe')

       else:
           print('safe')


if __name__ == '__main__':
    main()