from django.urls import path
from .views import index
from .views import other_page
from .views import BBLoginView
from .views import profile
from .views import BBLogoutView
from .views import ChangeUserInfoView
from .views import BBPasswordChangeView
from .views import RegisterUserView, RegisterDoneView

app_name = 'main'
urlpatterns = [
    path ('accounts/register/done/', RegisterDoneView.as_view(),name='register_done'),
    path ('accounts/register/', RegisterUserView.as_view(),name='register'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path ('<str:page>/', other_page, name='other'),
    path ('', index, name='index'),
    path ('/', index, name='index'),
    path ('accounts/profile/', profile, name='profile'),
    path ('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path ('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path ('accounts/profile', profile, name='profile'),
    path ('accounts/password/change', BBPasswordChangeView.as_view(), name='password_change'),

]