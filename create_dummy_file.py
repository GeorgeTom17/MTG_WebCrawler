import csv
import random

with open('Dominaria.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([0, 0, 0])
    for i in range(0, 3):
        nbr = random.randint(1, 295)
        amnt = random.randint(1, 5)
        foil = random.randint(0, 1)
        writer.writerow([nbr, amnt, foil])
