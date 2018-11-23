import time
import matplotlib.pyplot as plt
import random as R 

# ---------------------------------------------------------------------

# 获取当前时间（秒）小数点后第n个数字作为随机数，默认范围为0~9，可通过w改变
def get_random_time(n = 3):
    while True:
        now = time.time() * (10**(n-1))
        diff = int((now - int(now)) * 10)
        return diff

# 获取当前时间（秒）小数点后第n个数字作为随机数，随机生成0和1
def random_one(n = 3):
    now = time.time() * (10**(n-1))
    diff = int((now - int(now)) * 10)
    if diff < 5:
        return 0
    else:
        return 1





# ---------------------------------------------------------------------
# 使用random 生成0~9的整数
for i in iter(range(10)):
    plt.subplot(2,  1,  1) 
    plt.scatter(i, R.randint(0,9))
    plt.subplot(2,  1,  2)
    plt.scatter(i, get_random_time())  
plt.subplot(2,  1,  1) 
plt.title('random')
plt.subplot(2,  1,  2) 
plt.title('time')
plt.show()
# ---------------------------------------------------------------------

# now = time.time()
# print('当前时间：',time.time())

# for i in range(10):
#     print('当前时间以秒为单位的小数部分：',time.time()-int(time.time()))






