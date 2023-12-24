import json

data = []

for i in range(121):
    image_path = f"synt_af/large/img/{i}.nii.gz"
    label_path = f"synt_af/large/label/{i}.nii.gz"
    file_data = {
        "image": image_path,
        "label": label_path
    }
    data.append(file_data)

# 将数据保存为 JSON 文件
with open('liver_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("生成的文件路径列表已保存为 liver_data.json 文件。")