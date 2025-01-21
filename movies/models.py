from django.db import models

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    duration = models.IntegerField()  # durée en minutes
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # note sur 10
    actors = models.TextField()  # Liste des acteurs, séparés par des virgules
    description = models.TextField()


    def __str__(self):
        return self.title
    
    def get_duration_display(self):
        total_minutes = self.duration
        hours = total_minutes // 60
        minutes = total_minutes % 60

        if hours >= 24:  # Si la durée dépasse 24 heures
            days = hours // 24
            hours = hours % 24
            return f"{days} jours {hours} heures {minutes} minutes"

        return f"{hours} heures {minutes} minutes"
