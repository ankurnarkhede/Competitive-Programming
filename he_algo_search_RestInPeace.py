
# Every time you come across a number, Little Jhool carefully manipulates it. He doesn't want you to face numbers which have "21" as a part of them. Or, in the worst case possible, are divisible by 21.
#
# If you end up facing such a number you feel sad... and no one wants that - because you start chanting "The streak is broken!" , if the number doesn't make you feel sad, you say, "The streak lives still in our heart!
# #
# Input Format:
# The first line contains a number, t, denoting the number of test cases.
# After that, for t lines there is one number in every line.
#
# Output Format:
# Print the required string, depending on how the number will make you feel.
#
# Constraints:
# 1 ≤ t ≤ 100
# 1 ≤ n ≤ 1000000


n=int(input())
# print("count=",n)

for i in range(0,n,1):
    num=int(input())
    if((num%21==0) or ('21' in str(num))):
        print('The streak is broken!')
    else:
        print('The streak lives still in our heart!')