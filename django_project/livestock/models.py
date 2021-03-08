from django.db import models
from datetime import datetime


class AnimalType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class AnimalHealth(models.Model):
    title = models.CharField(max_length=50)
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class AnimalStatus(models.Model):
    title = models.CharField(max_length=50)
    style = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Animal Statuses"

    def __str__(self):
        return self.title


class Animal(models.Model):
    title = models.CharField(max_length=100)
    identification = models.CharField(max_length=50)
    type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.identification}, {self.type}"


class AnimalLog(models.Model):
    date = models.DateTimeField(default=datetime.now)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    number = models.DecimalField(max_digits=7, decimal_places=0)
    status = models.ForeignKey(AnimalStatus, on_delete=models.CASCADE, null=True, blank=True)
    health = models.ForeignKey(AnimalHealth, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)


class MeatType(models.Model):
    title = models.CharField(max_length=50)
    type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    style = models.CharField(max_length=50, null=True, blank=True)
    # price or cost

    def __str__(self):
        return f"{self.title}, {self.type}"


class AnimalHarvest(models.Model):
    date = models.DateTimeField(default=datetime.now)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    type = models.ForeignKey(MeatType, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    count = models.DecimalField(max_digits=7, decimal_places=1, null=True, blank=True)
    packages = models.DecimalField(max_digits=7, decimal_places=0, null=True, blank=True)

    class Meta:
        ordering = ("date", "animal")

    def __str__(self):
        return f"{self.animal}, {self.type}"
