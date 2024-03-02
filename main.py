from models import nnij, quotes
import connect

while True:
    num = 0
    c = 0
    
    print()
    print('Введіть запит:')
    print("- за ім'ям (Albert, Martin) - введіть ім'я та натисніть Enter")
    print('- за тегом (change, deep-thoughts, thinking, world, humor, obvious, simile) - введіть тег та натисніть Enter')
    print('- за кількома тегами через кому без пробілів - уведіть теги та натисніть Enter')
    print('вийти з режиму запитів - Enter')
    print('')
    a = input()
    if a == '':
        exit
    if a == 'Albert' or a == 'Martin':
       names = nnij.objects()
       for name in names:
           name_author = [f'знайдено автора: {nnij.fullname}, народився: {nnij.born_date}, {nnij.born_location}, про автора: {nnij.description}']
           print(name_author)
           print()
           continue
    if a == 'change' or a == 'deep-thoughts' or a == 'thinking' or a == 'world' or a == 'humor' or a == 'obvious' or a == 'simile':
        tags = quotes.objects()
        for tag in tags:
            tags_ = [f'знайдено цитату: {quotes.quote}']
            print(tags_)
            print()
            continue
        
        b = a.split(",")
        num = len(b)
        
        if num == 1:
            print('УВАГА! Запит неточний, повторіть його!')
            print()
            continue
        if num > 1:
            for b1 in b:
                if b1 in tags:
                    text = quotes.quote                    
                    print([f'знайдено цитату: {text}'])  
                    c = +1
                if c == 0:
                    print('УВАГА! Запит неточний, повторіть його!')
                    print()
                    c = 0
                continue     
                      

