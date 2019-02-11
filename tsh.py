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


read_file()
