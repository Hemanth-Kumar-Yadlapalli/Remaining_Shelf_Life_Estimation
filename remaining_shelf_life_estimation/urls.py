"""remaining_shelf_life_estimation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.contrib import admin
from Remote_User import views as remoteuser
from remaining_shelf_life_estimation import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', remoteuser.login, name="login"),
    re_path(r'^Register1/$', remoteuser.Register1, name="Register1"),
    re_path(r'^Predict_Remaining_Shelf_Life_Estimation/$', remoteuser.Predict_Remaining_Shelf_Life_Estimation, name="Predict_Remaining_Shelf_Life_Estimation"),
    re_path(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    re_path(r'^serviceproviderlogin/$', serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    re_path(r'^View_Remote_Users/$', serviceprovider.View_Remote_Users, name="View_Remote_Users"),
    re_path(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts, name="charts"),
    re_path(r'^charts1/(?P<chart_type>\w+)', serviceprovider.charts1, name="charts1"),
    re_path(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
    re_path(r'^Find_Prediction_Of_Remaining_Shelf_Life_Estimation_Ratio/$', serviceprovider.Find_Prediction_Of_Remaining_Shelf_Life_Estimation_Ratio, name="Find_Prediction_Of_Remaining_Shelf_Life_Estimation_Ratio"),
    re_path(r'^train_model/$', serviceprovider.train_model, name="train_model"),
    re_path(r'^View_Prediction_Of_Remaining_Shelf_Life_Estimation/$', serviceprovider.View_Prediction_Of_Remaining_Shelf_Life_Estimation, name="View_Prediction_Of_Remaining_Shelf_Life_Estimation"),
    re_path(r'^Download_Trained_DataSets/$', serviceprovider.Download_Trained_DataSets, name="Download_Trained_DataSets"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


