from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.Parent.models.leave import Leave
from apps.Parent.serializer.leave import LeaveSerializer
from rest_framework import status


@api_view(['GET'])
#@permission_classes([IsAuthenticated])  
def leave_request_view(request):
    
    leaves = Leave.objects.all()  
    serializer = LeaveSerializer(leaves, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])  
#@permission_classes([IsAuthenticated])  
def update_leave_status(request, pk):
    try:
        leave = Leave.objects.get(id=pk)
    except Leave.DoesNotExist:
        return Response({'error': 'Leave request not found.'}, status=status.HTTP_404_NOT_FOUND)
    leave.status = request.data.get('status', leave.status)
    leave.save()
    serializer = LeaveSerializer(leave)
    return Response(serializer.data)