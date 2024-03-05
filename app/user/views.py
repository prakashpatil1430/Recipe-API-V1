from .serializers import UserSerializer
from rest_framework import generics
# Create your views here.


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
