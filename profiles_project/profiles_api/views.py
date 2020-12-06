from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .serializers import HelloSerializer


class HelloAPI(APIView):
    """Test APIView"""
    serializer_class = HelloSerializer
    
    def get(self, request, format=None):
        """Return a list of APIView's features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
            ]
        return Response({'messgae':'Hello Guys', 'api_view':an_apiview})
    
    def post(self, request):
        """Creates a hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def put(self, request, pk=None):
        """Update the object"""
        return Response({'message': 'PUT API'})
    
    def patch(self, request, pk=None):
        """Update the object partially"""
        return Response({'message': 'PATCH API'})
    
    def delete(self, request, pk=None):
        """Delete the object"""
        return Response({'message': 'DELETE API'})
    

class HelloViewSets(viewsets.ViewSet):
    """Testing ViewSet"""
    serializer_class = HelloSerializer
    
    def list(self, request):
        """List all the features of VieSet"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})
    
    def create(self, request):
        """Creating a hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self, request, pk=None):
        """Retrieve a single object"""
        return Response({'message':'Retrieveing object'})
    
    def update(self, request, pk=None):
        """Updating a single object"""
        return Response({'message':'Updating the object'})
    
    def update(self, request, pk=None):
        """Partial updating the  object"""
        return Response({'message':'Partial updating the object'})
    
    def destroy(self, request, pk=None):
        """Deleting a single object"""
        return Response({'message':'Deleting the object'})