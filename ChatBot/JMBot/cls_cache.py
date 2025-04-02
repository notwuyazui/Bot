import os
import shutil

def clear_folder(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)  # 删除文件或符号链接
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # 删除子目录及内容
        except Exception as e:
            print(f"删除失败: {item_path} - {str(e)}")

folder_path = "C:/Users/13928/AppData/Local/nonebot2"
clear_folder(folder_path)
