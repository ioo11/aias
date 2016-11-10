def linear_search(number):
    try:
        file = open('/mnt/data/stud/aias/works/py/ContactList.txt')
        result = []
        i = 0
        for row in file:
            row_numder = row.split(' ')
            if(is_substring(number, row_numder[1])):
                result.append(i)
                print(row_numder[0], row_numder[1].rstrip('\n'))
            i += 1
        return result
    except Exception as e:
        print(e)
    finally:
        file.close()


def is_substring(a, b):
    (a, b) = (a, b) if len(a) <= len(b) else (b, a)
    i = 0
    for j in range(len(a), len(b)+1):
        if b[i:j] == a:
            return True
        i += 1
    return False


print(linear_search('22'))
