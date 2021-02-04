from django import template

register = template.Library()

@register.filter()
def is_digit(string):
    if string.isdigit():
       return float(string)
    else:
        try:
            float(string)
            return float(string)
        except ValueError:
            string = 0.5
            return string

@register.filter()
def color_function(value):
    if is_digit(value):
        if value < 0:
            color1 = 'green'
            return color1
        elif value > 1 and value < 2:
            color1 = '#F6BFB3'
            return color1
        elif value > 2 and value < 5:
            color1 = '#F97A5E'
            return color1
        elif value > 5:
            color1 = '#F93105'
            return color1

