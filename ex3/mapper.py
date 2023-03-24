#!/usr/bin/python3
"""mapper.py"""

import sys

# Chương trình Python chạy trên Hadoop MapReduce qua tính năng Streaming.
# Dữ liệu vào từ thiết bị nhập chuẩn (STDIN)
# Kết quả xử lý gửi ra thiết bị xuất chuẩn (STDOUT)
f = open('input.txt', 'r')
o = open('output.txt', 'w')

comment = 0

for line in f:
    if comment < 4:
        comment +=1
        continue
    # loại bỏ ký tự trắng ở đầu và cuối chuỗi
    line = line.strip()
    # tách ra thành các từ
    fromNode, toNode = line.split('\t')
    # đưa ra thiết bị xuất chuẩn các cặp <word, 1>, cách nhau bằng ký tự tab
    print('%s\t%s\t1' % (fromNode,toNode))
    o.write('%s\t%s\t1\n' % (fromNode,toNode))
