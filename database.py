import re
import psycopg2


class DataBase:
    def __init__(self, database_url):
        config_list = re.split(':|/|@', database_url)[3:]
        self.host = config_list[2]
        self.database = config_list[4]
        self.user = config_list[0]
        self.password = config_list[1]
        self.port = config_list[3]

    def connect_to_db(self):
        conn = None

        try:
            conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port)

        except Exception as error:
            print("DATABASE CONNECTION FAILED" + str(error))
        finally:
            return conn

    def query_data_base(self, statement):
        db = self.connect_to_db()
        rows = []
        try:
            if db is not None:
                cur = db.cursor()
                cur.execute(statement)
                rows = cur.fetchall()
                cur.close()
        except Exception as error:
            print("QUERY TO DATABASE FAILED" + str(error))
        finally:
            if db is not None:
                db.close()
        return rows

    def build_query(self, column_list, table):
        column = ','.join([str(col) for col in column_list])

        statement = "SELECT" + ' ' + column + ' ' + "FROM" + ' ' + table

        return statement

    def select_query(self, column_list, table):
        statement = self.build_query(column_list,table)
        rows = self.query_data_base(statement)
        return self.select_query_result_to_dictionary(column_list,rows)

    def select_query_result_to_dictionary(self, columns, rows):
        dic_list = []
        for index, row in enumerate(rows):
            dic = {}
            for i, column in enumerate(columns):
                dic[column] = rows[index][i]
            dic_list.append(dic)

        return dic_list
