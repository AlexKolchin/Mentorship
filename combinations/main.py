def variable_len(*args):
    answer = 1
    for x in args:
        answer *= x
    print(answer)
variable_len(3,7,4)