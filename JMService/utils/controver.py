import jmcomic, os, time, yaml
from PIL import Image
import shutil

def all2PDF(input_folder, pdfpath, pdfname):
    start_time = time.time()
    paht = input_folder
    zimulu = []  # 子目录（里面为image）
    image = []  # 子目录图集
    sources = []  # pdf格式的图

    with os.scandir(paht) as entries:
        for entry in entries:
            if entry.is_dir():
                zimulu.append(int(entry.name))
    # 对数字进行排序
    zimulu.sort()

    for i in zimulu:
        with os.scandir(paht + "/" + str(i)) as entries:
            for entry in entries:
                if entry.is_dir():
                    print("这一级不应该有自录")
                if entry.is_file():
                    image.append(paht + "/" + str(i) + "/" + entry.name)

    if "jpg" in image[0]:
        output = Image.open(image[0])
        image.pop(0)

    for file in image:
        if "jpg" in file:
            img_file = Image.open(file)
            if img_file.mode == "RGB":
                img_file = img_file.convert("RGB")
            sources.append(img_file)

    pdf_file_path = pdfpath + "/" + pdfname
    if pdf_file_path.endswith(".pdf") == False:
        pdf_file_path = pdf_file_path + ".pdf"
    output.save(pdf_file_path, "pdf", save_all=True, append_images=sources)
    end_time = time.time()
    run_time = end_time - start_time
    print("运行时间：%3.2f 秒" % run_time)

def jmIds2PDF(jmIds):
    config = "D:/Desktop/myfile/UESTC-courses/Grade6/Bot/JMService/utils/config.yml"
    loadConfig = jmcomic.JmOption.from_file(config)
    for id in jmIds:
        jmcomic.download_album(id,loadConfig)

    with open(config, "r", encoding="utf8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        path = data["dir_rule"]["base_dir"]

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                if os.path.exists(os.path.join(path +'/' +entry.name + ".pdf")):
                    print("文件：《%s》 已存在，跳过" % entry.name)
                    continue
                else:
                    print("开始转换：%s " % entry.name)
                    all2PDF(path + "/" + entry.name, path, entry.name)

def delete_books():
    config = "D:/Desktop/myfile/UESTC-courses/Grade6/Bot/JMService/utils/config.yml"
    try:
        # 加载配置文件
        with open(config, "r", encoding="utf8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            path = data["dir_rule"]["base_dir"]
            
        # 安全校验
        if not os.path.exists(path):
            print(f"路径不存在: {path}")
            return
            
        # 删除操作
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print(f"已删除: {file_path}")
            except Exception as e:
                print(f"删除失败 {file_path}: {e}")
                
        print("清理完成")
        
    except Exception as e:
        print(f"操作失败: {str(e)}")
        raise
    
    
def jmId2PDF(jmId):
    config = "D:/Desktop/myfile/UESTC-courses/Grade6/Bot/JMService/utils/config.yml"
    loadConfig = jmcomic.JmOption.from_file(config)
    jmcomic.download_album(jmId,loadConfig)

    with open(config, "r", encoding="utf8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        path = data["dir_rule"]["base_dir"]

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                if os.path.exists(os.path.join(path +'/' +entry.name + ".pdf")):
                    print("文件：《%s》 已存在，跳过" % entry.name)
                    continue
                else:
                    print("开始转换：%s " % entry.name)
                    all2PDF(path + "/" + entry.name, path, entry.name)

if __name__ == '__main__':
    jmIds = ['1096392']
    jmIds2PDF(jmIds)