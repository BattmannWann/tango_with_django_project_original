import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django 
django.setup()

from rango.models import Category, Page


def populate():
    
    python_pages = [
        
        {'title': 'Official Python Tutorial',
         'url': 'https://docs.python.org/3/tutorial/'},
        
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/'},
        
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithankis.net/tutorials/python/'}
        
        ]
    
    django_pages = [
        
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoprojects.com/en/2.1/intro/tutorial01/'},
        
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/'},
        
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/'}
        
        ]
    
    
    other_pages = [
        
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/'},
        
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org'}
        
        ]
    
    cats = {
        
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}
            
        }
    
    
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])
            
        for v in cat_data['views']:
            add_page(c, v)
            
        #made the index variable 'likes' as a standalone l may not be clear, especially when using other editors and etc...    
        for likes in cat_data['likes']:
            add_page(c, likes) 
            
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category = c):
            
            print(f'- {c}: {p}, {v}, {likes}')
            
            
def add_page(cat, title, url, views = 0):
    
    p = Page.objects.get_or_create(category = cat, title = title)[0]
    p.url = url
    
    p.views = views
    p.save()
    
    return p

def add_cat(name, views = 0, likes = 0):
    
    c = Category.objects.get_or_create(name = name, views = views, likes = likes)[0]
    c.save()
    
    return c


#Execution starts here for this file. If this file is not run directly, then this is not the case (i.e if this file is imported or has any of its contents imported)

if __name__ == '__main__':
    
    print('Starting Rango population script...')
    populate()