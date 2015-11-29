from django.conf.urls import url

from . import views

urlpatterns = [ # Make views.NAME the same as name=NAME for simplicity. The first specifies which function to call in views.py, the second is for variable names in our html files.
    url(r'^$', views.index, name='index'),
	url(r'^index.html$', views.index, name='index'),
    url(r'^history$', views.history, name='history')
]
