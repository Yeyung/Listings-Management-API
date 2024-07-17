from django.urls import path
from .views import ShopListCreateView, ShopDetailView, ListingListCreateView, ListingDetailView, ListingSearchView

urlpatterns = [
    path('shops/', ShopListCreateView.as_view(), name='shop-list-create'),
    path('shops/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
    path('shops/<int:shopId>/listings/', ListingListCreateView.as_view(), name='listing-list-create'),
    path('listings/<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('listings/search/', ListingSearchView.as_view(), name='listing-search'),
]
