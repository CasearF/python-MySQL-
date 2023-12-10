import pymysql


class join:
    def join(self,host,user,password,library_name):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=library_name,
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cursor = self.conn.cursor()


class GetColumn:
    def GetColumn(self, cursor, conn, table_name):
        query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'abc' AND TABLE_NAME = '{table_name}';"
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        column_names = [item["COLUMN_NAME"] for item in results]
        print(column_names)
        # 创建一个字典来存储列名和对应的值
        column_values_dict = {}

        # 提示用户输入每列的值
        for column_name in column_names:
            while True:
                value = input(f"请输入{column_name}的值：")
                if value:
                    column_values_dict[column_name] = value
                    break
                else:
                    print("输入不能为空，请重新输入")

        # 检查输入值的数量是否与列的数量匹配
        if len(column_values_dict) == len(column_names):
            # 构建参数化的INSERT查询
            placeholders = ", ".join(["%s"] * len(column_names))
            insert_query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({placeholders})"
            print(insert_query)

            # 执行参数化查询
            # cursor.execute(insert_query, list(column_values_dict.values()))
            try:
                cursor.execute(insert_query, list(column_values_dict.values()))
            except Exception as e:
                print(f"输入有误: {e}")
            conn.commit()
        else:
            print("输入的值的数量与列的数量不匹配")


class Inquire:
    def run(self, cursor, conn, table_name):
        try:
            # 获取用户输入
            column_name = input("请输入要查询的列名: ")
            search_term = input("请输入要搜索的关键词: ")

            # 将空格替换为`
            column_name = column_name.replace(" ", "`")
            search_term = search_term.replace(" ", "`")

            # 构建查询语句
            query = f"SELECT * FROM {table_name} WHERE `{column_name}` LIKE '%{search_term}%'"
            n = input("是否确认操作无误（yes/no）")
            # 执行查询
            if n == "yes":
                print("确认操作")
                cursor.execute(query)
                results = cursor.fetchall()

                # 输出查询结果
                if results:
                    for result in results:
                        print(result)
                    else:
                        print("没有找到相关数据!")
            else:
                print("取消操作")

        except pymysql.Error as e:
            print(f"查询错误: {e}")
        except Exception as e:
            print(f"输入有误: {e}")


class delt:
    def deltf(self, cursor, conn, table_name):
        # 获取用户输入
        column_name = input("请输入要删除的列名: ")
        search_term = input("请输入要删除的关键词: ")
        query = (
            f"SELECT * FROM {table_name} WHERE `{column_name}` LIKE '%{search_term}%'"
        )

        # 执行查询
        cursor.execute(query)
        results = cursor.fetchall()

        # 输出查询结果
        if results:
            column_name = column_name.replace(" ", "`")
            search_term = search_term.replace(" ", "`")

            # 构建查询语句
            sql = f"DELETE FROM {table_name} WHERE `{column_name}` LIKE '%{search_term}%';"
            n = input("是否确认操作无误（yes/no）")
            # 执行查询
            if n == "yes":
                try:
                    # 执行SQL语句
                    cursor.execute(sql)
                    # 提交到数据库执行
                    conn.commit()
                    print("成功")
                except Exception as e:
                    # 发生错误时回滚
                    conn.rollback()
                    print(f"执行SQL出错: {e}")
            else:
                print("取消操作")
        else:
            print("没有找到相关数据!")


class Renewal:
    def Renewalf(self, cursor, conn, table_name):
        # 获取用户输入
        column_name = input("输入要更改的列名")  # 用实际列名替换
        search_term = input("输入要查询的关键字")  # 用实际搜索词替换
        new_value = input("输入要更改的值")  # 用实际的新值替换
        query = (
            f"SELECT * FROM {table_name} WHERE `{column_name}` LIKE '%{search_term}%'"
        )

        # 执行查询
        cursor.execute(query)
        results = cursor.fetchall()

        # 输出查询结果
        if results:
            column_name = column_name.replace(" ", "`")
            search_term = search_term.replace(" ", "`")

            # 构建查询语句
            rwl = f"UPDATE {table_name} SET {column_name} = '{new_value}' WHERE {column_name} LIKE '%{search_term}%';"
            n = input("是否确认操作无误（yes/no）")
            # 执行查询
            if n == "yes":
                try:
                    # 执行SQL语句
                    cursor.execute(rwl)
                    # 提交到数据库执行
                    conn.commit()
                    print("成功")
                except Exception as e:
                    # 发生错误时回滚
                    self.conn.rollback()
                    print(f"执行SQL出错: {e}")
        else:
            print("没有找到相关数据!")


def close(cursor, conn):
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接