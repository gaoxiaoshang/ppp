# caffe模块要在Python的路径下;
# 这里我们将把caffe 模块添加到Python路径下.
import sys

caffe_root = 'D:/CNN/caffe/'  # 该文件要从路径{caffe_root}/examples下运行，否则要调整这一行。
sys.path.insert(0, caffe_root + 'python')

import caffe
# 如果你看到"No module named _caffe",那么要么就是你没有正确编译pycaffe；要么就是你的路径有错误。