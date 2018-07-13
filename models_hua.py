# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Distancesinterpolatedvalues(models.Model):
    div_id = models.AutoField(db_column='DIV_Id', primary_key=True)  # Field name made lowercase.
    div_mea_id = models.IntegerField(db_column='DIV_MEA_Id')  # Field name made lowercase.
    div_center_x = models.DecimalField(db_column='DIV_Center_X', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    div_center_y = models.DecimalField(db_column='DIV_Center_Y', max_digits=10, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    div_geomcenter = models.BinaryField(db_column='DIV_GeomCenter', blank=True, null=True)  # Field name made lowercase.
    div_center_distance = models.FloatField(db_column='DIV_Center_Distance', blank=True, null=True)  # Field name made lowercase.
    div_point_distance = models.FloatField(db_column='DIV_Point_Distance', blank=True, null=True)  # Field name made lowercase.
    div_idw = models.FloatField(db_column='DIV_IDW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DistancesInterpolatedValues'


class Measurements(models.Model):
    id = models.BigAutoField(primary_key=True)
    geomcol1 = models.BinaryField(db_column='GeomCol1', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(blank=True, null=True)
    lon = models.DecimalField(max_digits=10, decimal_places=5)
    lat = models.DecimalField(max_digits=10, decimal_places=5)
    level = models.IntegerField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    operatorname = models.CharField(max_length=50, blank=True, null=True)
    mcc = models.CharField(max_length=3, blank=True, null=True)
    mnc = models.CharField(max_length=3, blank=True, null=True)
    node = models.CharField(max_length=11, blank=True, null=True)
    cellid = models.CharField(max_length=11, blank=True, null=True)
    lac = models.CharField(max_length=11, blank=True, null=True)
    network_type = models.CharField(max_length=2, blank=True, null=True)
    qual = models.IntegerField(blank=True, null=True)
    snr = models.IntegerField(blank=True, null=True)
    cqi = models.IntegerField(blank=True, null=True)
    lterssi = models.IntegerField(blank=True, null=True)
    appversioncode = models.IntegerField(blank=True, null=True)
    psc = models.IntegerField(blank=True, null=True)
    dl_bitrate = models.IntegerField(blank=True, null=True)
    ul_bitrate = models.IntegerField(blank=True, null=True)
    nlac1 = models.IntegerField(blank=True, null=True)
    ncellid1 = models.IntegerField(blank=True, null=True)
    nrxlev1 = models.IntegerField(blank=True, null=True)
    nlac2 = models.IntegerField(blank=True, null=True)
    ncellid2 = models.IntegerField(blank=True, null=True)
    nrxlev2 = models.IntegerField(blank=True, null=True)
    nlac3 = models.IntegerField(blank=True, null=True)
    ncellid3 = models.IntegerField(blank=True, null=True)
    nrxlev3 = models.IntegerField(blank=True, null=True)
    nlac4 = models.IntegerField(blank=True, null=True)
    ncellid4 = models.IntegerField(blank=True, null=True)
    nrxlev4 = models.IntegerField(blank=True, null=True)
    nlac5 = models.IntegerField(blank=True, null=True)
    ncellid5 = models.IntegerField(blank=True, null=True)
    nrxlev5 = models.IntegerField(blank=True, null=True)
    nlac6 = models.IntegerField(blank=True, null=True)
    ncellid6 = models.IntegerField(blank=True, null=True)
    nrxlev6 = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    event = models.CharField(max_length=20, blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    locationsource = models.CharField(max_length=2, blank=True, null=True)
    altitude = models.IntegerField(blank=True, null=True)
    conntype = models.CharField(max_length=5, blank=True, null=True)
    conninfo = models.CharField(max_length=25, blank=True, null=True)
    avgping = models.IntegerField(blank=True, null=True)
    minping = models.IntegerField(blank=True, null=True)
    maxping = models.IntegerField(blank=True, null=True)
    stdevping = models.IntegerField(blank=True, null=True)
    pingloss = models.IntegerField(blank=True, null=True)
    testdlbitrate = models.IntegerField(blank=True, null=True)
    testulbitrate = models.IntegerField(blank=True, null=True)
    geomcol2 = models.TextField(db_column='GeomCol2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    devicemanufacturer = models.CharField(db_column='DeviceManufacturer', max_length=30, blank=True, null=True)  # Field name made lowercase.
    devicemodel = models.CharField(db_column='DeviceModel', max_length=30, blank=True, null=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    versionname = models.CharField(db_column='VersionName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=30, blank=True, null=True)  # Field name made lowercase.
    androidversion = models.CharField(db_column='AndroidVersion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    servingcelltime = models.IntegerField(db_column='ServingCellTime', blank=True, null=True)  # Field name made lowercase.
    os = models.CharField(max_length=30, blank=True, null=True)
    os_id = models.CharField(max_length=128, blank=True, null=True)
    camp = models.ForeignKey('Campaigns', models.DO_NOTHING, blank=True, null=True)
    ssid = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Measurements'


class Roi(models.Model):
    roi_id = models.AutoField(db_column='ROI_Id', primary_key=True)  # Field name made lowercase.
    roi_geomcenter = models.BinaryField(db_column='ROI_GeomCenter', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROI'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(db_column='SRID', primary_key=True)  # Field name made lowercase.
    auth_name = models.CharField(db_column='AUTH_NAME', max_length=256, blank=True, null=True)  # Field name made lowercase.
    auth_srid = models.IntegerField(db_column='AUTH_SRID', blank=True, null=True)  # Field name made lowercase.
    srtext = models.CharField(db_column='SRTEXT', max_length=2048, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SPATIAL_REF_SYS'


class Testavg(models.Model):
    lon = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    geomcol1 = models.BinaryField(db_column='Geomcol1', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TestAVG'


class Testfusion(models.Model):
    lon = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    geomcol1 = models.BinaryField(db_column='Geomcol1', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TestFusion'


class Testidwsave(models.Model):
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    geomcol1 = models.BinaryField(db_column='Geomcol1', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TestIDWsave'


class Testidwsave1(models.Model):
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    geomcol1 = models.BinaryField(db_column='Geomcol1', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TestIDWsave1'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class C2DmRegDevices(models.Model):
    c2dm_id = models.AutoField(primary_key=True)
    c2dm_regid = models.CharField(unique=True, max_length=250)
    c2dm_active = models.IntegerField()
    c2dm_date = models.DateTimeField()
    c2dm_androidid = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'c2dm_reg_devices'


class Campaigns(models.Model):
    camp_id = models.AutoField(unique=True)
    create_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535)
    network_type = models.CharField(max_length=10)
    accuracy = models.IntegerField()
    radius = models.IntegerField()
    velocity = models.IntegerField()
    dist_frequency = models.IntegerField()
    name = models.CharField(max_length=70, blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaigns'


class Devices(models.Model):
    android_id = models.CharField(primary_key=True, max_length=16)
    device_id = models.CharField(unique=True, max_length=16)
    device_serial = models.CharField(max_length=16)
    device_mac = models.TextField()  # This field type is a guess.
    device_brand = models.CharField(max_length=30, blank=True, null=True)
    device_model = models.CharField(max_length=30, blank=True, null=True)
    device_product = models.CharField(max_length=30, blank=True, null=True)
    device_build_id = models.CharField(max_length=30, blank=True, null=True)
    os = models.CharField(max_length=30, blank=True, null=True)
    os_version = models.CharField(max_length=30, blank=True, null=True)
    os_id = models.CharField(max_length=128, blank=True, null=True)
    subscriber_id = models.CharField(max_length=16)
    uuid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'devices'
        unique_together = (('android_id', 'device_id', 'device_mac', 'subscriber_id', 'uuid', 'device_serial'),)


class DevicesPerCampaign(models.Model):
    dc_campid = models.ForeignKey(Campaigns, models.DO_NOTHING, db_column='dc_campid')
    dc_devid = models.ForeignKey(C2DmRegDevices, models.DO_NOTHING, db_column='dc_devid')
    sent_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'devices_per_campaign'
        unique_together = (('dc_campid', 'dc_devid'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Metric(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metric'


class Originalfusion(models.Model):
    lon = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    geomcol1 = models.BinaryField(db_column='Geomcol1', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'originalFusion'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Testtable(models.Model):
    id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testtable'


class UserRoles(models.Model):
    role_id = models.AutoField(unique=True)
    authority = models.CharField(max_length=10)
    user = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'user_roles'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    passwordformat = models.IntegerField(blank=True, null=True)
    passwordsalt = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
