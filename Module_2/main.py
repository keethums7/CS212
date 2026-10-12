# TODO: Split this code into modules: file loading, the Z3 model and solving,
#       and user input and output (requirement 7)

import csv
from z3 import Solver, Int, Bool, And, Or, Implies, Sum, If, sat, unsat

# Load a CSV file into a list of dictionaries (requirement 2)
# Each row becomes a dictionary whose keys are the column names,
# for example {"section_id": "S01", "course": "CS133Y", ...}
def load_csv(filename):
    rows = []
    with open(filename, newline="") as file:    # "with" closes the file when done
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows

instructors = load_csv("Data/instructors.csv")
classrooms = load_csv("Data/classrooms.csv")
sections = load_csv("Data/sections.csv")

# Every value is read as a string, so convert the numbers to int
# and split the semicolon lists into Python lists
for teacher in instructors:
    teacher["max_sections"] = int(teacher["max_sections"])
    teacher["qualified_courses"] = teacher["qualified_courses"].split(";")
for section in sections:
    section["earliest_slot"] = int(section["earliest_slot"])
    section["latest_slot"] = int(section["latest_slot"])

# One set of decision variables per section (requirement 3)
slot = []
instructor = []
room = []
for section in sections:
    section_id = section["section_id"]
    slot.append(Int("slot_" + section_id))
    instructor.append(Int("instructor_" + section_id))
    room.append(Int("room_" + section_id))

# One tracking flag per constraint group (requirement 6)
group_names = ["domain", "room_conflict", "instructor_conflict", "qualification",
               "workload", "time_window"]
flags = {}        # a dictionary, like an object in JS or a Dictionary in C#
flag_list = []
for name in group_names:
    flags[name] = Bool(name)
    flag_list.append(flags[name])

solver = Solver()
solver.set("timeout", 10000)    # milliseconds

# Every constraint is added through this function so it belongs to a group
def add(group, constraint):
    solver.add(Implies(flags[group], constraint))

# TODO: Add the constraints for the other rules (requirement 4):
#       domain, room_conflict, instructor_conflict, qualification and time_window

# Counting with Sum and If (rule 5)
# If(condition, 1, 0) works like the ternary operator: condition ? 1 : 0
for w in range(len(instructors)):
    terms = []
    for j in range(len(sections)):
        terms.append(If(instructor[j] == w, 1, 0))
    count = Sum(terms)
    add("workload", count <= instructors[w]["max_sections"])

result = solver.check(flag_list)    # the flags are passed in as assumptions
if result == sat:
    model = solver.model()
    # Read a value from the model and convert it to a Python int
    first_slot = model.eval(slot[0], model_completion=True).as_long()
    # TODO: Read every section's slot, instructor and room out of the model,
    #       return the schedule as a list of dictionaries and print it
    #       as a table sorted by time slot (requirement 5)
elif result == unsat:
    print("Conflicting rules:", solver.unsat_core())
# TODO: Handle the case where result is unknown (the solver timed out)

# TODO: Run the program on each data set in the unsolvable_data folder (requirement 6)
# TODO: Write the test module with a plain Python schedule checker (requirement 8)
