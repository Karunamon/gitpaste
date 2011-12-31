from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('saic.paste.views',
    url(r'^owner/anonymous/', 'user_pastes', name='anon_pastes'),
    url(r'^owner/(?P<owner>.+)/', 'user_pastes', name='user_pastes'),
    url(r'^(?P<pk>\d+)/adopt/$', 'paste_adopt', name='paste_adopt'),
    url(r'^(?P<pk>\d+)/edit/$', 'paste_edit', name='paste_edit'),
    url(r'^(?P<pk>\d+)/fork/$', 'paste_fork', name='paste_fork'),
    url(r'^(?P<pk>\d+)/download/$', 'paste_download', name='paste_download'),
    url(r'^(?P<pk>\d+)/favorite/$', 'paste_favorite', name='paste_favorite'),
    url(r'^(?P<pk>\d+)/delete/$', 'paste_delete', name='paste_delete'),
    url(r'^(?P<pk>\d+)/raw/$', 'paste_raw', name='paste_raw'),
    url(r'^commit/(?P<pk>.+)/adopt/$', 'commit_adopt', name='commit_adopt'),
    url(r'^users/$', 'users', name='users'),
    url(r'^(?P<pk>\d+)/$', 'paste_view', name='paste_view'),
    url(r'^favorites/$', 'favorites', name='favorites'),
    url(r'^accounts/login/$', 'login', name='login'),
    url(r'^accounts/logout/$', 'logout', name='logout'),
    url(r'^accounts/register/$', 'register', name='register'),
    url(r'^accounts/preference/$', 'preference', name='preference'),
    url(r'^accounts/timezone/$', 'set_timezone', name='set_timezone'),
    url(r'^$', 'paste', name='paste'),
)
