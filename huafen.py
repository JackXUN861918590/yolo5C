import os
import random
import shutil

# 设置数据集路径
dataset_path = r"F:\Train"
images_path = os.path.join(dataset_path, "images")
labels_path = os.path.join(dataset_path, "labelimg")

# 创建训练集和验证集目录
train_path = os.path.join(dataset_path, "train")
val_path = os.path.join(dataset_path, "val")
os.makedirs(train_path, exist_ok=True)
os.makedirs(val_path, exist_ok=True)

# 获取所有图像和标签文件的路径
images = os.listdir(images_path)
labels = os.listdir(labels_path)

# 确保图像和标签文件数量一致
assert len(images) == len(labels)

# 将文件名列表随机排序
random.shuffle(images)

# 计算训练集和验证集的数量
train_size = int(0.8 * len(images))
val_size = len(images) - train_size

# 创建训练集和验证集目录
train_path = os.path.join(dataset_path, "train")
train_images_path = os.path.join(train_path, "images")
train_labels_path = os.path.join(train_path, "labels")
os.makedirs(train_images_path, exist_ok=True)
os.makedirs(train_labels_path, exist_ok=True)

val_path = os.path.join(dataset_path, "val")
val_images_path = os.path.join(val_path, "images")
val_labels_path = os.path.join(val_path, "labels")
os.makedirs(val_images_path, exist_ok=True)
os.makedirs(val_labels_path, exist_ok=True)

# 复制训练集图像和标签文件到train目录
for i in range(train_size):
    image_name = images[i]
    label_name = image_name.replace(".jpg", ".txt")
    src_image = os.path.join(images_path, image_name)
    src_label = os.path.join(labels_path, label_name)
    dst_image = os.path.join(train_images_path, image_name)
    dst_label = os.path.join(train_labels_path, label_name)
    shutil.copyfile(src_image, dst_image)
    shutil.copyfile(src_label, dst_label)

# 复制验证集图像和标签文件到val目录
for i in range(train_size, len(images)):
    image_name = images[i]
    label_name = image_name.replace(".jpg", ".txt")
    src_image = os.path.join(images_path, image_name)
    src_label = os.path.join(labels_path, label_name)
    dst_image = os.path.join(val_images_path, image_name)
    dst_label = os.path.join(val_labels_path, label_name)
    shutil.copyfile(src_image, dst_image)
    shutil.copyfile(src_label, dst_label)

print("数据集已成功划分为训练集和验证集！")
