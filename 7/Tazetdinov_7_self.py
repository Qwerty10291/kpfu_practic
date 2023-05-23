def modify_list(data:list):
    i = 0
    while i < len(data):
        if data[i] % 2 == 0:
            data[i] //= 2
        else:
            data.pop(i)
            i -= 1
        i += 1
