# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime

from django.db import models


class AdminHandleLog(models.Model):
    """
    管理员操作日志
    """
    admin_hadle_log_id = models.AutoField(primary_key=True)  # id
    admin = models.ForeignKey('AdminInfo', models.DO_NOTHING, blank=True, null=True)  # 管理员id(外键)
    handle_time = models.DateTimeField(auto_now_add=datetime.now())  # 操作时间
    event = models.CharField(max_length=256)  # 操作事件

    class Meta:
        managed = False
        db_table = 'admin_handle_log'

    def to_dict(self):
        data = {
            'id': self.admin_hadle_log_id,
            'admin_id': self.admin_id,
            'handel_time': self.handle_time,
            'event': self.event
        }
        return data


class AdminInfo(models.Model):
    """
    管理员信息
    """
    admin_id = models.AutoField(primary_key=True)  # id
    admin_role = models.ForeignKey('AdminRole', models.DO_NOTHING, blank=True, null=True)  # 管理员角色id(外键)
    name = models.CharField(max_length=64)  # 名称
    leader_id = models.IntegerField(blank=True, null=True)  # 上级管理员id
    create_time = models.DateTimeField(auto_now_add=datetime.now())  # 创建时间
    is_delete = models.IntegerField(default=0)  # 是否禁用 0不禁用   1禁用
    password = models.CharField(max_length=128)  # 密码
    last_time = models.DateTimeField(auto_now_add=datetime.now(), blank=True, null=True)  # 最后登录时间
    sex = models.IntegerField(default=1)  # 性别 0 女   1 男
    age = models.IntegerField(blank=True, null=True)  # 年龄
    phone_num = models.CharField(max_length=11)  # 手机号
    email = models.CharField(max_length=64, blank=True, null=True)  # 邮箱

    class Meta:
        managed = False
        db_table = 'admin_info'

    def to_dict(self):
        data = {
            'id': self.admin_id,
            'role_id': self.admin_role_id,
            'name': self.name,
            'leader_id': self.leader_id,
            'create_time': self.create_time,
            'is_delete': self.is_delete,
            'last_time': self.last_time,
            'sex': self.sex,
            'age': self.age,
            'phone_num': self.phone_num,
            'email': self.email
        }
        return data


class AdminLoginLog(models.Model):
    """
    管理员登录日志
    """
    admin_login_id = models.AutoField(primary_key=True)  # id
    admin = models.ForeignKey(AdminInfo, models.DO_NOTHING, blank=True, null=True)  # 管理员id（外键）
    login_time = models.DateTimeField(auto_now_add=datetime.now())  # 登录时间
    login_ip = models.CharField(max_length=64)  # 登录ip

    class Meta:
        managed = False
        db_table = 'admin_login_log'

    def to_dict(self):
        data = {
            'id': self.admin_login_id,
            'admin_id': self.admin_id,
            'login_time': self.login_ip,
            'login_ip': self.login_ip
        }
        return data


class AdminPower(models.Model):
    """
    管理员权限
    """
    admin_power_id = models.AutoField(primary_key=True)  # id
    name = models.CharField(max_length=64)  # 权限名
    description = models.CharField(max_length=256)  # 描述
    admin_role = models.ManyToManyField('AdminRole', through='Relationship23')  # 角色id

    class Meta:
        managed = False
        db_table = 'admin_power'

    def to_dict(self):
        data = {
            'id': self.admin_power_id,
            'name': self.name,
            'description': self.description,
        }
        return data


class AdminRole(models.Model):
    """
    管理员角色
    """
    admin_role_id = models.AutoField(primary_key=True)  # id
    name = models.CharField(max_length=64)  # 角色名
    is_delete = models.IntegerField(default=0)  # 是否禁用 0 否   1 禁用
    create_time = models.DateTimeField(auto_now_add=datetime.now())  # 创建日期
    description = models.CharField(max_length=256)  # 描述

    class Meta:
        managed = False
        db_table = 'admin_role'

    def to_dict(self):
        data = {
            'id': self.admin_role_id,
            'name': self.name,
            'is_delete': self.is_delete,
            'create_time': self.create_time,
            'description': self.description,
            'powers': [i.name for i in self.adminpower_set.all()]
        }
        return data


