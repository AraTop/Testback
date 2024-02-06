from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views import View
from menu.models import Menu

class MenuClickView(View):
    def get(self, request, menu_item_id):
        try:
            menu_item = Menu.objects.get(id=menu_item_id)
            # Ваша логика обработки клика на пункт меню
            # В данном примере просто рендерим шаблон и передаем в него данные меню
            return render(request, 'menu/menu.html', {'menu_item_id': menu_item_id, 'menu_item': menu_item})
        except Menu.DoesNotExist:
            return HttpResponseNotFound("Страница не найдена")
