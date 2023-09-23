import datetime

date_string = input("请输入日期（格式：YYYY-MM-DD）：")
year, month, day = map(int, date_string.split('-'))

# 创建日期对象
date = datetime.date(year, month, day)

# 获取星期几（0代表星期一，1代表星期二，依此类推）
weekday = date.weekday()

# 星期几的名称
weekday_name = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

print(f"{date_string} 是{weekday_name[weekday]}")
