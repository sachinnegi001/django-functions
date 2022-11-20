from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home" ),
    path('signin/',views.signin,name="signin" ),
    path('signup/',views.signup,name="signup" ),
    path('logout',views.logout_user,name='logout'),
    path('profile/',views.profiles,name="profile" ),
    path('editprofile/',views.editprofiles,name="editprofile" ),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


