from django import template

register = template.Library()

def is_digit1(string):
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
    test_value = is_digit1(value)
    if test_value < 0:
        color1 = '#05F97A'
        return color1
    elif test_value >= 1 and test_value < 2:
        color1 = '#F9DEDD'
        return color1
    elif test_value > 2 and test_value < 5:
        color1 = '#FB5652'
        return color1
    elif test_value > 5:
        color1 = '#D20400'
        return color1
    elif test_value >= 0 and test_value < 1:
        color1 = 'white'
        return color1

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