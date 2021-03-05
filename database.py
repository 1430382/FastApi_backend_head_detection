from peewee import *
# connect to database using ORM
mysql_db = MySQLDatabase('head_detection', user='root', password='',
													host='localhost', port=3306)
# Models
class BaseModel(Model):
	class Meta:
		database = mysql_db
class Detect(BaseModel):
	id = IntegerField()
	id_sucursal = IntegerField()
	uuid_registro = CharField()
	direction       = CharField()
	date_complete   = DateTimeField()
	class Meta:
		db_table = 'detect'
