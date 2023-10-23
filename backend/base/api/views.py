from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


from django.core.exceptions import PermissionDenied

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from ..api.serializers import NoteSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle

from rest_framework import generics
from ..models import Business
from .serializers import BusinessSerializer
from django_ratelimit.decorators import ratelimit

from rest_framework.decorators import throttle_classes

from rest_framework.throttling import SimpleRateThrottle

#loadbalancing
import psutil
from django.http import HttpResponse, JsonResponse
import random
   

from django.http import HttpResponse
from .load_balancer import route_request  # Import the route_request function

class CustomUserRateThrottle(SimpleRateThrottle):
    rate = '10/second'

    def get_cache_key(self, request, view):
        # Customize the cache key based on your requirements
        user = request.user if request.user.is_authenticated else 'anonymous'
        return f'custom_rate_throttle_{user}'

@api_view(['GET'])
@throttle_classes([CustomUserRateThrottle])  # Apply throttling
@ratelimit(rate='100/d', method='GET', key='ip', block=True)
def business(request):
    if request.method == 'GET':
        queryset = Business.objects.using('Users').all()
        serializer = BusinessSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        raise PermissionDenied(detail='Rate limit exceeded')

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')  # New field
        email = request.data.get('email')
        first_name = request.data.get('first_name')


        if username and password and password == confirm_password:  # Check if passwords match
            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                            )

            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid registration data'}, status=status.HTTP_400_BAD_REQUEST)



# Custom TokenObtainPairSerializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        # Add custom claims if needed
        return token

# Custom TokenObtainPairView
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# List available API routes
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)

# Get user's notes (requires authentication)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)



def load_balancing_view(request):
       # Define dummy IPs of your backend servers and their CPU thresholds
       backend_servers = [
           {"ip": "192.168.1.101", "cpu_threshold": 80},
           {"ip": "192.168.1.102", "cpu_threshold": 80},
           # Add more backend servers as needed
       ]

       # Function to get an available server based on CPU utilization
       def get_available_server():
           available_servers = []
           for server in backend_servers:
               cpu_percent = psutil.cpu_percent(interval=1, percpu=False)
               if cpu_percent < server["cpu_threshold"]:
                   available_servers.append(server)
           if not available_servers:
               return random.choice(backend_servers)
           return random.choice(available_servers)

       # Simulate routing requests to available servers
       selected_server = get_available_server()

       # In a real-world scenario, you would make an actual HTTP request to the selected server.
       # Here, we'll return a JSON response with the selected server's IP for simulation purposes.
       response_data = {"message": "Request routed to server", "server_ip": selected_server["ip"]}
       return JsonResponse(response_data)
   


