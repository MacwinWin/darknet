import os
files = [file_name for file_name in os.listdir('./data/my-yolov3-mask-data/') if file_name.endswith('.jpg')]
with open('./build/darknet/x64/data/train.txt', 'a') as train_txt:
    for file_name in files:
        train_txt.write('data/my-yolov3-mask-data/{}\n'.format(file_name))
