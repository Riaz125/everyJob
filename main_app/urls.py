from django.urls import path
# import all the functions in the views folder (controller functions)
# and attach them as methods to the views object
from . import views  # views is the name of the file

urlpatterns = [
    path('', views.home, name='home'),
    # We will have login, logout, jobtitle/index/home, jobpost detail routes


    path('everyjob/create/', views.JobTitleCreate.as_view(),
         name='job_title_create'),
    path('accounts/signup/', views.signup, name='signup'),
    path('everyjob/<int:job_title_id>/add_job_post/',
         views.GetJobPostForm, name='add_job_post'),
    path('everyjob/<int:job_title_id>/post_job/',
         views.JobPostCreate, name='post_job'),
    # path('everyjob/<int:job_title_id>/',
    #      views.JobPostCreate, name='add_job_post'),
    path('everyjob/create/', views.JobTitleCreate.as_view(),
         name='job_title_create'),
    path('everyjob/<int:job_title_id>/',
         views.job_title_detail, name='detail'),
]
