from django.urls import path
from .views import ItemList, ItemDetail, LocationList,LocationDetail

urlpatterns = [
    path('Item/',ItemList.as_view()),
    path('Item/<int:pk>',ItemDetail.as_view()),
    path('Location/', LocationList.as_view()),
    path('Location/<int:pk>', LocationDetail.as_view()),
]