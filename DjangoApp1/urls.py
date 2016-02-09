# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from DjangoApp1 import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^bar/(?P<bar_name_slug>[\w\-]+)/$', views.bares, name='bar'),
 	url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
	url(r'^login/$', views.user_login, name='login'),
	url(r'^mainpage/$', views.mainpage, name='mainpage'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^like_bar/$', views.like_bar, name='like_bar'),
	url(r'^like_tapas/$', views.like_tapas, name='like_tapas'),
 	url(r'^add_tapa/(?P<bar_name_slug>[\w\-]+)/$', views.add_tapa, name='add_tapa'), # NEW MAPPING!
	url(r'^reclama_datos/$', views.reclama_datos, name='reclama_datos'),
    ) # New!


'''
El caracter r antes de la cadena de texto indica que es una cadena de caracteres en crudo. Esto permite que no tengamos que poner constantemente sentencias de escape para caracteres propios de expresiones regulares.
El caracter ^ indica el comienzo de nuestra expresión.
El caracter $ indica el fin de nuestra expresión.

'''
