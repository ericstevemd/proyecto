from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import User
from user.serializers import userSerializer


@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == 'GET':
        userm = User.objects.all()
        serializer = userSerializer(userm, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        userm = User.objects.get(pk=pk)
    except userm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = userSerializer(userm)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = userSerializer(userm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        userm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

