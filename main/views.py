from rest_framework.views import APIView
from rest_framework.response import Response
from .parser import main
from .serializers import ParsingSerializer
class ParsingView(APIView):
    def get(self, request):
        parsing = main()

        serializer = ParsingSerializer(instance=parsing, many=True)
        return Response(serializer.data)