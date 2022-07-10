from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from producto.models import proveedor
from Proveedor.serializers import ProveedorSerializer

@api_view(['GET', 'POST'])
def proveedor_list(request):

    if request.method == 'GET':
        provedor = proveedor.objects.all()
        serializer = ProveedorSerializer(provedor, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def proveerdo_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        provedor = proveedor.objects.get(pk=pk)
    except provedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProveedorSerializer(provedor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProveedorSerializer(provedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        provedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

