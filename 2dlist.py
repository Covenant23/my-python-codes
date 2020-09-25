[1,2,3,4,5,6,7,7,7,6,6]
def eliminate(first_list):
    result = []
    total_list = []
    for i in first_list:
        for item in i:
            if item not in result:
                result.append(item)
        total_list.append(result)
        result = []
    return total_list


print(eliminate([[7,1,2,3,2,3,4,5,6,7],[7,7,6,6]]))


