import csv
from os.path import join as p_join
from os import getenv
import sys
from  time import ctime, strftime, strptime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# order of columns to display
headers_order=(
    ('UserID',),
    ('timeStamp',),
    ('Floating Button Result', 'Floating Button Event', 'BluetoothCommunication', 'Floating Button click','btn_click'),
    ('event',),
    ('Device',),
    ('Platform',)
    ('version',),
    ('entityId',),
    ('page_name',),
    ('app_open',),
    ('mode_device',)
      )


events_type=set()
path=p_join(getenv('HOME'),'Downloads',sys.argv[1])
data=[]
with open(path,'r') as ff:
    csv_data = csv.reader(ff)
    i=0

    for row in csv_data:
        if i == 0:
            # headers = row;
            # print(headers)
            # print()
            pass
        else:
            if i in (200,499,500,501,502): print('Row {}: '.format(i),row)
            # new_row = {'Date': row[0],'Patform': row[5], 'Device': row[6], 'UserID': row[7]}
            new_row = { 'UserID': row[7], 'Patform': row[5], 'Device': row[6]}
            # print(type(row),new_row)
            for x in row[8].lstrip('{').rstrip('}').split(';'):
                if len(x)>0:

                    key,val=x.split(':',1)
                    key=key.strip()
                    val=val.strip()
                    events_type.add(key)
                    if key=='timeStamp': val=strftime('%D %H:%M:%S',strptime(ctime(float(val)/1000.0)))
                    # print('{:>25}:{}'.format(key,val))
                    new_row[key] = val
            data.append(new_row)
        i+=1
        # if i==1000: break



# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Project_278c0e241b49.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("Floating_Button_Results").sheet1


print(data[0])

sheet.clear()

res=[(k,v )for k,v in data[0].items()]
print(res)

row=1
row=4
for i in [x for x in data if 'Floating Button Result' in x.keys()]:
    vals=list(i.values())
    print(vals)
    for column in range(len(i)):
        sheet.update_cell(row, column+1, vals[column])
    # sheet.update_cell(row, 2, i['UserID'])
    # sheet.update_cell(row, 1, i['UserID'])
    # sheet.update_cell(row, 1, i['UserID'])
    # sheet.update_cell(row, 1, i['UserID'])
    # sheet.update_cell(row, 1, i['UserID'])
    # sheet.update_cell(row, 1, i['UserID'])

    row+=1

print(len(data),events_type)
for i in events_type:
    print(i)


print(sheet.get_all_values())
