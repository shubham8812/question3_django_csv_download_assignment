from django.urls import path,re_path,include
from . import views


# TEMPLATE URLS!
app_name = 'csv_download'

urlpatterns = [ re_path(r'^upload/',views.upload,name='upload'),
                re_path(r'^download/',views.download,name='download'),
]
