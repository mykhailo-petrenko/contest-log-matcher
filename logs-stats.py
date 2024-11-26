from os import listdir
from os.path import isfile, join

from cabrillo.cabrillo.parser import parse_log_file, InvalidLogException, InvalidQSOException

# cab = parse_log_file('logs/DL5XL.log')
# cab = parse_log_file('logs/PA7F.log')

# print(cab.callsign)
#
# print(cab.qso)
#
# print(cab.text())


def logs_list(path="logs/"):
    logs = [join(path, log_file) for log_file in listdir(path) if isfile(join(path, log_file))]
    return logs

def read_dir_and_print_debug():
    logs = logs_list()
    good = 0
    invalid = 0
    valid = []
    for log_file in logs:
        print(f">>{log_file}:")

        try:
            log = parse_log_file(log_file, ignore_unknown_key=True, check_categories=False)
        except InvalidLogException as error:
            print(error)
            invalid = invalid + 1
            continue
        except InvalidQSOException as error:
            print(error)
            invalid = invalid + 1
            continue
        except Exception as error:
            print(error)

            invalid = invalid + 1
            continue

        valid.append(log_file)
        good = good + 1
        print("ok")

    print(f"+ {good} / - {invalid} ")
    print("\n".join(valid))


def main():
    read_dir_and_print_debug()


if __name__ == "__main__":
    main()
