from django.shortcuts import render
import json


# Create your views here.

import json
import pymysql
from sshtunnel import SSHTunnelForwarder

# 按模块获取模块bug总数的sql
sql = "SELECT name,COUNT(*)  \
      FROM (SELECT project,id,module,title,resolvedBy,keywords FROM zt_bug WHERE product=2 AND deleted='0') bug \
        LEFT JOIN (SELECT id,name FROM zt_module WHERE root=2) module ON bug.module=module.id   \
        GROUP BY module.`name`"

developers = {'王科': u"'数据统计展示','2D展示','实时视频展示','事件查看','首页'",
              '罗泽东': u"'数据统计展示','2D展示','实时视频展示','用户登录、登出'",
              '陈天树': u"'事件查看'",
              '李晨心': u"'角色管理old','用户管理old','角色管理','用户管理','菜单管理','摄像头管理','大喇叭管理','接口','设备管理'",
              '邓成凯': u"'角色管理old','用户管理old','角色管理','用户管理','菜单管理','摄像头管理','大喇叭管理','接口','设备管理'"
              }
bug_type = ['参数唯一性约束', '参数范围约束', '非法字符约束', '流程异常处理', '接口规范', '功能缺陷', '必选参数约束', '数据类型约束', '权限约束', '其他']


def get_developer_bug_count(developer):
    # 获取每个开发者的bug总数
    sql = "SELECT SUM(CASE WHEN name IN (%s) THEN 1 ELSE 0 END) \
            FROM (SELECT bug.title,bug.keywords,bug.resolvedBy,module.name  \
                    FROM (SELECT project,id,module,title,resolvedBy,keywords FROM zt_bug WHERE product=2 AND deleted='0') bug \
                    LEFT JOIN (SELECT id,name FROM zt_module WHERE root=2) module ON bug.module=module.id) module_keywords" % \
          developers[developer]
    # print sql
    result = get_data_from_zentao(sql)
    bug_count = int(result[0][0])
    # print bug_count
    return bug_count


def get_developer_bug_type_count(developer):
    bug_type_count = {}
    # 获取每个开发者各bug类型的bug总数
    sql = "SELECT keywords,count(*) \
            FROM (SELECT bug.title,bug.keywords,bug.resolvedBy,module.name \
                    FROM (SELECT project,id,module,title,resolvedBy,keywords FROM zt_bug WHERE product=2 AND deleted='0') bug \
                    LEFT JOIN (SELECT id,name FROM zt_module WHERE root=2) module ON bug.module=module.id) module_keywords \
            WHERE name IN (%s)    \
            GROUP BY keywords" % developers[developer]
    # print sql
    result = get_data_from_zentao(sql)
    for i in result:
        bug_type_count[i[0]] = i[1]
    # print(json.dumps(bug_type_count,encoding='utf-8',ensure_ascii=False))
    return bug_type_count


def get_final_results():
    final_results = {}
    for developer in developers.keys():
        final_results[developer] = {}
        final_results[developer]['total'] = get_developer_bug_count(developer)
        final_results[developer]['type_count'] = get_developer_bug_type_count(developer)
    # print(json.dumps(final_results, encoding='utf-8', ensure_ascii=False))
    return final_results

def main_page(request):
    # if request.method == "POST":
    #     print(request.POST.get('query'))
    # if not request.POST.get('query'):
    #     return render(request, 'main.html')
    #
    # print(f"从数据库获取的数据: {get_final_results()}")
    # print(f"数据库数据类型 type {type(get_final_results())}")
    data_p = [
        {
            "name": request.POST.get('query'),
            "value": 11
        },
        {
            "name": '初级工程师',
            "value": 10
        },
        {
            "name": '8年',
            "value": 6
        },
        {
            "name": 'Python',
            "value": 5
        },
        {
            "name": 'Django',
            "value": 4
        }
    ]
    if data_p[0]['name'] == '张三':
        bug =  [
            {"name": "功能缺陷", "value": 20},
            {"name": "流程异常处理", "value": 12},
            {"name": "参数唯一性约束", "value": 5},
            {"name": "参数范围约束", "value": 2},
            {"name": "必选参数约束", "value": 0},
            {"name": "接口规范", "value": 0},
            {"name": "数据类型约束", "value": 0},
            {"name": "非法字符约束", "value": 1},
            {"name": "其他", "value": 1},
        ]
    else:
        bug = [
            {"name": "功能缺陷", "value": 43},
            {"name": "流程异常处理", "value": 32},
            {"name": "参数唯一性约束", "value": 13},
            {"name": "参数范围约束", "value": 10},
            {"name": "必选参数约束", "value": 5},
            {"name": "接口规范", "value": 1},
            {"name": "数据类型约束", "value": 1},
            {"name": "非法字符约束", "value": 1},
            {"name": "其他", "value": 1},
        ]

    Skill = [
        {"value": 1048, "name": '行业支撑部'},
        {"value": 735, "name": '规划技术部'},
        {"value": 580, "name": '市场发展部'},
        {"value": 484, "name": '数智创新部'},
        {"value": 300, "name": '智慧城市平台部'}
    ]

    return render(request, "main.html", {
        'List': json.dumps(data_p),
        'skill': json.dumps(Skill),
        'bugs': json.dumps(bug)
    })

# def home_page(request):
#
#     return render(request, 'home.html')
