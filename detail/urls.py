from django.urls import path

from .views import AccountList, AccountDetail

app_name = 'detail'

urlpatterns = [
    path('accounts/', AccountList.as_view(), name='account-list'),
    path('accounts/<pk>', AccountDetail.as_view(), name='account-detail')
]
