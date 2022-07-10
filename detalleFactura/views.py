from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from producto.models import detallefactura
from detalleFactura.serializers import detallefacturaSerializer

@api_view(['GET', 'POST'])
def detalle_list(request):

    if request.method == 'GET':
        detalle = detallefactura.objects.all()
        serializer = detallefacturaSerializer(detalle, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = detallefacturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        detalle = detallefactura.objects.get(pk=pk)
    except detalle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = detallefacturaSerializer(detalle)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = detallefacturaSerializer(detalle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        detalle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

