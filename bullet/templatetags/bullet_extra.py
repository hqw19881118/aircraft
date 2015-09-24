# encoding:utf-8

__author__ = 'huangqingwei'

from django import template

register = template.Library()


@register.filter
def total_price(num, price):
    return num * price if num and price else 0

@register.filter
def append(value, suffix):
    return '{}{}'.format(value, suffix)