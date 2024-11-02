from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import FileSerializer

from .models import File

@api_view(['GET'])
def file_list(request):
    files = File.objects.all()

    serializer = FileSerializer(files, many=True)

    return JsonResponse(serializer.data, safe=False)