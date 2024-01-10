import os
from tqdm import tqdm

folder_path = r"#請輸入資料夾路徑"  #資料夾路徑

file_list = os.listdir(folder_path)  #列出資料夾中的所有檔案

progress_bar = tqdm(total=len(file_list), desc="Processing Files", unit="file")  #tqdm進度條

for filename in file_list:
    new_filename = "前綴" + filename  #建立新的檔案名稱，加上"前綴"

    old_filepath = os.path.join(folder_path, filename)
    new_filepath = os.path.join(folder_path, new_filename)  #建立完整的檔案路徑
    os.rename(old_filepath, new_filepath)  #重新命名檔案

    progress_bar.update(1)  #更新進度條

progress_bar.close()  #關閉進度條

print("檔案命名完成！")
