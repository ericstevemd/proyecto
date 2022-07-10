from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rol.models import rol
from rol.serializers import rolSerializer




@api_view(['GET', 'POST'])
def rol_list(request):

    if request.method == 'GET':
        roluser = rol.objects.all()
        serializer = rolSerializer(roluser, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = rolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def rol_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        roluser = rol.objects.get(pk=pk)
    except roluser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = rolSerializer(roluser)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = rolSerializer(roluser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        roluser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

