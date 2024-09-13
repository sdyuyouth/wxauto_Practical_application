from wxauto import WeChat
import pandas as pd


wx = WeChat()

# 假设Excel文件名为 'completed.xlsx'，并且有'姓名'这一列
excel_file = "在这里输入Excel文件名的完整路径，其中单个反斜杠需要转义，例如：C:\\Users\\Administrator\\Desktop\\completed.xlsx"

# 在这里改header的参数，header=1表示从第二行开始读取列名，如果没有表头，即“姓名”在第一行，则header=0
df = pd.read_excel(excel_file, header=1)

# 将'姓名'列转换为列表
completed_names = df['姓名'].tolist()

# 定义所有人的名单列表
classmates = [
    '在这里输入全体同学的名字，用英文逗号隔开，例如：张三,李四,王五',
    '可以让ai生成，例如：xxx以上为我们全体同学的名单，请你按照python的列表语法格式为我生成一个列表',
]

# 将两个列表转换为集合
all_names_set = set(classmates)
completed_names_set = set(completed_names)

# 使用集合的差集操作找出未完成任务的人员名单
uncompleted_names_set = all_names_set - completed_names_set

# 将结果转换回列表
uncompleted_names = list(uncompleted_names_set)

print("未完成人员：", uncompleted_names)

# 要发送的消息
message = input("请输入要发送的消息：")

# 遍历未完成任务的人员名单，发送消息
for person in uncompleted_names:
    wx.SendMsg(message, person)
