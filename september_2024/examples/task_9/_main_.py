import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import csv

X = []
Y = []
cnt_2015 = 0
cnt_2016 = 0
cnt_2017 = 0
total_today = 0
total = 0
total_holiday_today = 0
total_holiday = 0

# Временная
total_first = 0

with open("data.csv", encoding='utf_8') as r_file:
    file_reader = csv.reader(r_file, delimiter=',')
    cnt = 0
    for row in file_reader:
        if cnt != 0:
            X.append(tuple([i for i in row[:10]]))
            Y.append((row[-1]))
        else:
            cnt = 1
for i in range(len(X)):
    if (str(X[i][0]))[3] == '5' and str(X[i][6]) == '1':
        cnt_2015 += 1
    if (str(X[i][0]))[3] == '6' and str(X[i][6]) == '1':
        cnt_2016 += 1
    if (str(X[i][0]))[3] == '7' and str(X[i][6]) == '1':
        cnt_2017 += 1

for i in range(1, len(X)):
    total_today += int(X[i][1])
    if i % 24 == 0:
        total += (total_today / 24)
        total_today = 0
    if str(X[i][6]) == '1':
        total_holiday_today += int(X[i][1])
        if i % 24 == 0:
            total_holiday += (total_holiday_today / 24)
            total_holiday_today = 0

for i in range(24):
    total_first += int(X[i][1])
print(f"В первый день арендовали {total_first}")
print(f"Среднее арифметическое арендованных велосипедов за все дни: {total / (len(X) / 24)}")
print(cnt_2015)
print(cnt_2016)
print(cnt_2017)

