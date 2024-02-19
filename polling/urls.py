from django.urls import path
from polling.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name='poll_indes'),
    path('polls/<int:id>', detail_view, name='poll_detail')
]