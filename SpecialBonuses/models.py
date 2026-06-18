from django.db import models
from bd_models.models import Special

# Create your models here.
class SpecialBonuses(models.Model):
    special = models.ForeignKey(
        Special,
        on_delete=models.CASCADE,
        related_name="bonuses"
    )
    bonus = models.IntegerField(help_text="This adds this amount of health to the ball before applying to percentage bonus")