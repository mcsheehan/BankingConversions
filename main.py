# This is a sample Python script.

# Press Alt+Shift+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import csv
import datetime
from dataclasses import dataclass
from time import strftime


@dataclass
class FreeAgentRow:
    timestamp: str
    description: str
    value: str


def save_free_agent(file_to_save: str, free_agent_rows: list[FreeAgentRow]):
    with open(file_to_save, 'w', newline="") as file:
        spamwriter = csv.writer(file, delimiter=',')
        for row in free_agent_rows:
            spamwriter.writerow([row.timestamp, row.description, row.value])


def process_tide_csv_to_freeagent_rows(tide_path: str) -> list[FreeAgentRow]:
    results = []
    with open(tide_path, 'r') as file:
        csvreader = csv.reader(file)
        for index, row in enumerate(csvreader):
            if index == 0:
                continue

            timestamp = datetime.datetime.strptime(row[0], "%Y-%m-%d").timetuple()
            actual_time = strftime("%d/%m/%Y", timestamp)
            description = row[2]
            money_value = row[6]
            results.append(FreeAgentRow(actual_time, description, money_value))

    return results


def process_starling_csv_to_freeagent_rows() -> list[FreeAgentRow]:

    pass


def process_tide():
    freeagent_rows = process_tide_csv_to_freeagent_rows(tide_path="/home/mark/freshtide/transactions-2023-03-01.csv")
    save_free_agent("/home/mark/freshtide/freeagent.csv", freeagent_rows)


def process_starling():
    pass


if __name__ == '__main__':
    # process_tide()
    process_starling()