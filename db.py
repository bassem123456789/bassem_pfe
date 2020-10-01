from peewee import *
import psycopg2
import datetime


db = PostgresqlDatabase('pfe', user='postgres', password='123456789',
                           host='127.0.0.1', port='5432')



class Profile(Model):
      first_name = CharField(null=False)
      last_name = CharField(null=False)
      mail = CharField(null=False)
      phone = CharField(null=False)
      city = CharField(null=False)
      adresse = CharField(null=False)


      class Meta():
          database = db




class category(Model):
      category_name = CharField(unique=True)
      parent_category = IntegerField(null=True)   ##RECURSIVE RELATION

      class Meta():
          database = db

class item(Model):
    name = CharField(null=False)
    cat = ForeignKeyField(category, backref="category", null=False)
    culture = CharField(null=True)
    cible_resource = CharField(null=True)
    substance = CharField(null=True)
    societe_resource = CharField(null=True)
    descrip_resource = TextField(null=True)
    code = IntegerField(null=False)
    Date = DateTimeField(default=datetime.datetime.now)



    class Meta():
        database = db


class client(Model):
    name = CharField(null=False)
    phone = IntegerField(null=False)
    code = IntegerField(null=False)
    Date = DateTimeField(default=datetime.datetime.now)

    class Meta():
        database = db


class Guide(Model):
      clas_guide = CharField(unique=False)
      substance = CharField(null=False)
      concentration = CharField(null=False)
      tf_guide = CharField(null=False)
      produit = CharField(null=False)
      societe = CharField(null=False)
      utilisation = CharField(null=False)
      num = IntegerField(unique=True)

      class Meta():
          database = db
















db.connect()
db.create_tables([Profile, category, item, client, Guide])

