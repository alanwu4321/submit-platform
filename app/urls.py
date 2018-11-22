from django.conf.urls import url
from app import views,urls
from django.urls import path,include



urlpatterns = [
    path('',views.adminsubmit,name="index"),
    path('user/',views.userssubmit,name="user_index"),
    path('user-oldToNew/',views.userssortbyOtoNew,name="user-oldToNew"),
    path('user-newToOld/',views.userssortbyNewtoO,name="user-newToOld"),
    path('history/',views.history,name="user_history"),
    path('user-historysortbyOtoNew/',views.historysortbyOtoNew,name="history-oldToNew"),
    path('user-historysortbyNewtoO/',views.historysortbyNewtoO,name="history-newToOld"),

]