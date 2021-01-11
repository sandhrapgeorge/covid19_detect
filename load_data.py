import pandas as pd
import os
import shutil
import random

file_path = "Chest_xray_Corona_Metadata.csv"
images_path1 = "Coronahack-Chest-XRay-Dataset/train"
images_path2 = "Coronahack-Chest-XRay-Dataset/test"
df = pd.read_csv(file_path)
target_dir = "new_data_covid/covid"
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print("covid folder created")

cnt = 0
for (i, raw) in df.iterrows():
    if raw["Label"] == "Pnemonia" and raw["Label_1_Virus_category"] == "Virus":
        file_name = raw["X_ray_image_name"]
        if raw["Dataset_type"] == "TRAIN":
            image_path = os.path.join(images_path1, file_name)
            image_copy_path = os.path.join(target_dir, file_name)
            shutil.copy2(image_path, image_copy_path)
        elif raw["Dataset_type"] == "TEST":
            image_path = os.path.join(images_path2, file_name)
            image_copy_path = os.path.join(target_dir, file_name)
            shutil.copy2(image_path, image_copy_path)
        cnt += 1
print("no.of images", cnt)

kaggle_file_path = "COVID-19-master/X-Ray Image DataSet/No_findings"
target_dir1 = "new_data_covid/no_findings"
image_names = os.listdir(kaggle_file_path)
random.shuffle(image_names)
for i in range(401):
    image_name = image_names[i]
    image_path = os.path.join(kaggle_file_path, image_name)
    target_path = os.path.join(target_dir1, image_name)
    shutil.copy2(image_path, target_path)

source_dir = "source_data/pneumonia"
destination_dir1 = "dataset/train/Pneumonia"
destination_dir2 = "dataset/valid/Pneumonia"
destination_dir3 = "dataset/test/Pneumonia"
image_names1 = os.listdir(source_dir)
random.shuffle(image_names1)
for i in range(1932):
    image_name = image_names1[i]
    image_path = os.path.join(source_dir, image_name)
    if i < 1536:
        target_path = os.path.join(destination_dir1, image_name)
        shutil.copy2(image_path, target_path)
    elif i < 1920:
        target_path = os.path.join(destination_dir2, image_name)
        shutil.copy2(image_path, target_path)
    else:
        target_path = os.path.join(destination_dir3, image_name)
        shutil.copy2(image_path, target_path)



