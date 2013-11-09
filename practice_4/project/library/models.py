# ~*~ coding: utf-8 ~*~


from django.db import models
import datetime
# Create your models here.


'''
Author
'''
class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(blank=True,null=True)

    def get_absolute_url(self):
        return "/library/authors/%i" % self.id

    def __unicode__(self):
        return u'%s %s.' % (self.first_name, self.last_name)
#IntegrityError: Problem installing fixture 'data.json': Could not load library.Author(pk=3): library_author.email may not be NULL


'''
Book
'''
class Book(models.Model):
    title = models.CharField('Название',max_length=128)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField(default=datetime.datetime.now()) #auto_now_add=True - не редактируемый вариант

    def authors_names(self):
        return self.authors.all()

    def get_absolute_url(self):
        return "/library/books/%i" % self.id

    def __unicode__(self):
        return self.title


'''
Publisher
'''
class Publisher(models.Model):
    title = models.CharField('Название',max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.URLField('Адрес сайта')

    def __unicode__(self):
        return self.title


'''
BooksImage
'''
class BooksImage(models.Model):
    book_cover = models.ForeignKey('Book')
    small_image = models.ImageField(upload_to='bookImages/small')
    big_image = models.ImageField(upload_to='bookImages/big', blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.id

    def small_image_tag(self):
        return '<img src="%s">' %(self.small_image.url)

    def big_image_tag(self):
        return '<img src="%s">' %(self.big_image.url)

    def images_count(self):
        i = 0 
        if self.small_image:
            i += 1
        if self.big_image:
            i += 1
        return i

    small_image_tag.allow_tags=True
    big_image_tag.allow_tags=True