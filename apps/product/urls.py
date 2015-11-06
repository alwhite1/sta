from django.conf.urls import patterns, url
from apps.product.views import CategoriesList


urlpatterns = patterns('apps.product.views',
                       url(r'^$', CategoriesList.as_view(), name='categories'),
                       url(r'^last/', 'get_last', name='last'),
                       url(r'^(?P<category_slug>[\w-]+)/$', 'get_category', name='category_products'),
                       url(r'^(?P<category_slug>[-\w]+)/(?P<product_slug>[-\w]+)/$',
                           'get_product', name='single_product'),
                       )
