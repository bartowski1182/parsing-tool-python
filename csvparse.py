import csv
import datetime
import time
import string



Y = 2000 # dummy leap year to allow input X-02-29 (leap day)
seasons = [('Winter', (datetime.date(Y,  1,  1),  datetime.date(Y,  3, 20))),
           ('Spring', (datetime.date(Y,  3, 21),  datetime.date(Y,  6, 20))),
           ('Summer', (datetime.date(Y,  6, 21),  datetime.date(Y,  9, 22))),
           ('Autumn', (datetime.date(Y,  9, 23),  datetime.date(Y, 12, 20))),
           ('Winter', (datetime.date(Y, 12, 21),  datetime.date(Y, 12, 31)))]



with open('nuforcScrape.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    row0 = reader.next()
    row0.append('Week')
    row0.append('Month')
    row0.append('Year')
    row0.append('Weekend')
    row0.append('Season')
    row0.append('Country')
    row0.append('Region')
    for row in reader:
        try:
            date = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M')
        except ValueError:
            try:
                date = datetime.datetime.strptime(row[0], '%Y-%m-%d')
            except ValueError:
                pass

        row.append(str(date.isocalendar()[1]))
        row.append(date.strftime('%B'))
        row.append(str(date.year))

        if date.weekday() > 4:
            row.append('True')
        else:
            row.append('False')


        tempDate = date.replace(year=Y)
        row.append(next(season for season, (start, end) in seasons
            if start <= tempDate.date() <= end))

        
        bracketIndex = row[1].find('(')

        if bracketIndex != -1 and row[1].find('I-24') == -1 and row[1].find('(Belmont)') != -1:
            if row[1].find('in orbit'):
                row.append('Not specified')
            else:
                row.append(row[1][bracketIndex+1:-1])
                row[1] = row[1][:(-bracketIndex)+1]
        else:
            row.append('USA')

        if (row[12] == 'USA' or row[12] == 'Canada' or row[12].lower() == 'Mexico'):
            row.append('North America')
        elif (row[12] == 'Greece' or row[12] == 'Bulgaria' or row[12] == 'UK/England'):
            row.append('Europe')
        elif row[12] == 'Australia':
            row.append('Oceania')
        elif row[12] == 'Colombia':
            row.append('South America')
        elif row[12] == 'Japan':
            row.append('Asia')
        elif row[12] == 'Not specified':
            row.append('Not specified')
        else:
            raw_input(row[12])

        print(', '.join(row))

