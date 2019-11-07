# 多线程
import threading
import time


def work():
    print("我是多线程运行")
    time.sleep(1)
    return

start_time = time.time()
for i in range(5):
    t = threading.Thread(target=work)
    t.start()
end_time = time.time()
print('花费时间:%.2fs' % (end_time - start_time))














# 单线程
def work():
    print("work")
    time.sleep(1)
    return


if __name__ == "__main__":
    start_time = time.time()
    for i in range(5):
        work()
    end_time = time.time()
    print('花费时间:%.2fs' % (end_time - start_time))