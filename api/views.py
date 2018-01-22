from rest_framework import generics

from .models import BucketList
from .serializers import BucketListSerializer


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucket_list."""
        serializer.save()

