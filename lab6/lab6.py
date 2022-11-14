 
import os
import random

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thurdsay', 'Friday', 'Saturday', 'Sunday']
TIME = ['Morning', 'Evening']
HEADER = "Model; Output value; Time of computation;\n"
FILENAME = "Solutions.csv"
MODELS = ['A', 'B', 'C']

path = os.getcwd()


for day in DAYS:
    try:
        os.mkdir(path + '/' + day)
    except OSError:
        pass

    for t in TIME:
        try:
            os.mkdir(path + '/' + day + '/' + t)
        except OSError:
            pass

        file = open(path + '/' + day + '/' + t + '/' + FILENAME, "w")
        file.write(HEADER)
        file.write(f"{MODELS[random.randint(0, 2)]}; {random.randint(0, 1000)}; {random.randint(0, 1000)}s;\n")
        file.close()
        