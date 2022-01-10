from rest_framework.views import APIView
from rest_framework.response import Response

from main.models import Ad
from main.permission import IsAdAuthor
from .parser import main
from .serializers import AdSerializer, ParsingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

class ParsingView(APIView):
    def get(self, request):
        parsing = main()

        serializer = ParsingSerializer(instance=parsing, many=True)
        return Response(serializer.data)


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.action is ['update', 'partial_update', 'destroy']:
            permissions = [IsAdAuthor, ]
        else:
            permissions = [IsAuthenticated, ]
        return [permission() for permission in permissions]

    def get_serializer_context(self):
        return {'request': self.request}