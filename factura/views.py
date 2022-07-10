from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from producto.models import factura
from factura.serializers import facturaSerializer

@api_view(['GET', 'POST'])
def factura_list(request):

    if request.method == 'GET':
        forma = factura.objects.all()
        serializer = facturaSerializer(forma, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = facturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def factura_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        forma = factura.objects.get(pk=pk)
    except forma.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = facturaSerializer(forma)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = facturaSerializer(forma, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        forma.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

