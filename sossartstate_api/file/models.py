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
    name
    return 'Secctions/Resources/'+"%s/%s/%s" % (
        user_email,
        seccion,
        filename
    )

class File(models.Model):
    """Represent a File object"""
    codeFile = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                verbose_name='ID')
    uploadOnFile = models.DateTimeField(auto_now_add=True)

    file = models.FileField(upload_to='files/', blank=True)

    def __str__(self):
        return 'The File was created as: {}'.format(self.file.name)

# Model to the profile picture to the user........................................................................
