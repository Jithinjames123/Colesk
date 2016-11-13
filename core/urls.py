from django.conf.urls import url
from . import views

urlpatterns = [ url(r'^$', views.main_page, name = 'main_page'),
    			url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
				url(r'^networks/$', views.networks, name = 'networks'),
				url(r'^you/$',views.profile, name = 'profile'),
				url(r'^feed/$', views.my_feed, name = 'my_feed'),
				url(r'^new/$', views.new_post, name = 'new_post'),
				url(r'^login/$', views.login, name = 'login'),
				url(r'^signup/$', views.sign_up, name = 'sign_up'),
				url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name = 'post_edit'),
			]					