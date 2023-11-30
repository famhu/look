# 导入time模块
import time

# 定义一个专注时钟类
class FocusTimer:

    # 初始化方法，设置专注时间和休息时间（单位为秒）
    def __init__(self, focus_time, break_time):
        self.focus_time = focus_time
        self.break_time = break_time

    # 开始专注时钟的方法
    def start(self):
        # 打印开始专注的提示信息
        print("开始专注！")
        # 记录开始专注的时间
        start_time = time.time()
        # 循环检查是否达到专注时间
        while True:
            # 计算已经专注的时间
            elapsed_time = time.time() - start_time
            # 如果已经达到专注时间，跳出循环
            if elapsed_time >= self.focus_time:
                break
            # 打印剩余专注时间（保留两位小数）
            print(f"剩余专注时间：{self.focus_time - elapsed_time:.2f}秒")
            # 暂停一秒
            time.sleep(1)
        # 打印结束专注的提示信息
        print("结束专注！")
        # 打印开始休息的提示信息
        print("开始休息！")
        # 记录开始休息的时间
        start_time = time.time()
        # 循环检查是否达到休息时间
        while True:
            # 计算已经休息的时间
            elapsed_time = time.time() - start_time
            # 如果已经达到休息时间，跳出循环
            if elapsed_time >= self.break_time:
                break
            # 打印剩余休息时间（保留两位小数）
            print(f"剩余休息时间：{self.break_time - elapsed_time:.2f}秒")
            # 暂停一秒
            time.sleep(1)
        # 打印结束休息的提示信息
        print("结束休息！")

# 创建一个专注时钟对象，设置专注时间为25分钟，休息时间为5分钟
focus_timer = FocusTimer(25 * 60, 5 * 60)
# 调用开始专注时钟的方法
focus_timer.start()
