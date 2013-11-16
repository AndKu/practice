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
    birthyear = models.IntegerField(null=True,blank=True)

    def year(self):
        if self.birthyear:
            return self.birthyear
        else:
            return 'возраст неизвестен'

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
    description = models.TextField(null=False,blank=False,default="")

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