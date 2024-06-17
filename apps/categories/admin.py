from django.contrib import admin
from .models import Category
from .models import SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
        fields = '__all__'


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = SubCategory
        fields = '__all__'