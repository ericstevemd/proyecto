from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from producto.models import tipo_articulo
from tipoArticulo.serializers import tipoarticuloSerializer 


@api_view(['GET', 'POST'])
def art_list(request):

    if request.method == 'GET':
        art = tipo_articulo.objects.all()
        serializer = tipoarticuloSerializer(art, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = tipoarticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def art_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        art = tipo_articulo.objects.get(pk=pk)
    except art.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = tipoarticuloSerializer(art)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = tipoarticuloSerializer(art, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

