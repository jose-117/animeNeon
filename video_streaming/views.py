from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Video
from .serializers import streaming_videoSerializers
from http import HTTPStatus
from datetime import datetime
from django.http import Http404

class MetodosPlural(APIView):
    def post(self, request):
        if request.data.get("title")==None or not request.data['title']:
            return JsonResponse({"estado":"error", "mensaje":"El campo title es obligarotio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("description")==None or not request.data['description']:
            return JsonResponse({"estado":"error", "mensaje":"El campo description es obligarotio"}, status=HTTPStatus.BAD_REQUEST)
        if request.data.get("video_file")==None or not request.data['video_file']:
            return JsonResponse({"estado":"error", "mensaje":"El campo video_file es obligarotio"}, status=HTTPStatus.BAD_REQUEST)
        
        try:
            Video.objects.create(title=request.data['title'], 
                                 description=request.data['description'], 
                                 video_file=request.data['video_file'], 
                                 created_at=datetime.now())
            return JsonResponse({"estado":"ok", "mensaje":"Se creo exitosamente el registro"}, status=HTTPStatus.CREATED)
        except Exception as e:
            raise Http404
