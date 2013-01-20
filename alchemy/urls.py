from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from alchemy.resources import api

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'alchemy.views.home', name='home'),
	# url(r'^alchemy/', include('alchemy.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# url(r'^admin/', include(admin.site.urls)),

	url('^angular/?$', TemplateView.as_view(
		template_name="angular.html"
	)),

	url(r'^api/', include(api.urls)),
)
