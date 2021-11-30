# -*- coding: utf-8 -*-
# @Time     : 2021/11/24 15:14
# @Author   : fanzhaoran
# @File     : serializes.py.py

from rest_framework import serializers

from .models import BugInfo


class BugInfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BugInfo
        fields = [
            '',
            '',
            '',
            '',
        ]
