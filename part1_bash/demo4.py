#--- coding:UTF-8 ---
res = 0
# range 只有 3 个参数都存在, 最后一个才能表示步长
for i in range(1,101,10):
    res += i

print(res)