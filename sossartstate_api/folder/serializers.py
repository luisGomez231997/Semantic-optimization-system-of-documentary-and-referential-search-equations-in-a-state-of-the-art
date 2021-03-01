  
# libreria serializers
from rest_framework import serializers
from file.serializers import FileSerializer
from .models import Folder



# ========== Serializador para un FolderSerializer =================================================================
class FolderSerializer(serializers.ModelSerializer):

    files = FileSerializer(many=True, read_only=True)
    class Meta:
        model = Folder
        fields = [
            'name',
            'document_id',
            'description',
            'custom_user',
            'creat_at',
            'files'
            ]

class CreateFolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = '__all__'

    def create(self, validated_data):
        folder = Folder.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            custom_user=validated_data['custom_user']
        )
        folder.save()
        return folder


class UpdateFolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = [
            'name',
            'description',
            'custom_user',
            'creat_at',
            'files'
            ]

    def update(self, instance, validated_data):
        Folder = super().update(instance, validated_data)
        return Folder

class DeleteFolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = '__all__'

    def perform_destroy(self, instance):
        instance.delete()