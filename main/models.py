# from django.db import models
#
#
# class Contact(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField(blank=False)
#     subject = models.CharField(max_length=500, blank=True)
#     message = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Message: {self.name} - {self.message[:150]}..."