from datetime import datetime

from mongoengine import *
from mongoengine.fields import ObjectId, ReferenceField, BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField

class Contact(Document):  
    fullname = StringField(max_length=150)
    mail = StringField(max_length=150)
    log_field = BooleanField(default=False)