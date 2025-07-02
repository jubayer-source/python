# jubayer-source github 
# jubayer_source username for all.

def unique_list(l):
    x = []

    for a in l:
        if a not in x:
            x.append(a)

    return x

print(unique_list([1,2,2,3,3,3,4,5,5,6,7]))

############################## Another approach

def unique_value(input_list):

    return list(set(input_list))

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
print(f"Unique List :",unique_value(sample_list))
