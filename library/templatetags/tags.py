from django import template

register = template.Library()


@register.simple_tag
def favourite_quantity(request):
    return request.user.favourite_books.all().count()
