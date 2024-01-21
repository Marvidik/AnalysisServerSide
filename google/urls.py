from django.urls import path,include
from .views import getlatestgoogle,post_new_analysis
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("todays_data/",getlatestgoogle, name="todays_data"),
    path("addgoogle/",post_new_analysis,name="postgogle")
    
]


urlpatterns+=staticfiles_urlpatterns()
