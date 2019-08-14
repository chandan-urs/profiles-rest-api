from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Retruns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get,post,put,delete,patch,)',
            'Is similar to traditional Django view',
            'Gives you the most control over application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
