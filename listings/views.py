from rest_framework import generics
from .models import Shop, Listing
from .serializers import ShopSerializer, ListingSerializer

class ShopListCreateView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get_queryset(self):
        return Listing.objects.filter(shop_id=self.kwargs['shopId'])

    def perform_create(self, serializer):
        shop = Shop.objects.get(id=self.kwargs['shopId'])
        serializer.save(shop=shop)

class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingSearchView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        queryset = Listing.objects.all()
        query = self.request.query_params.get('q', None)
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset
