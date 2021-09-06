# -*- coding: utf-8 -*-
# @Time     : 2021/9/6 17:31
# @Author   : fanzhaoran
# @File     : 工厂模式.py
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    """
    抽象类 定义统一接口类型
    """

    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    """
    具体产品角色类，继承抽象类
    """

    def __init__(self, is_huabei=False):
        self.is_huabei = is_huabei

    def pay(self, money):
        if self.is_huabei:
            print(f"使用花呗支付了:{money}")
        else:
            print(f"使用支付宝支付了:{money}")


class Wechatpay(Payment):
    """
    具体产品角色类，继承抽象类
    """

    def pay(self, money):
        print(f"使用微信支付了:{money}")


class PaymentFactory(metaclass=ABCMeta):
    """
    定义工厂类接口，规范工厂类
    """

    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    """
    创建一个阿里支付工厂类，这个类只负责阿里支付的相关实现
    """

    def create_payment(self):
        return Alipay()


class WechatpayFactory(PaymentFactory):
    """
创建一个微信支付工厂类
"""


def create_payment(self):
    return Wechatpay()


class HuabeipayFactory(PaymentFactory):
    """
    创建一个花呗支付工厂类
    """

    def create_payment(self):
        return Alipay(is_huabei=True)


if __name__ == '__main__':
    alifac = AlipayFactory()
    alipay = alifac.create_payment()
    alipay.pay(100)
    huafac = HuabeipayFactory()
    huabei = huafac.create_payment()
    huabei.pay(100)
"""
OUT:
使用支付宝支付了:100
使用花呗支付了:100
"""
# 新增一个产品
'''
'class BankPay(Payment):
	# 定义一个银联支付产品类
	
	def pay(self, money):
      print(f"使用银联支付了:{money}")

class BankpayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()

if __name__ == "__main__":
    bankfac = BankpayFactory()
    bankpay = bankfac.create_payment()
    bankpay.pay(100)

"""
OUT:
使用银联支付了:100
"""

'
'
'''
