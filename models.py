from peewee import *


db = SqliteDatabase('view_memory.db')

class BaseModel(Model):
    class Meta:
        database = db

class Picture(BaseModel):
    filepath = CharField(unique=True)
    status = CharField(choices=['not_viewed', 'viewed', 'skipped'])
    viewed_date = DateTimeField()

