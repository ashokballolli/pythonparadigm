

file_date = '2020-07-16'

path = 'C:\\Work\\Asfina\\TaskForce\\Files'

files_tables = { 'hallesche_policies_tmp': {'Policies': path+'\\hallesche\\{}_Policies_Hallesche_Tasos_TARIFFS.xlsx'.format(file_date)},
                 'munchner_verein_tmp': {'Commission Movements': path+'\\mv\\{}_Commission Movements_MV_Tasos.xlsx'.format(file_date)}
                }

for table_name in files_tables:
    print(table_name)
    for sheet_name in files_tables[table_name]:
        if table_name == 'munchner_verein_tmp':
            print("Inside if: ", table_name)

        elif table_name == 'hallesche_policies_tmp':
            print("Inside elif: ", table_name)
