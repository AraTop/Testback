from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)  # Поле родительского элемента
    menu_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title
