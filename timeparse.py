import csv
with open('duration.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if row[0].find('minute') != -1:
            row.append(float(row[0][:row[0].find(' minute')])*60)
        elif row[0].find('second') != -1:
            row.append(float(row[0][:row[0].find(' second')]))
        elif row[0].find('hour') != -1:
            row.append(float(row[0][:row[0].find(' hour')])*360)
        else:
            print(row[0])
            raw_input()

        print(row[1])
