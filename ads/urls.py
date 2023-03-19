from django.urls import path

from ads.views import main_view, CategoryView, CategoryDetailView, AdView, AdDetailView

urlpatterns = [
    path('', main_view),
    path('cat/', CategoryView.as_view()),
    path('cat/<int:pk>', CategoryDetailView.as_view()),
    path('ad/', AdView.as_view()),
    path('ad/<int:pk>', AdDetailView.as_view()),
]
