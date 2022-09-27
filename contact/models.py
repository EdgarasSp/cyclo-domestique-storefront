from django.db import models

# Create your models here.

STATUS = ((0, "New"), (1, "Pending"), (2, "Solved"))
class ContactForm(models.Model):
    subject_type = models.CharField(max_length=100, null=True, blank=False)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    email_address = models.EmailField(max_length=50, null=True, blank=False)
    message = models.TextField(max_length=1000, null=True, blank=True)
    received_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.email_address

    class Meta:
        ordering = ['-received_date']
