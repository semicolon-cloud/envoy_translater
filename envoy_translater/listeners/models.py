from uuid import uuid4

from jsonfield import JSONField

from django.db import models
from django.utils import timezone

def hex_uuid():
    return uuid4().hex


class Listener(models.Model):
    """
    Database model representation of a listener.
    """
    uuid = models.CharField(max_length=32, default=hex_uuid, primary_key=True)
    listener_name = models.CharField(max_length=200)
    description = models.CharField(max_length=512)
    ip = models.CharField(max_length=40)
    external_ip = models.CharField(max_length=40)
    port = models.IntegerField(default=0)
    type = models.CharField(default=0, max_length=20)
    created_on = models.DateTimeField(default=timezone.now)

    def to_dict(self):
        return {
            'uuid': self.uuid,
            'listener_name': self.listener_name,
            'description': self.description,
            'ip': self.ip,
            'external_ip': self.external_ip,
            'port': self.port,
            'type': self.type,
            'created_on': self.created_on,
        }

    class Meta:
        unique_together = ('ip', 'port')

class TLSProxy(models.Model):
    uuid = models.CharField(max_length=32, default=hex_uuid, primary_key=True)
    listener = models.ForeignKey(Listener, on_delete=models.CASCADE)
    snis = models.TextField()

    keystone_user = JSONField(default={})
    project_id = models.CharField(max_length=64, null=True)

    target_servers = JSONField(default=[])

class HTTPProxy(models.Model):
    uuid = models.CharField(max_length=32, default=hex_uuid, primary_key=True)
    listener = models.ForeignKey(Listener, on_delete=models.CASCADE)
    hosts = models.TextField()

    keystone_user = JSONField(default={})
    project_id = models.CharField(max_length=64, null=True)

    target_servers = JSONField(default=[])