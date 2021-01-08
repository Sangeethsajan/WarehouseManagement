from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'list', views.product_list),
    url(r'path', views.product_path),
    url(r'', views.product_form)
]