#--- coding:UTF-8 ---
fp=open(r'/home/mr.txt', 'a+')
print("xxx", file=fp)
fp.close()

# 运行时不加sudo直接 python3 demo2.py 不行, home目录没有新建文件的权限
#

# try:
# sudo python3 demo2.py
# cat /home/<tab>