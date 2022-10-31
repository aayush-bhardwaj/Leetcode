def right_shift(input_list):
    """
    Function to do right shift
    :param input_list:
    :return:
    """
    last_item = input_list.pop()
    input_list = [last_item] + input_list
    return input_list

if __name__ == "__main__":
    input = [1,2,3,4]
    output = right_shift(input)
    print(output)
