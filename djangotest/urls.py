from django.urls import path
from . import views
app_name = 'student'

urlpatterns = [
    path('login/',views.login, name = "login"),
    path('register/', views.register, name = "register"),
    path('studenthome/', views.StHomepage, name = "sthomepage"),
    path('adminhome/', views.AdHomepage, name = "adhomepage"),
    path('logout/', views.logout, name = "logout"),
    path('update/<int:s_id>',views.updatestudent, name = "update_student"),
    path('Studentlist/', views.getstudents, name = "studentlist"),
    path('status/<int:s_id>', views.studentstatus, name = "status"),
]