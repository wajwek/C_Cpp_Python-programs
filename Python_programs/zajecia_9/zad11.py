def flatten(nested_list):
    tab = []
    if isinstance(nested_list, list):
        for n in nested_list:
            tab.extend(flatten(n))
    else:
        tab.append(nested_list)
    return tab
print(flatten([1, [2,3,[32,1]]]))