# -*- coding: utf-8 -*-
# @Time     : 2021/11/24 15:31
# @Author   : fanzhaoran
# @File     : serializers.py.py
from rest_framework import serializers

from .models import Person
from .models import Program
from .models import ProgramInFo


class PersonItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProgramInFo
        fields = [
            'person',
            'program',
            'module_name',
            'bugs_Any',
            'bugs_deal',
            'bugs_start_time',
            'bugs_end_time',
            'work_list',
        ]


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    person_item = PersonItemSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ['name', 'gender', 'id_no',
                  'birth_date', 'experience',
                  'Level', 'work_zone', 'skill',
                  'person_item',
                  ]


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Program
        fields = ['name', 'module']

# class PersonProgramSerializer(serializers.ModelSerializer):
#     person_item = PersonItemSerializer(many=True)
#
#     class Meta:
#         model = Person
#         fields = ['name', 'gender', 'id_no',
#                   'birth_date', 'experience',
#                   'Level', 'work_zone', 'skill',
#                   'person_item',
#                   ]
#         read_only_fields = ['person_item']
#
#     def create(self, validated_data):
#         program_info_data = validated_data.pop('person_item')
#
#         if validated_data['person_item']:
#             del validated_data['person_item']
#
#         person = Person.objects.create(**validated_data)
#
#         for pro in program_info_data:
#             ProgramInFo.objects.create(person=person, **pro)
#         return person
#
#     def update(self, instance, validated_data):
#         program_info_data = validated_data.pop('person_item')
#         program = instance.program
#
#         instance.name = validated_data.get('name', instance.name)
#         instance.gender = validated_data.get('gender', instance.gender)
#         instance.id_no = validated_data.get('gender', instance.id_no)
#         instance.work_zone = validated_data.get('gender', instance.work_zone)
#         instance.birth_date = validated_data.get('gender', instance.birth_date)
#         instance.experience = validated_data.get('gender', instance.experience)
#         instance.Level = validated_data.get('gender', instance.Level)
#         instance.skill = validated_data.get('gender', instance.skill)
#         instance.save()
#
#         program.is_premium_member = program_info_data.get(
#             "is_premium_member",
#             program.is_premium_member
#         )
#
#         program.has_support_contract = program_info_data.get(
#             'has_support_contract',
#             program.has_support_contract
#         )
#         program.save()
#         return instance
