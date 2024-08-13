import json
import pandas as pd

def process_and_write_to_excel(json_file, output_excel_file):
    # 读取 JSON 文件
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 提取 collateral_id 为指定值的元素
    filtered_data = [
        vault for vault in data 
        if vault['collateral_id'] == 'd0ec4cc7-edf6-5359-bf23-41fc9d26444e'
    ]
    
    # 计算 P = 1.5 * art / ink
    for vault in filtered_data:
        art = float(vault['art'])
        ink = float(vault['ink'])
        if ink != 0:
            vault['P'] = 1.5 * art / ink
        else:
            vault['P'] = None  # 避免除以零的情况
    
    # 将结果写入 Excel 表格
    df = pd.DataFrame(filtered_data)
    df.to_excel(output_excel_file, index=False)

# 调用函数
process_and_write_to_excel('greater_than_1000_art_vaults.json', 'output.xlsx')

print("数据已写入 output.xlsx 文件中")