from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello World! "})

    def post(self, request):
        name = request.data.get("name")
        if not name:
            return Response({"message": "No name passed!"})
        return Response({"message": f"Hello there, {name}"})


@api_view(["GET", "POST"])
def hello_world(request):
    if request.method == "GET":
        return Response({"message": "Hello World from functional view!"})
    else:
        name = request.data.get("name")
        if not name:
            return Response({"message": "No name passed"})
        return Response({"message": f"Hello there: {name}"})
