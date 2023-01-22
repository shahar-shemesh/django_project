
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile, name='profile'),
    path('system/', user_views.system, name='system'),

# ###########################     START:     FOR Not Secure Version        ####################################
#                                                                                                    ##########
#     path('login/', user_views.NOT_SC_login, name='login'),                                         ##########
#     path('register/', user_views.NOT_SC_register, name='register'),                                ##########
#     path('quick_user/', user_views.NOT_SC_quickUser, name='quick_user'),                           ##########
#                                                                                                    ##########
# ###########################     END:     FOR Not Secure Version        ######################################



#############################     START:     FOR Secure Version        ######################################
                                                                                                   ##########
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  ##########
    path('register/', user_views.register, name='register'),                                       ##########
    path('quick_user/', user_views.quickUser, name='quick_user'),                                  ##########
                                                                                                   ##########
#############################     END:     FOR Secure Version        ########################################





    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('', include('Comunication_LTD.urls')),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),

]
