from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.Teacher.models.timetable import TimeTable
from apps.Teacher.serializers.timetable import TimeTableSerializer


@api_view(["GET", "POST"])
def timetable_view(request):
    if request.method == "GET":
        timetables = TimeTable.objects.all()
        serializer = TimeTableSerializer(timetables, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TimeTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
