from django.urls import path
from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
)

app_name = 'inventory'
urlpatterns = [
    path('items/', ItemListView.as_view(), name='item_list'),
    path('items/add/', ItemCreateView.as_view(), name='item_create'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('items/<int:pk>/edit/', ItemUpdateView.as_view(), name='item_update'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]
