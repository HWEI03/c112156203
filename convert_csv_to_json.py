import csv
import json

# 讀取 CSV 檔案
csv_file_path = 'data.csv'
json_file_path = 'data.json'

data = []

with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# 將資料轉換成 JSON 格式並寫入檔案
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"CSV 檔案已成功轉換為 JSON 並儲存至 {json_file_path}")