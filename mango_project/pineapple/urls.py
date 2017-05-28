from django.conf.urls import url
from pineapple import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^category/$', views.index, name='index'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    # raw, ignore the slashes
    # string starts with "category"
    # FORWARDSLASH
    # PARENS
    # ? = 0 or 1 DID NOT KNOW THIS
    # P
    # <category_name_slug>
    # braces/bracket
    # BACKSLASH
    # word
    # BACKSLASH
    # MINUS
    # braces/bracket
    # One or more
    # PARENS
    # FORWARDSLASH
    # End of string
    # [\w\-]+) - looks for any sequence of alphanumeric characters
    # a-z, A-Z or 0-9 and any hyphens (since slug). We can match as many as
    # we like with []+
    # SOOO
    # url pattern will match sequence of alphanumerica characters and hyphens between
    # pineapple/category/ and the last/
    # This sequesnce will be stored in the parameter category_name_slug and passed
    # to views.show_category()
    # so URL pineapple/category/python-books/ would have category_name_slug
    # python-books

    # which view to use = show_category
    # is the name of the URL that will be used to identify the view





    # keep this
    url(r'^happy/', views.happy, name='happy'),
    url(r'^admin/', admin.site.urls),
]
