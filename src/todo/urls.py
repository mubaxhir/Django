from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/<int:month>/<int:day>', views.get_purchases_by_date, name='get_purchases_by_date'),
    path('all', views.get_purchases, name='get_purchases'),
    path('create',views.post_purchases,name='post_purchases'),
    path('predictor',views.predictor,name='predictor'),
]