def check_duplicates(string):
    count = 0
    lists = []
    for i in string:
        if i not in lists:
            lists.append(i)
        else:
            count += 1
    return count


print(check_duplicates("Nillohit"))
