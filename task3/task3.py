import datetime as dt
import sys
import csv


class Action:
    def __init__(self, user, date, action, amount):
        self.user = user
        self.date = dt.datetime.fromisoformat(date)
        self.action = action
        self.amount = amount


class Barrel:
    def __init__(self, overall, current):
        self.overall = overall
        self.current = current

    def top_up(self, amount):
        if amount > (self.overall - self.current):
            return False
        else:
            self.current += amount
            return True

    def scoop(self, amount):
        if amount > self.current:
            return False
        else:
            self.current -= amount
            return True


def parse_line(line):
    date = line[: line.find("Z")]
    user = line[line.find("[") + 1: line.find("]")]
    action = "scoop" if "scoop" in line else "top_up"
    if action == "scoop":

        amount = int(line[line.find("scoop") + 6: line.find("l")])
    else:
        amount = int(line[line.find("top_up") + 6: line.find("l")])
    return Action(user, date, action, amount)


def head_check(start, log_file, barrel):
    for l in log_file:
        action = parse_line(l)
        if (action.date >= start):
            return l
        if action.date < start:
            if action.action == "top_up":
                barrel.top_up(action.amount)
            else:
                barrel.scoop(action.amount)
    return None


def interval_check(line, end, barrel, res):
    action = parse_line(line)
    if (action.date <= end):
        if action.action == "top_up":
            res[0] += 1
            if barrel.top_up(action.amount):
                res[2] += action.amount
            else:
                res[1] += 1
                res[3] += action.amount
        else:
            res[4] += 1
            if barrel.scoop(action.amount):
                res[6] += action.amount
            else:
                res[5] += 1
                res[7] += action.amount
        return True
    else:
        return False


def parse_handler(start, end, log_file, barrel):
    res = [0] * 10
    line = head_check(start, log_file, barrel)
    if line is None:
        return None
    res[8] = barrel.current
    if not interval_check(line, end, barrel, res):
        return res
    for line in log_file:
        if not interval_check(line, end, barrel, res):
            return res


def write_csv(res):
    with open("out.csv", mode="w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",", quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        rows = ("Количество попыток налить воду в бочку",
                "Процент ошибок допущеный при наливании за указанный период",
                "Объем налитой в бочку за указанный период",
                "Объем не налитой в бочку за указанный период",
                "Количество попыток отчерпать воду из бочки",
                "Процент ошибок допущеный при отчерпывании за указанный период",
                "Объем отчерпнутой из бочки за указанный период",
                "Объем не отчерпнутой из бочки за указанный период",
                "Объем воды в бочке в начале указанного периода",
                "Объем воды в бочке в конце указанного периода")
        csv_writer.writerow(rows)
        csv_writer.writerow(res)


def parse_log(path, first, last):
    log_file = open(path, "r")
    log_file.readline()
    barrel = Barrel(int(log_file.readline()), int(log_file.readline()))
    start = dt.datetime.fromisoformat(first)
    end = dt.datetime.fromisoformat(last)

    res = parse_handler(start, end, log_file, barrel)
    if res is not None:
        res[9] = barrel.current
        res[1] = res[1]/res[0] if res[0] != 0 else 0
        res[5] = res[5]/res[4] if res[4] != 0 else 0
        write_csv(res)
    log_file.close()


def main():
    usage = ("\033[1m" + "\033[91m" +
             "Usage:" + " python3 task3.py " +
             "path_to_log beg_datetime end_datetime" +
             "\033[0m")
    if len(sys.argv) != 4:
        print(usage)
        exit()
    parse_log(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == "__main__":
    main()
