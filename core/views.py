from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiView = [
            'Uses HTTP requests method as function(get, post, patch, put, delete)',
            'is simmiliar to traditional django views',
            'Gives you the most control over you the application logic',
            'Is mapped maually to URLs',
        ]

        return Response({'messege': 'Hello', 'an_apiView': an_apiView})
