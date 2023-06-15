from django.db import models


class Network (models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
class Show (models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  release_date = models.DateField()
  network = models.ForeignKey(Network, related_name="shows", on_delete= models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

if __name__ == "__main__":
	new_network = Network.objects.create(name = "NBC")
	new_show = Show.objects.create(title = "Brookyn 99", description = "Cool cool cool cool cool", release_date = "2013-09-17", network =  new_network)


