from django.contrib import admin
from django.apps import apps
from .models import Person
from .models import ProgramInFo
from .models import Program

# from .models import BugInfo
# from .models import PersonPie


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_no', 'gender', 'Level')
    search_fields = ('name', 'id_no')
    date_hierarchy = 'create_time'

#
# @admin.register(BugInfo)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('bug_name', 'bug_count')
#     search_fields = ('bug_name',)
#
#
# @admin.register(PersonPie)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('person', 'bug_model')
#     search_fields = ('person',)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'module')
    search_fields = ('name', 'module')


@admin.register(ProgramInFo)
class ProgramInfoAdmin(admin.ModelAdmin):
    list_display = ('person', 'module_name')
    search_fields = ('module_name', 'person')

    def show_title(self, obj):
        return [b.name for b in obj.program.all()]

    filter_vertical = ('program',)


# Register your models here.
# admin.site.register(Person)
# admin.site.register(Program)
# admin.site.register(ProgramInFo)
# 定义导航顺序
apps_index = ["Person", "Program", "ProgramInFo"]


def find_app_index(app_label):
    app = apps.get_app_config(app_label)
    main_menu_index = getattr(app, 'main_menu_index', 9999)
    return main_menu_index


def index_decorator(func):
    def inner(*args, **kwargs):
        templateresponse = func(*args, **kwargs)
        app_list = templateresponse.context_data['app_list']
        print("app_list:", app_list)
        app_list.sort(key=lambda r: find_app_index(r['app_label']))
        print("app_list:", app_list)
        print(type(app_list))
        for app in app_list:
            if app["app_label"] == "PersonInfo":
                # 按照指定顺序排序
                print("进来了")
                models = app["models"]
                new_models = []
                for i in models:
                    model_name = i["object_name"]
                    pos = apps_index.index(model_name)
                    new_models.append({"pos": pos, "model": i})
                new_models.sort(key=lambda s: s["pos"])
                # app['models'].sort(key=lambda x: find_app_index(x['name']))
                models = [x["model"] for x in new_models]
                app["models"] = models
                print("models:", models)
        return templateresponse

    return inner


admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)
admin.site.site_header = "个人信息后台管理"
admin.site.site_title = '个人信息后台管理'
admin.site.index_title = '个人信息后台管理'

