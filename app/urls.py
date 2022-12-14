"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import re_path
from app import views

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^datatable/', views.DataTable.as_view()),
    # re_path(r'^datatable/(?P<station>\d+)/', views.DataTable.as_view()),
    re_path(r'^datatable/$', views.DataTable.as_view()),
    re_path(r'^linechart/$', views.LineChartView.as_view()),
    re_path(r'^temperaturelinechart/$', views.TemperatureLineChartView.as_view()),
    re_path(r'^windspeedlinechart/$', views.WindSpeedLineChartView.as_view()),
    re_path(r'^pressurelinechart/$', views.PressureLineChartView.as_view()),
    re_path(r'^solarradiationlinechart/$', views.SolarRadiationLineChartView.as_view()),
    re_path(r'^rainfall_BarChart/$', views.rainfall_BarChartView.as_view()),
    re_path(r'^humidity_BarChart/$', views.humidity_BarChartView.as_view()),
    re_path(r'^windrose/$', views.WindRoseChartView.as_view()),
    re_path(r'^fakedata/$', views.FakeData.as_view()),
    re_path(r'^download/', views.Download.as_view()),

]
