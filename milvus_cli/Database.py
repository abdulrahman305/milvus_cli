from pymilvus import db
from Types import ConnectException
from tabulate import tabulate

class Database():
  alias = "default"
  def create_database(self,dbName=None,alias=None):
    tempAlias = alias if alias else self.alias
    try:
      res = db.create_database(db_name=dbName,using=tempAlias)
      print(res)
    except Exception as e:
      raise f"Create database error!{str(e)}"
    
  def list_databases(self,alias=None):
    tempAlias = alias if alias else self.alias
    try:
      res = db.list_database(using=tempAlias)
      print('----',res)
      return res
    except Exception as e:
      raise f"List database error!{str(e)}"
  
  def drop_database(self,dbName=None,alias=None):
    tempAlias = alias if alias else self.alias
    try:
      res = db.drop_database(db_name=dbName,using=tempAlias)
      print(res)
    except Exception as e:
      raise f"Drop database error!{str(e)}"
    
  def using_database(self,dbName=None,alias=None):
    tempAlias = alias if alias else self.alias
    try:
      res = db.using_database(db_name=dbName,using=tempAlias)
      print(res)
    except Exception as e:
      raise f"Using database error!{str(e)}"