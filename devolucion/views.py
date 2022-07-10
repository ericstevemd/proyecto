from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from producto.models import devolucion
from devolucion.serializers import devolucionSerializer

@api_view(['GET', 'POST'])
def devolucion_list(request):

    if request.method == 'GET':
        devo = devolucion.objects.all()
        serializer = devolucionSerializer(devo, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = devolucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def devolucion_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        devo = devolucion.objects.get(pk=pk)
    except devo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = devolucionSerializer(devo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = devolucionSerializer(devo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        devo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

