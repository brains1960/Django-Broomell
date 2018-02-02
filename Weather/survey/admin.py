# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import GlobalData, Trial, Participants, Response

# Register your models here.
admin.site.register(GlobalData)
admin.site.register(Trial)
admin.site.register(Participants)
admin.site.register(Response)