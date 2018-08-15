from peewee import MySQLDatabase


database = MySQLDatabase(
    'a4',
    **{'charset': 'utf8',
       'passwd': 'test',
       'port': 13306,
       'user': 'root',
       'host': 'localhost',
       'use_unicode': True}
)
