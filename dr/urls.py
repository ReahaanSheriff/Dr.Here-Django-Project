from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient, name='patient'),
    path('/<str:usr>/', views.patient, name='patient'),
    path('all_doctors/', views.all_doctors, name='all_doctors'),
    path('all_doctors/<str:usr>/', views.all_doctors, name='all_doctors'),
    path('all_doctors/', views.all_doctors, name='all_doctors'),
    path('login/', views.login, name='login'),
    path('login/<str:i>', views.login, name='login'),
    path('signin', views.signin, name='signin'),
    path('signin/<str:i>/', views.signin, name='signin'),
    path('app/', views.ap_det, name='app'),
    path('doctor/',views.doctor, name = 'doctor'),
    path('doctor/<str:usr>/', views.doctor, name='doctor'),
    path('doctor/patients/<str:usr>', views.patients_doc, name='patients'),
    path('doctor/schedule/<str:usr>', views.schedule_doc, name='schedule'),
    path('doctor/patients/', views.patients_doc, name='patients'),
    path('doctor/schedule/', views.schedule_doc, name='schedule'),
    path('doc_profile', views.doc_profile, name='doc_profile'),
    path('ap_fix/<str:usr>/<str:i>', views.ap_fix, name='ap_fix'),
    path('ap_fix/', views.ap_fix, name='ap_fix'),
]

