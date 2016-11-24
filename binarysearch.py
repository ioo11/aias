def binary_search(querry, contact_list):
    ret = 'Sorry, nothing was found =('
    if len(contact_list) > 0:
        mid = len(contact_list)//2
        if is_substring(contact_list[mid]['number'], querry):
            ret = contact_list[mid]
            return ret
        elif contact_list[mid]['number'] < querry:
            ret = binary_search(querry, contact_list[(mid+1):])
            return ret
        else:
            ret = binary_search(querry, contact_list[:mid])
            return ret
    else:
        return ret


def read_file(path):
    try:
        file = open(path)
        result = []
        for row in file:
            temp = row.split(' ')
            temp = {'name': temp[0], 'number': temp[1].rstrip('\n')}
            result.append(temp)
        return result
    except Exception as e:
        print(e)
    finally:
        file.close()


def is_substring(a, b):
    (a, b) = (a, b) if len(a) <= len(b) else (b, a)
    for j in range(0, len(a)):
        if b[j] != a[j]:
            return False
    return True

contact_list = read_file('/mnt/data/stud/aias/works/py/ContactListSorted.txt')
print(binary_search('548400', contact_list))
