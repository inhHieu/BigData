#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter
import sys
import numpy as np

f = open('output.txt', 'r')

current_f_node = None
current_t_node = None
current_t_count = int(0)
t_count = None

# lấy dữ liệu từ thiết bị nhập chuẩn
for line in f:
    # loại bỏ ký tự trắng ở đầu và cuối chuỗi
    line = line.strip()

    # tách ra thành cặp <word, 1> (Chú ý: Ở file reducer.py cặp <word, 1> xuất ra với ký tự phân cách tab)
    f_node, t_node, t_count = line.split('\t')
    # print(f_node,t_node)
    # chuyển giá trị count thành kiểu số
    try:
        t_count = int(t_count)
    except ValueError:
        # nếu không phải giá trị số thì bỏ qua
        continue
    # Ở cuối pha Map, các cặp (key, value) đã được sắp xếp theo key (ở đây là các từ).
    # Vì vậy ở pha Reduce, chương trình sẽ cộng giá trị value của dãy liên tiếp các từ trùng nhau
    # cho đến khi gặp từ mới.
    if t_node == current_t_node: # nếu from node trùng với from node đang xét thì tăng giá trị đếm của từ đang xét
        current_t_count += t_count
    else:
        if current_t_node: # nếu gặp từ mới thì in ra số lần xuất hiện của từ đang xét
            print('%s\t%s\t%s' % (current_f_node, current_t_node,current_t_count))

# #         # sau đó chuyển sang xử lý từ mới
        current_f_node = f_node
        current_t_node = t_node
        current_t_count = t_count

# # # in ra từ cuối cùng
if current_t_node == t_node:
    print('%s\t%s\t%s' % (current_f_node, current_t_node,current_t_count))

