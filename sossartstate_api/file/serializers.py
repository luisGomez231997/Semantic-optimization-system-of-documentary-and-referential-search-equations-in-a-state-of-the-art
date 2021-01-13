  
from .models import File
                        
#libreria serializers
from rest_framework import serializers

 
# ========== Serializador para una File =================================================================
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
    
# ========== Serializador para eliminar la File ==========
class DeleteFileSerializers(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = "__all__"

    def perform_destroy(self, instance):
            instance.delete()         
          