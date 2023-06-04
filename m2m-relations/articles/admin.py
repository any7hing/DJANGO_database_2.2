from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tags, Scope

class ScopeInLineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') is True:
                count +=1
        if count != 1:
            raise ValidationError('Обязательно должен быть один главный тэг')
        return super().clean()

class ScopeInLine(admin.TabularInline):
    model = Scope
    formset = ScopeInLineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine]

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass