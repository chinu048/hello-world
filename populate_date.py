import csv

def populateDateTime():
    date_format = ''
    with open('/home/ubuntu/hello_world/data.csv', 'r') as file:
        reader = csv.reader(file)
        cnt = 0
        for row in reader:
            if cnt == 0:
                cnt = cnt + 1
                continue
            elif cnt > 1:
                break
            val = row[2][0:7].split('-')
            date_format = '22/' + val[1] + '/' + val[0] 
            cnt = cnt + 1
    with open('/home/ubuntu/hello_world/main.config', 'a') as file:
        file.write('\ndate_time_requirement = ' + date_format)

populateDateTime()