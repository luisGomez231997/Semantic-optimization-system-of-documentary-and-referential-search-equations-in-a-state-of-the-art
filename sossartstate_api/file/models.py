from django.db import models
from django.conf import settings
# Importamos los usuarios.
from folder.models import Folder
import uuid
# Create models here........................................................................

# Model to the file in the evidences of the teachers........................................................................

def get_upload_path(instance, filename):
    """Metodo para crear la ruta al archivo"""
    user_email = instance.custom_user.email

    return 'Folders/'+"%s/%s" % (
        user_email,
        creat_at
    )

class File(models.Model):
    """Represent a File object"""
    uploadOnFile = models.DateTimeField(auto_now_add=True)
    folder = models.ForeignKey(Folder, related_name='files', on_delete=models.PROTECT)
    file = models.FileField(upload_to=get_upload_path, blank=True)

    def __str__(self):
        return 'The File was created as: {}'.format(self.file.name)

# Model to the profile picture to the user........................................................................
