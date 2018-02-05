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
    row0.append('Special Event')
    for row in reader:
        try:
            date = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M')
        except ValueError:
            try:
                date = datetime.datetime.strptime(row[0], '%Y-%m-%d')
            except ValueError:
                pass

        isoDate = date.isocalendar()
        row.append(str(isoDate[1]))
        row.append(date.strftime('%B'))
        row.append(str(date.year))

        if date.weekday() > 4:
            row.append('True')
        else:
            row.append('False')

        tempDate = date.replace(year=Y)
        row.append(next(season for season, (start, end) in seasons
            if start <= tempDate.date() <= end))

        #bracketIndex = row[1].rfind('(')

        #if bracketIndex != -1 and row[1].find('I-24') == -1 and row[1].find('(Belmont)') == -1:
        #    if row[1].find('in orbit') != -1:
        #        row.append('Not specified')
        #    else:
        #        row.append(row[1][bracketIndex+1:-1])
        #        row[1] = row[1][:(-bracketIndex)+1]
        #else:
        #    row.append('USA')

        if row[1].find('Canada') != -1:
            row.append('Canada')
        elif row[1].find('Mexico') != -1:
            row.append('Mexico')
        elif row[1].find('Greece') != -1:
            row.append('Greece')
        elif row[1].find('Bulgaria') != -1:
            row.append('Bulgaria')
        elif row[1].find('UK/England') != -1:
            row.append('UK/England')
        elif row[1].find('England') != -1:
            row.append('England')
        elif row[1].find('Australi') != -1:
            row.append('Australia')
        elif row[1].find('Colombia') != -1:
            row.append('Colombia')
        elif row[1].find('Japan') != -1:
            row.append('Japan')
        elif row[1].find('Germany') != -1:
            row.append('Germany')
        elif row[1].find('Brazil') != -1:
            row.append('Brazil')
        elif row[1].find('India') != -1:
            row.append('India')
        elif row[1].find('Denmark') != -1:
            row.append('Denmark')
        elif row[1].find('UK/Scotland') != -1:
            row.append('UK/Scotland')
        elif row[1].find('Iran') != -1:
            row.append('Iran')
        elif row[1].find('Spain') != -1:
            row.append('Spain')
        elif row[1].find('Malta') != -1:
            row.append('Malta')
        elif row[1].find('UK/Wales') != -1:
            row.append('UK/Wales')
        elif row[1].find('Turkey') != -1:
            row.append('Turkey')
        elif row[1].find('New Zealand') != -1:
            row.append('New Zealand')
        elif row[1].find('Indonesia') != -1:
            row.append('Indonesia')
        elif row[1].find('Northern Ireland') != -1:
            row.append('Northern Ireland')
        elif row[1].find('Lithuania') != -1:
            row.append('Lithuania')
        elif row[1].find('Zambia') != -1:
            row.append('Zambia')
        elif row[1].find('Poland') != -1:
            row.append('Poland')
        elif row[1].find('Macedonia') != -1:
            row.append('Macedonia')
        elif row[1].find('Vietnam') != -1:
            row.append('Vietnam')
        elif row[1].find('Thailand') != -1:
            row.append('Thailand')
        elif row[1].find('Panama') != -1:
            row.append('Panama')
        elif row[1].find('Portugal') != -1:
            row.append('Portugal')
        elif row[1].find('Serbia') != -1:
            row.append('Serbia')
        elif row[1].find('U.A.E.') != -1:
            row.append('U.A.E.')
        elif row[1].find('Belgium') != -1:
            row.append('Belgium')
        elif row[1].find('South Africa') != -1:
            row.append('South Africa')
        elif row[1].find('Philippines') != -1:
            row.append('Philippines')
        elif row[1].find('France') != -1:
            row.append('France')
        elif row[1].find('Pakistan') != -1:
            row.append('Pakistan')
        elif row[1].find('Ukraine') != -1:
            row.append('Ukraine')
        elif row[1].find('Netherlands') != -1:
            row.append('Netherlands')
        elif row[1].find('Montenegro') != -1:
            row.append('Montenegro')
        elif row[1].find('Surinam') != -1:
            row.append('Suriname')
        elif row[1].find('Haiti') != -1:
            row.append('Haiti')
        elif row[1].find('Venezuela') != -1:
            row.append('Venezuela')
        elif row[1].find('Estonia') != -1:
            row.append('Estonia')
        elif row[1].find('Peru') != -1:
            row.append('Peru')
        elif row[1].find('Ireland') != -1:
            row.append('Ireland')
        elif row[1].find('Italy') != -1:
            row.append('Italy')
        elif row[1].find('Hampshire') != -1:
            row.append('England')
        elif row[1].find('Puerto Rico') != -1:
            row.append('Puerto Rico')
        elif row[1].find('Egypt') != -1:
            row.append('Egypt')
        elif row[1].find('Iraq') != -1:
            row.append('Iraq')
        elif row[1].find('Brasil') != -1:
            row.append('Brazil')
        elif row[1].find('Sri Lanka') != -1:
            row.append('Sri Lanka')
        elif row[1].find('Chile') != -1:
            row.append('Chile')
        elif row[1].find('Hungary') != -1:
            row.append('Hungary')
        elif row[1].find('Malaysia') != -1:
            row.append('Malaysia')
        elif row[1].find('Nepal') != -1:
            row.append('Nepal')
        elif row[1].find('Cyprus') != -1:
            row.append('Cyprus')
        elif row[1].find('Norway') != -1:
            row.append('Norway')
        elif row[1].find('Switzerland') != -1:
            row.append('Switzerland')
        elif row[1].find('Hong Kong') != -1:
            row.append('China')
        elif row[1].find('Botswana') != -1:
            row.append('Botswana')
        elif row[1].find('Argentina') != -1:
            row.append('Argentina')
        elif row[1].find('Kenya') != -1:
            row.append('Kenya')
        elif row[1].find('Croatia') != -1:
            row.append('Croatia')
        elif row[1].find('China') != -1:
            row.append('China')
        elif row[1].find('Israel') != -1:
            row.append('Israel')
        elif row[1].find('Saipan') != -1:
            row.append('Saipan')
        elif row[1].find('Cambodia') != -1:
            row.append('Cambodia')
        elif row[1].find('Finland') != -1:
            row.append('Finland')
        elif row[1].find('Mauritius') != -1:
            row.append('Mauritius')
        elif row[1].find('Bahamas') != -1:
            row.append('Bahamas')
        elif row[1].find('UAE') != -1:
            row.append('U.A.E.')
        elif row[1].find('Costa Rica') != -1:
            row.append('Costa Rica')
        elif row[1].find('Cuba') != -1:
            row.append('Cuba')
        elif row[1].find('Guernsey') != -1:
            row.append('Guernsey')
        elif row[1].find('St. Helena Island') != -1:
            row.append('UK')
        elif row[1].find('Sweden') != -1:
            row.append('Sweden')
        elif row[1].find('Bangladesh') != -1:
            row.append('Bangladesh')
        elif row[1].find('Uruguay') != -1:
            row.append('Uruguay')
        elif row[1].find('Yellowstone National Park') != -1:
            row.append('USA')
        elif row[1].find('Luxemburg') != -1:
            row.append('Luxembourg')
        elif row[1].find('UK/Enland') != -1:
            row.append('UK/Enland')
        elif row[1].find('United Arab Emirates') != -1:
            row.append('U.A.E.')
        elif row[1].find('Bosnia/Herzegovina') != -1:
            row.append('Bosnia/Herzegovina')
        elif row[1].find('Guam') != -1:
            row.append('Guam')
        elif row[1].find('Lebanon') != -1:
            row.append('Lebanon')
        elif row[1].find('Menorca') != -1:
            row.append('Spain')
        elif row[1].find('Turks & Caicos') != -1:
            row.append('Turks & Caicos')
        elif row[1].find('Kuwait') != -1:
            row.append('Kuwait')
        elif row[1].find('Kazakhstan') != -1:
            row.append('Kazakhstan')
        elif row[1].find('Dominican Republic') != -1:
            row.append('Dominican Republic')
        elif row[1].find('Phoenix') != -1:
            row.append('USA')
        elif row[1].find('Saudi Arabia') != -1:
            row.append('Saudi Arabia')
        elif row[1].find('Russia') != -1:
            row.append('Russia')
        elif row[1].find('U. S. Virgin Islands') != -1:
            row.append('U. S. Virgin Islands')
        elif row[1].find('St. Kitts') != -1:
            row.append('Federation of Saint Kitts and Nevis')
        elif row[1].find('Abu Dhabi') != -1:
            row.append('U.A.E.')
        elif row[1].find('Austria') != -1:
            row.append('Austria')
        elif row[1].find('Kosovo') != -1:
            row.append('Kosovo')
        elif row[1].find('Romania') != -1:
            row.append('Romania')
        elif row[1].find('Bosnia') != -1:
            row.append('Bosnia')
        elif row[1].find('Jamaica') != -1:
            row.append('Jamaica')
        elif row[1].find('Ecuador') != -1:
            row.append('Ecuador')
        elif row[1].find('Salt Lake City to Portland') != -1:
            row.append('USA')
        elif row[1].find('Czech Republic') != -1:
            row.append('Czech Republic')
        elif row[1].find('Rockhampton') != -1:
            row.append('Australia')
        elif row[1].find('Slovenia') != -1:
            row.append('Slovenia')
        elif row[1].find('Honduras') != -1:
            row.append('Honduras')
        elif row[1].find('Myanmar') != -1:
            row.append('Myanmar')
        elif row[1].find('Kenosha/Racine') != -1:
            row.append('USA')
        elif row[1].find('new Zealand') != -1:
            row.append('New Zealand')
        elif row[1].find('UK/Birmingham') != -1:
            row.append('UK/Birmingham')
        elif row[1].find('between TN and CA') != -1:
            row.append('USA')
        elif row[1].find('UK/Endland') != -1:
            row.append('UK/England')
        elif row[1].find('UK/North Wales') != -1:
            row.append('UK/North Wales')
        elif row[1].find('Sultanate of Oman') != -1:
            row.append('Sultanate of Oman')
        elif row[1].find('South Korea') != -1:
            row.append('South Korea')
        elif row[1].find('Nigeria') != -1:
            row.append('Nigeria')
        elif row[1].find('Guatamala') != -1:
            row.append('Guatemala')
        elif row[1].find('Belarus') != -1:
            row.append('Belarus')
        elif row[1].find('Nicaragua') != -1:
            row.append('Nicaragua')
        elif row[1].find('Bolivia') != -1:
            row.append('Bolivia')
        elif row[1].find('U.A.R.') != -1:
            row.append('U.A.E.')
        elif row[1].find('Tenerife') != -1:
            row.append('Spain')
        elif row[1].find('Latvia') != -1:
            row.append('Latvia')
        elif row[1].find('Canary Island') != -1:
            row.append('Spain')
        elif row[1].find('Taiwan') != -1:
            row.append('Taiwan')
        elif row[1].find('Albania') != -1:
            row.append('Albania')
        elif row[1].find('Maldives') != -1:
            row.append('Maldives')
        elif row[1].find('UAR') != -1:
            row.append('U.A.E.')
        elif row[1].find('Ethiopia') != -1:
            row.append('Ethiopia')
        elif row[1].find('Tunisia') != -1:
            row.append('Tunisia')
        elif row[1].find('Guyana') != -1:
            row.append('Guyana')
        elif row[1].find('Afghanistan') != -1:
            row.append('Afghanistan')
        elif row[1].find('Slovakia') != -1:
            row.append('Slovakia')
        elif row[1].find('Trinidad') != -1:
            row.append('Trinidad/Tobago')
        elif row[1].find('Iceland') != -1:
            row.append('Iceland')
        elif row[1].find('Grand Turk') != -1:
            row.append('Turks & Caicos')
        elif row[1].find('Dubai') != -1:
            row.append('U.A.E.')
        elif row[1].find('Barbados') != -1:
            row.append('Barbados')
        elif row[1].find('Palau') != -1:
            row.append('Palau')
        elif row[1].find('Luxembourg') != -1:
            row.append('Luxembourg')
        elif row[1].find('Algeria') != -1:
            row.append('Algeria')
        elif row[1].find('Arizona') != -1:
            row.append('USA')
        elif row[1].find('New York City (GW Bridge)') != -1:
            row.append('USA')
        elif row[1].find('St. Lucia') != -1:
            row.append('St. Lucia')
        elif row[1].find('Barstow') != -1:
            row.append('USA')
        elif row[1].find('Bermuda') != -1:
            row.append('Bermuda')
        elif row[1].find('Papua/New Guinea') != -1:
            row.append('Papua/New Guinea')
        elif row[1].find('Armenia') != -1:
            row.append('Armenia')
        elif row[1].find('Jordan') != -1:
            row.append('Jordan')
        elif row[1].find('Cape Verde Islands') != -1:
            row.append('Cape Verde Islands')
        elif row[1].find('Zimbabwe') != -1:
            row.append('Zimbabwe')
        elif row[1].find('El Salvador') != -1:
            row.append('El Salvador')
        elif row[1].find('Bahrain') != -1:
            row.append('Bahrain')
        elif row[1].find('Fiji') != -1:
            row.append('Fiji')
        elif row[1].find('Azerbaijan') != -1:
            row.append('Azerbaijan')
        elif row[1].find('Belize') != -1:
            row.append('Belize')
        elif row[1].find('Viet Nam') != -1:
            row.append('Vietnam')
        elif row[1].find('Kazakstan') != -1:
            row.append('Kazakhstan')
        elif row[1].find('Antigua') != -1:
            row.append('Antigua and Barbuda')
        elif row[1].find('Manchester') != -1:
            row.append('England')
        elif row[1].find('Bloemfontein') != -1:
            row.append('South Africa;')
        elif row[1].find('Grenada') != -1:
            row.append('Grenada')
        elif row[1].find('Hellenic Republic') != -1:
            row.append('Greece')
        elif row[1].find('Mozambique') != -1:
            row.append('Mozambique')
        elif row[1].find('Oman') != -1:
            row.append('Oman')
        elif row[1].find('Germanu') != -1:
            row.append('Germany')
        elif row[1].find('Georgia') != -1:
            row.append('Georgia')
        elif row[1].find('Namibia') != -1:
            row.append('Namibia')
        elif row[1].find('Seoul') != -1:
            row.append('South Korea')
        elif row[1].find('Norwich') != -1:
            row.append('Englang')
        elif row[1].find('Syria') != -1:
            row.append('Syria')
        elif row[1].find('British Virgin Islands') != -1:
            row.append('British Virgin Islands')
        elif row[1].find('Faroe Islands') != -1:
            row.append('Faroe Islands')
        elif row[1].find('Tanzania') != -1:
            row.append('Tanzania')
        elif row[1].find('St. Martin') != -1:
            row.append('St. Martin')
        elif row[1].find('PRC') != -1:
            row.append('China')
        elif row[1].find('Liberia') != -1:
            row.append('Liberia')
        elif row[1].find('Botswama') != -1:
            row.append('Botswana')
        elif row[1].find('Rhodes') != -1:
            row.append('Greece')
        elif row[1].find('UK/S.Wales') != -1:
            row.append('UK/Wales')
        elif row[1].find('Paraguay') != -1:
            row.append('Paraguay')
        elif row[1].find('(UK/ North Wales)') != -1:
            row.append('(UK/Wales)')
        elif row[1].find('Republic of Korea') != -1:
            row.append('South Korea')
        elif row[1].find('Mongolia') != -1:
            row.append('Mongolia')
        elif row[1].find('Lesotho') != -1:
            row.append('Lesotho')
        elif row[1].find('UK england') != -1:
            row.append('UK/England')
        elif row[1].find('Morocco') != -1:
            row.append('Morocco')
        elif row[1].find('Cameroon') != -1:
            row.append('Cameroon')
        elif row[1].find('Gambia') != -1:
            row.append('Gambia')
        elif row[1].find('Cancun') != -1:
            row.append('Mexico')
        elif row[1].find('Burkina Faso') != -1:
            row.append('Burkina Faso')
        elif row[1].find('Solomon Islands') != -1:
            row.append('Solomon Islands')
        elif row[1].find('Ghana') != -1:
            row.append('Ghana')
        elif row[1].find('United Kingdom') != -1:
            row.append('UK')
        elif row[1].find('St. Maarten') != -1:
            row.append('St. Maarten')
        elif row[1].find('Kyrgystan') != -1:
            row.append('Kyrgyzstan')
        elif row[1].find('UK/London') != -1:
            row.append('UK')
        elif row[1].find('Guatemala') != -1:
            row.append('Guatemala')
        elif row[1].find('Brunei') != -1:
            row.append('Brunei')
        elif row[1].find('Mexioc') != -1:
            row.append('Mexico')
        elif row[1].find('Uzbekistan') != -1:
            row.append('Uzbekistan')
        elif row[1].find('US Virgin Islands') != -1:
            row.append('U. S. Virgin Islands')
        elif row[1].find('Kyrgyzistan') != -1:
            row.append('Kyrgyzstan')
        elif row[1].find('Slovak Republic') != -1:
            row.append('Slovakia')
        elif row[1].find('Milan') != -1:
            row.append('Italy')
        elif row[1].find('Corsica') != -1:
            row.append('France')
        elif row[1].find('Virgin Islands') != -1:
            row.append('U. S. Virgin Islands')
        elif row[1].find('Aruba') != -1:
            row.append('Aruba')
        elif row[1].find('Curacao') != -1:
            row.append('Curacao')
        elif row[1].find('Martinique') != -1:
            row.append('Martinique')
        elif row[1].find('Senegal') != -1:
            row.append('Senegal')
        elif row[1].find('Natherlands') != -1:
            row.append('Netherlands')
        elif row[1].find('Grand Canaria Island') != -1:
            row.append('Spain')
        elif row[1].find('Turks (and Caicos)') != -1:
            row.append('Turks & Caicos')
        elif row[1].find('Grand Cayman') != -1:
            row.append('Grand Cayman')
        elif row[1].find('Yugoslavia') != -1:
            row.append('Yugoslavia')
        elif row[1].find('greece') != -1:
            row.append('Greece')
        elif row[1].find('Singapore') != -1:
            row.append('Singapore')
        elif row[1].find('boxnia') != -1:
            row.append('Bosnia')
        elif row[1].find('Sinai') != -1:
            row.append('Egypt')
        elif row[1].find('East Timor') != -1:
            row.append('East Timor')
        elif row[1].find('Grenadine Islands') != -1:
            row.append('Grenadine Islands')
        elif row[1].find('Rome') != -1:
            row.append('Italy')
        elif row[1].find('S. Africa') != -1:
            row.append('South Africa')
        elif row[1].find('Scotland') != -1:
            row.append('UK/Scotland')
        elif row[1].find('Wales') != -1:
            row.append('UK/Wales')
        elif row[1].find('Congo') != -1:
            row.append('Congo')
        elif row[1].find('Uganda') != -1:
            row.append('Uganda')
        elif row[1].find('French Polynesia') != -1:
            row.append('French Polynesia')
        elif row[1].find('Palestine') != -1:
            row.append('Palestine')
        elif row[1].find('Tuvalu') != -1:
            row.append('Tuvalu')
        elif row[1].find('Qatar') != -1:
            row.append('Qatar')
        elif row[1].find('Libya') != -1:
            row.append('Libya')
        elif row[1].find('Malawi') != -1:
            row.append('Malawi')
        elif row[1].find('Gibralter') != -1:
            row.append('Gibraltar')
        elif row[1].find('Jamica') != -1:
            row.append('Jamaica')
        elif row[1].find('Antarctica') != -1:
            row.append('Antarctica')
        elif row[1].find('Swaziland') != -1:
            row.append('Swaziland')
        elif row[1].find('Moldova') != -1:
            row.append('Moldova')
        elif row[1].find('Tonga') != -1:
            row.append('Tonga')
        elif row[1].find('Turkmenistan') != -1:
            row.append('Turkmenistan')
        elif row[1].find('PuertoRico') != -1:
            row.append('Puerto Rico')
        elif row[1].find('Somalia') != -1:
            row.append('Somalia')
        elif row[1].find('Seychelles') != -1:
            row.append('Seychelles')
        elif row[1].find('UK/Englnd') != -1:
            row.append('UK/England')
        elif row[1].find('Finlnd') != -1:
            row.append('Finland')
        elif row[1].find('Khazakhstan') != -1:
            row.append('kazakhstan')
        elif row[1].find('USSR') != -1:
            row.append('Russia')
        elif row[1].find('') != -1:
            row.append('')
        elif row[1].find('in orbit') != -1:
            row.append('Not Applicable')
        elif len(row[2]) == 0:
            row.append('Not Applicable')
        else:
            row.append('USA')

        if row[12] == 'USA' or row[12] == 'Canada' or row[12] == 'Mexico' or row[12] == 'Panama' or row[12] == 'Haiti' or row[12] == 'Puerto Rico' or row[12] == 'Bahamas' or row[12] == 'Costa Rica' or row[12] == 'Cuba' or row[12] == 'Turks & Caicos' or row[12] == 'Dominican Republic' or row[12] == 'U. S. Virgin Islands' or row[12] == 'Federation of Saint Kitts and Nevis' or row[12] == 'Jamaica' or row[12] == 'Honduras' or row[12] == 'Guatemala' or row[12] == 'Nicaragua' or row[12] == 'Barbados' or row[12] == 'St. Lucia' or row[12] == 'Bermuda' or row[12] == 'El Salvador' or row[12] == 'Belize' or row[12] == 'Antigua and Barbuda' or row[12] == 'Grenada' or row[12] == 'British Virgin Islands' or row[12] == 'St. Martin' or row[12] == 'St. Maarten' or row[12] == 'Martinique':
            row.append('North America')
        elif (row[12] == 'Greece' or row[12] == 'Bulgaria' or row[12] == 'England' or row[12] == 'UK/England') or row[12] == 'Germany' or row[12] == 'Denmark' or row[12] == 'Spain' or row[12] == 'UK/Scotland' or row[12] == 'Malta' or row[12] == 'UK/Wales' or row[12] == 'Northern Ireland' or row[12] == 'Lithuania' or row[12] == 'Poland' or row[12] == 'Macedonia' or row[12] == 'Portugal' or row[12] == 'Serbia' or row[12] == 'Belgium' or row[12] == 'France' or row[12] == 'Ukraine' or row[12] == 'Netherlands' or row[12] == 'Montenegro' or row[12] == 'Estonia' or row[12] == 'Ireland' or row[12] == 'Italy' or row[12] == 'Hungary' or row[12] == 'Cyprus' or row[12] == 'Norway' or row[12] == 'Switzerland' or row[12] == 'Croatia' or row[12] == 'Finland' or row[12] == 'Guernsey' or row[12] == 'UK' or row[12] == 'Sweden'or row[12] == 'Luxembourg' or row[12] == 'Bosnia/Herzegovina' or row[12] == 'Austria' or row[12] == 'Kosovo' or row[12] == 'Romania' or row[12] == 'Bosnia' or row[12] == 'Czech Republic' or row[12] == 'Slovenia' or row[12] == 'UK/Birmingham' or row[12] == 'UK/North Wales' or row[12] == 'Belarus' or row[12] == 'Latvia' or row[12] == 'Albania' or row[12] == 'Slovakia' or row[12] == 'Iceland' or row[12] == 'Georgia' or row[12] == 'Faroe Islands' or row[12] == 'Grand Cayman' or row[12] == 'Yugoslavia' or row[12] == 'Gibraltar' or row[12] == 'Moldova':
            row.append('Europe')
        elif row[12] == 'Australia' or row[12] == 'New Zealand' or row[12] == 'Saipan' or row[12] == 'Guam' or row[12] == 'Palau' or row[12] == 'Papua/New Guinea' or row[12] == 'Fiji' or row[12] == 'Solomon Islands' or row[12] == 'French Polynesia' or row[12] == 'Tuvalu' or row[12] == 'Tonga':
            row.append('Oceania')
        elif row[12] == 'Colombia' or row[12] == 'Brazil' or row[12] == 'Suriname' or row[12] == 'Venezuela' or row[12] == 'Peru' or row[12] == 'Chile' or row[12] == 'Argentina' or row[12] == 'Uruguay' or row[12] == 'Ecuador' or row[12] == 'Bolivia' or row[12] == 'Guyana' or row[12] == 'Trinidad/Tobago' or row[12] == 'Paraguay' or row[12] == 'Aruba' or row[12] == 'Curacao' or row[12] == 'Grenadine Islands':
            row.append('South America')
        elif row[12] == 'Japan' or row[12] == 'Iran' or row[12] == 'India' or row[12] == 'Turkey' or row[12] == 'Indonesia' or row[12] == 'Vietnam' or row[12] == 'Thailand' or row[12] == 'U.A.E.' or row[12] == 'Philippines' or row[12] == 'Pakistan' or row[12] == 'Iraq' or row[12] == 'Sri Lanka' or row[12] == 'Malaysia' or row[12] == 'Nepal' or row[12] == 'China' or row[12] == 'Israel' or row[12] == 'Cambodia' or row[12] == 'Bangladesh' or row[12] == 'Lebanon' or row[12] == 'Kuwait' or row[12] == 'Kazakhstan' or row[12] == 'Saudi Arabia' or row[12] == 'Russia' or row[12] == 'Myanmar' or row[12] == 'Sultanate of Oman' or row[12] == 'South Korea' or row[12] == 'Taiwan' or row[12] == 'Maldives' or row[12] == 'Afghanistan' or row[12] == 'Armenia' or row[12] == 'Jordan' or row[12] == 'Bahrain' or row[12] == 'Azerbaijan' or row[12] == 'Vietnam' or row[12] == 'Oman' or row[12] == 'Syria' or row[12] == 'Mongolia' or row[12] == 'Kyrgyzstan' or row[12] == 'Brunei' or row[12] == 'Uzbekistan' or row[12] == 'Singapore' or row[12] == 'East Timor' or row[12] == 'Palestine' or row[12] == 'Qatar' or row[12] == 'Turkmenistan':
            row.append('Asia')
        elif row[12] == 'Zambia' or row[12] == 'South Africa' or row[12] == 'Egypt' or row[12] == 'Botswana' or row[12] == 'Kenya' or row[12] == 'Mauritius' or row[12] == 'Nigeria' or row[12] == 'Ethiopia' or row[12] == 'Tunisia' or row[12] == 'Algeria' or row[12] == 'Cape Verde Islands' or row[12] == 'Zimbabwe' or row[12] == 'Mozambique' or row[12] == 'Namibia' or row[12] == 'Tanzania' or row[12] == 'Liberia' or row[12] == 'Lesotho' or row[12] == 'Morocco' or row[12] == 'Cameroon' or row[12] == 'Gambia' or row[12] == 'Burkina Faso' or row[12] == 'Ghana' or row[12] == 'Senegal' or row[12] == 'Congo' or row[12] == 'Uganda' or row[12] == 'Libya' or row[12] == 'Malawi' or row[12] == 'Swaziland' or row[12] == 'Somalia' or row[12] == 'Seychelles':
            row.append('Africa')
        elif row[12] == 'Antarctica':
            row.append('Antarctica')
        else:
            row.append('Not specified')


        if date.month == 2 and date.day == 14:
            row.append('Valentines')
        elif date.month == 1 and date.day == 1:
            row.append('New Years Day')
        elif date.month == 3 and date.day == 17:
            row.append('Saint Patricks Day')
        elif date.month == 7 and date.day == 4 and row[12] == 'USA':
            row.append('4th of July')
        elif date.month == 10 and date.day == 31:
            row.append('Halloween')
        elif date.month == 12 and date.day == 24:
            row.append('Christmas Eve')
        elif date.month == 12 and date.day == 25:
            row.append('Christmas Day')
        elif date.month == 12 and date.day == 31:
            row.append('New Years Eve')

        row.append(str(date.day))     

        print('$'.join(row))
