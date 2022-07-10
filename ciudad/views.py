from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from producto.models import ciudad
from ciudad.serializers import ciudadSerializer

@api_view(['GET', 'POST'])
def ciudad_list(request):

    if request.method == 'GET':
        ciud = ciudad.objects.all()
        serializer = ciudadSerializer(ciud, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ciudadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ciudad_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        ciud = ciudad.objects.get(pk=pk)
    except ciud.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ciudadSerializer(ciud)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ciudadSerializer(ciud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ciud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

