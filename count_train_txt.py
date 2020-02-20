import os
Y_count = 0
N_count = 0
files = [file_name for file_name in os.listdir('build/darknet/x64/data/my-yolov3-mask-data/') if file_name.endswith('.txt')]
for file_name in files:
    with open('build/darknet/x64/data/my-yolov3-mask-data/{}'.format(file_name)) as file:
        lines = file.readlines()
        for line in lines:
            if line.split(' ')[0] == '1':
                Y_count += 1
            elif line.split(' ')[0] == '0':
                N_count += 1
print(Y_count, N_count)
