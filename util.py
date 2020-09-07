def print_2d_array(arr):
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()


num_to_alp = lambda x: chr(x + 64)    # int -> char
alp_to_num = lambda x: ord(x) - 64    # char -> int