class AmountOfMaterial(models.Model):
    """
    原料用量
    """
    amount_id = models.AutoField(primary_key=True)  # id
    material_info = models.ForeignKey('MaterialInfo', models.DO_NOTHING, blank=True, null=True)  # 原料信息id（外键）
    time = models.DateTimeField()  # 使用日期--> 销售数据中来
    amount_of_use = models.IntegerField()  # 使用量 --> 销售数据中来计算

    class Meta:
        managed = False
        db_table = 'amount_of_material'

    def to_dict(self):
        data = {
            'id': self.amount_id,
            'material_id': self.material_info.material_info_id,
            'time': self.time,
            'amount_of_use': self.amount_of_use
        }
        return data


class EmpHandleLog(models.Model):
    """
    员工操作日志
    """
    emp_handle_log_id = models.AutoField(primary_key=True)  # id
    emp = models.ForeignKey('EmpInfo', models.DO_NOTHING, blank=True, null=True)  # 员工id（外键）
    handle_time = models.DateTimeField(auto_now_add=datetime.now())  # 操作时间
    event = models.CharField(max_length=256)  # 操作事件

    class Meta:
        managed = False
        db_table = 'emp_handle_log'

    def to_dict(self):
        data = {
            'id': self.emp_handle_log_id,
            'emp_id': self.emp_id,
            'handle_time': self.handle_time,
            'event': self.event
        }
        return data


class EmpInfo(models.Model):
    """
    员工信息
    """
    emp_id = models.AutoField(primary_key=True)  # id
    store_info = models.ForeignKey('StoreInfo', models.DO_NOTHING, blank=True, null=True)  # 商店id（外键）
    store_role = models.ForeignKey('StoreRole', models.DO_NOTHING, blank=True, null=True)  # 角色id（外键）
    name = models.CharField(max_length=64)  # 姓名
    emp_no = models.CharField(max_length=64, blank=True, null=True)  # 员工工号
    sex = models.IntegerField(default=1)  # 性别  0 女  1 男
    age = models.IntegerField(blank=True, null=True)  # 年龄
    join_time = models.DateTimeField(blank=True, null=True)  # 进入工作时间
    work_status = models.CharField(max_length=32, blank=True, null=True)  # 工作状态：兼职/全职
    salary = models.IntegerField(blank=True, null=True)  # 工资
    subsidy = models.IntegerField(blank=True, null=True)  # 奖金
    work_time = models.IntegerField(blank=True, null=True)  # 工作时间
    password = models.CharField(max_length=128)  # 密码

    class Meta:
        managed = False
        db_table = 'emp_info'

    def to_dict(self):
        data = {
            'id': self.emp_id,
            'store_name': self.store_info.name,
            'role_name': self.store_role.name,
            'name': self.name,
            'emp_no': self.emp_no,
            'sex': self.sex,
            'age': self.age,
            'join_time': self.join_time,
            'work_status': self.work_status,
            'salary': self.salary,
            'subsidy': self.subsidy,
            'work_time': self.work_time,
        }
        return data


class EmpLoginLog(models.Model):
    """
    员工登录日志
    """
    emp_login_id = models.AutoField(primary_key=True)  # id
    merchant = models.ForeignKey('MerchantInfo', models.DO_NOTHING, blank=True, null=True)  # 商家id（外键）
    emp = models.ForeignKey(EmpInfo, models.DO_NOTHING, blank=True, null=True)  # 员工id（外键）
    longin_time = models.DateTimeField(auto_now_add=datetime.now())  # 登录时间
    login_ip = models.CharField(max_length=64)  # 登录ip

    class Meta:
        managed = False
        db_table = 'emp_login_log'

    def to_dict(self):
        data = {
            'id': self.emp_login_id,
            'merchant_name': self.merchant.name,
            'emp_name': self.emp.name,
            'longin_time': self.longin_time,
            'login_ip': self.login_ip
        }
        return data


class GoodsInfo(models.Model):
    """
    商品信息
    """
    goods_id = models.AutoField(primary_key=True)  # id
    store_info = models.ForeignKey('StoreInfo', models.DO_NOTHING, blank=True, null=True)  # 商店id（外键）
    goods_type = models.ForeignKey('GoodsType', models.DO_NOTHING, blank=True, null=True)  # 商品分类id（外键）
    name = models.CharField(max_length=64)  # 名称
    price = models.IntegerField()  # 价格

    class Meta:
        managed = False
        db_table = 'goods_info'

    def to_dict(self):
        data = {
            'id': self.goods_id,
            'store_name': self.store_info.name,
            'type_name': self.goods_type.name,
            'name': self.name,
            'price': self.price
        }
        return data


