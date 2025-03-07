#https://youtu.be/UcUm82jWeKc
from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import magic

ext_validator= FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'pdf'])


def validate_file_mimetype(file):
    accept=["image/jpeg", "image/png", "application/pdf"]
    file_mime_type = magic.from_buffer(file.read(1024),mime=True)
    print(file_mime_type)
    if file_mime_type not in accept:
        raise ValidationError("Unsupported File Type")
    

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    
    image = models.FileField(upload_to='dogs/', validators=[ext_validator,validate_file_mimetype])

    def delete(self):
        self.image.delete()
        super().delete()
    
    