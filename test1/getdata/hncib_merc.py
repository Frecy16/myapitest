import csv
import hashlib
from itertools import islice
from openpyxl import Workbook


# 生成指纹数据的方法
def gen_md5(data):
    # 生成md5
    md5 = hashlib.md5()  # 获取一个md5加密算法对象
    md5.update(data.encode('utf-8'))  # 制定需要加密的字符串
    return md5.hexdigest()  # 返回加密后的16进制字符串


def getdata(ordfilename, number):
    n = 1  # 定义初始值用于计数
    name = str(ordfilename).split(".")[0]  # 生成新的文件名，用于写入数据后保存文件时的文件命名
    out_set = set()  # 创建一个空集合，用于保存后续生成的不重复的数据
    wb = Workbook()  # 创建openpyxl模块里的Workbook类的实例
    ws = wb.active  # 调用正在运行的工作表
    # 打开要处理的文件
    with open(f"C:\\Users\\frecy\\Desktop\\{ordfilename}", "r", encoding="utf-8") as f:
        csv_file = csv.reader(f)  # 读取csv文件内容，返回一个 reader 对象
        # 通过 islice 用None替换掉第一行，实现过滤掉首行的目的
        for line in islice(csv_file, 1, None):
            # try…except捕获传入的序号非数字的异常
            try:
                # 判断传入的数字是不是大于0
                if number <= 0:
                    print("序号必须大于0")
                    return ValueError
                else:
                    re_str = str(line).strip("['").split("|")[number - 1]  # 按照|分割读取csv文件的每行内容，并去除首尾的“['”字符
                    # print(re_str)
                    output_data = gen_md5(re_str)  # 调用gen_md5()方法，生成指纹数据
                    if output_data not in out_set:
                        out_set.add(output_data)  # 判断指纹数据是否已经在集合中，不在就添加到集合中，用于去除重复的数据
                        # print(re_str)
                        ws.cell(n, 1, re_str)  # 将不重复的数据存入到工作表第1列，第n行中
                        n += 1  # 计数自动加1
            except TypeError:
                print("序号必须是大于0的整数")
                return TypeError
    wb.save(f"C:\\Users\\frecy\\Desktop\\{name}.xlsx")  # 将写好的工作表保存为同名的.xlsx文件，文件存放到电脑桌面上


if __name__ == "__main__":
    getdata("2020DATA1.csv", 3)  # 调用getdata方法，开始取数据并生成文件
    # getdata("20210111DATA.csv", 3)
