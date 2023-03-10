from django.conf.urls import url  ### IMPORTANT
from . import views ### IMPORTANT


urlpatterns = [ ### IMPORTANT - don't organize as patterns() 
                ### while importing patterns from django.conf.urls
                ### for some reason it doesn't work
    url(r'^$', views.test),
    url(r'^login/.*$', views.test, name='login'),
    url(r'^signup/.*', views.test, name='signup'),
    url(r'^question/(?P<id>[0-9]+)/$', views.test, name='question'),
    url(r'^ask/.*', views.test, name='ask'),
    url(r'^popular/.*', views.test, name='popular'),
    url(r'^new/.*', views.test, name='new')
]

### THIS CODE DIDN'T WORK:

# urlpatterns = patterns('qa.views',
#     url(r'^$', 'test'),
#     url(r'^login/.*$', 'test', name='login'),
#     url(r'^signup/.*', 'test', name='signup'),
#     url(r'^question/(?P<id>[0-9]+)/$', 'test', name='question'),
#     url(r'^ask/.*', 'test', name='ask'),
#     url(r'^popular/.*', 'test', name='popular'),
#     url(r'^new/.*', 'test', name='new')
# )

### BECAUSE name patterns failed to import. Therefore I decided to use list insread of patterns()
#   File "/home/box/web/ask/ask/urls.py", line 16, in <module>                                                                                 
#     from django.conf.urls import url, include, patterns                                                                                      
# ImportError: cannot import name 'patterns'
