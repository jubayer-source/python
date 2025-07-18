# jubayer-source github 
# jubayer_source

def list_sum(num_List):
    
    # if not num_List:
    #     return 0
    if len(num_List) == 1:
        return num_List[0]
    
    else:
        return num_List[0] + list_sum(num_List[1:])

print(list_sum([0]))
