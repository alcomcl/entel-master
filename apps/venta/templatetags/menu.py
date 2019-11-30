import re
from django import template
from django.urls import reverse, NoReverseMatch, reverse_lazy

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if pattern == path:
        return 'active'
    return ''


@register.simple_tag
def fecha():
    return date.today()
  
