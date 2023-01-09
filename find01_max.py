def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    max=data[0]
    for i in range(len(data)):
        if data[i]>max:
            max=data[i]
    

    
    return max
print(find_max([1,3,4,5,6,7,8]))
    