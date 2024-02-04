
from django.db import models

# Doctor Details
class DoctorDetails(models.Model):
    
    # IntegerField for id
    Doc_id = models.IntegerField(default=1, unique=True)

    # IntegerField for id
    Hos_id = models.IntegerField(default=1)

    # CharField for name
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Doc_id)

