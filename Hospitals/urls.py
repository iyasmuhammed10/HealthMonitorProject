from Hospitals import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.signin, name='login'),
    path('addpatient', views.addpatient, name='addpatient'),
    path('adddoctor', views.adddoctor, name='adddoctor'),

]