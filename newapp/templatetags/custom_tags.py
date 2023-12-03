from django import template
register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    # d = context['request'].GET.copy()
    # for k, v in kwargs.items():
    #     d[k] = v
    #     return d.urlencode()
    request_data = context['request'].GET.copy()
    for param, value in kwargs.items():
        request_data[param] = value
    return request_data.urlencode()