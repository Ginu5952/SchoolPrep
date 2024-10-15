from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from apps.Parent.models.writemsg import WriteMsg
from apps.Parent.serializer.writemsg import WriteMsgSerializer
from apps.Teacher.serializer.message import MessageResponseUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from apps.Teacher.models.teacher import Teacher

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated]) 
def message_view(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        return Response(
            {"error": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        
        messages = WriteMsg.objects.select_related('student')
        serializer = WriteMsgSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        if "id" in request.data:
            try:
                message = WriteMsg.objects.get(id=request.data["id"])
            except WriteMsg.DoesNotExist:
                return Response(
                    {"error": "Message not found."}, status=status.HTTP_404_NOT_FOUND
                )

            serializer = MessageResponseUpdateSerializer(
                message, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        required_fields = ["id", "response"]
        missing_fields = [
            field for field in required_fields if field not in request.data
        ]

        if missing_fields:
            return Response(
                {
                    "error": f"The following fields are required: {', '.join(missing_fields)}"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = MessageResponseUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
