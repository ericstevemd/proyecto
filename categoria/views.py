from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from producto.models import categoria
from categoria.serializers import categoriaSerializer

@api_view(['GET', 'POST'])
def categoria_l(request):

    if request.method == 'GET':
        detalle = categoria.objects.all()
        serializer = categoriaSerializer(detalle, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = categoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def categoria_d(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        detalle = categoria.objects.get(pk=pk)
    except detalle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = categoriaSerializer(detalle)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = categoriaSerializer(detalle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        detalle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

