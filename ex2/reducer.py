#!/usr/bin/python3

import sys

(current_year, current_temp, max_temp, min_temp) = (None, None, 0, 0)

count = 0
total = 0
for line in sys.stdin:
    year, temp = line.strip().split('\t')
    if (current_year != None) and (current_year != year):
        # Nhiệt độ trung bình được làm tròn đến 1 chữ số phần thập phân và nhân 10
        print('%s\t%.3d\t%.3d\t%.3d'% (current_year, int(round(total / count, 1)),max_temp,min_temp))
        (current_year, current_temp, max_temp, min_temp) = (year, int(temp),int(temp),int(temp))
        total = current_temp 
        count = 1
    else:
        (current_year, current_temp, max_temp, min_temp) = (year, int(temp),max(max_temp, int(temp)) ,min(min_temp, int(temp)))
        total += current_temp
        count += 1
        
if current_year:
	print('%s\t%.3d\t%.3d\t%.3d'% (current_year, int(round(total / count, 1)),max_temp,min_temp))
