from django.db import models

# Create your models here.


class SearchResult(models.Model):
    searchID = models.TextField()
    searchWord = models.TextField()
    websiteURL = models.TextField()
    retrieveTime = models.DateTimeField(auto_now=True)
    searchResult = models.TextField()
    websiteDescription = models.TextField()
    label = models.TextField()



#--------Utils--------#
def get_model_fields(model):
    return model._meta.fields

