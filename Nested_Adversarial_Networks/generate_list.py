from os import listdir
from os.path import isfile, join
import re
train_image_pattern = re.compile("^[0-9]+\.jpg$")
annotation_pattern = re.compile("^([0-9]+)_([0-9]+)_([0-9]+)\.png$")

train_image_path = 'LV-MHP-v2/train/images'
annotations_path = 'LV-MHP-v2/train/parsing_annos'
train_images = [f for f in listdir(train_image_path) if isfile(join(train_image_path, f)) and train_image_pattern.match(f)]
annotations = [f for f in listdir(annotations_path) if isfile(join(annotations_path, f)) and annotation_pattern.match(f)]


output_file = open("lv-mhp-v2.txt", "w")
for annotation in annotations:
    corresponding_train = annotation.split("_")[0] + ".jpg"
    if corresponding_train in train_images:
        output_file.write(join(train_image_path, corresponding_train) + "\t" + join(annotations_path, annotation))
        output_file.write("\n")

