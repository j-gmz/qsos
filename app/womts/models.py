from django.db import models
from django.urls import reverse 
from simple_history.models import HistoricalRecords

# Create your models here.
class Womt(models.Model):
    work_order_name = models.SlugField(max_length=20, 
                                       unique=True,
                                       primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50,
                                  default="unknown")

    status_choices = (
        ('received', 'RECEIVED'),
        ('assigned', 'ASSIGNED'),
        ('additional dq work', 'ADDITIONAL DQ WORK'),
        ('closed', 'CLOSED')
    )
    status = models.CharField(max_length=50,
                              choices=status_choices, 
                              default="new")

    assigned_to_choices = (
        ('dq', 'DQ'),
        ('care', 'CARE'),
        ('supply chain', 'SUPPLY CHAIN'),
        ('service', 'SERVICE'),
        ('m and a', 'M AND A')
    )
    assigned_to = models.CharField(max_length=50,
                                   choices=assigned_to_choices,
                                   default='DQ')

    history = HistoricalRecords()
    
    def get_absolute_url(self):
        return reverse("womts:womt_detail", kwargs={"pk": self.work_order_name})
    ## todo: learn to add a created_by that is auto populated--

    #### Make it a non-nullable foreign key and fill it wherever you create such objects. 
    #### If that’s a model form, you can make it a required argument to your form class 
    #### and fill it during save():

