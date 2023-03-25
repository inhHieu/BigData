#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter
import sys
import numpy as np

#fl = open('output.txt', 'r')

current_F = None
current_T = '.'
F = None
current_ct = 1

arrTo = np.full(10,0)
arrFrom = np.full(10,None)

# lấy dữ liệu từ thiết bị nhập chuẩn
for line in sys.stdin:
    line = line.strip()
    F, T, ct = line.split('\t')
    try:
        ct = int(ct)
    except ValueError:
        # nếu không phải giá trị số thì bỏ qua
        continue
    # Ở cuối pha Map, các cặp (key, value) đã được sắp xếp theo key (ở đây là các từ).
    # Vì vậy ở pha Reduce, chương trình sẽ cộng giá trị value của dãy liên tiếp các từ trùng nhau
    # cho đến khi gặp từ mới.
        #
    if F == current_F:
        current_T += ','+T 
        current_ct += ct
    else:
        for x in range(len(arrTo)):
            if current_ct > arrTo[x]:
                arrTo[x] = current_ct
                arrFrom[x] = current_F
                break
        if current_F:
            print('%s\t%s\t%d' % (current_F, current_T,current_ct))
        current_F = F
        current_T = T
        current_ct = 1
if current_F == F:
    print('%s\t%s\t%d' % (current_F, current_T,current_ct))
for i in range(len(arrFrom)):
    print('%s\t%s' % (arrFrom[i],arrTo[i]))
