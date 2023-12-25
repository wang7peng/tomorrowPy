import datetime

year = datetime.datetime.now().year
print("当前" + str(year) + "年")
print(datetime.datetime.now().strftime('%m-%d'))
print(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

a = input("幸运数字: ")
print(a + " 的ASCII字符: ", ord(a))

oldyear = input("请输入年份: ")
# 输入的是字符串, 要进行数字转换
age = year - int(oldyear)

if age < 18:
    print("未成年")
if age >= 18 and age < 35:
    print("青年人")
if age >= 35 and age < 60:
    print("中年人")
if age >= 60:
    print("老年人")

# print 调用函数前用 ,