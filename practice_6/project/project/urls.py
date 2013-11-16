from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'library.views.books'),
    url(r'^library/$', 'library.views.books'),
    url(r'^library/books/$', 'library.views.books'),
    url(r'^library/books/(?P<book_id>\w+)/$', 'library.views.book'),
    url(r'^library/authors/$', 'library.views.authors'),
    url(r'^library/authors/(?P<author_id>\w+)/$', 'library.views.author'),
    #url(r'^log/$', 'pages.views.listing'),
    #url(r'^log/(?P<dir_name>\w+)/$', 'pages.views.listing'),

    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
