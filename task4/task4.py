import re
import sys


def strcmp(a, b):
    return "OK" if (re.compile(b.replace("*", ".*"))).match(a) else "KO"


def main():
    usage = ("\033[1m" + "\033[91m" +
             "Usage:" + " python3 task4.py string other_string" +
             "\033[0m")
    if (len(sys.argv) != 3):
        print(usage)
        exit()
    print(strcmp(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()
