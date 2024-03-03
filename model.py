from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ObjectId, ReferenceField, BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Contact(Document):    
    mail = StringField()
   
    description = StringField()
    
class quotes(Document):
    author_id = ReferenceField(nnij)
    quote = StringField()
    tags = ListField()