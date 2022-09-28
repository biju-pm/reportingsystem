from django.urls import path
from .views import VendorList, VendorDetail, VendorCategoryList, ApiKeysList, ApiKeysDetail

urlpatterns = [
    path('vendors/api/', VendorList.as_view()),
    path('vendors/api/<int:pk>/', VendorDetail.as_view()),
    path('vendors/category/api/', VendorCategoryList.as_view()),
    path('vendors/apikeys/api/', ApiKeysList.as_view()),
    path('vendors/apikeys/api/<int:pk>/', ApiKeysDetail.as_view()),
]
