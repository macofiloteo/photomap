from django.db import models
from djgeojson.fields import PointField


def upload_to(instance,filename):
    return 'image_coordinates/%s/%s' % (instance.layer_name_link, filename)

class Barangay(models.Model):
    name = models.CharField(max_length=20)
    geom = PointField()

    def __str__(self):
        return self.name

class ImageSpot(models.Model):

    geom = PointField()
    description = models.TextField()
    establishment_type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to = upload_to, default='/static/photomap/img/zambologo.jpeg')

    def __str__(self):
        return self.name
    @property
    def popupContent(self):
        return '<img style="width:150px;" src="{}" /><p>{}</p>'.format(
            self.image.url,
            self.description
        )

    @property
    def est_type(self):
        return self.establishment_type
