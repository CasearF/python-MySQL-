import module
import pymysql

join = module.join()
GetColumn = module.GetColumn()  # 增
delt = module.delt()  # 删
Renewal = module.Renewal()  # 改
Inquire = module.Inquire()  # 查
host = input("请输入数据库地址")
user = input("请输入用户名")
password = input("请输入密码")
while True:
    try:
        print("1；增\n2；删\n3；改\n4；查")
        i = int(input("选择功能"))
        if 1 <= i <= 4:
            library_name = input("请输入数据库名")
            table_name = input("请输入表名")
            join.join(host,user,password,library_name)
            if i == 1:
                GetColumn.GetColumn(join.cursor, join.conn, table_name)
                module.close(join.cursor, join.conn)
            elif i == 2:
                delt.deltf(join.cursor, join.conn, table_name)
                module.close(join.cursor, join.conn)
            elif i == 3:
                Renewal.Renewalf(join.cursor, join.conn, table_name)
                module.close(join.cursor, join.conn)
            elif i == 4:
                Inquire.run(join.cursor, join.conn, table_name)
                module.close(join.cursor, join.conn)
        else:
            print("输入的数字不在1到4之间")
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！！")
