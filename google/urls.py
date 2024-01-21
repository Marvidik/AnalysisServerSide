from django.urls import path,include
from .views import getlatestgoogle,post_new_analysis,get_particular_google
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("todays_data/",getlatestgoogle, name="todays_data"),
    path("addgoogle/",post_new_analysis,name="postgogle"),
    path("filtergoogle/",get_particular_google,name="filter-google")

   
    
]


urlpatterns+=staticfiles_urlpatterns()
