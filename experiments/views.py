from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework import parsers
from experiments.models import Experiment, FileUpload
from experiments.serializers import ExperimentSerializer, UserSerializer, \
    FileUploadSerializer
from experiments.permissions import IsOwnerOrReadOnly


class FileUploadList(generics.ListCreateAPIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,
                        datafile=self.request.data.get('datafile'))


class ExperimentList(generics.ListCreateAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ExperimentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
