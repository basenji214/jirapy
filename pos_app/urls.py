from django.urls import path
from . import views

urlpatterns = [
    path('',views.jira_dashboard, name='jira_dashboard'),
    path('search/', views.search_issues, name='search_issues'),
]
