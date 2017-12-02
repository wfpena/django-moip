from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscriptions(models.Model):
    plano = models.CharField(max_length=255)
    cliente = models.CharField(max_length=255)

    def __unicode__(self):
        return self.plano + ' ' + self.cliente

    def __str__(self):
        return self.plano + ' ' + self.cliente

    @property
    def code(self):
        return 'assinatura{0}'.format(self.id)

    class Meta:
        verbose_name = _('Assinatura')
        verbose_name_plural = _('Assinaturas')


class Client(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    @property
    def code(self):
        return 'cliente{0}'.format(self.id)

    class Meta:
        verbose_name = _('Cliente')
        verbose_name_plural = _('Clientes')
