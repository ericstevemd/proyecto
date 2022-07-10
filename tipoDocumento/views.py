from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from producto.models import tipoDocumento
from tipoDocumento.serializers import tipodocumentoSerializer


@api_view(['GET', 'POST'])
def doc_list(request):

    if request.method == 'GET':
        doc = tipoDocumento.objects.all()
        serializer = tipodocumentoSerializer(doc, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = tipodocumentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def doc_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        doc = tipoDocumento.objects.get(pk=pk)
    except doc.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = tipodocumentoSerializer(doc)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = tipodocumentoSerializer(doc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        doc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

