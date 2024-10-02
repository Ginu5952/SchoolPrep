from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from apps.Teacher.models.teacher import Teacher,Class
from apps.Teacher.serializer.teacher import TeacherSerializer,ClassSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny

@api_view(['GET', 'POST'])
@permission_classes([AllowAny]) 
def teacher_list(request):
    if request.method == "GET":
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny]) 
def teacher_detail(request, pk):
    teacher = Teacher.objects.filter(pk=pk).first()

    if teacher is None:
        return Response({"error": "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([AllowAny]) 
def class_detail(request, pk):
  
    class_ = get_object_or_404(Class, pk=pk)


    if request.method == "GET":
        serializer = ClassSerializer(class_)
        return Response(serializer.data, status=status.HTTP_200_OK)


    elif request.method == "PUT":
        serializer = ClassSerializer(class_, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        class_.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
