from django.conf.urls.defaults import *

urlpatterns = patterns('catalog.views',
	(r'^$', 'index', {'template_name':'catalog/index.html'}, 'catalog_home'),
	(r'^category/(?P<category_slug>[-\w]+/$', 'show_category',
		{'template_name': 'catalog/category.html'}, 'catalog_category'),
	(r'product/(?P<product_slug>[-\w]+)/$',
		'show_product', {
	'template_name':'catalog/product.html'}, 'catalog_product'),
)
	
