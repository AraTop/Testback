from django import template
from menu.models import Menu
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = Menu.objects.filter(parent=None)

    rendered_menu = '<ul class="menu">'
    for item in menu_items:
        if Menu.objects.filter(parent=item).exists():
            rendered_menu += f'<details><summary><a href="http://127.0.0.1:8000/item/{item.pk}/">{item.title}</a></summary>'
        else:
            rendered_menu += f'<li><a href="http://127.0.0.1:8000/item/{item.pk}/">{item.title}</a></li>'
        # Ищем дочерние элементы текущего элемента меню
        children = Menu.objects.filter(parent=item)
        if children.exists():
            rendered_menu += '<ul class="submenu">'
            for child in children:
                if Menu.objects.filter(parent=child).exists():
                    rendered_menu += f'<details><summary><a href="http://127.0.0.1:8000/item/{child.pk}/">{child.title}</a></summary>'
                else:
                    rendered_menu += f'<li><a href="http://127.0.0.1:8000/item/{child.pk}/">{child.title}</a></li>'
                children_two = Menu.objects.filter(parent=child)
                if children_two.exists():
                    rendered_menu += '<ul class="submenu">'
                    for child_two in children_two:
                        rendered_menu += f'<li><a href="http://127.0.0.1:8000/item/{child_two.pk}/">{child_two.title}</a></li>'
                    rendered_menu += '</ul>'
            rendered_menu += '</ul>'
    rendered_menu += '</ul>'

    return mark_safe(rendered_menu)