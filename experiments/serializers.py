from django.contrib.auth.models import User
from rest_framework import serializers
from experiments.models import Experiment, FileUpload


class FileUploadSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FileUpload
        fields = ('datafile', 'created', 'owner')


class ExperimentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Experiment
        fields = ('id', 'title', 'description', 'nes_id', 'created',
                  'updated', 'owner')


class UserSerializer(serializers.ModelSerializer):
    experiments = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Experiment.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'experiments')
