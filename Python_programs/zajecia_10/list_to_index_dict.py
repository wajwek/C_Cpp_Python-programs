def list_to_index_dict(input_list):
    """
    Creates a dictionary mapping each unique element from the list 
    to a list of its indices in the original list.
    """
    unique_elements = set(input_list)
    result_dict = {}
    
    for element in unique_elements:
        indices = []
        for i in range(len(input_list)):
            if input_list[i] == element:
                indices.append(i)
        result_dict[element] = indices
        
    return result_dict

print(list_to_index_dict([1, 2, 2, 3, 1]))
