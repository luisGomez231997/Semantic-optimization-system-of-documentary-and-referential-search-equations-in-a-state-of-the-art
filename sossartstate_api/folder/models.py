from django.db import models
from django.utils import timezone

# import to foreing models
from customuser.models import CustomUser


# Create model  to a Folder..........................................................
class Folder(models.Model):
    """Represent a Secction object"""
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=5000)
    custom_user = models.ForeignKey(CustomUser, related_name='folders', on_delete=models.PROTECT)
    creat_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'The Folder was created as: {}, with a code: {}'.format(
            self.name,
            self.id)

