from django.db import models


class Reading(models.Model):
    location = models.CharField(max_length=40)
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}° in {} at {}'.format(
            self.temperature,
            self.location,
            self.timestamp,
        )

    def save(self, *args, **kwargs):
        print(self)
        super(Reading, self).save(*args, **kwargs)


class Thermostat(models.Model):
    location = models.CharField(max_length=40)
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
