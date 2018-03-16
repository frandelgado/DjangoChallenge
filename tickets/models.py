from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from solo.models import SingletonModel


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Holiday(models.Model):
    class Meta:
        ordering = ['date']
        verbose_name = _('Holiday')
        verbose_name_plural = _('Holidays')

    name = models.CharField(max_length=255, verbose_name=_('name'))
    date = models.DateField(null=True, blank=True,
                            verbose_name=_('holiday date'))

    def __str__(self):
        return '{1} ({0})'.format(self.name, str(self.date))


class WorkHourSetting(SingletonModel):
    class Meta:
        verbose_name = _('Working hours settings')

    start_hour = models.IntegerField(
        default=9,
        verbose_name=_('Work start time'),
        help_text=_('i.e.: "9" for 9am')
    )
    end_hour = models.IntegerField(
        default=18,
        verbose_name=_('Work end time'),
        help_text=_('i.e.: "18" for 6pm')
    )

    def calculate_working_hours(self):
        return self.end_hour - self.start_hour


class ServiceCategory(TimeStampedModel):
    name = models.CharField(_('service subcategory'), max_length=200)
    sla = models.IntegerField(null=True, blank=True, verbose_name=_('sla'),
                              help_text=_('sla in hours'))
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('service subcategory')
        verbose_name_plural = _('service subcategories')
        ordering = ['name']

    def __str__(self):
        return self.name


class ServiceOrder(TimeStampedModel):
    SO_STATUS = [
        ('in_progress', _('In progress')),
        ('resolved', _('Resolved')),
        ('done', _('Done')),
        ('cancelled', _('Cancelled')),
    ]

    category = models.ForeignKey(ServiceCategory, null=True,
                                 blank=True, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField(verbose_name=_('expiry date'),
                                       null=True, blank=True)
    status = models.CharField(max_length=50, choices=SO_STATUS,
                              default='in_progress')
    description = models.TextField(verbose_name=_('description'))

    class Meta:
        verbose_name = _('service order')
        verbose_name_plural = _('service orders')

    def __str__(self):
        return "{} - {}".format(self.id, self.category)
