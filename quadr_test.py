import sys
from quadr_functions import *

#this function performs the testing
def main():
    i_file = open("input.txt", 'r')
    g_file = open("golden.txt", 'r')
    o_file = open("output.txt", 'w')
    r_file = open("result.txt", 'w')
    input_list = i_file.read().splitlines()
    golden_list = g_file.read().splitlines()
    j = 0
    for line in input_list:
        a, b, c = get_nums(line)
        o_file.writelines(quadr(a, b, c) + '\n')
        if(quadr(a, b, c) == golden_list[j]):
            r_file.writelines("test passed \n")
        else:
            r_file.writelines("test not passed \n")
        j = j + 1
    i_file.close()
    g_file.close()
    r_file.close()
    o_file.close()
main()
