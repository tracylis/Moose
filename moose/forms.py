import re
import models #not necessary
from django.core.exceptions import ObjectDoesNotExist
from vBVS.FrontEnd.models import *
#from vBVS.FrontEnd.models import Resource,Runplan,Run,User,Buildsready,Baselineinfo, Notification, Notificationlist
from django import forms
from django.db import models
from django.forms import ModelForm
from django.db import connection
from django.forms.util import ErrorList # validation error reports


class Login(forms.Form):

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    


