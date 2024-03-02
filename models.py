# from datetime import datetime

# from mongoengine import EmbeddedDocument, Document
# from mongoengine.fields import ReferenceField, BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField

# class Authors(Document):
#     ID = StringField()
#     name = StringField()
   
# class Quotes(EmbeddedDocument):
#     quote = StringField()
#     author = ReferenceField(Authors)
#     tags = StringField()

from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ObjectId, ReferenceField, BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class nnij(Document):
    _id = ObjectId()
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    
class quotes(Document):
    author_id = ReferenceField(nnij)
    quote = StringField()
    tags = ListField()
  

    
