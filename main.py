# -*- coding:utf-8 -*-
import datetime
import query
import sendEmail

# 运行开始时间
start_time = datetime.datetime.today()
print("\n\n\n\n【程序开始时间为：】", start_time)
week_dict = {0: '一', 1: '二', 2: '三', 3: '四', 4: '五', 5: '六', 6: '日'}
week_tuple = ['一', '二', '三', '四', '五', '六', '日']
# 判断是不是周四，第周四发送前面7天的数据
if datetime.datetime.now().weekday() != 3:
    exit("今天是周%s，周四才能获取数据\n"
         "请检查服务器时间或者等周四再取数据\n"
         "程序退出.......................\n" % week_tuple[datetime.datetime.now().weekday()])
else:
    print("今天是周四，正在获取数据......")
end = (datetime.datetime.now() - datetime.timedelta(days=1)).date().strftime('%Y%m%d')
start = (datetime.datetime.now() - datetime.timedelta(days=7)).date().strftime('%Y%m%d')
file_name = start + '-' + end + "告警数据"

# 循环发送三级告警
for i in range(1, 4):
    query.read_mysql_to_csv(i, start, datetime.datetime.now().date().strftime('%Y%m%d'))
query.yasuo(file_name)
end_time = datetime.datetime.today()
cost_time = str(end_time - start_time)
message = "fanghuanhua你好：\n" \
          "\t请注意查收%s 到 %s 车平台的告警数据。\n" \
          "PS:请核对数据日期是否准确" % (start, end)
message += "\n数据查询时常长：%s " % cost_time
sendEmail.send(message, file_name + '.tar.gz')
