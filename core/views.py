from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from . import serializers
from . import permissions
from . models import UserProfile
from rest_framework import status, viewsets, filters


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiView = [
            'Uses HTTP requests method as function(get, post, patch, put, delete)',
            'is simmiliar to traditional django views',
            'Gives you the most control over you the application logic',
            'Is mapped maually to URLs',
        ]

        return Response({'messege': 'Hello', 'an_apiView': an_apiView})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            messege = f'hello {name}'
            return Response({'messege': messege})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle Updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle Partial Update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Resturns a hello messege"""

        a_viewset = [
            'Uses HTTP requests method as function(list, create, patch, put, destroy)',
            'automatically maps to URL using routers',
            'provides more functionality with less codes',
        ]

        return Response({'messege': 'hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create an new hello messege"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            messege = f'hello {name}'
            return Response({'messege': messege})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle a object by its id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """"Handle Creating and Updating User Profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle Creating an user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
