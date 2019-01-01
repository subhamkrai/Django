from django import template

register =  template.Libary()

@egister.filter(name='cut')
def cut(value,arg):
    """
    This cuts all values of "arg" from the string!
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
