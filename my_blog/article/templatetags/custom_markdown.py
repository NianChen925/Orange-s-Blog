# -*- coding: utf-8 -*-
import markdown2

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()  #自定义filter时必须加上

# @符号开始的代码不是注释
@register.filter(is_safe=True)  #注册template filter
@stringfilter  #希望字符串作为参数
def custom_markdown(value):
    return mark_safe(markdown2.markdown(force_unicode(value),extras=["code-friendly"]))
