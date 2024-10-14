from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from apps.Parent.models.writemsg import WriteMsg
from apps.Parent.serializer.writemsg import WriteMsgSerializer
from apps.Teacher.serializer.message import MessageResponseUpdateSerializer

@api_view(['GET', 'POST'])
def message_view(request):
    if request.method == "GET":
        messages = WriteMsg.objects.all()
        serializer = WriteMsgSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        if 'id' in request.data:
            try:
                message = WriteMsg.objects.get(id=request.data['id'])
            except WriteMsg.DoesNotExist:
                return Response({"error": "Message not found."}, status=status.HTTP_404_NOT_FOUND)

            serializer = MessageResponseUpdateSerializer(message, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer = WriteMsgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