class GoodsType(models.Model):
    """
    商品分类
    """
    goods_type_id = models.AutoField(primary_key=True)  # id
    name = models.CharField(max_length=64)  # 分类名
    store_info = models.ForeignKey('StoreInfo', models.DO_NOTHING, blank=True, null=True)  # 商店id（外键）


    class Meta:
        managed = False
        db_table = 'goods_type'

    def to_dict(self):
        data = {
            'id': self.goods_type_id,
            'name': self.name,
            'store_name': self.store_info.name
        }
        return data


class MaterialInfo(models.Model):
    """
    原料信息
    """
    material_info_id = models.AutoField(primary_key=True)  # id
    material_type = models.ForeignKey('MaterialType', models.DO_NOTHING, blank=True, null=True)  # 原料分类id(外键)
    name = models.CharField(max_length=64)  # 分类名

    class Meta:
        managed = False
        db_table = 'material_info'

    def to_dict(self):
        data = {
            'id': self.material_info_id,
            'type_name': self.material_type.name,
            'name': self.name
        }
        return data


class MaterialType(models.Model):
    """
    原料分类
    """
    material_type_id = models.AutoField(primary_key=True)  # id
    merchant = models.ForeignKey('MerchantInfo', models.DO_NOTHING, blank=True, null=True)  # 商家id（外键）
    name = models.CharField(max_length=64)  # 分类名
    create_time = models.DateTimeField(auto_now_add=datetime.now())  # 创建时间
    emp_id = models.IntegerField()  # 创建人id
    is_delete = models.IntegerField(default=0)  # 是否禁用 0 否   1 禁用

    class Meta:
        managed = False
        db_table = 'material_type'

    def to_dict(self):
        data = {
            'id': self.material_type_id,
            'merchant_name': self.materialinfo_set.name,
            'name': self.name,
            'create_time': self.create_time,
            'emp_id': self.emp_id,
            'is_delete': self.is_delete
        }
        return data


class MerchantInfo(models.Model):
    """
    商家信息
    """
    merchant_id = models.AutoField(primary_key=True)  # id
    name = models.CharField(max_length=64)  # 名称
    password = models.CharField(max_length=128)  # 密码
    sex = models.IntegerField(blank=True, null=True)  # 性别  0 女  1男
    icon = models.CharField(max_length=64, blank=True, null=True)  # 头像
    email = models.CharField(max_length=64, blank=True, null=True)  # 邮箱
    phone_number = models.CharField(max_length=11)  # 手机号
    address = models.CharField(max_length=128, blank=True, null=True)  # 地址

    class Meta:
        managed = False
        db_table = 'merchant_info'

    def to_dict(self):
        data = {
            'id': self.merchant_id,
            'name': self.name,
            'sex': self.sex,
            'icon': self.icon,
            'email': self.email,
            'phone_number': self.phone_number,
            'address': self.address
        }
        return data


class Recipe(models.Model):
    """
    配方
    """
    recipe_id = models.AutoField(primary_key=True)  # id
    goods = models.ForeignKey(GoodsInfo, models.DO_NOTHING, blank=True, null=True)  # 商品id(外键)
    material_info = models.ForeignKey(MaterialInfo, models.DO_NOTHING, blank=True, null=True)  # 原料id(外键)
    need_count = models.IntegerField()  # 所需数量
    unit = models.CharField(max_length=32)  # 单位

    class Meta:
        managed = False
        db_table = 'recipe'

    def to_dict(self):
        data = {
            'id': self.recipe_id,
            'goods_name': self.goods.name,
            'material_name': self.material_info.name,
            'need_count': self.need_count,
            'unit': self.unit
        }
        return data


