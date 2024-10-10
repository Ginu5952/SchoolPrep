#from rest_framework.decorators import api_view, permission_classes
#from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.Parent.models.writemsg import WriteMsg
from apps.Parent.serializer.writemsg import WriteMsgSerializer
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET', 'POST'])
#@permission_classes([IsAuthenticated])  
def message_view(request):
    if request.method == "GET":
        messages = WriteMsg.objects.all()  
        serializer = WriteMsgSerializer(messages, many=True)
        return Response(serializer.data)

    # elif request.method == "POST":
          
    #     serializer = WriteMsgSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status = status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == "POST":
        # If the teacher is replying, we expect the response field to be populated
        if 'response' in request.data and request.data['response'] != "":
            serializer = WriteMsgSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # If it's a new message from the parent
        else:
            serializer = WriteMsgSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)