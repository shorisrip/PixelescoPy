from peewee import *
import datetime

db = SqliteDatabase('view_memory.db')

class BaseModel(Model):
    class Meta:
        database = db

class Image(BaseModel):
    filepath = CharField(unique=True, null=False)
    status = CharField(choices=['not_viewed', 'viewed', 'skipped'], null=False)
    viewed_date = DateTimeField(null=True)
    created_date = DateTimeField(default=datetime.datetime.now)

