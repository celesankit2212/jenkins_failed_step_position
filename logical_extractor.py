import re
from case_reader import case_execution_reader
from executable_pattern import usable_patterns


def execution_reader():

    first_pattern, second_pattern = usable_patterns()
    fail_position = []
    error_position = []

    count = 0
    line_executions = []
    line_of_execution = case_execution_reader()

    list_execution = re.split("\n", line_of_execution)

    for line in list_execution:

        if re.search(second_pattern, line):
            executions_new_line = re.search(second_pattern, line).group(1)
            line_executions.append(executions_new_line)
            length_line_executions = int(len(line_executions))

            if length_line_executions > 1:
                line_executions = line_executions[-1]
            for each_one in line_executions:
                for extend_executions in each_one:
                    count += 1
                    if "F" == extend_executions:
                        fail_position.append(count+length_line_executions)
                    elif "E" == extend_executions:
                        error_position.append(count+length_line_executions)

        elif re.search(first_pattern, line):
            fail_position = []
            error_position = []
            line_executions = []
            count = 0
            final_report = []
            file_name = re.search(first_pattern, line).group(1)
            executions = re.search(first_pattern, line).group(2)
            for each in executions:
                count += 1
                if "F" == each:
                    fail_position.append(count)
                elif "E" == each:
                    error_position.append(count)

        final_report.append([file_name, fail_position, error_position])
        print("For file "+str(final_report[-1][0])+", failed at "+str(final_report[-1][1])+" and Error at "
            +str(final_report[-1][2]) + " among total "+str(count)+" Cases of Execution.")


if __name__ == '__main__':
    execution_reader()
