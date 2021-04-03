from django.urls import path,include
from myapp.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('crud',views.EmployeeViewSet,basename='employee')

urlpatterns=[
    path('',include(router.urls))
]