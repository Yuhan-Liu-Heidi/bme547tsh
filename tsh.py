def read_file():
    """Read data from test_data.txt

    Args:
        None

    Returns:
        data(str): test data
    """
    f = open("test_data.txt", "r")
    data = f.read()
    return data


def separate_data(data):
    """Separate data into different patients

    Args:
        data(str): test data

    Returns:
        info(dictionary): information of patients
    """
    Data = data.split('\n')
    D = {
            'Name': '',
            'Age': '',
            'Gender': '',
            'TSH result': ''
        }
    Name = []
    Age = []
    Gender = []
    TSH = []
    for i, item in enumerate(Data):
        if item != 'END':
            if i % 4 == 0:
                Name.append(item)
            elif i % 4 == 1:
                Age.append(item)
            elif i % 4 == 2:
                Gender.append(item)
            else:
                TSH.append(item)
        else:
            break
    print(Name)
    print(Age)
    print(Gender)
    print(TSH)
    


data = read_file()
separate_data(data)
