from django.db import models

# Create your models here.
class Season_Blog(models.Model):
    WINTER = 'WTR'
    SUMMER = 'SMR'
    FALL = 'FL'
    SPRING = 'SPR'

    SEASON_CHOICES = [
        (WINTER, "Winter"),
        (SUMMER, "Summer"),
        (FALL, "Fall"),
        (SPRING, "Spring")
    ]

    season_name = models.CharField(
        max_length = 3,
        choices = SEASON_CHOICES,
        default = WINTER
    )

    season_desc = models.CharField(
        max_length = 200,
        default="season description in few lines"
    )