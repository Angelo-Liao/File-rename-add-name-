import os
from tqdm import tqdm

folder_path = r"D:\Downloads\发条少女（迷之呆梨）fantia 2023年04月订阅\01_2034_真空☁️\$1800_💙💙"  # 資料夾路徑

# 列出資料夾中的所有檔案
file_list = os.listdir(folder_path)

# 設置tqdm進度條
progress_bar = tqdm(total=len(file_list), desc="Processing Files", unit="file")

# 迴圈處理每一個檔案
for filename in file_list:
    # 建立新的檔案名稱，加上"1800_"
    new_filename = "$1800_💙💙" + filename

    # 建立完整的檔案路徑
    old_filepath = os.path.join(folder_path, filename)
    new_filepath = os.path.join(folder_path, new_filename)

    # 重新命名檔案
    os.rename(old_filepath, new_filepath)

    # 更新進度條
    progress_bar.update(1)

# 關閉進度條
progress_bar.close()

print("檔案命名完成！")
