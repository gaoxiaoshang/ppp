from __future__ import print_function

import glob
import os
import pandas as pd
import torch


import shutil



# load data and label

train_dir = 'F:\\FaceAaing\\CHA15\\Train'
test_dir = 'F:\\FaceAaing\\CHA15\\Validation'
train_list = glob.glob(os.path.join(train_dir, '*.jpg'))
test_list = glob.glob(os.path.join(test_dir, '*.jpg'))

print(f"Train Data: {len(train_list)}")
print(f"Test Data: {len(test_list)}")

# 读取train_jpg文件名
train_name=[]
for path in test_list:
    (x,y)=os.path.split(path)
    train_name.append(y)
print(train_list)
print((train_name))

train_label=pd.read_csv('F:\\FaceAaing\\CHA15\\Reference.csv',header=0)


train_p=[]
for zz in train_name:

    train_p.append(int(train_label[train_label['name']==str(zz)]['age'].values))

print(train_p)
path_ori='F:\\FaceAaing\\CHA15'
##创造文件夹
for z in range(85):
    path_to = path_ori + '\\TTX\\' + str(z+1)
    # print(path_to)
    if( not os.path.exists(path_to)):
        os.mkdir(path_to)

## 移动文件夹

for index ,p in enumerate(train_name):
    path_come=test_list[index]
    path_to=path_ori+'\\TTV\\'+str(train_p[index])
    if( not os.path.exists(path_to)):
        os.mkdir(path_to)
    # print(path_come)
    # print(path_to)
#     # shutil.move(path_come, path_to)


