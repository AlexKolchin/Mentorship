def missing_num(input_list):
    list_etalon = list(range(1, 11))
    result = list(set(list_etalon) - set(input_list))
    return print(result[0])

input_list = [1,8,4,5,6,7,2,9,10]
missing_num(input_list)