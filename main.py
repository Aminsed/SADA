import csv
import json

def read_csv_file(csv_file_path):
    data = {}
    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=['Year', 'Rank', 'Company', 'Revenue', 'Profit'])
        next(csv_reader, None)
        key = 0
        for rows in csv_reader:
            data[key] = rows
            key += 1
        return data


raw_data = read_csv_file("data.csv")
print(f"Total number of rows before cleaning: {len(raw_data)}")


def convert_to_int(*, dict_input, **kwargs):
    new_data = {}
    for key in kwargs:
        if key in dict_input:
            if key == 'Profit' or key == 'Revenue':
                try:
                    new_data[key] = (int(float(dict_input[key]) * 1000000))
                except ValueError:
                    continue
            elif key == 'Company':
                new_data[key] = (dict_input[key])
            else:
                try:
                    new_data[key] = (int(dict_input[key]))
                except ValueError:
                    continue
        else:
            print('key not found')
    if "Profit" in new_data:
        return new_data


def remove_invalid(filename):
    final_list = []
    rows = read_csv_file(filename)
    for row in rows:
        line = convert_to_int(dict_input=rows[row], Company=False, Year=True, Rank=True, Revenue=True, Profit=True)
        if line is not None:
            final_list.append(line)
    return final_list


cleaned_data = remove_invalid("data.csv")
print(f'Total number of rows after cleaning:{len(cleaned_data)}')

sorted_based_on_profit = sorted(cleaned_data, key=lambda i: i['Profit'], reverse=True)
print('Top 20 rows with the highest profit values:')
for company in sorted_based_on_profit[:21]:
    print(company)

def write_to_json(json_file_path, data_source):
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(data_source, f, ensure_ascii=False, indent=4)

write_to_json("data2.json", cleaned_data)