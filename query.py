# -*- coding:utf-8 -*-
import pymysql
import os
import datetime
import codecs
import csv


# describe :  查询数据
def conn_mysql(level, start, end):
    sql = open('sql/sql.txt', 'r', encoding='utf-8').read()
    try:
        conn = pymysql.connect(host='172.16.4.100', port=3309, user='xaevdata_rds_ro', passwd='b772C69C9E3566@D',
                               charset='utf8')
        print("连接到mysql服务器...............成功！")
        cur = conn.cursor()
        print("连接到数据库查询数据..................")
        cur.execute(sql % (level, start, end))
        print("连接到数据库查询数据.............成功！")
        return cur.fetchall()
    except Exception as e:
        print('无法连接到mysql服务器，请检查是否打开VPN或者网络故障', e)


# 读取数据
def read_mysql_to_csv(level, start, end):
    header = ['ALARM_SEQ', 'VIN', 'VIN&PLATE_NUMBER', 'BRAND_MODEL', 'ORG_NAME', 'PLATE_NUMBER', 'item_cname',
              'ALARM_LEVEL', 'START_TIME', 'END_TIME', 'ALARM_TYPE_CODE', 'STATUS', 'ALARM_TYPE_VALUE', 'VEHICLE_SEQ',
              'item_code', 'duration']
    filename = 'csv/' + str(level) + '级告警' + start + '-' + end + '.csv'
    try:
        os.mkdir('csv/')
        print("创建文件目录成功")
    except Exception as e:
        print("文件目录已经存在")
    with codecs.open(filename=filename, mode='w', encoding='gb2312') as f:
        write = csv.writer(f, dialect='excel')
        write.writerow(header)
        conn = conn_mysql(level, start, end)
        try:
            for result in conn:
                write.writerow(result)
            print("创建%s成功" % filename)
        except Exception as e:
            print("创建%s失败" % filename, e)


# 压缩文件并删除csv
def yasuo(tar_name):
    os.chdir('csv/')
    # 　压缩Csv文件
    tar = os.system("tar czvf %s.tar.gz *.csv" % tar_name)
    if tar == 0:
        print("csv文件压缩成功")
    else:
        print("csv文件压缩失败")
    # 压缩后删除csv文件
    delete = os.system('rm -f *.csv')
    if delete == 0:
        print("csv文件删除成功")
    else:
        print("csv文件删除失败")


if __name__ == "__main__":
    end = datetime.date.today().strftime('%Y%m%d')
    start = (datetime.datetime.now() - datetime.timedelta(days=7)).date().strftime('%Y%m%d')
    for i in range(1, 4):
        read_mysql_to_csv(i, start, end)
    # yasuo(start, end)
