from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from producto.models import cliente
from clientes.serializers import clientefacturaSerializer

@api_view(['GET', 'POST'])
def cliente_l(request):

    if request.method == 'GET':
        clie = cliente.objects.all()
        serializer = clientefacturaSerializer(clie, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = clientefacturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cliente_d(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        clie = cliente.objects.get(pk=pk)
    except clie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = clientefacturaSerializer(clie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = clientefacturaSerializer(clie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        clie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

