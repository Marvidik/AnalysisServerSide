from django.db import models


# Create your models here.
from django.db import models

def validate_csv_file(value):
    if not value.name.endswith('.csv'):
        raise Exception('File must be a CSV.')

class GoogleData(models.Model):
    Total_ad_spend=models.FloatField()
    Avg_cpc=models.FloatField()
    Avg_cost_per_conversion=models.FloatField()
    Total_revenue=models.FloatField()
    data=models.FileField(validators=[validate_csv_file])
    today=models.DateField()



    def __str__(self):
        return str(self.today )


