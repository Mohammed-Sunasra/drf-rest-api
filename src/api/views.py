from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import HelloWorldSerializer, SubscriberSerializer

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello World! "})

    def post(self, request):
        serializer = HelloWorldSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data
            name = valid_data.get("name")
            age = valid_data.get("age")
            return Response({"message": f"Hello {name}, You're {age} years old. "})
        else:
            return Response({"message": serializer.errors, "status": HTTP_400_BAD_REQUEST})


@api_view(["GET", "POST"])
def hello_world(request):
    if request.method == "GET":
        return Response({"message": "Hello World from functional view!"})
    else:
        name = request.data.get("name")
        if not name:
            return Response({"message": "No name passed"})
        return Response({"message": f"Hello there: {name}"})

# class SubscriberView(APIView):
#     def get(self, request):
#         all_subscribers = Subscriber.objects.all()
#         serialized_subscribers = SubscriberModelSerializer(all_subscribers, many=True)
#         return Response(serialized_subscribers.data)

#     def post(self, request):
#         serializer = SubscriberModelSerializer(data=request.data)
#         if serializer.is_valid():
#             instance = Subscriber.objects.create(**serializer.data)
#             return Response({"message": f"Subscriber created successfully with id: {instance.id}"})
#         else:
#             return Response({"message": serializer.errors})

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed! ", "status": HTTP_401_UNAUTHORIZED})
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})