class Relationship14(models.Model):
    """
    商品和口味中间表
    """
    taste_type = models.ForeignKey('TasteType', models.DO_NOTHING, primary_key=True)
    goods = models.ForeignKey(GoodsInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'relationship_14'
        unique_together = (('taste_type', 'goods'),)


class Relationship23(models.Model):
    """
    管理员权限与角色中间表
    """
    admin_power = models.ForeignKey(AdminPower, models.DO_NOTHING, primary_key=True)
    admin_role = models.ForeignKey(AdminRole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'relationship_23'
        unique_together = (('admin_power', 'admin_role'),)


class Relationship7(models.Model):
    """
    店员权限和角色中间表
    """
    store_power = models.ForeignKey('StorePower', models.DO_NOTHING, primary_key=True)
    store_role = models.ForeignKey('StoreRole', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'relationship_7'
        unique_together = (('store_power', 'store_role'),)


class SimulatorData(models.Model):
    """
    模拟器数据
    """
    simulator_data_id = models.AutoField(primary_key=True)  # id
    goods_id = models.IntegerField(null=True)  # 商品id （店员录入）
    name = models.CharField(max_length=64)  # 商品名称
    score = models.FloatField()  # 评分
    place = models.CharField(max_length=128)  # 售出地区
    sole_time = models.DateTimeField()  # 销售时间
    type_goods = models.IntegerField()  # 商品分类
    type_taste = models.IntegerField()  # 口味分类
    t_price = models.IntegerField()  # 价位分类
    create_time = models.DateTimeField()  # 创建时间
    update_time = models.DateTimeField()  # 修改时间
    merchant_name = models.CharField(max_length=64)  # 商家名

    class Meta:
        managed = False
        db_table = 'simulator_data'

    def to_dict(self):
        data = {
            'id': self.simulator_data_id,
            'goods_id': self.goods_id,
            'name': self.name,
            'score': self.score,
            'place': self.place,
            'sole_time': self.sole_time,
            'type_goods': self.type_goods,
            'type_taste': self.type_taste,
            't_price': self.t_price,
            'create_time': self.create_time,
            'update_time': self.update_time,
            'merchant_name': self.merchant_name
        }
        return data


class StoreInfo(models.Model):
    """
    店铺信息
    """
    store_info_id = models.AutoField(primary_key=True)  # id
    merchant = models.ForeignKey(MerchantInfo, models.DO_NOTHING, blank=True, null=True)  # 商家id(外键)
    name = models.CharField(max_length=64)  # 店铺名
    address = models.CharField(max_length=128)  # 地址

    class Meta:
        managed = False
        db_table = 'store_info'

    def to_dict(self):
        data = {
            'id': self.store_info_id,
            'merchant_name': self.merchant.name,
            'name': self.name,
            'address': self.address
        }
        return data


class StorePower(models.Model):
    """
    店员权利
    """
    store_power_id = models.AutoField(primary_key=True)  # id
    name = models.CharField(max_length=64)  # 权利名
    store_role = models.ManyToManyField('StoreRole', through='Relationship7')  # 角色id(外键)

    class Meta:
        managed = False
        db_table = 'store_power'

    def to_dict(self):
        data = {
            'id': self.store_power_id,
            'name': self.name
        }
        return data


class StoreRole(models.Model):
    """
    店员角色
    """
    store_role_id = models.AutoField(primary_key=True)  # id
    name = models.CharField(max_length=64)  # 权利名

    class Meta:
        managed = False
        db_table = 'store_role'

    def to_dict(self):
        data = {
            'id': self.store_role_id,
            'name': self.name,
            'powers': [i.name for i in self.storepower_set.all()]
        }
        return data


class TasteType(models.Model):
    """
    口味分类
    """
    taste_type_id = models.AutoField(primary_key=True)  # id
    taste = models.CharField(max_length=128)  # 口味名
    sales = models.IntegerField()  # 销量
    score = models.FloatField()  # 评分
    create_time = models.DateTimeField(auto_now_add=datetime.now())  # 创建时间
    update_time = models.DateTimeField(auto_now=datetime)  # 更新时间
    goods_info = models.ManyToManyField('GoodsInfo', through='Relationship14')  # 商品信息id(外键)

    class Meta:
        managed = False
        db_table = 'taste_type'

    def to_dict(self):
        data = {
            'id': self.taste_type_id,
            'taste': self.taste,
            'sales': self.sales,
            'score': self.score,
            'create_time': self.create_time,
            'update_time': self.update_time,
            'goods_names': [i.name for i in self.goods_info.all()]
        }
        return data
