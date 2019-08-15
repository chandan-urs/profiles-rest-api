from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions


class HelloAPIView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Retruns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get,post,put,delete,patch,)',
            'Is similar to traditional Django view',
            'Gives you the most control over application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request, format=None):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk=None):
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return Hello world message"""
        a_viewset = [
            'Uses actions (list,create, retrieve, update, partial update)',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code'
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hi {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        return Response({'http-method': 'GET'})

    def partial_update(self, request, pk=None):
        return Response({'http-method': 'Patch'})

    def destroy(self, request, pk=None):
        return Response({'http-method': 'Delete'})


class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating view sets"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
