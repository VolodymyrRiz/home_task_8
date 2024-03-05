# from models import Authors, Quotes

# import connect

# # створення об'єктів Authors
# author1 = Authors()
# author2 = Authors()

# #  Останнє - створюємо об'єкт Quotes і зберігаємо його
# Quotes('quote', author=[author1, author1], tags = []).save()
#from models2 import nnij, quotes
from models import Contact
import connect

# потім - створення об'єктів Record

#  Останнє - створюємо об'єкт Note і зберігаємо його
# quotes(author_id = '65df9c849fdbbcc80b137406', quote='“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', tags = ["change", "deep-thoughts", "thinking", "world"]).save()
# quotes(author_id = '65df9c849fdbbcc80b137406', quote='“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', tags = ["inspirational", "life", "live", "miracle", "miracles"]).save()
# quotes(author_id = '65df9c849fdbbcc80b137406', quote='“Try not to become a man of success. Rather become a man of value.”', tags = ["adulthood", "success", "value"]).save()
# quotes(author_id = '65df9c849fdbbcc80b137407', quote='“A day without sunshine is like, you know, night.”', tags = ["humor", "obvious", "simile"]).save()
Contact(fullname='jkjkj jkjk', mail='riz@ukr.net', log_field=False).save()
