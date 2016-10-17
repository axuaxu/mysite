# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Plinks(models.Model):
    link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.link 

class rentdb(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    num = models.CharField(blank=True, null=True, max_length=200)
    udate = models.CharField(blank=True, null=True, max_length=200)
    surl = models.CharField(blank=True, null=True, max_length=200)
    title = models.CharField(blank=True, null=True, max_length=200)
    address = models.CharField(blank=True, null=True, max_length=200)
    pcode = models.CharField(blank=True, null=True, max_length=200)
    rent = models.CharField(blank=True, null=True, max_length=200)
    rstyle = models.CharField(blank=True, null=True, max_length=200)
    method = models.CharField(blank=True, null=True, max_length=200)
    rooms = models.CharField(blank=True, null=True, max_length=200)
    length = models.CharField(blank=True, null=True, max_length=200)
    intime = models.CharField(blank=True, null=True, max_length=200)
    desc = models.TextField(blank=True, null=True, max_length=200)
    tenant = models.CharField(blank=True, null=True, max_length=200)
    treq = models.CharField(blank=True, null=True, max_length=200)
    condition = models.CharField(blank=True, null=True, max_length=200)
    equip = models.CharField(blank=True, null=True, max_length=200)
    env = models.CharField(blank=True, null=True, max_length=200)
    bus = models.CharField(blank=True, null=True, max_length=200)
    metro = models.CharField(blank=True, null=True, max_length=200)
    train = models.CharField(blank=True, null=True, max_length=200)
    hway = models.CharField(blank=True, null=True, max_length=200)
    oname = models.CharField(blank=True, null=True, max_length=200)
    phone = models.CharField(blank=True, null=True, max_length=200)
    phone2 = models.CharField(blank=True, null=True, max_length=200)
    email = models.CharField(blank=True, null=True, max_length=200)
    wechat = models.CharField(blank=True, null=True, max_length=200)
    qq = models.CharField(blank=True, null=True, max_length=200)
    aprice = models.CharField(blank=True, null=True, max_length=200)
    atitle = models.CharField(blank=True, null=True, max_length=200)
    abus = models.CharField(blank=True, null=True, max_length=200)
    ametro = models.CharField(blank=True, null=True, max_length=200)
    atrain = models.CharField(blank=True, null=True, max_length=200)
    ahway = models.CharField(blank=True, null=True, max_length=200)
    area1 = models.CharField(blank=True, null=True, max_length=200)
    area2 = models.CharField(blank=True, null=True, max_length=200)
    area3 = models.CharField(blank=True, null=True, max_length=200)
    def __str__(self):
        return self.title

class Monrent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    num = models.CharField(blank=True, null=True, max_length=200)
    udate = models.CharField(blank=True, null=True, max_length=200)
    surl = models.CharField(blank=True, null=True, max_length=200)
    title = models.CharField(blank=True, null=True, max_length=200)
    address = models.CharField(blank=True, null=True, max_length=200)
    pcode = models.CharField(blank=True, null=True, max_length=200)
    rent = models.CharField(blank=True, null=True, max_length=200)
    rstyle = models.CharField(blank=True, null=True, max_length=200)
    method = models.CharField(blank=True, null=True, max_length=200)
    rooms = models.CharField(blank=True, null=True, max_length=200)
    length = models.CharField(blank=True, null=True, max_length=200)
    intime = models.CharField(blank=True, null=True, max_length=200)
    desc = models.TextField(blank=True, null=True, max_length=200)
    tenant = models.CharField(blank=True, null=True, max_length=200)
    treq = models.CharField(blank=True, null=True, max_length=200)
    condition = models.CharField(blank=True, null=True, max_length=200)
    equip = models.CharField(blank=True, null=True, max_length=200)
    env = models.CharField(blank=True, null=True, max_length=200)
    bus = models.CharField(blank=True, null=True, max_length=200)
    metro = models.CharField(blank=True, null=True, max_length=200)
    train = models.CharField(blank=True, null=True, max_length=200)
    hway = models.CharField(blank=True, null=True, max_length=200)
    oname = models.CharField(blank=True, null=True, max_length=200)
    phone = models.CharField(blank=True, null=True, max_length=200)
    phone2 = models.CharField(blank=True, null=True, max_length=200)
    email = models.CharField(blank=True, null=True, max_length=200)
    wechat = models.CharField(blank=True, null=True, max_length=200)
    qq = models.CharField(blank=True, null=True, max_length=200)
    aprice = models.CharField(blank=True, null=True, max_length=200)
    atitle = models.CharField(blank=True, null=True, max_length=200)
    abus = models.CharField(blank=True, null=True, max_length=200)
    ametro = models.CharField(blank=True, null=True, max_length=200)
    atrain = models.CharField(blank=True, null=True, max_length=200)
    ahway = models.CharField(blank=True, null=True, max_length=200)
    area1 = models.CharField(blank=True, null=True, max_length=200)
    area2 = models.CharField(blank=True, null=True, max_length=200)
    area3 = models.CharField(blank=True, null=True, max_length=200)
    
    def __str__(self):
        return self.title

    def __unicode__(self):
    #    if self.is_basal:
    #       s = u"%s [BASAL]" % (self.name)
    #    else:
    #       s = self.name
        return u'title: %s' %  self.title


class Monrent_flex_all(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    num = models.CharField(blank=True, null=True, max_length=200)
    udate = models.CharField(blank=True, null=True, max_length=200)
    surl = models.CharField(blank=True, null=True, max_length=200)
    title = models.CharField(blank=True, null=True, max_length=200)
    address = models.CharField(blank=True, null=True, max_length=200)
    pcode = models.CharField(blank=True, null=True, max_length=200)
    rent = models.CharField(blank=True, null=True, max_length=200)
    rstyle = models.CharField(blank=True, null=True, max_length=200)
    method = models.CharField(blank=True, null=True, max_length=200)
    rooms = models.CharField(blank=True, null=True, max_length=200)
    length = models.CharField(blank=True, null=True, max_length=200)
    intime = models.CharField(blank=True, null=True, max_length=200)
    desc = models.TextField(blank=True, null=True, max_length=200)
    tenant = models.CharField(blank=True, null=True, max_length=200)
    treq = models.CharField(blank=True, null=True, max_length=200)
    condition = models.CharField(blank=True, null=True, max_length=200)
    equip = models.CharField(blank=True, null=True, max_length=200)
    env = models.CharField(blank=True, null=True, max_length=200)
    bus = models.CharField(blank=True, null=True, max_length=200)
    metro = models.CharField(blank=True, null=True, max_length=200)
    train = models.CharField(blank=True, null=True, max_length=200)
    hway = models.CharField(blank=True, null=True, max_length=200)
    oname = models.CharField(blank=True, null=True, max_length=200)
    phone = models.CharField(blank=True, null=True, max_length=200)
    phone2 = models.CharField(blank=True, null=True, max_length=200)
    email = models.CharField(blank=True, null=True, max_length=200)
    wechat = models.CharField(blank=True, null=True, max_length=200)
    qq = models.CharField(blank=True, null=True, max_length=200)
    aprice = models.CharField(blank=True, null=True, max_length=200)
    atitle = models.CharField(blank=True, null=True, max_length=200)
    abus = models.CharField(blank=True, null=True, max_length=200)
    ametro = models.CharField(blank=True, null=True, max_length=200)
    atrain = models.CharField(blank=True, null=True, max_length=200)
    ahway = models.CharField(blank=True, null=True, max_length=200)
    area1 = models.CharField(blank=True, null=True, max_length=200)
    area2 = models.CharField(blank=True, null=True, max_length=200)
    area3 = models.CharField(blank=True, null=True, max_length=200)
    def __str__(self):
        return self.title

    def __unicode__(self):
    #    if self.is_basal:
    #       s = u"%s [BASAL]" % (self.name)
    #    else:
    #       s = self.name
        return u'title: %s' %  self.title
class Meta:
        managed = False
        db_table = 'Monrent_flex_all'
