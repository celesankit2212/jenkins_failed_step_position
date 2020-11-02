def case_execution_reader():

    file_read = open(r"execution_file.txt", 'r')
    execution = file_read.read()

    return execution


if __name__ == '__main__':
    case_execution_reader()
