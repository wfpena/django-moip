from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Subscriptions(models.Model):
    plano = models.CharField(max_length=255)
    cliente = models.CharField(max_length=255)

    def __unicode__(self):
        return self.plano + ' ' + self.cliente

    def __str__(self):
        return self.plano + ' ' + self.cliente

    class Meta:
        verbose_name = _('Assinatura')
        verbose_name_plural = _('Assinaturas')