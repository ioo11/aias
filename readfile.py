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
