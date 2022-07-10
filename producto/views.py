from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from producto.models import porducto
from producto.serializers import porductoSerializer

@api_view(['GET', 'POST'])
def prod_list(request):

    if request.method == 'GET':
        prod = porducto.objects.all()
        serializer = porductoSerializer(prod, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = porductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def prod_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        prod = porducto.objects.get(pk=pk)
    except prod.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = porductoSerializer(prod)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = porductoSerializer(prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

