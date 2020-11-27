from django import template
register = template.Library()


def removeSpaces(name):
    name = name.replace(' ', '')
    return name

register.filter('removeSpaces', removeSpaces)