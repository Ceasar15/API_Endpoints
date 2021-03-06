from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

# def generate_ticket_id():
#     return str(uuid.uuid()).split("-")[-1]

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    #ticket_id = models.CharField(max_length=255, blank=True, auto_created=True)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.ticket_id)
    
    # def save(self, *args, **kwargs):
    #     if len(self.ticket_id.strip(" ")) == 0:
    #         self.ticket_id = generate_ticket_id()
        
    #     super(Ticket, self).save(*args, **kwargs) # The real save() button

    class Meta:
        ordering = ["-created"]

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default='', editable=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value=value, allow_unicode=True)
        super().save(*args, **kwargs)
        
