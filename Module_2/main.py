# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "z3>=0.2.0",
# ]
# ///

import csv
from z3 import Solver, Int, Bool, And, Or, Implies, Sum, If, sat, unsat

if __name__ == "__main__":

    for csv_file in ["classrooms", "instructors", "sections"]:
        # fill the full filepath from the substring provided
        path = f"Data/{csv_file}.csv"
        print(f"Reading {csv_file}.csv...\n")

        # open file and convert to list of dicts
        file = open(f"Data/{csv_file}.csv")
        csv_data = list(csv.DictReader(file))

        # converting cells to ints where applicable
        for row in csv_data:
            for key in row.keys():
                try:
                    row[key] = int(row[key])
                except:
                    continue
            # print(row)

        # add to the full list of rows
        data_list.append(csv_data)

    # print the full list (contains all rows from all .csv files)
    print("Full data:\n")
    for i in data_list:
        print(i)
