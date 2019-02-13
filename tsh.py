def read_file():
    """Read data from test_data.txt

    Args:
        None

    Returns:
        data (str): test data
    """
    f = open("test_data.txt", "r")
    data = f.read()
    return data


def separate_data(data):
    """Separate data into different patients

    Args:
        data (str): test data

    Returns:
        Name (list): name
        Age (list): age
        Gender (list): gender
        TSH (list): TSH results
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
        name (list): patient names

    Returns:
        FName (list): first names
        LName (lish): last names
    """
    FName = []
    LName = []
    for item in name:
        n = str(item).split()
        FName.append(n[0])
        LName.append(n[-1])
    return FName, LName


def sort_tsh(tsh):
    """Sort TSH result and make diagnosis

    Hyperthyroidism - any of TSH results < 1.0;
    Hypothyroidism - any of TSH results > 4.0;
    Normal thyroid function - other;
    Assuming no single patient will have test results
    both above 4.0 and below 1.0;
    Number of results may vary.

    Args:
        tsh (list): TSH test results

    Returns:
        TSH (list): TSH results without 'TSH' string
        diagnosis (str): result of diagnosis
    """
    TSH = []
    diagnosis = []
    for item in tsh:
        n = str(item).split(',')
        n.remove('TSH')
        n.sort()
        TSH.append(n)
        diag = 'Normal thyroid function'
        if float(n[0]) < 1.000:
            diag = 'Hypothyroidism'
        elif float(n[-1]) > 4.000:
            diag = 'Hyperthyroidism'
        diagnosis.append(diag)
    return TSH, diagnosis


def save_file(dic):
    """Save dictionary to JSON file

    Args:
        dic: Dictionary of assembled individual info

    Returns:
        None
    """
    import json
    fname = dic['First name']
    lname = dic['Last name']
    file_name = str('{}-{}.json'.format(fname, lname))
    out_file = open(file_name, "w")
    json.dump(dic, out_file)
    out_file.close()


def main():
    """Main function

    Use modules to read TSH test data from file, convert
    into lists of information (one information per list,
    in the same order).
    A dictionary is generated from the lists for each
    patient, and then saved into a JSON file.
    Print the progress and mark when finished.

    Args:
        None

    Returns:
        None
    """
    data = read_file()
    Name, Age, Gender, TSH = separate_data(data)
    FName, LName = sort_name(Name)
    TSH, diagnosis = sort_tsh(TSH)
    for i in range(len(FName)):
        dic_patient = {
            "First name": FName[i],
            "Last name": LName[i],
            "Age": Age[i],
            "Gender": Gender[i],
            "Diagnosis": diagnosis[i],
            "TSH": TSH[i]
        }
        print("Finished {}/{}".format(i + 1, len(FName)))
        save_file(dic_patient)
    print("Task finished")


if __name__ == "__main__":
    main()
