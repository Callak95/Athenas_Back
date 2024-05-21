from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Pessoa
from .serializers import PessoaSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def create(self, request, *args, **kwargs):
        nome = request.data.get('nome')
        data_nascimento = request.data.get('data_nascimento')
        
        if Pessoa.objects.filter(nome=nome, data_nascimento=data_nascimento).exists():
            return Response({'error': 'Pessoa já existe.'}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)