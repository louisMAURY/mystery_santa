def cleanCsv(csv_file):
    with open(csv_file, 'r') as workfile:
        splited_list = []
        appened_list = []
        for i in workfile:
            splited_list = i.split(';')
            del splited_list[2]
            appened_list.append(splited_list)
        del appened_list[0]
        return appened_list

print(cleanCsv("B2A.csv"))