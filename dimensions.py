import nibabel as nib

# 读取.nii.gz文件
file_path = '/share/home/ncu22/SyntheticTumors/datafolds/04_LiTS/img/liver_47.nii.gz'
img = nib.load(file_path)

# 获取数据的维度大小
data = img.get_fdata()
dimensions = data.shape
type = img.get_data_dtype()

print("数据维度大小为:", dimensions)
print(f"数据类型（dtype）：{type}")
