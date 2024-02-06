from django.urls import path
from .views import MenuClickView

urlpatterns = [
    path('item/<int:menu_item_id>/', MenuClickView.as_view(), name='menu_item_click'),
]