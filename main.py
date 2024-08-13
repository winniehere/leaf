import requests
import json

# 基础 URL
base_url = 'https://leaf-api.pando.im/api/vats'

# 初始参数
cursor = ''
limit = 20  # 你可以根据需要调整这个值

# 存储所有结果的列表
all_vaults = []

while True:
    # 构建请求 URL
    params = {'cursor': cursor, 'limit': limit}
    response = requests.get(base_url, params=params)
    
    # 检查请求是否成功
    if response.status_code == 200:
        data = response.json()
        
        
        # 处理数据
        all_vaults.extend(data['data']['vaults'])
        
        # 获取分页信息
        pagination = data['data']['pagination']
        cursor = pagination.get('next_cursor')
        has_next = pagination.get('has_next')
        print("page: ", pagination)
        # 如果没有下一页，退出循环
        if not has_next:
            print("没有下一页了")
            break
    else:
        print(f"请求失败，状态码: {response.status_code}")
        break

# 将结果写入到 JSON 文件中
with open('vaults_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_vaults, f, ensure_ascii=False, indent=4)

print("数据已写入 vaults_data.json 文件中")