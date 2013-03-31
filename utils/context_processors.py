from ecomstore.catalog.models import Category
from ecomstore import settings

def ecomstore(request):
	return {
		'active_categories' : Category.objects.filter(is_active=True),
		'site_name': settings.SITE_NAME,
		'meta_keywods' : settings.META_KEYWODS,
		'meta_description' : settings.META_DESCRIPTION',
		'request': request
	}
