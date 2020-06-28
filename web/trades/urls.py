from django.urls import path

from . import views

app_name = "trades"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:trade_id>/', views.detail, name='detail'),
    path('<int:trade_id>/results/', views.results, name='results'),
    path('<int:trade_id>/vote/', views.vote, name='vote'),
]