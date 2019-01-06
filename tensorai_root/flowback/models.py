from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from tensorai.settings import *
from django.core.validators import RegexValidator

# Create your models here.
class Well_Profile(models.Model):
    #well_id = models.AutoField(primary_key=True, blank = True, null = True)
    company_choices = (
    ('Oxy', 'Oxy'),
    ('Riverbend', 'Riverbend'),
    ('Concho', 'Concho'),
    )
    company = models.CharField(max_length=100, choices=company_choices, default='')
    well_name = models.CharField(max_length=50, blank = True, default='')
    API10 = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    engineer = models.ManyToManyField(User)
    prod_path_choices = (
    ('production casing', 'production casing'),
    ('production tubing', 'production tubing'),
    )
    prod_path = models.CharField(max_length=100, choices=prod_path_choices, default='')
    prod_path_diameter = models.IntegerField()
    team_choices = (
    ('Asset team 1', 'Asset team 1'),
    ('Asset team 2', 'Asset team 2'),
    ('Asset team 3', 'Asset team 3'),
    )
    team = models.CharField(max_length=100, choices=team_choices, default='')
    formation_choices= (
    ('WCA','WCA'),
    ('WCB','WCB'),
    ('WCC','WCC'),
    ('1BS','1BS'),
    ('2BS','2BS'),
    ('3BS','3BS'),
    ('HOBAN','HOBAN'),
    )
    formation = models.CharField(max_length=100, choices=formation_choices, default='')
    asset_choices = (
    ('TX Asset 1', 'TX Asset 1'),
    ('TX Asset 2', 'TX Asset 2'),
    ('NM Asset 1', 'NM Asset 1'),
    ('NM Asset 2', 'NM Aseet 2'),
    )
    asset = models.CharField(max_length=100, choices=asset_choices, default='')
    region_choices = (
    ('TX Delaware Basin', 'Tx Delaware Basin'),
    ('Midland Basin', 'Midland Basin'),
    ('NM Delaware Basin', 'NM Delaware Basin')
    )
    region = models.CharField(max_length=100, choices=region_choices, default='')
    flowback_company = models.CharField(max_length=100, default='')
    flowback_start_date = models.DateTimeField(null = False)
    contractor_name = models.CharField(max_length=100, default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. 10 digits allowed.")
    contractor_phone = models.CharField(validators=[phone_regex], max_length=10, blank=True) # validators should be a list
    facility = models.CharField(max_length=100, default='')
    initial_shut_in_psi = models.IntegerField()
    initial_res_psi = models.IntegerField()
    total_frac_fluid = models.IntegerField()
    total_sand_pumped = models.IntegerField()
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(editable=False, null=True)
    def save(self, *args, **kwargs):
        #''' On save, update timestamps '''
        if not self.well_name:
            self.date_updated = timezone.now()
        else:
            self.date_created = timezone.now()
        return super(Well_Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.well_name

    #"recently" is being defined as within 1 day of "now"
    def was_updated_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_updated <= now

    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_created <= now

    pass

class Well_Data(models.Model):
    data_well_name = models.ForeignKey(Well_Profile, on_delete=models.CASCADE)
    data_date = models.DateTimeField()
    data_time = models.DateTimeField()
    data_tubing_psi = models.IntegerField()
    data_csg_psi = models.IntegerField()
    data_choke_size = models.IntegerField()
    data_sep_psi = models.IntegerField()
    data_oil_rate = models.IntegerField()
    data_water_rate = models.IntegerField()
    data_gas_rate = models.IntegerField()
    data_flowline_psi = models.IntegerField()
    data_chlorides = models.IntegerField()
    data_sand_percent = models.IntegerField()
    data_h2s = models.IntegerField()
    data_remarks = models.CharField(max_length=300, default="")
