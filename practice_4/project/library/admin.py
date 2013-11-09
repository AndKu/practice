# -*- coding: utf-8 -*-


from django.contrib import admin
from library.models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email']
    list_display_links = ['last_name', 'first_name']
    ordering = ['last_name', 'first_name']


class BooksImageInline(admin.TabularInline):
    model = BooksImage


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'publication_date', 'images_count']
    list_display_links = ['title']
    search_fields = ['title']
    ordering =['publication_date']
    fieldsets = (
        (None, {'fields': ('title', 'authors', 'publication_date',)}),
        ('Выходные данные', {
            'classes': ('wide',),
            'fields': ('publisher',),
        }),
    )
    inlines = [BooksImageInline,]

    def cover(self, obj):
        return BooksImage.objects.get(id=obj.id).small_image_tag()

    def big_cover(self, obj):
        return BooksImage.objects.get(id=obj.id).big_image_tag()

    def images_count(self, obj):
        return BooksImage.objects.get(book_cover=obj.id).images_count()

    cover.allow_tags=True
    big_cover.allow_tags=True

class BooksImageAdmin(admin.ModelAdmin):
    list_display = ['book_cover','small_image_tag','big_image_tag']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'city']
    list_display_links = ['title']
    ordering = ['title']
    list_filter = ['country', 'city']
    fieldsets = (
        (None, {'fields': ('title', )}),
        ('Контактная информация', {
            'classes': ('wide',),
            'fields': ('country', 'city', 'address', 'website',),
        }),
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BooksImage, BooksImageAdmin)
admin.site.register(Publisher, PublisherAdmin)