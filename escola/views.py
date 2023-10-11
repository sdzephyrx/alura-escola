from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import \
    AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculados

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos(as)"""
    queryset = Aluno.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'V2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as mastriculas de um aluno(a)"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos(as) matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaMatriculasAlunoSerializer