from django import template
from urllib.parse import unquote #python3

register = template.Library()



def unquote_filter(value):
    if value:
        return unquote(value)
        
        

register.filter(unquote_filter)