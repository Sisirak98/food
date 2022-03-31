from django.urls import path
from . import views
app_name='taskapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('log',views.log,name='log'),
    path('regis',views.regis,name='regis'),
    path('lout',views.lout,name='lout'),
    path('demo',views.allcat,name='allcat'),
    path('<slug:c_slug>/',views.allcat,name='all'),
    path('<slug:c_slug>/<slug:pro_slug>/',views.prodetails,name='allpro'),
    path('addr',views.add,name='new'),


]