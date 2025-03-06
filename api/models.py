from django.db import models


# Create your models here.
class VulnerabilityModel(models.Model):
    cve_id = models.CharField(max_length=50, unique=True, db_index=True)
    base_severity = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.cve_id


class VulnerabilityStatus(models.Model):
    cve_id = models.CharField(max_length=50, unique=True, db_index=True)
    fix_status = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.cve_id} - {self.fix_status}"
