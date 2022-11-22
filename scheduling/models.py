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
