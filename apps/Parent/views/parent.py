from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.Parent.models.parent import Parent
from apps.Parent.serializer.parent import ParentSerializer




@api_view(['GET'])
def parent_list(request):
    if request.method == 'GET':
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data)