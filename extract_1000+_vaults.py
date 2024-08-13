import json

# 从 JSON 文件中读取数据并提取 art 值大于 1000 的元素
with open('vaults_data.json', 'r', encoding='utf-8') as f:
    all_vaults = json.load(f)

# 存储 art 值大于 1000 的元素
greater_than_1000_art_vaults = [vault for vault in all_vaults if float(vault['art']) > 1000]

# 将 art 值大于 1000 的元素写入到另一张表
with open('greater_than_1000_art_vaults.json', 'w', encoding='utf-8') as f:
    json.dump(greater_than_1000_art_vaults, f, ensure_ascii=False, indent=4)

print("数据已写入 vaults_data.json 和 greater_than_1000_art_vaults.json 文件中")