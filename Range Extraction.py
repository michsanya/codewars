# A format for expressing an ordered list of integers is to use a comma separated list of either
#
# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
# The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans
# at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
# in the range format.
#
# Example:
#
# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-6,-3-1,3-5,7-11,14,15,17-20"
# Courtesy of rosettacode.org

def solution(args):
    stroke = ''
    a = []
    sub = []
    args.sort()
    sub.append(args[0])
    for i in args:
        if i == max(sub):
            continue
        if i - max(sub) == 1:
            sub.append(i)
        if i - max(sub) > 1:
            a.append(sub)
            sub = []
            sub.append(i)
    a.append(sub)
    for i in a:
        if len(i) == 1:
            stroke = stroke + ',' + str(i[0])
        if len(i) == 2:
            stroke = stroke + ',' + str(i[0]) + ',' + str(i[1])
        if len(i) > 2:
            stroke = stroke + ',' + str(i[0])+'-'+str(i[-1])
    stroke = stroke[1:]

    return stroke

print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 20, 23]))
