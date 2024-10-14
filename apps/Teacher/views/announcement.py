from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.Teacher.models import Announcement
from apps.Teacher.serializer.announcement import AnnouncementSerializer


@api_view(["GET"])
def announcement_view(request):
    # Optionally, you could add pagination or filtering here
    announcements = Announcement.objects.all()
    serializer = AnnouncementSerializer(announcements, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])  # Ensures the user is authenticated
def announcement_create(request):
    # Check if the user is an admin
    if request.user.is_superuser:
        serializer = AnnouncementSerializer(
            data=request.data, context={"request": request}
        )  # Pass request context
        if serializer.is_valid():
            serializer.save()  # Now it will use the user from the context
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Return validation errors if any
        return Response(
            {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )

    # If user is not an admin, return a permission error
    return Response(
        {"error": "You do not have permission to create announcements."},
        status=status.HTTP_403_FORBIDDEN,
    )
