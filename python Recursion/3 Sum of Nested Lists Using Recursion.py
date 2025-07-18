
def recursive_list_sum(data_List):
    total = 0

    for element in data_List:

        if type(element) == type([]):
# If the element is a list, recursively call the recursive_list_sum function on the element
            total = total + recursive_list_sum(element)
        
        else:
            total = total + element
    
    return total

print(recursive_list_sum([1, 2, [3, 4], [5, 6]]))
