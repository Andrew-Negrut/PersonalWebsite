from django.urls import path

from .views import home_page_view, experience_page_view, resume_page_view, about_page_view

urlpatterns = [
    path("", home_page_view, name="home"),
    path("experience/", experience_page_view, name="experience"),
    path("resume/", resume_page_view, name="resume"),
    path("about/", about_page_view, name="about"),
]