from django.db import models
from django.contrib.auth.models import User

# Hospitals Details
class HospitalsDetails(models.Model):
    
    # IntegerField for id
    Hos_id = models.IntegerField(default=1, unique=True)

    # CharField for password
    password = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Save the current instance of ModelA
        super().save(*args, **kwargs)

        # Create an instance of ModelB with the same details and save it
        user = User.objects.create(username=self.Hos_id)
        user.set_password(self.password)
        user.save()
        # Adjust the fields accordingly


    def __str__(self):
        return str(self.Hos_id)
