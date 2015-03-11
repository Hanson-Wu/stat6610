import csv

#source file
reader = csv.reader(open('F:\\CSUEB\\courses\\STAT 6610 - Data Visualization\\hmwks\\hmwk7\\birth-rate.csv', 'r'), delimiter=",")
#target file
writer = csv.writer(open('F:\\CSUEB\\courses\\STAT 6610 - Data Visualization\hmwks\\hmwk7\\birth-rate-yearly2.csv', 'w'), delimiter=",")

rows_so_far = 0

data = ["year", "rate"]
writer.writerow(data)

for row in reader:
    if rows_so_far == 0:
        header = row
        rows_so_far += 1
    else:
        
        for i in range(2):
            if i > 0 and row[i]:
                data = [header[i], row[i]]
                writer.writerow(data)
        break;
        rows_so_far += 1
