from django.contrib import admin

from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Поля, по которым будет работать поиск (поисковая строка сверху)
    search_fields = ['name', 'slug']

    # Поля, по которым можно фильтровать (сайдбар справа)
    list_filter = ['name']  # Фильтр по имени (и slug, если добавить)

    # Какие поля отображать в списке всех категорий (опционально)
    list_display = ['id', 'name', 'slug', 'created_at']

    # Поля, по которым можно сортировать (кликая на заголовок)
    sortable_by = ['name', 'created_at']