import mysql.connector as mysql
from tabulate import tabulate as tb
"""this module specially design for those who don't know SQL and want to interact with databaes:
default server that it interact with is Xampp :"""
class database:


    """each function use 'db_name' as database name for using it :"""
    def __init__(self,db_name="",host='localhost',user='root',password=''):
        """user can change the server , default is xampp :
        each function use 'db_name' as database name for using it :"""

        self.db_name = db_name
        self.mysqlconnect = mysql.connect(
            host=host,
            user=user,
            password=password
        )
        self.mydbcur = self.mysqlconnect.cursor()

    def table_format(self, data, header, format = "psql"):
        print(tb(data, header, format))

    def create_database(self, db_name):
        """accept one argument 'database_name' and create database if not exist:"""

        self.mydbcur.execute(f"create database if not exists {db_name}")
        print(f"creating database '{db_name}', query executed :".title())

    def show_databses(self):
        """To show all databases on server :"""
        self.mydbcur.execute("show databases")
        self.table_format(self.mydbcur,"All_Databases".split(','))
        return self.mydbcur

    def show_tables(self):
        """To show all tables on 'db_name' database :"""
        self.mydbcur.execute(f"use {self.db_name}")
        self.mydbcur.execute("show tables")
        self.table_format(self.mydbcur,f"tables_in_{self.db_name}".split(','))
        return self.mydbcur

    def create_table(self,table_name, columns):
        """accept two argument to create table 'table_name' of columns 'columns':"""
        self.mydbcur.execute(f"create table if not exists {self.db_name}.{table_name}({columns})")
        print(f"creating table '{table_name}', query executed :".title())

    def show_data(self,colums,table_name,cluase = "where 1=1"):
        """To retrive data from table in 'db_name' database :
        SYNTEX :
                obj.show_data('*','t_name', 'clause 1=1')"""

        if colums == "*":
            self.mydbcur.execute(f"desc {self.db_name}.{table_name}")
            colum = [x[0] for x in self.mydbcur]
        else:
            colum = colums.split(',')
        self.mydbcur.execute(f"select {colums} from {(self.db_name)}.{(table_name)} {cluase}")
        data = [x for x in self.mydbcur]
        self.table_format(data,colum)
        print(f"{len(data)} rows executed :")
        return data

    def show_all_column(self,table_name,cluase = "where 1=1"):
        self.show_data("*",table_name,cluase)

    def show_dis_data(self,colums,table_name,cluase = "where 1=1"):
        self.show_data("distinct"+colums,table_name,cluase)

    def insert_data(self,table_name,columns ="",values=""):
        self.mydbcur.execute(f"insert into {self.db_name}.{table_name}({columns}) values({values})")
        self.mydbcur.execute("commit")

    def insert_multi_data(self,table_name,columns = "",values = ""):
        data = values.split(',')
        for val in data:
            self.insert_data(table_name,columns,val)

    def update_data(self,table_name,column_values,condition ='where 1=1'):
        self.mydbcur.execute(f"update {self.db_name}.{table_name} set {column_values} {condition}")
        self.mydbcur.execute("commit")

    def delete_data(self,table_name,condition = 'where 1=1'):
        self.mydbcur.execute(f"delete from {self.db_name}.{table_name} {condition}")
        self.mydbcur.execute("commit")
        print("Data deleted :")
    

    def delete_database(self,db_name):
        self.mydbcur.execute(f"drop database {db_name}")
        self.mydbcur.execute("commit")
        print(f"{db_name} deleted :")

    def delete_table(self,table_name):
        self.mydbcur.execute(f"drop table {self.db_name}.{table_name}")
        self.mydbcur.execute("commit")
        print(f"{table_name} deleted :")

    def describe(self,table):
        self.mydbcur.execute(f"desc {self.db_name}.{table}")
        for x in self.mydbcur:
            print(x)
        return self.mydbcur

    def add_column(self,table_name,column_name,constraint):
        self.mydbcur.execute(f"alter table {self.db_name}.{table_name} add {column_name} {constraint}")
        self.mydbcur.execute("commit")

    def modify_column(self,table_name,column_name,constraint):
        self.mydbcur.execute(f"alter table {self.db_name}.{table_name} modify {column_name} {constraint}")
        print(f"alter table {self.db_name}.{table_name} modify {column_name} {constraint}")
        self.mydbcur.execute("commit")

    def modify_column_location(self, table_name, column_name, constraint, after_before,column_2nd):
        self.mydbcur.execute(f"alter table {self.db_name}.{table_name} modify {column_name} {constraint} {after_before} {column_2nd}")
        self.mydbcur.execute("commit")

    def delete_column(self,table_name,column_name):
        self.mydbcur.execute(f"alter table {self.db_name}.{table_name} drop column {column_name}")
        self.mydbcur.execute("commit")

    def rename_column(self,table_name,column_name,new_name,constraint):
        self.mydbcur.execute(f"alter table {self.db_name}.{table_name} change {column_name} {new_name} {constraint}")
        self.mydbcur.execute("commit")

    def rename_table(self,table_name,new_name):
        self.mydbcur.execute(f"use {self.db_name}")
        self.mydbcur.execute(f"alter table {table_name} rename to {new_name}")
        self.mydbcur.execute("commit")

    def create_index(self,index_name,table_name,columns):
        self.mydbcur.execute(f"create index {index_name} on {self.db_name}.{table_name}({columns})")
        self.mydbcur.execute("commit")

    def execute(self,statment):
        self.mydbcur.execute(f"use {self.db_name}")
        self.mydbcur.execute(f"{statment}")
        return self.mydbcur







