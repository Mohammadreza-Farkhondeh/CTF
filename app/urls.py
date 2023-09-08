from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.level1, name='level1'),
    path('', views.level3, name='level3'),
    path('files/', views.files, name='files'),
    path('files/<str:filename>', views.files, name='files'),
    path('XXopp3nh3im3rXX/', views.level4, name='level4'),
    path('4tt4ck-0n_71t4n/', views.level5, name='level5'),
    path('1nd14n4-j0n38/', views.level6, name='level6'),
    path('84r813XXXX/', views.level7, name='level7'),
    path('CH3rN08Y1/', views.level8, name='level8'),
    path('5H3r10CK/', views.level9, name='level9'),
]
