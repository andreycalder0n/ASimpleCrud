from projects.serializers import ProjectSerializer
from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
#Api para concectar la base de datos con nuestra app
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer