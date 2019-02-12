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
        Name(list): name
        Age(list): age
        Gender(list): gender
        TSH(list): TSH results
    """
    Data = data.split('\n')
    Name = []
    Age = []
    Gender = []
    TSH = []
    patient_num = 0
    for i, item in enumerate(Data):
        if item != 'END':
            patient_num += 1
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
    return Name, Age, Gender, TSH


def sort_name(name):
    """Separate data into first/last name

    Args:
        name(list): list of patient names

    Returns:
        FName(list): list of first names
        LName(lish): list of last names
    """
    FName = []
    LName = []
    for item in name:
        n = str(item).split()
        FName.append(n[0])
        LName.append(n[-1])
    return FName, LName


data = read_file()
Name, Age, Gender, TSH = separate_data(data)
FName, LName = sort_name(Name)
print(FName, LName)
