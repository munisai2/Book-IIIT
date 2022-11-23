from django.db import models

# Create your models here.
class Resource(models.Model):
    ROOM_CATEGORIES=(
        ('VCR',"Video Conference Room"),
        ('MR',"Meeting Room"),
        ('240S',"240 Seater"),
        ('120-A',"120 Seater Room-1"),
        ('120-B',"120 Seater Room-2"),
        ('PMR',"Personal Meeting Room")
        
        
    )
    number = models.IntegerField()
    category = models.CharField(max_length=5,choices=ROOM_CATEGORIES)
    capacity=models.IntegerField()
    seats=models.IntegerField()

    def __str__(self):
        return f'{self.number}.  {self.category} with {self.seats} for {self.category} people'

class user_detail(models.Model):
    
    username=models.CharField(max_length=100,null=True)
    email=models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    mobile_number =models.CharField(max_length=14)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super(user_detail, self).save(*args, **kwargs)