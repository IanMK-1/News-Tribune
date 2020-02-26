from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.news_today, name='newsToday'),
    path('search/', views.search_results, name='search_results'),
    re_path('archives/(\d{4}-\d{2}-\d{2})/', views.past_days_news, name='pastNews'),
    re_path('article/(\d+)', views.article, name ='article')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
