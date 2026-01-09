# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Academiclevels(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AcademicLevels'


class Areas(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Areas'


class Averageunits(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AverageUnits'


class Beneficiarytypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BeneficiaryTypes'


class Benefitdepprodelements(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    depositproductionid = models.ForeignKey('Depositproductions', models.DO_NOTHING, db_column='DepositProductionId')  # Field name made lowercase.
    elementid = models.ForeignKey('Elements', models.DO_NOTHING, db_column='ElementId')  # Field name made lowercase.
    measurementunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='MeasurementUnitId')  # Field name made lowercase.
    lawqty = models.DecimalField(db_column='LawQty', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    quantityunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='QuantityUnitId', related_name='benefitdepprodelements_quantityunitid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BenefitDepProdElements'


class Benefitplantminerals(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    code = models.CharField(db_column='Code', max_length=32)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=128)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    taxable = models.IntegerField(db_column='Taxable')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BenefitPlantMinerals'


class Benefitplantprodelements(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    plantproductionid = models.ForeignKey('Plantproductions', models.DO_NOTHING, db_column='PlantProductionId')  # Field name made lowercase.
    elementid = models.ForeignKey('Elements', models.DO_NOTHING, db_column='ElementId')  # Field name made lowercase.
    lawunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='LawUnitId')  # Field name made lowercase.
    lawqty = models.DecimalField(db_column='LawQty', max_digits=24, decimal_places=8)  # Field name made lowercase.
    finecontentunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='FineContentUnitId', related_name='benefitplantprodelements_finecontentunitid_set')  # Field name made lowercase.
    finecontentqty = models.DecimalField(db_column='FineContentQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qtyinkg = models.DecimalField(db_column='QtyInKg', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    qtyinoz = models.DecimalField(db_column='QtyInOz', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    stock = models.DecimalField(db_column='Stock', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    quantityunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='QuantityUnitId', related_name='benefitplantprodelements_quantityunitid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BenefitPlantProdElements'


class Canonlogs(models.Model):
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    expedientid = models.UUIDField(db_column='ExpedientId')  # Field name made lowercase.
    canonperiodid = models.UUIDField(db_column='CanonPeriodId')  # Field name made lowercase.
    canonstateid = models.UUIDField(db_column='CanonStateId')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surcharge = models.DecimalField(db_column='Surcharge', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surchargepercentage = models.DecimalField(db_column='SurchargePercentage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paid = models.DecimalField(db_column='Paid', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    id = models.UUIDField(db_column='Id',primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CanonLogs'


class Canonmultypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CanonMulTypes'


class Canonperiods(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CanonPeriods'


class Canonstates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CanonStates'


class Canons(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    expedientid = models.ForeignKey('Expedients', models.DO_NOTHING, db_column='ExpedientId')  # Field name made lowercase.
    canonperiodid = models.ForeignKey(Canonperiods, models.DO_NOTHING, db_column='CanonPeriodId')  # Field name made lowercase.
    canonstateid = models.ForeignKey(Canonstates, models.DO_NOTHING, db_column='CanonStateId')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surcharge = models.DecimalField(db_column='Surcharge', max_digits=24, decimal_places=8)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paid = models.DecimalField(db_column='Paid', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    surchargepercentage = models.DecimalField(db_column='SurchargePercentage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    pertenencias = models.SmallIntegerField(db_column='Pertenencias', blank=True, null=True)  # Field name made lowercase.
    superficie = models.BigIntegerField(db_column='Superficie', blank=True, null=True)  # Field name made lowercase.
    yacencia = models.CharField(db_column='Yacencia', max_length=32, blank=True, null=True)  # Field name made lowercase.
    payercompanyid = models.ForeignKey('Companies', models.DO_NOTHING, db_column='PayerCompanyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Canons'


class Ccts(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    code = models.CharField(db_column='Code', max_length=32)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=128)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ccts'


class Ciius(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    code = models.CharField(db_column='Code', unique=True, max_length=8)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=256)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ciius'


class Commitmentstates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CommitmentStates'


class Commitmenttypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CommitmentTypes'


class Commitments(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    presentationcommitmentid = models.ForeignKey('Presentationcommitments', models.DO_NOTHING, db_column='PresentationCommitmentId')  # Field name made lowercase.
    trainername = models.CharField(db_column='TrainerName', max_length=64)  # Field name made lowercase.
    topics = models.CharField(db_column='Topics', max_length=512)  # Field name made lowercase.
    hours = models.IntegerField(db_column='Hours')  # Field name made lowercase.
    beneficiaries = models.CharField(db_column='Beneficiaries', max_length=512)  # Field name made lowercase.
    assistants = models.IntegerField(db_column='Assistants')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Commitments'


class Companies(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=128)  # Field name made lowercase.
    cuit = models.CharField(db_column='Cuit', max_length=64, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    inscnumberlaw = models.CharField(db_column='InscNumberLaw', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ciiuid = models.ForeignKey(Ciius, models.DO_NOTHING, db_column='CiiuId', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=128, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=128, blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    nro = models.IntegerField(db_column='Nro')  # Field name made lowercase.
    phone = models.BigIntegerField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    cuil = models.BigIntegerField(db_column='Cuil', blank=True, null=True)  # Field name made lowercase.
    royaltybalance = models.DecimalField(db_column='RoyaltyBalance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    mulbalance = models.DecimalField(db_column='MulBalance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    conceptbalance = models.DecimalField(db_column='ConceptBalance', max_digits=24, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Companies'


class Companycontractors(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    contractorid = models.ForeignKey('Contractors', models.DO_NOTHING, db_column='ContractorId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompanyContractors'


class Companyemployees(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='EmployeeId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompanyEmployees'


class Companyexpedients(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    expedientid = models.ForeignKey('Expedients', models.DO_NOTHING, db_column='ExpedientId')  # Field name made lowercase.
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    mustpaycanon = models.BooleanField(db_column='MustPayCanon')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompanyExpedients'


class Companyminingactivities(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    miningactivityid = models.ForeignKey('Miningactivities', models.DO_NOTHING, db_column='MiningActivityId')  # Field name made lowercase.
    registrationnumber = models.CharField(db_column='RegistrationNumber', max_length=8, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompanyMiningActivities'


class Companyprojectexpedients(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='ProjectId')  # Field name made lowercase.
    companyexpedientid = models.ForeignKey(Companyexpedients, models.DO_NOTHING, db_column='CompanyExpedientId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompanyProjectExpedients'


class Companyprojects(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='ProjectId')  # Field name made lowercase.
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompanyProjects'


class Companyresponsibles(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    responsibleid = models.ForeignKey('Responsibles', models.DO_NOTHING, db_column='ResponsibleId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompanyResponsibles'


class Conceptnotetypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConceptNoteTypes'


class Conceptnotes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    conceptnotetypeid = models.ForeignKey(Conceptnotetypes, models.DO_NOTHING, db_column='ConceptNoteTypeId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConceptNotes'


class Conceptpayments(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConceptPayments'


class Conceptstates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConceptStates'


class Conceptvepdetails(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    conceptvepid = models.ForeignKey('Conceptveps', models.DO_NOTHING, db_column='ConceptVepId')  # Field name made lowercase.
    conceptid = models.ForeignKey('Concepts', models.DO_NOTHING, db_column='ConceptId')  # Field name made lowercase.
    conceptstateid = models.ForeignKey(Conceptstates, models.DO_NOTHING, db_column='ConceptStateId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surcharge = models.DecimalField(db_column='Surcharge', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surchargepercentage = models.DecimalField(db_column='SurchargePercentage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paid = models.DecimalField(db_column='Paid', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConceptVepDetails'


class Conceptveplogs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    conceptvepid = models.ForeignKey('Conceptveps', models.DO_NOTHING, db_column='ConceptVepId')  # Field name made lowercase.
    conceptvepstateid = models.ForeignKey('Conceptvepstates', models.DO_NOTHING, db_column='ConceptVepStateId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConceptVepLogs'


class Conceptvepnotes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    conceptvepid = models.ForeignKey('Conceptveps', models.DO_NOTHING, db_column='ConceptVepId')  # Field name made lowercase.
    conceptnoteid = models.ForeignKey(Conceptnotes, models.DO_NOTHING, db_column='ConceptNoteId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConceptVepNotes'


class Conceptveppaymentreceipts(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    conceptvepid = models.ForeignKey('Conceptveps', models.DO_NOTHING, db_column='ConceptVepId')  # Field name made lowercase.
    fullpath = models.TextField(db_column='FullPath')  # Field name made lowercase.
    relativepath = models.TextField(db_column='RelativePath')  # Field name made lowercase.
    confirmedamount = models.DecimalField(db_column='ConfirmedAmount', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    receiptdate = models.DateTimeField(db_column='ReceiptDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConceptVepPaymentReceipts'


class Conceptvepstates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConceptVepStates'


class Conceptveps(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    conceptvepstateid = models.ForeignKey(Conceptvepstates, models.DO_NOTHING, db_column='ConceptVepStateId')  # Field name made lowercase.
    linkedconceptvepid = models.ForeignKey('self', models.DO_NOTHING, db_column='LinkedConceptVepId', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='Subtotal', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surcharge = models.DecimalField(db_column='Surcharge', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surchargepercentage = models.DecimalField(db_column='SurchargePercentage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=24, decimal_places=8)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paid = models.DecimalField(db_column='Paid', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    observation = models.CharField(db_column='Observation', max_length=256, blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', max_length=128, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.UUIDField(db_column='TransactionId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConceptVeps'


class Concepts(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    conceptstateid = models.ForeignKey(Conceptstates, models.DO_NOTHING, db_column='ConceptStateId')  # Field name made lowercase.
    regconcepttypeid = models.ForeignKey('Regconcepttypes', models.DO_NOTHING, db_column='RegConceptTypeId')  # Field name made lowercase.
    concepto = models.CharField(db_column='Concepto', max_length=256)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surcharge = models.DecimalField(db_column='Surcharge', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surchargepercentage = models.DecimalField(db_column='SurchargePercentage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paid = models.DecimalField(db_column='Paid', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    generationdate = models.DateTimeField(db_column='GenerationDate', blank=True, null=True)  # Field name made lowercase.
    royaltyddjjid = models.ForeignKey('Royaltyddjjs', models.DO_NOTHING, db_column='RoyaltyDDJJId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Concepts'


class Contracttypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContractTypes'


class Contractoremployees(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    contractorid = models.ForeignKey('Contractors', models.DO_NOTHING, db_column='ContractorId')  # Field name made lowercase.
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='EmployeeId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContractorEmployees'


class Contractormodes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContractorModes'


class Contractorresponsibles(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    contractorid = models.ForeignKey('Contractors', models.DO_NOTHING, db_column='ContractorId')  # Field name made lowercase.
    responsibleid = models.ForeignKey('Responsibles', models.DO_NOTHING, db_column='ResponsibleId')  # Field name made lowercase.
    serviceid = models.ForeignKey('Services', models.DO_NOTHING, db_column='ServiceId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContractorResponsibles'


class Contractortypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ContractorTypes'


class Contractors(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    cuit = models.CharField(db_column='Cuit', max_length=16)  # Field name made lowercase.
    businessname = models.CharField(db_column='BusinessName', max_length=64)  # Field name made lowercase.
    ciiuid = models.ForeignKey(Ciius, models.DO_NOTHING, db_column='CiiuId')  # Field name made lowercase.
    registrationnumber = models.CharField(db_column='RegistrationNumber', max_length=64)  # Field name made lowercase.
    areaid = models.ForeignKey(Areas, models.DO_NOTHING, db_column='AreaId')  # Field name made lowercase.
    zoneid = models.ForeignKey('Zones', models.DO_NOTHING, db_column='ZoneId')  # Field name made lowercase.
    nativecommunityid = models.ForeignKey('Nativecommunities', models.DO_NOTHING, db_column='NativeCommunityId')  # Field name made lowercase.
    contractormodeid = models.ForeignKey(Contractormodes, models.DO_NOTHING, db_column='ContractorModeId')  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    employeesqty = models.IntegerField(db_column='EmployeesQty')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    federalregnumber = models.CharField(db_column='FederalRegNumber', max_length=64, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=128)  # Field name made lowercase.
    femaleemployeesqty = models.IntegerField(db_column='FemaleEmployeesQty', blank=True, null=True)  # Field name made lowercase.
    maleemployeesqty = models.IntegerField(db_column='MaleEmployeesQty', blank=True, null=True)  # Field name made lowercase.
    nonbinaryemployeesqty = models.IntegerField(db_column='NonBinaryEmployeesQty', blank=True, null=True)  # Field name made lowercase.
    contractorsqty = models.IntegerField(db_column='ContractorsQty', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contractors'


class Currentaccountmovements(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    currentaccountid = models.ForeignKey('Currentaccounts', models.DO_NOTHING, db_column='CurrentAccountId')  # Field name made lowercase.
    actualamount = models.DecimalField(db_column='ActualAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    lastamount = models.DecimalField(db_column='LastAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    movementtypeid = models.ForeignKey('Movementtypes', models.DO_NOTHING, db_column='MovementTypeId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CurrentAccountMovements'


class Currentaccounts(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CurrentAccounts'


class Currentexpedients(models.Model):
    companyid = models.UUIDField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName')  # Field name made lowercase.
    expediente = models.IntegerField()
    nombreexpediente = models.TextField(db_column='NombreExpediente')  # Field name made lowercase.
    fecha = models.DateTimeField()
    debtamount = models.DecimalField(db_column='DebtAmount', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    daterange = models.IntegerField(db_column='DateRange', blank=True, null=True)  # Field name made lowercase.
    sit_legal_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CurrentExpedients'


class Depmineralelementunits(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    depositmineralelementid = models.ForeignKey('Depositmineralelements', models.DO_NOTHING, db_column='DepositMineralElementId')  # Field name made lowercase.
    measurementunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='MeasurementUnitId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepMineralElementUnits'


class Depproductionelements(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    depositproductionid = models.ForeignKey('Depositproductions', models.DO_NOTHING, db_column='DepositProductionId')  # Field name made lowercase.
    elementid = models.ForeignKey('Elements', models.DO_NOTHING, db_column='ElementId')  # Field name made lowercase.
    measurementunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='MeasurementUnitId')  # Field name made lowercase.
    lawqty = models.DecimalField(db_column='LawQty', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    avglawmeasunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='AvgLawMeasUnitId', related_name='depproductionelements_avglawmeasunitid_set', blank=True, null=True)  # Field name made lowercase.
    avglawqty = models.DecimalField(db_column='AvgLawQty', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    quantityunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='QuantityUnitId', related_name='depproductionelements_quantityunitid_set', blank=True, null=True)  # Field name made lowercase.
    vnrprice = models.DecimalField(db_column='VNRPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    vnrtotal = models.DecimalField(db_column='VNRTotal', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepProductionElements'


class Depositcoordinates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    depositid = models.ForeignKey('Deposits', models.DO_NOTHING, db_column='DepositId')  # Field name made lowercase.
    east = models.CharField(db_column='East', max_length=30, blank=True, null=True)  # Field name made lowercase.
    west = models.CharField(db_column='West', max_length=30, blank=True, null=True)  # Field name made lowercase.
    altitude = models.CharField(db_column='Altitude', max_length=30, blank=True, null=True)  # Field name made lowercase.
    totalarea = models.DecimalField(db_column='TotalArea', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    occupiedarea = models.DecimalField(db_column='OccupiedArea', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    lat = models.DecimalField(db_column='Lat', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    lng = models.DecimalField(db_column='Lng', max_digits=65535, decimal_places=65535)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepositCoordinates'


class Depositdeclaredminerals(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    depositid = models.ForeignKey('Deposits', models.DO_NOTHING, db_column='DepositId')  # Field name made lowercase.
    depositmineralid = models.ForeignKey('Depositminerals', models.DO_NOTHING, db_column='DepositMineralId')  # Field name made lowercase.
    phase = models.IntegerField(db_column='Phase')  # Field name made lowercase.
    category = models.IntegerField(db_column='Category')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepositDeclaredMinerals'


class Depositmineralelements(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    depositmineralid = models.ForeignKey('Depositminerals', models.DO_NOTHING, db_column='DepositMineralId')  # Field name made lowercase.
    elementid = models.ForeignKey('Elements', models.DO_NOTHING, db_column='ElementId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepositMineralElements'


class Depositmineralunits(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    depositmineralid = models.ForeignKey('Depositminerals', models.DO_NOTHING, db_column='DepositMineralId')  # Field name made lowercase.
    measurementunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='MeasurementUnitId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepositMineralUnits'


class Depositminerals(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    mineraltypeid = models.ForeignKey('Mineraltypes', models.DO_NOTHING, db_column='MineralTypeId')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=128)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    taxable = models.IntegerField(db_column='Taxable')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepositMinerals'


class Depositplantminerals(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    depositmineralid = models.ForeignKey(Depositminerals, models.DO_NOTHING, db_column='DepositMineralId')  # Field name made lowercase.
    benefitplantmineralid = models.ForeignKey(Benefitplantminerals, models.DO_NOTHING, db_column='BenefitPlantMineralId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepositPlantMinerals'


class Depositproductions(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    depositdeclaredmineralid = models.ForeignKey(Depositdeclaredminerals, models.DO_NOTHING, db_column='DepositDeclaredMineralId')  # Field name made lowercase.
    measurementunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='MeasurementUnitId', blank=True, null=True)  # Field name made lowercase.
    producedqty = models.DecimalField(db_column='ProducedQty', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferredqty = models.DecimalField(db_column='TransferredQty', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    valuationtypeid = models.ForeignKey('Valuationtypes', models.DO_NOTHING, db_column='ValuationTypeId', blank=True, null=True)  # Field name made lowercase.
    transferredamount = models.DecimalField(db_column='TransferredAmount', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    internalmarketsoldqty = models.DecimalField(db_column='InternalMarketSoldQty', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    internalmarketsoldamount = models.DecimalField(db_column='InternalMarketSoldAmount', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketsoldqty = models.DecimalField(db_column='ExternalMarketSoldQty', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketsoldqtyinkg = models.DecimalField(db_column='ExternalMarketSoldQtyInKg', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketsoldamount = models.DecimalField(db_column='ExternalMarketSoldAmount', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketsoldamountusd = models.DecimalField(db_column='ExternalMarketSoldAmountUsd', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    ncmcode = models.CharField(db_column='NcmCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ncmdesc = models.CharField(db_column='NcmDesc', max_length=256, blank=True, null=True)  # Field name made lowercase.
    initialstock = models.DecimalField(db_column='InitialStock', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    finalstock = models.DecimalField(db_column='FinalStock', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    declaredprice = models.DecimalField(db_column='DeclaredPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketdeclaredprice = models.DecimalField(db_column='ExternalMarketDeclaredPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketvnr = models.DecimalField(db_column='ExternalMarketVNR', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    internalmarketdeclaredprice = models.DecimalField(db_column='InternalMarketDeclaredPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    internalmarketvnr = models.DecimalField(db_column='InternalMarketVNR', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    vnr = models.DecimalField(db_column='VNR', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepositProductions'


class Depositsecproductions(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    depositid = models.ForeignKey('Deposits', models.DO_NOTHING, db_column='DepositId')  # Field name made lowercase.
    productionid = models.ForeignKey('Productions', models.DO_NOTHING, db_column='ProductionId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepositSecProductions'


class Deposittypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepositTypes'


class Deposits(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    deposittypeid = models.ForeignKey(Deposittypes, models.DO_NOTHING, db_column='DepositTypeId', blank=True, null=True)  # Field name made lowercase.
    miningmethodid = models.ForeignKey('Miningmethods', models.DO_NOTHING, db_column='MiningMethodId', blank=True, null=True)  # Field name made lowercase.
    substanceid = models.ForeignKey('Productions', models.DO_NOTHING, db_column='SubstanceId', blank=True, null=True)  # Field name made lowercase.
    productionid = models.ForeignKey('Productions', models.DO_NOTHING, db_column='ProductionId', related_name='deposits_productionid_set', blank=True, null=True)  # Field name made lowercase.
    productionplant = models.BooleanField(db_column='ProductionPlant', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    presentationid = models.ForeignKey('Presentations', models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Deposits'


class Destinations(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Destinations'


class Economiccycles(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EconomicCycles'


class Elements(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=32)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', unique=True, max_length=8)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Elements'


class Employees(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    personid = models.OneToOneField('People', models.DO_NOTHING, db_column='PersonId')  # Field name made lowercase.
    hiredate = models.DateTimeField(db_column='HireDate')  # Field name made lowercase.
    contracttypeid = models.ForeignKey(Contracttypes, models.DO_NOTHING, db_column='ContractTypeId')  # Field name made lowercase.
    academiclevelid = models.ForeignKey(Academiclevels, models.DO_NOTHING, db_column='AcademicLevelId')  # Field name made lowercase.
    worktypeid = models.ForeignKey('Worktypes', models.DO_NOTHING, db_column='WorkTypeId', blank=True, null=True)  # Field name made lowercase.
    jobid = models.ForeignKey('Jobs', models.DO_NOTHING, db_column='JobId', blank=True, null=True)  # Field name made lowercase.
    workspaceid = models.ForeignKey('Workspaces', models.DO_NOTHING, db_column='WorkspaceId', blank=True, null=True)  # Field name made lowercase.
    grossincome = models.DecimalField(db_column='GrossIncome', max_digits=24, decimal_places=8)  # Field name made lowercase.
    labordays = models.CharField(db_column='LaborDays', max_length=64)  # Field name made lowercase.
    laborhours = models.DecimalField(db_column='LaborHours', max_digits=4, decimal_places=2)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    cctid = models.ForeignKey(Ccts, models.DO_NOTHING, db_column='CctId')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employees'


class Expmunintersections(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nroexp = models.IntegerField(db_column='NroExp')  # Field name made lowercase.
    nomexp = models.CharField(db_column='NomExp', max_length=256, blank=True, null=True)  # Field name made lowercase.
    nomdep = models.CharField(db_column='NomDep', max_length=256, blank=True, null=True)  # Field name made lowercase.
    nommun = models.CharField(db_column='NomMun', max_length=256, blank=True, null=True)  # Field name made lowercase.
    supexp = models.FloatField(db_column='SupExp')  # Field name made lowercase.
    supmun = models.FloatField(db_column='SupMun')  # Field name made lowercase.
    supint = models.FloatField(db_column='SupInt')  # Field name made lowercase.
    porint = models.FloatField(db_column='PorInt')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExpMunIntersections'


class Expedientdates(models.Model):
    tipo_sit = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExpedientDates'


class Expedients(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    nombre = models.CharField(db_column='Nombre', max_length=128)  # Field name made lowercase.
    zoneid = models.ForeignKey('Zones', models.DO_NOTHING, db_column='ZoneId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    departamen = models.CharField(db_column='Departamen', max_length=256, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=64, blank=True, null=True)  # Field name made lowercase.
    expediente = models.IntegerField(db_column='Expediente')  # Field name made lowercase.
    geom = models.TextField(db_column='Geom', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grupominero = models.IntegerField(db_column='GrupoMinero', blank=True, null=True)  # Field name made lowercase.
    municipio = models.CharField(db_column='Municipio', max_length=256, blank=True, null=True)  # Field name made lowercase.
    pertenencias = models.SmallIntegerField(db_column='Pertenencias')  # Field name made lowercase.
    superficie = models.BigIntegerField(db_column='Superficie')  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=16)  # Field name made lowercase.
    yacencia = models.CharField(db_column='Yacencia', max_length=32, blank=True, null=True)  # Field name made lowercase.
    distribution = models.IntegerField(db_column='Distribution', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Expedients'


class Exportcountries(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    plantid = models.ForeignKey('Plants', models.DO_NOTHING, db_column='PlantId')  # Field name made lowercase.
    zoneid = models.ForeignKey('Zones', models.DO_NOTHING, db_column='ZoneId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExportCountries'


class Extmarketdepprodelements(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    depositproductionid = models.ForeignKey(Depositproductions, models.DO_NOTHING, db_column='DepositProductionId')  # Field name made lowercase.
    elementid = models.ForeignKey(Elements, models.DO_NOTHING, db_column='ElementId')  # Field name made lowercase.
    measurementunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='MeasurementUnitId')  # Field name made lowercase.
    lawqty = models.DecimalField(db_column='LawQty', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    quantityunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='QuantityUnitId', related_name='extmarketdepprodelements_quantityunitid_set', blank=True, null=True)  # Field name made lowercase.
    vnrprice = models.DecimalField(db_column='VNRPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    vnrtotal = models.DecimalField(db_column='VNRTotal', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExtMarketDepProdElements'


class Extmarketplantprodelements(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    plantproductionid = models.ForeignKey('Plantproductions', models.DO_NOTHING, db_column='PlantProductionId')  # Field name made lowercase.
    elementid = models.ForeignKey(Elements, models.DO_NOTHING, db_column='ElementId')  # Field name made lowercase.
    lawunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='LawUnitId')  # Field name made lowercase.
    lawqty = models.DecimalField(db_column='LawQty', max_digits=24, decimal_places=8)  # Field name made lowercase.
    finecontentunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='FineContentUnitId', related_name='extmarketplantprodelements_finecontentunitid_set')  # Field name made lowercase.
    finecontentqty = models.DecimalField(db_column='FineContentQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qtyinkg = models.DecimalField(db_column='QtyInKg', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    qtyinoz = models.DecimalField(db_column='QtyInOz', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    stock = models.DecimalField(db_column='Stock', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    quantityunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='QuantityUnitId', related_name='extmarketplantprodelements_quantityunitid_set', blank=True, null=True)  # Field name made lowercase.
    vnrprice = models.DecimalField(db_column='VNRPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    vnrtotal = models.DecimalField(db_column='VNRTotal', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExtMarketPlantProdElements'


class Furtivecompanies(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=128)  # Field name made lowercase.
    cuit = models.CharField(db_column='Cuit', max_length=64, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=128, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.TextField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=128, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FurtiveCompanies'


class Furtivepresentationdeclaredcosts(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    furtivepresentationid = models.ForeignKey('Furtivepresentations', models.DO_NOTHING, db_column='FurtivePresentationId')  # Field name made lowercase.
    royaltycostid = models.ForeignKey('Royaltycosts', models.DO_NOTHING, db_column='RoyaltyCostId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FurtivePresentationDeclaredCosts'


class Furtivepresentationprodbymuns(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    furtivepresentationprodid = models.ForeignKey('Furtivepresentationprods', models.DO_NOTHING, db_column='FurtivePresentationProdId')  # Field name made lowercase.
    municipalityid = models.ForeignKey('Municipalities', models.DO_NOTHING, db_column='MunicipalityId')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=24, decimal_places=8)  # Field name made lowercase.
    percentage = models.DecimalField(db_column='Percentage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FurtivePresentationProdByMuns'


class Furtivepresentationprods(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    furtivepresentationid = models.ForeignKey('Furtivepresentations', models.DO_NOTHING, db_column='FurtivePresentationId')  # Field name made lowercase.
    producttype = models.IntegerField(db_column='ProductType')  # Field name made lowercase.
    mineralid = models.ForeignKey(Depositminerals, models.DO_NOTHING, db_column='MineralId', blank=True, null=True)  # Field name made lowercase.
    mineralelementid = models.ForeignKey(Depositmineralelements, models.DO_NOTHING, db_column='MineralElementId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey(Benefitplantminerals, models.DO_NOTHING, db_column='ProductId', blank=True, null=True)  # Field name made lowercase.
    productmineralid = models.ForeignKey(Depositplantminerals, models.DO_NOTHING, db_column='ProductMineralId', blank=True, null=True)  # Field name made lowercase.
    elementid = models.ForeignKey(Elements, models.DO_NOTHING, db_column='ElementId', blank=True, null=True)  # Field name made lowercase.
    measurementunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='MeasurementUnitId')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=24, decimal_places=8)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=24, decimal_places=8)  # Field name made lowercase.
    vnr = models.DecimalField(db_column='Vnr', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FurtivePresentationProds'


class Furtivepresentationveplogs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    furtivepresentationvepid = models.ForeignKey('Furtivepresentationveps', models.DO_NOTHING, db_column='FurtivePresentationVepId')  # Field name made lowercase.
    statepaymentid = models.ForeignKey('Statepayments', models.DO_NOTHING, db_column='StatePaymentId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FurtivePresentationVepLogs'


class Furtivepresentationvepreceipts(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    furtivepresentationvepid = models.ForeignKey('Furtivepresentationveps', models.DO_NOTHING, db_column='FurtivePresentationVepId')  # Field name made lowercase.
    fullpath = models.TextField(db_column='FullPath')  # Field name made lowercase.
    relativepath = models.TextField(db_column='RelativePath')  # Field name made lowercase.
    confirmedamount = models.DecimalField(db_column='ConfirmedAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    receiptdate = models.DateTimeField(db_column='ReceiptDate', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FurtivePresentationVepReceipts'


class Furtivepresentationveps(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    furtivepresentationid = models.ForeignKey('Furtivepresentations', models.DO_NOTHING, db_column='FurtivePresentationId')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    statepaymentid = models.ForeignKey('Statepayments', models.DO_NOTHING, db_column='StatePaymentId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surcharge = models.DecimalField(db_column='Surcharge', max_digits=24, decimal_places=8)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    observation = models.CharField(db_column='Observation', max_length=512, blank=True, null=True)  # Field name made lowercase.
    informedpaymentamount = models.DecimalField(db_column='InformedPaymentAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    informedpaymentdate = models.DateTimeField(db_column='InformedPaymentDate', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FurtivePresentationVeps'


class Furtivepresentations(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    furtivecompanyid = models.ForeignKey(Furtivecompanies, models.DO_NOTHING, db_column='FurtiveCompanyId')  # Field name made lowercase.
    royaltyperiodid = models.ForeignKey('Royaltyperiods', models.DO_NOTHING, db_column='RoyaltyPeriodId')  # Field name made lowercase.
    royaltystateid = models.ForeignKey('Royaltystates', models.DO_NOTHING, db_column='RoyaltyStateId')  # Field name made lowercase.
    productiontype = models.IntegerField(db_column='ProductionType')  # Field name made lowercase.
    presentationdate = models.DateTimeField(db_column='PresentationDate', blank=True, null=True)  # Field name made lowercase.
    observation = models.CharField(db_column='Observation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guides = models.IntegerField(db_column='Guides')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FurtivePresentations'


class Genders(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Genders'


class Generaldata(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    ciiuid = models.ForeignKey(Ciius, models.DO_NOTHING, db_column='CiiuId', blank=True, null=True)  # Field name made lowercase.
    economiccycleid = models.ForeignKey(Economiccycles, models.DO_NOTHING, db_column='EconomicCycleId', blank=True, null=True)  # Field name made lowercase.
    presentationid = models.ForeignKey('Presentations', models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    projectcycleid = models.ForeignKey('Projectcycles', models.DO_NOTHING, db_column='ProjectCycleId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    submittedprojectcycleid = models.ForeignKey('Projectcycles', models.DO_NOTHING, db_column='SubmittedProjectCycleId', related_name='generaldata_submittedprojectcycleid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GeneralData'


class Generaldatacompanycontractors(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    generaldataid = models.ForeignKey(Generaldata, models.DO_NOTHING, db_column='GeneralDataId')  # Field name made lowercase.
    companycontractorid = models.ForeignKey(Companycontractors, models.DO_NOTHING, db_column='CompanyContractorId')  # Field name made lowercase.
    serviceid = models.ForeignKey('Services', models.DO_NOTHING, db_column='ServiceId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GeneralDataCompanyContractors'


class Generaldatacompanyemployees(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    generaldataid = models.ForeignKey(Generaldata, models.DO_NOTHING, db_column='GeneralDataId')  # Field name made lowercase.
    companyemployeeid = models.ForeignKey(Companyemployees, models.DO_NOTHING, db_column='CompanyEmployeeId')  # Field name made lowercase.
    serviceid = models.ForeignKey('Services', models.DO_NOTHING, db_column='ServiceId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GeneralDataCompanyEmployees'


class Generaldataminingactivities(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    generaldataid = models.ForeignKey(Generaldata, models.DO_NOTHING, db_column='GeneralDataId')  # Field name made lowercase.
    miningactivityid = models.ForeignKey('Miningactivities', models.DO_NOTHING, db_column='MiningActivityId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GeneralDataMiningActivities'


class Generatedmonthlyreportdetails(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    generatedmonthlyreportid = models.ForeignKey('Generatedmonthlyreports', models.DO_NOTHING, db_column='GeneratedMonthlyReportId')  # Field name made lowercase.
    municipalityname = models.TextField(db_column='MunicipalityName')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GeneratedMonthlyReportDetails'


class Generatedmonthlyreports(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    month = models.IntegerField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    year = models.DecimalField(db_column='Year', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GeneratedMonthlyReports'


class Intmarketdepprodelements(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    depositproductionid = models.ForeignKey(Depositproductions, models.DO_NOTHING, db_column='DepositProductionId')  # Field name made lowercase.
    elementid = models.ForeignKey(Elements, models.DO_NOTHING, db_column='ElementId')  # Field name made lowercase.
    measurementunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='MeasurementUnitId')  # Field name made lowercase.
    lawqty = models.DecimalField(db_column='LawQty', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    quantityunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='QuantityUnitId', related_name='intmarketdepprodelements_quantityunitid_set', blank=True, null=True)  # Field name made lowercase.
    vnrprice = models.DecimalField(db_column='VNRPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    vnrtotal = models.DecimalField(db_column='VNRTotal', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IntMarketDepProdElements'


class Intmarketplantprodelements(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    plantproductionid = models.ForeignKey('Plantproductions', models.DO_NOTHING, db_column='PlantProductionId')  # Field name made lowercase.
    elementid = models.ForeignKey(Elements, models.DO_NOTHING, db_column='ElementId')  # Field name made lowercase.
    lawunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='LawUnitId')  # Field name made lowercase.
    lawqty = models.DecimalField(db_column='LawQty', max_digits=24, decimal_places=8)  # Field name made lowercase.
    finecontentunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='FineContentUnitId', related_name='intmarketplantprodelements_finecontentunitid_set')  # Field name made lowercase.
    finecontentqty = models.DecimalField(db_column='FineContentQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    qtyinkg = models.DecimalField(db_column='QtyInKg', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    qtyinoz = models.DecimalField(db_column='QtyInOz', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    stock = models.DecimalField(db_column='Stock', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    quantityunitid = models.ForeignKey('Measurementunits', models.DO_NOTHING, db_column='QuantityUnitId', related_name='intmarketplantprodelements_quantityunitid_set', blank=True, null=True)  # Field name made lowercase.
    vnrprice = models.DecimalField(db_column='VNRPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    vnrtotal = models.DecimalField(db_column='VNRTotal', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IntMarketPlantProdElements'


class Interbankingreqreslogs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=100)  # Field name made lowercase.
    collectingentity = models.IntegerField(db_column='CollectingEntity', blank=True, null=True)  # Field name made lowercase.
    debtid = models.BigIntegerField(db_column='DebtId', blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=1, blank=True, null=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    request = models.TextField(db_column='Request', blank=True, null=True)  # Field name made lowercase.
    responsestatuscode = models.IntegerField(db_column='ResponseStatusCode', blank=True, null=True)  # Field name made lowercase.
    responsecontent = models.TextField(db_column='ResponseContent', blank=True, null=True)  # Field name made lowercase.
    exceptionmessage = models.TextField(db_column='ExceptionMessage', blank=True, null=True)  # Field name made lowercase.
    exceptionstacktrace = models.TextField(db_column='ExceptionStackTrace', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    requestorigin = models.TextField(db_column='RequestOrigin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InterbankingReqResLogs'


class Interestlogs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    paymentflayerid = models.ForeignKey('Paymentflayers', models.DO_NOTHING, db_column='PaymentFlayerId')  # Field name made lowercase.
    interest = models.DecimalField(db_column='Interest', max_digits=24, decimal_places=8)  # Field name made lowercase.
    percentage = models.DecimalField(db_column='Percentage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InterestLogs'


class Investmentareas(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvestmentAreas'


class Investmentlocations(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvestmentLocations'


class Investmentsuppliertypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    presentationinvestmentid = models.ForeignKey('Presentationinvestments', models.DO_NOTHING, db_column='PresentationInvestmentId')  # Field name made lowercase.
    suppliertypeid = models.ForeignKey('Suppliertypes', models.DO_NOTHING, db_column='SupplierTypeId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvestmentSupplierTypes'


class Investmenttypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    investmentid = models.ForeignKey('Investments', models.DO_NOTHING, db_column='InvestmentId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvestmentTypes'


class Investments(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Investments'


class Jobs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=256)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Jobs'


class Logtypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=128)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LogTypes'


class Macroreqreslogs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=100)  # Field name made lowercase.
    collectingentity = models.IntegerField(db_column='CollectingEntity', blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vepid = models.UUIDField(db_column='VepId', blank=True, null=True)  # Field name made lowercase.
    transactionid = models.UUIDField(db_column='TransactionId', blank=True, null=True)  # Field name made lowercase.
    request = models.TextField(db_column='Request', blank=True, null=True)  # Field name made lowercase.
    responsestatuscode = models.IntegerField(db_column='ResponseStatusCode', blank=True, null=True)  # Field name made lowercase.
    responsecontent = models.TextField(db_column='ResponseContent', blank=True, null=True)  # Field name made lowercase.
    exceptionmessage = models.TextField(db_column='ExceptionMessage', blank=True, null=True)  # Field name made lowercase.
    exceptionstacktrace = models.TextField(db_column='ExceptionStackTrace', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    requestorigin = models.TextField(db_column='RequestOrigin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MacroReqResLogs'


class Markets(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Markets'


class Materials(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=128)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Materials'


class Measurementunits(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=128)  # Field name made lowercase.
    acronym = models.CharField(db_column='Acronym', max_length=8)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MeasurementUnits'


class Mineraltypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=32)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MineralTypes'


class Minerals(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Minerals'


class Miningactivities(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MiningActivities'


class Miningmethods(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MiningMethods'


class Movementtypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MovementTypes'


class Mulnotetypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MulNoteTypes'


class Mulnotes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    mulnotetypeid = models.ForeignKey(Mulnotetypes, models.DO_NOTHING, db_column='MulNoteTypeId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MulNotes'


class Mulstates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MulStates'


class Mulvepdetails(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    mulvepid = models.ForeignKey('Mulveps', models.DO_NOTHING, db_column='MulVepId')  # Field name made lowercase.
    multaid = models.ForeignKey('Multas', models.DO_NOTHING, db_column='MultaId')  # Field name made lowercase.
    mulstateid = models.ForeignKey(Mulstates, models.DO_NOTHING, db_column='MulStateId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surcharge = models.DecimalField(db_column='Surcharge', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surchargepercentage = models.DecimalField(db_column='SurchargePercentage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paid = models.DecimalField(db_column='Paid', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MulVepDetails'


class Mulveplogs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    mulvepid = models.ForeignKey('Mulveps', models.DO_NOTHING, db_column='MulVepId')  # Field name made lowercase.
    mulvepstateid = models.ForeignKey('Mulvepstates', models.DO_NOTHING, db_column='MulVepStateId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MulVepLogs'


class Mulvepnotes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    mulvepid = models.ForeignKey('Mulveps', models.DO_NOTHING, db_column='MulVepId')  # Field name made lowercase.
    mulnoteid = models.ForeignKey(Mulnotes, models.DO_NOTHING, db_column='MulNoteId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MulVepNotes'


class Mulveppaymentreceipts(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    mulvepid = models.ForeignKey('Mulveps', models.DO_NOTHING, db_column='MulVepId')  # Field name made lowercase.
    fullpath = models.TextField(db_column='FullPath')  # Field name made lowercase.
    relativepath = models.TextField(db_column='RelativePath')  # Field name made lowercase.
    confirmedamount = models.DecimalField(db_column='ConfirmedAmount', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    receiptdate = models.DateTimeField(db_column='ReceiptDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MulVepPaymentReceipts'


class Mulvepstates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MulVepStates'


class Mulveps(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    mulvepstateid = models.ForeignKey(Mulvepstates, models.DO_NOTHING, db_column='MulVepStateId')  # Field name made lowercase.
    linkedmulvepid = models.ForeignKey('self', models.DO_NOTHING, db_column='LinkedMulVepId', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='Subtotal', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surcharge = models.DecimalField(db_column='Surcharge', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surchargepercentage = models.DecimalField(db_column='SurchargePercentage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=24, decimal_places=8)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paid = models.DecimalField(db_column='Paid', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    observation = models.CharField(db_column='Observation', max_length=256, blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', max_length=128, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.UUIDField(db_column='TransactionId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MulVeps'


class Multas(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    mulstateid = models.ForeignKey(Mulstates, models.DO_NOTHING, db_column='MulStateId')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surcharge = models.DecimalField(db_column='Surcharge', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surchargepercentage = models.DecimalField(db_column='SurchargePercentage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paid = models.DecimalField(db_column='Paid', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    canonmultypeid = models.ForeignKey(Canonmultypes, models.DO_NOTHING, db_column='CanonMulTypeId')  # Field name made lowercase.
    concept = models.CharField(db_column='Concept', max_length=256)  # Field name made lowercase.
    generationdate = models.DateTimeField(db_column='GenerationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Multas'


class Municipalities(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=128)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=128, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Municipalities'


class Nationalities(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nationalities'


class Nativecommunities(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NativeCommunities'


class Normstates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NormStates'


class Norms(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Norms'


class Notetypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NoteTypes'


class Notes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    notetypeid = models.ForeignKey(Notetypes, models.DO_NOTHING, db_column='NoteTypeId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notes'


class Paramlogs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    paramid = models.ForeignKey('Params', models.DO_NOTHING, db_column='ParamId')  # Field name made lowercase.
    key = models.CharField(db_column='Key', max_length=64)  # Field name made lowercase.
    value = models.TextField(db_column='Value')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ParamLogs'


class Params(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    key = models.CharField(db_column='Key', unique=True, max_length=64)  # Field name made lowercase.
    value = models.TextField(db_column='Value')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Params'


class Paymentflayerdetails(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    paymentflayerid = models.ForeignKey('Paymentflayers', models.DO_NOTHING, db_column='PaymentFlayerId')  # Field name made lowercase.
    conceptid = models.UUIDField(db_column='ConceptId')  # Field name made lowercase.
    royaltyconceptid = models.ForeignKey('Royaltyconcepts', models.DO_NOTHING, db_column='RoyaltyConceptId', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentFlayerDetails'


class Paymentflayerlogs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    paymentflayerid = models.ForeignKey('Paymentflayers', models.DO_NOTHING, db_column='PaymentFlayerId')  # Field name made lowercase.
    statepaymentid = models.ForeignKey('Statepayments', models.DO_NOTHING, db_column='StatePaymentId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentFlayerLogs'


class Paymentflayernotes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    paymentflayerid = models.ForeignKey('Paymentflayers', models.DO_NOTHING, db_column='PaymentFlayerId')  # Field name made lowercase.
    royaltynoteid = models.ForeignKey('Royaltynotes', models.DO_NOTHING, db_column='RoyaltyNoteId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentFlayerNotes'


class Paymentflayers(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    statepaymentid = models.ForeignKey('Statepayments', models.DO_NOTHING, db_column='StatePaymentId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surcharge = models.DecimalField(db_column='Surcharge', max_digits=24, decimal_places=8)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    royaltyconceptid = models.ForeignKey('Royaltyconcepts', models.DO_NOTHING, db_column='RoyaltyConceptId')  # Field name made lowercase.
    royaltyddjjid = models.ForeignKey('Royaltyddjjs', models.DO_NOTHING, db_column='RoyaltyDDJJId')  # Field name made lowercase.
    informedpaymentamount = models.DecimalField(db_column='InformedPaymentAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    informedpaymentdate = models.DateTimeField(db_column='InformedPaymentDate')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    observation = models.CharField(db_column='Observation', max_length=512, blank=True, null=True)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=24, decimal_places=8)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', max_length=128, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.UUIDField(db_column='TransactionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentFlayers'


class Payments(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    paymentflayerid = models.ForeignKey(Paymentflayers, models.DO_NOTHING, db_column='PaymentFlayerId')  # Field name made lowercase.
    statepaymentid = models.ForeignKey('Statepayments', models.DO_NOTHING, db_column='StatePaymentId')  # Field name made lowercase.
    totalinformedamount = models.DecimalField(db_column='TotalInformedAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payments'


class People(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    cuil = models.CharField(db_column='Cuil', max_length=16)  # Field name made lowercase.
    dni = models.CharField(db_column='Dni', max_length=16)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=128)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='Birthdate')  # Field name made lowercase.
    genderid = models.ForeignKey(Genders, models.DO_NOTHING, db_column='GenderId')  # Field name made lowercase.
    nationalityid = models.ForeignKey(Nationalities, models.DO_NOTHING, db_column='NationalityId', blank=True, null=True)  # Field name made lowercase.
    zoneid = models.ForeignKey('Zones', models.DO_NOTHING, db_column='ZoneId', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    hasdisability = models.BooleanField(db_column='HasDisability')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'People'


class Periodgroups(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeriodGroups'


class Periods(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Periods'


class Permissions(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=128)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)  # Field name made lowercase.
    ordering = models.IntegerField(db_column='Ordering')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Permissions'


class Plantcoordinates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    plantid = models.ForeignKey('Plants', models.DO_NOTHING, db_column='PlantId')  # Field name made lowercase.
    zoneid = models.ForeignKey('Zones', models.DO_NOTHING, db_column='ZoneId')  # Field name made lowercase.
    east = models.CharField(db_column='East', max_length=30)  # Field name made lowercase.
    west = models.CharField(db_column='West', max_length=30)  # Field name made lowercase.
    altitude = models.CharField(db_column='Altitude', max_length=30)  # Field name made lowercase.
    occupiedarea = models.DecimalField(db_column='OccupiedArea', max_digits=12, decimal_places=2)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    lat = models.DecimalField(db_column='Lat', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    lng = models.DecimalField(db_column='Lng', max_digits=65535, decimal_places=65535)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlantCoordinates'


class Plantdeclaredminerals(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    plantid = models.ForeignKey('Plants', models.DO_NOTHING, db_column='PlantId')  # Field name made lowercase.
    depositplantmineralid = models.ForeignKey(Depositplantminerals, models.DO_NOTHING, db_column='DepositPlantMineralId')  # Field name made lowercase.
    otherdescription = models.CharField(db_column='OtherDescription', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlantDeclaredMinerals'


class Plantmaterials(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    plantid = models.ForeignKey('Plants', models.DO_NOTHING, db_column='PlantId')  # Field name made lowercase.
    materialid = models.ForeignKey(Materials, models.DO_NOTHING, db_column='MaterialId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlantMaterials'


class Plantminerals(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    plantid = models.ForeignKey('Plants', models.DO_NOTHING, db_column='PlantId')  # Field name made lowercase.
    mineralid = models.ForeignKey(Minerals, models.DO_NOTHING, db_column='MineralId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlantMinerals'


class Plantproductionelements(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    plantproductionid = models.ForeignKey('Plantproductions', models.DO_NOTHING, db_column='PlantProductionId')  # Field name made lowercase.
    elementid = models.ForeignKey(Elements, models.DO_NOTHING, db_column='ElementId')  # Field name made lowercase.
    lawunitid = models.ForeignKey(Measurementunits, models.DO_NOTHING, db_column='LawUnitId')  # Field name made lowercase.
    lawqty = models.DecimalField(db_column='LawQty', max_digits=24, decimal_places=8)  # Field name made lowercase.
    finecontentunitid = models.ForeignKey(Measurementunits, models.DO_NOTHING, db_column='FineContentUnitId', related_name='plantproductionelements_finecontentunitid_set')  # Field name made lowercase.
    finecontentqty = models.DecimalField(db_column='FineContentQty', max_digits=18, decimal_places=6)  # Field name made lowercase.
    stock = models.DecimalField(db_column='Stock', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    qtyinkg = models.DecimalField(db_column='QtyInKg', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    qtyinoz = models.DecimalField(db_column='QtyInOz', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    avgfinecontentqty = models.DecimalField(db_column='AvgFineContentQty', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    avgfinecontentunitid = models.ForeignKey(Measurementunits, models.DO_NOTHING, db_column='AvgFineContentUnitId', related_name='plantproductionelements_avgfinecontentunitid_set', blank=True, null=True)  # Field name made lowercase.
    avglawqty = models.DecimalField(db_column='AvgLawQty', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    avglawunitid = models.ForeignKey(Measurementunits, models.DO_NOTHING, db_column='AvgLawUnitId', related_name='plantproductionelements_avglawunitid_set', blank=True, null=True)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    quantityunitid = models.ForeignKey(Measurementunits, models.DO_NOTHING, db_column='QuantityUnitId', related_name='plantproductionelements_quantityunitid_set', blank=True, null=True)  # Field name made lowercase.
    vnrprice = models.DecimalField(db_column='VNRPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    vnrtotal = models.DecimalField(db_column='VNRTotal', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlantProductionElements'


class Plantproductions(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    plantdeclaredmineralid = models.ForeignKey(Plantdeclaredminerals, models.DO_NOTHING, db_column='PlantDeclaredMineralId')  # Field name made lowercase.
    measurementunitid = models.ForeignKey(Measurementunits, models.DO_NOTHING, db_column='MeasurementUnitId', blank=True, null=True)  # Field name made lowercase.
    producedqty = models.DecimalField(db_column='ProducedQty', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    producedqtyinoz = models.DecimalField(db_column='ProducedQtyInOz', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    producedqtyinkg = models.DecimalField(db_column='ProducedQtyInKg', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    internalmarketsoldqty = models.DecimalField(db_column='InternalMarketSoldQty', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    internalmarketsoldqtyinoz = models.DecimalField(db_column='InternalMarketSoldQtyInOz', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    internalmarketsoldqtyinkg = models.DecimalField(db_column='InternalMarketSoldQtyInKg', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    internalmarketsoldamount = models.DecimalField(db_column='InternalMarketSoldAmount', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketsoldqty = models.DecimalField(db_column='ExternalMarketSoldQty', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketsoldqtyinoz = models.DecimalField(db_column='ExternalMarketSoldQtyInOz', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketsoldqtyinkg = models.DecimalField(db_column='ExternalMarketSoldQtyInKg', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketsoldamount = models.DecimalField(db_column='ExternalMarketSoldAmount', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketsoldamountusd = models.DecimalField(db_column='ExternalMarketSoldAmountUsd', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    ncmcode = models.CharField(db_column='NcmCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ncmdesc = models.CharField(db_column='NcmDesc', max_length=256, blank=True, null=True)  # Field name made lowercase.
    transferredqty = models.DecimalField(db_column='TransferredQty', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferredqtyinoz = models.DecimalField(db_column='TransferredQtyInOz', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferredqtyinkg = models.DecimalField(db_column='TransferredQtyInKg', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    transferredamount = models.DecimalField(db_column='TransferredAmount', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    initialstock = models.DecimalField(db_column='InitialStock', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    finalstock = models.DecimalField(db_column='FinalStock', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    declaredprice = models.DecimalField(db_column='DeclaredPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketdeclaredprice = models.DecimalField(db_column='ExternalMarketDeclaredPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    externalmarketvnr = models.DecimalField(db_column='ExternalMarketVNR', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    internalmarketdeclaredprice = models.DecimalField(db_column='InternalMarketDeclaredPrice', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    internalmarketvnr = models.DecimalField(db_column='InternalMarketVNR', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    vnr = models.DecimalField(db_column='VNR', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlantProductions'


class Planttypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlantTypes'


class Plants(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    planttypeid = models.ForeignKey(Planttypes, models.DO_NOTHING, db_column='PlantTypeId')  # Field name made lowercase.
    presentationid = models.ForeignKey('Presentations', models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    materialid = models.ForeignKey(Materials, models.DO_NOTHING, db_column='MaterialId', blank=True, null=True)  # Field name made lowercase.
    destinationid = models.ForeignKey(Destinations, models.DO_NOTHING, db_column='DestinationId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Plants'


class Precomnatcommunities(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    presentationcommitmentid = models.ForeignKey('Presentationcommitments', models.DO_NOTHING, db_column='PresentationCommitmentId')  # Field name made lowercase.
    nativecommunityid = models.ForeignKey(Nativecommunities, models.DO_NOTHING, db_column='NativeCommunityId')  # Field name made lowercase.
    other = models.CharField(db_column='Other', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PreComNatCommunities'


class Preliminarypaymentstates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PreliminaryPaymentStates'


class Preliminarypayments(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    cuit = models.CharField(db_column='Cuit', max_length=64)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    preliminarypaymentstateid = models.ForeignKey(Preliminarypaymentstates, models.DO_NOTHING, db_column='PreliminaryPaymentStateId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paid = models.DecimalField(db_column='Paid', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', max_length=128, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.UUIDField(db_column='TransactionId', blank=True, null=True)  # Field name made lowercase.
    expedientid = models.ForeignKey(Expedients, models.DO_NOTHING, db_column='ExpedientId', blank=True, null=True)  # Field name made lowercase.
    vepid = models.ForeignKey('Veps', models.DO_NOTHING, db_column='VepId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PreliminaryPayments'


class Presentationcommitments(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    presentationid = models.ForeignKey('Presentations', models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    commitmenttypeid = models.ForeignKey(Commitmenttypes, models.DO_NOTHING, db_column='CommitmentTypeId')  # Field name made lowercase.
    nativecommunityid = models.ForeignKey(Nativecommunities, models.DO_NOTHING, db_column='NativeCommunityId', blank=True, null=True)  # Field name made lowercase.
    zoneid = models.ForeignKey('Zones', models.DO_NOTHING, db_column='ZoneId')  # Field name made lowercase.
    beneficiarytypeid = models.ForeignKey(Beneficiarytypes, models.DO_NOTHING, db_column='BeneficiaryTypeId')  # Field name made lowercase.
    investmentareaid = models.ForeignKey(Investmentareas, models.DO_NOTHING, db_column='InvestmentAreaId')  # Field name made lowercase.
    commitmentstateid = models.ForeignKey(Commitmentstates, models.DO_NOTHING, db_column='CommitmentStateId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    beneficiariesnumber = models.IntegerField(db_column='BeneficiariesNumber')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    investmentamount = models.DecimalField(db_column='InvestmentAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    otherbeneficiarytype = models.CharField(db_column='OtherBeneficiaryType', max_length=128, blank=True, null=True)  # Field name made lowercase.
    otherinvestmentarea = models.CharField(db_column='OtherInvestmentArea', max_length=128, blank=True, null=True)  # Field name made lowercase.
    othercommitmenttype = models.CharField(db_column='OtherCommitmentType', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresentationCommitments'


class Presentationcontractors(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    presentationid = models.ForeignKey('Presentations', models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    contractorid = models.ForeignKey(Contractors, models.DO_NOTHING, db_column='ContractorId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresentationContractors'


class Presentationemployees(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    presentationid = models.ForeignKey('Presentations', models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EmployeeId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresentationEmployees'


class Presentationinvestments(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    presentationid = models.ForeignKey('Presentations', models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    investmentid = models.ForeignKey(Investments, models.DO_NOTHING, db_column='InvestmentId')  # Field name made lowercase.
    investmenttypeid = models.ForeignKey(Investmenttypes, models.DO_NOTHING, db_column='InvestmentTypeId', blank=True, null=True)  # Field name made lowercase.
    investmentamount = models.DecimalField(db_column='InvestmentAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    nextperiodinvestment = models.DecimalField(db_column='NextPeriodInvestment', max_digits=24, decimal_places=8)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    investmentlocationid = models.ForeignKey(Investmentlocations, models.DO_NOTHING, db_column='InvestmentLocationId')  # Field name made lowercase.
    otherinvestmentlocation = models.CharField(db_column='OtherInvestmentLocation', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresentationInvestments'


class Presentationlogs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    logtypeid = models.ForeignKey(Logtypes, models.DO_NOTHING, db_column='LogTypeId')  # Field name made lowercase.
    presentationid = models.ForeignKey('Presentations', models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    observations = models.CharField(db_column='Observations', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresentationLogs'


class Presentationnorms(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    presentationid = models.ForeignKey('Presentations', models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    normid = models.ForeignKey(Norms, models.DO_NOTHING, db_column='NormId')  # Field name made lowercase.
    normstateid = models.ForeignKey(Normstates, models.DO_NOTHING, db_column='NormStateId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    certgrantdate = models.DateTimeField(db_column='CertGrantDate', blank=True, null=True)  # Field name made lowercase.
    othernorm = models.CharField(db_column='OtherNorm', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresentationNorms'


class Presentationproductions(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    presentationid = models.ForeignKey('Presentations', models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    productionid = models.ForeignKey('Productions', models.DO_NOTHING, db_column='ProductionId')  # Field name made lowercase.
    oreextraction = models.IntegerField(db_column='OreExtraction')  # Field name made lowercase.
    oreunitid = models.ForeignKey('Units', models.DO_NOTHING, db_column='OreUnitId')  # Field name made lowercase.
    averageoreextraction = models.DecimalField(db_column='AverageOreExtraction', max_digits=24, decimal_places=8)  # Field name made lowercase.
    averageoreunitid = models.ForeignKey(Averageunits, models.DO_NOTHING, db_column='AverageOreUnitId')  # Field name made lowercase.
    processedore = models.IntegerField(db_column='ProcessedOre')  # Field name made lowercase.
    processedoreunitid = models.ForeignKey('Units', models.DO_NOTHING, db_column='ProcessedOreUnitId', related_name='presentationproductions_processedoreunitid_set')  # Field name made lowercase.
    averageprocessedore = models.DecimalField(db_column='AverageProcessedOre', max_digits=24, decimal_places=8)  # Field name made lowercase.
    averageprocessedoreunitid = models.ForeignKey(Averageunits, models.DO_NOTHING, db_column='AverageProcessedOreUnitId', related_name='presentationproductions_averageprocessedoreunitid_set')  # Field name made lowercase.
    productionvalue = models.DecimalField(db_column='ProductionValue', max_digits=24, decimal_places=8)  # Field name made lowercase.
    productionunitid = models.ForeignKey('Units', models.DO_NOTHING, db_column='ProductionUnitId', related_name='presentationproductions_productionunitid_set')  # Field name made lowercase.
    initialstock = models.DecimalField(db_column='InitialStock', max_digits=24, decimal_places=8)  # Field name made lowercase.
    productionsold = models.DecimalField(db_column='ProductionSold', max_digits=24, decimal_places=8)  # Field name made lowercase.
    finalstock = models.DecimalField(db_column='FinalStock', max_digits=24, decimal_places=8)  # Field name made lowercase.
    totalbilling = models.DecimalField(db_column='TotalBilling', max_digits=24, decimal_places=8)  # Field name made lowercase.
    unitcostamount = models.DecimalField(db_column='UnitCostAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    unitcostid = models.ForeignKey('Unitcosts', models.DO_NOTHING, db_column='UnitCostId')  # Field name made lowercase.
    estimatedproduction = models.DecimalField(db_column='EstimatedProduction', max_digits=24, decimal_places=8)  # Field name made lowercase.
    estimatedproductionunitid = models.ForeignKey('Units', models.DO_NOTHING, db_column='EstimatedProductionUnitId', related_name='presentationproductions_estimatedproductionunitid_set')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresentationProductions'


class Presentationreserves(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    presentationid = models.ForeignKey('Presentations', models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    reservetypeid = models.ForeignKey('Reservetypes', models.DO_NOTHING, db_column='ReserveTypeId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    depositmineralid = models.ForeignKey(Depositminerals, models.DO_NOTHING, db_column='DepositMineralId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresentationReserves'


class Presentationstates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresentationStates'


class Presentationtaxes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    presentationid = models.ForeignKey('Presentations', models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    taxid = models.ForeignKey('Taxes', models.DO_NOTHING, db_column='TaxId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresentationTaxes'


class Presentations(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    projectid = models.ForeignKey('Projects', models.DO_NOTHING, db_column='ProjectId')  # Field name made lowercase.
    periodid = models.ForeignKey(Periods, models.DO_NOTHING, db_column='PeriodId')  # Field name made lowercase.
    presentationstateid = models.ForeignKey(Presentationstates, models.DO_NOTHING, db_column='PresentationStateId')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    clonedfromid = models.ForeignKey('self', models.DO_NOTHING, db_column='ClonedFromId', blank=True, null=True)  # Field name made lowercase.
    isrectification = models.BooleanField(db_column='IsRectification')  # Field name made lowercase.
    confirmedproduction = models.BooleanField(db_column='ConfirmedProduction')  # Field name made lowercase.
    lastpresented = models.BooleanField(db_column='LastPresented')  # Field name made lowercase.
    presentationdate = models.DateTimeField(db_column='PresentationDate', blank=True, null=True)  # Field name made lowercase.
    lastproductionpresented = models.BooleanField(db_column='LastProductionPresented')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Presentations'


class Productionsales(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    presentationid = models.ForeignKey(Presentations, models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    productionid = models.ForeignKey('Productions', models.DO_NOTHING, db_column='ProductionId')  # Field name made lowercase.
    marketid = models.ForeignKey(Markets, models.DO_NOTHING, db_column='MarketId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductionSales'


class Productiontypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductionTypes'


class Productions(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    productiontypeid = models.ForeignKey(Productiontypes, models.DO_NOTHING, db_column='ProductionTypeId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    plantid = models.ForeignKey(Plants, models.DO_NOTHING, db_column='PlantId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Productions'


class Projectcycles(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProjectCycles'


class Projectstates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProjectStates'


class Projects(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    zoneid = models.ForeignKey('Zones', models.DO_NOTHING, db_column='ZoneId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    createdyear = models.CharField(db_column='CreatedYear', max_length=64)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    projectstateid = models.ForeignKey(Projectstates, models.DO_NOTHING, db_column='ProjectStateId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Projects'


class Regconcepttypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RegConceptTypes'


class Reservetypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReserveTypes'


class Reserves(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    presentationreserveid = models.ForeignKey(Presentationreserves, models.DO_NOTHING, db_column='PresentationReserveId')  # Field name made lowercase.
    elementid = models.ForeignKey(Elements, models.DO_NOTHING, db_column='ElementId', blank=True, null=True)  # Field name made lowercase.
    tonnage = models.DecimalField(db_column='Tonnage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    tonnageunitid = models.ForeignKey(Measurementunits, models.DO_NOTHING, db_column='TonnageUnitId')  # Field name made lowercase.
    averagetonnage = models.DecimalField(db_column='AverageTonnage', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    averageunitid = models.ForeignKey(Measurementunits, models.DO_NOTHING, db_column='AverageUnitId', related_name='reserves_averageunitid_set', blank=True, null=True)  # Field name made lowercase.
    finecontent = models.DecimalField(db_column='FineContent', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    finecontentunitid = models.ForeignKey(Measurementunits, models.DO_NOTHING, db_column='FineContentUnitId', related_name='reserves_finecontentunitid_set', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    qtyinkg = models.DecimalField(db_column='QtyInKg', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    qtyinoz = models.DecimalField(db_column='QtyInOz', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reserves'


class Responsibles(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    license = models.CharField(db_column='License', max_length=20)  # Field name made lowercase.
    board = models.CharField(db_column='Board', max_length=100)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    personid = models.OneToOneField(People, models.DO_NOTHING, db_column='PersonId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Responsibles'


class Rolepermissions(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Roles', models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.
    permissionid = models.ForeignKey(Permissions, models.DO_NOTHING, db_column='PermissionId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RolePermissions'


class Roles(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=128)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Roles'


class Roydistfiftys(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    rentamount = models.DecimalField(db_column='RentAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    royaltydistributionid = models.ForeignKey('Royaltydistributions', models.DO_NOTHING, db_column='RoyaltyDistributionId')  # Field name made lowercase.
    royaltyddjjid = models.ForeignKey('Royaltyddjjs', models.DO_NOTHING, db_column='RoyaltyDDJJId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    municipalityamount = models.DecimalField(db_column='MunicipalityAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    municipalityid = models.ForeignKey(Municipalities, models.DO_NOTHING, db_column='MunicipalityId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyDistFiftys'


class Roydistindexes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    royaltydistributionid = models.ForeignKey('Royaltydistributions', models.DO_NOTHING, db_column='RoyaltyDistributionId')  # Field name made lowercase.
    royaltyindexid = models.ForeignKey('Royaltyindexes', models.DO_NOTHING, db_column='RoyaltyIndexId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    municipalityid = models.ForeignKey(Municipalities, models.DO_NOTHING, db_column='MunicipalityId')  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=16)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyDistIndexes'


class Roydiststates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyDistStates'


class Royaltychangestates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltyddjjid = models.ForeignKey('Royaltyddjjs', models.DO_NOTHING, db_column='RoyaltyDDJJId')  # Field name made lowercase.
    royaltystateid = models.ForeignKey('Royaltystates', models.DO_NOTHING, db_column='RoyaltyStateId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyChangeStates'


class Royaltyconcepts(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyConcepts'


class Royaltycosttypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyCostTypes'


class Royaltycosts(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    royaltycosttypeid = models.ForeignKey(Royaltycosttypes, models.DO_NOTHING, db_column='RoyaltyCostTypeId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyCosts'


class Royaltyddjjexpedients(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltyddjjid = models.ForeignKey('Royaltyddjjs', models.DO_NOTHING, db_column='RoyaltyDDJJId')  # Field name made lowercase.
    expedientid = models.ForeignKey(Expedients, models.DO_NOTHING, db_column='ExpedientId')  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=16)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyDDJJExpedients'


class Royaltyddjjlogs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltyddjjid = models.ForeignKey('Royaltyddjjs', models.DO_NOTHING, db_column='RoyaltyDDJJId')  # Field name made lowercase.
    royaltystateid = models.ForeignKey('Royaltystates', models.DO_NOTHING, db_column='RoyaltyStateId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    isrectified = models.BooleanField(db_column='IsRectified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyDDJJLogs'


class Royaltyddjjs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltyperiodid = models.ForeignKey('Royaltyperiods', models.DO_NOTHING, db_column='RoyaltyPeriodId')  # Field name made lowercase.
    royaltystateid = models.ForeignKey('Royaltystates', models.DO_NOTHING, db_column='RoyaltyStateId')  # Field name made lowercase.
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    royaltyconceptid = models.ForeignKey(Royaltyconcepts, models.DO_NOTHING, db_column='RoyaltyConceptId')  # Field name made lowercase.
    isrectifying = models.BooleanField(db_column='IsRectifying')  # Field name made lowercase.
    royalityddjjrectid = models.ForeignKey('self', models.DO_NOTHING, db_column='RoyalityDDJJRectId', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    lawtype = models.IntegerField(db_column='LawType')  # Field name made lowercase.
    productiontype = models.IntegerField(db_column='ProductionType')  # Field name made lowercase.
    lastpresented = models.BooleanField(db_column='LastPresented')  # Field name made lowercase.
    presentationdate = models.DateTimeField(db_column='PresentationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyDDJJs'


class Royaltydeclaredcosts(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltycostid = models.ForeignKey(Royaltycosts, models.DO_NOTHING, db_column='RoyaltyCostid')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    royaltyddjjid = models.ForeignKey(Royaltyddjjs, models.DO_NOTHING, db_column='RoyaltyDDJJId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyDeclaredCosts'


class Royaltydistributions(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    cutoffdate = models.DateTimeField(db_column='CutoffDate')  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    presentationdate = models.DateTimeField(db_column='PresentationDate', blank=True, null=True)  # Field name made lowercase.
    royaltyperiodid = models.ForeignKey('Royaltyperiods', models.DO_NOTHING, db_column='RoyaltyPeriodId')  # Field name made lowercase.
    roydiststateid = models.ForeignKey(Roydiststates, models.DO_NOTHING, db_column='RoyDistStateId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyDistributions'


class Royaltygendatamuns(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltygeneraldataid = models.ForeignKey('Royaltygeneraldatas', models.DO_NOTHING, db_column='RoyaltyGeneralDataId')  # Field name made lowercase.
    municipalityid = models.ForeignKey(Municipalities, models.DO_NOTHING, db_column='MunicipalityId')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=24, decimal_places=8)  # Field name made lowercase.
    percentage = models.DecimalField(db_column='Percentage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyGenDataMuns'


class Royaltygeneraldatas(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltyddjjid = models.ForeignKey(Royaltyddjjs, models.DO_NOTHING, db_column='RoyaltyDDJJId')  # Field name made lowercase.
    productid = models.CharField(db_column='ProductId', max_length=128)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=128)  # Field name made lowercase.
    producttype = models.IntegerField(db_column='ProductType')  # Field name made lowercase.
    totalprodsold = models.DecimalField(db_column='TotalProdSold', max_digits=24, decimal_places=8)  # Field name made lowercase.
    totalfinalstock = models.DecimalField(db_column='TotalFinalStock', max_digits=24, decimal_places=8)  # Field name made lowercase.
    totalinitialstock = models.DecimalField(db_column='TotalInitialStock', max_digits=24, decimal_places=8)  # Field name made lowercase.
    totalproduction = models.DecimalField(db_column='TotalProduction', max_digits=24, decimal_places=8)  # Field name made lowercase.
    totalprice = models.DecimalField(db_column='TotalPrice', max_digits=24, decimal_places=8)  # Field name made lowercase.
    totalvnr = models.DecimalField(db_column='TotalVNR', max_digits=24, decimal_places=8)  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=24, decimal_places=8)  # Field name made lowercase.
    totalvbm = models.DecimalField(db_column='TotalVBM', max_digits=24, decimal_places=8)  # Field name made lowercase.
    totalroyality = models.DecimalField(db_column='TotalRoyality', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    declaredprodsold = models.DecimalField(db_column='DeclaredProdSold', max_digits=24, decimal_places=8)  # Field name made lowercase.
    declaredproduction = models.DecimalField(db_column='DeclaredProduction', max_digits=24, decimal_places=8)  # Field name made lowercase.
    declaredvnr = models.DecimalField(db_column='DeclaredVNR', max_digits=24, decimal_places=8)  # Field name made lowercase.
    parentid = models.UUIDField(db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    measurementname = models.TextField(db_column='MeasurementName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyGeneralDatas'


class Royaltyindexes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    denomination = models.IntegerField(db_column='Denomination')  # Field name made lowercase.
    municipalityid = models.ForeignKey(Municipalities, models.DO_NOTHING, db_column='MunicipalityId')  # Field name made lowercase.
    firstsecond = models.DecimalField(db_column='FirstSecond', max_digits=24, decimal_places=8)  # Field name made lowercase.
    third = models.DecimalField(db_column='Third', max_digits=24, decimal_places=8)  # Field name made lowercase.
    cbu = models.TextField(db_column='Cbu')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    periodgroupid = models.ForeignKey(Periodgroups, models.DO_NOTHING, db_column='PeriodGroupId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyIndexes'


class Royaltynotetypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyNoteTypes'


class Royaltynotes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    royaltynotetypeid = models.ForeignKey(Royaltynotetypes, models.DO_NOTHING, db_column='RoyaltyNoteTypeId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyNotes'


class Royaltyobservations(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltyddjjid = models.ForeignKey(Royaltyddjjs, models.DO_NOTHING, db_column='RoyaltyDDJJId')  # Field name made lowercase.
    observation = models.CharField(db_column='Observation', max_length=255)  # Field name made lowercase.
    guides = models.IntegerField(db_column='Guides')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyObservations'


class Royaltyperiods(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    isactual = models.BooleanField(db_column='IsActual')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    periodgroupid = models.ForeignKey(Periodgroups, models.DO_NOTHING, db_column='PeriodGroupId')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    presentationdate = models.DateTimeField(db_column='PresentationDate')  # Field name made lowercase.
    cutoffdate = models.DateTimeField(db_column='CutoffDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyPeriods'


class Royaltyproductdatas(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltyddjjid = models.ForeignKey(Royaltyddjjs, models.DO_NOTHING, db_column='RoyaltyDDJJId')  # Field name made lowercase.
    productid = models.CharField(db_column='ProductId', max_length=128)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=128)  # Field name made lowercase.
    producttype = models.IntegerField(db_column='ProductType')  # Field name made lowercase.
    initialstock = models.DecimalField(db_column='InitialStock', max_digits=24, decimal_places=8)  # Field name made lowercase.
    production = models.DecimalField(db_column='Production', max_digits=24, decimal_places=8)  # Field name made lowercase.
    projectid = models.ForeignKey(Projects, models.DO_NOTHING, db_column='ProjectId')  # Field name made lowercase.
    productionsold = models.DecimalField(db_column='ProductionSold', max_digits=24, decimal_places=8)  # Field name made lowercase.
    finalstock = models.DecimalField(db_column='FinalStock', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=24, decimal_places=8)  # Field name made lowercase.
    vnr = models.DecimalField(db_column='VNR', max_digits=24, decimal_places=8)  # Field name made lowercase.
    taxable = models.BooleanField(db_column='Taxable')  # Field name made lowercase.
    unitcostprice = models.DecimalField(db_column='UnitCostPrice', max_digits=24, decimal_places=8)  # Field name made lowercase.
    measurementname = models.TextField(db_column='MeasurementName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyProductDatas'


class Royaltyreceivedvalues(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltyddjjid = models.ForeignKey(Royaltyddjjs, models.DO_NOTHING, db_column='RoyaltyDDJJId')  # Field name made lowercase.
    productid = models.CharField(db_column='ProductId', max_length=128)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=128)  # Field name made lowercase.
    producttype = models.IntegerField(db_column='ProductType')  # Field name made lowercase.
    production = models.DecimalField(db_column='Production', max_digits=24, decimal_places=8)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=24, decimal_places=8)  # Field name made lowercase.
    vnr = models.DecimalField(db_column='VNR', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyReceivedValues'


class Royaltyrelatedmunicipalities(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltygeneraldataid = models.ForeignKey(Royaltygeneraldatas, models.DO_NOTHING, db_column='RoyaltyGeneralDataId')  # Field name made lowercase.
    municipalidadid = models.UUIDField(db_column='MunicipalidadId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    municipalidadname = models.CharField(db_column='MunicipalidadName', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyRelatedMunicipalities'


class Royaltyrelatedpresentations(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltyddjjid = models.ForeignKey(Royaltyddjjs, models.DO_NOTHING, db_column='RoyaltyDDJJId')  # Field name made lowercase.
    presentationid = models.ForeignKey(Presentations, models.DO_NOTHING, db_column='PresentationId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyRelatedPresentations'


class Royaltyrelatedprojects(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    royaltygeneraldataid = models.ForeignKey(Royaltygeneraldatas, models.DO_NOTHING, db_column='RoyaltyGeneralDataId')  # Field name made lowercase.
    projectid = models.ForeignKey(Projects, models.DO_NOTHING, db_column='ProjectId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    projectname = models.CharField(db_column='ProjectName', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyRelatedProjects'


class Royaltystates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoyaltyStates'


class Saledestinations(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    productionsaleid = models.ForeignKey(Productionsales, models.DO_NOTHING, db_column='ProductionSaleId')  # Field name made lowercase.
    zoneid = models.ForeignKey('Zones', models.DO_NOTHING, db_column='ZoneId')  # Field name made lowercase.
    zonetypeid = models.ForeignKey('Zonetypes', models.DO_NOTHING, db_column='ZoneTypeId')  # Field name made lowercase.
    salesquantity = models.IntegerField(db_column='SalesQuantity')  # Field name made lowercase.
    salesamount = models.DecimalField(db_column='SalesAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SaleDestinations'


class Securityparameters(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    sessiontime = models.IntegerField(db_column='SessionTime')  # Field name made lowercase.
    numberlogins = models.IntegerField(db_column='NumberLogins')  # Field name made lowercase.
    mincharacters = models.IntegerField(db_column='MinCharacters')  # Field name made lowercase.
    maxcharacters = models.IntegerField(db_column='MaxCharacters')  # Field name made lowercase.
    includecapitalletter = models.BooleanField(db_column='IncludeCapitalLetter')  # Field name made lowercase.
    includenumbers = models.BooleanField(db_column='IncludeNumbers')  # Field name made lowercase.
    includespecialcharacters = models.BooleanField(db_column='IncludeSpecialCharacters')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SecurityParameters'


class Servresgens(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    generaldataid = models.ForeignKey(Generaldata, models.DO_NOTHING, db_column='GeneralDataId')  # Field name made lowercase.
    responsibleid = models.ForeignKey(Responsibles, models.DO_NOTHING, db_column='ResponsibleId')  # Field name made lowercase.
    serviceid = models.ForeignKey('Services', models.DO_NOTHING, db_column='ServiceId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServResGens'


class Services(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Services'


class Statepayments(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StatePayments'


class Subplantmaterials(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    plantid = models.ForeignKey(Plants, models.DO_NOTHING, db_column='PlantId')  # Field name made lowercase.
    materialid = models.ForeignKey(Materials, models.DO_NOTHING, db_column='MaterialId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubPlantMaterials'


class Suppliertypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SupplierTypes'


class Taxtypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaxTypes'


class Taxes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    taxtypeid = models.ForeignKey(Taxtypes, models.DO_NOTHING, db_column='TaxTypeId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=128)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Taxes'


class Unitcosts(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnitCosts'


class Units(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Units'


class Userlogcategories(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserLogCategories'


class Userlogtypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=60)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    userlogcategoryid = models.ForeignKey(Userlogcategories, models.DO_NOTHING, db_column='UserLogCategoryId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserLogTypes'


class Userlogs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    fromuserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='FromUserId')  # Field name made lowercase.
    touserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='ToUserId', related_name='userlogs_touserid_set', blank=True, null=True)  # Field name made lowercase.
    userlogtypeid = models.ForeignKey(Userlogtypes, models.DO_NOTHING, db_column='UserLogTypeId')  # Field name made lowercase.
    extra = models.TextField(db_column='Extra', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserLogs'


class Users(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    roleid = models.ForeignKey(Roles, models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.
    objectid = models.CharField(db_column='ObjectId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', unique=True, max_length=64)  # Field name made lowercase.
    password = models.BinaryField(db_column='Password')  # Field name made lowercase.
    pin = models.BinaryField(db_column='Pin', blank=True, null=True)  # Field name made lowercase.
    biometric = models.BinaryField(db_column='Biometric', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=64)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='Birthdate', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=128, blank=True, null=True)  # Field name made lowercase.
    phonecountrycode = models.CharField(db_column='PhoneCountryCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    phoneareacode = models.CharField(db_column='PhoneAreaCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=16, blank=True, null=True)  # Field name made lowercase.
    fullphonenumber = models.CharField(db_column='FullPhoneNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    photo = models.CharField(db_column='Photo', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    verified = models.BooleanField(db_column='Verified')  # Field name made lowercase.
    cuildni = models.TextField(db_column='CuilDni', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    retries = models.SmallIntegerField(db_column='Retries')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class Valuationtypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ValuationTypes'


class Vepdetails(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    vepid = models.ForeignKey('Veps', models.DO_NOTHING, db_column='VepId')  # Field name made lowercase.
    canonid = models.ForeignKey(Canons, models.DO_NOTHING, db_column='CanonId')  # Field name made lowercase.
    canonstateid = models.ForeignKey(Canonstates, models.DO_NOTHING, db_column='CanonStateId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surcharge = models.DecimalField(db_column='Surcharge', max_digits=24, decimal_places=8)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paid = models.DecimalField(db_column='Paid', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    surchargepercentage = models.DecimalField(db_column='SurchargePercentage', max_digits=24, decimal_places=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VepDetails'


class Veplogs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    vepid = models.ForeignKey('Veps', models.DO_NOTHING, db_column='VepId')  # Field name made lowercase.
    vepstateid = models.ForeignKey('Vepstates', models.DO_NOTHING, db_column='VepStateId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VepLogs'


class Vepnotes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    vepid = models.ForeignKey('Veps', models.DO_NOTHING, db_column='VepId')  # Field name made lowercase.
    noteid = models.ForeignKey(Notes, models.DO_NOTHING, db_column='NoteId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VepNotes'


class Veppaymentreceipts(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    vepid = models.ForeignKey('Veps', models.DO_NOTHING, db_column='VepId')  # Field name made lowercase.
    fullpath = models.TextField(db_column='FullPath')  # Field name made lowercase.
    relativepath = models.TextField(db_column='RelativePath')  # Field name made lowercase.
    confirmedamount = models.DecimalField(db_column='ConfirmedAmount', max_digits=24, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    receiptdate = models.DateTimeField(db_column='ReceiptDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VepPaymentReceipts'


class Vepstates(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VepStates'


class Veps(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    vepstateid = models.ForeignKey(Vepstates, models.DO_NOTHING, db_column='VepStateId')  # Field name made lowercase.
    linkedvepid = models.ForeignKey('self', models.DO_NOTHING, db_column='LinkedVepId', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='Subtotal', max_digits=24, decimal_places=8)  # Field name made lowercase.
    surcharge = models.DecimalField(db_column='Surcharge', max_digits=24, decimal_places=8)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paid = models.DecimalField(db_column='Paid', max_digits=24, decimal_places=8)  # Field name made lowercase.
    paiddate = models.DateTimeField(db_column='PaidDate', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    surchargepercentage = models.DecimalField(db_column='SurchargePercentage', max_digits=24, decimal_places=8)  # Field name made lowercase.
    observation = models.CharField(db_column='Observation', max_length=256, blank=True, null=True)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=24, decimal_places=8)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', max_length=128, blank=True, null=True)  # Field name made lowercase.
    transactionid = models.UUIDField(db_column='TransactionId', blank=True, null=True)  # Field name made lowercase.
    manuallyverified = models.BooleanField(db_column='ManuallyVerified')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Veps'


class Vouchers(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    paymentid = models.ForeignKey(Payments, models.DO_NOTHING, db_column='PaymentId', blank=True, null=True)  # Field name made lowercase.
    relativepath = models.TextField(db_column='RelativePath')  # Field name made lowercase.
    confirmedamount = models.DecimalField(db_column='ConfirmedAmount', max_digits=24, decimal_places=8)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    fullpath = models.TextField(db_column='FullPath')  # Field name made lowercase.
    paymentflayerid = models.ForeignKey(Paymentflayers, models.DO_NOTHING, db_column='PaymentFlayerId')  # Field name made lowercase.
    receiptdate = models.DateTimeField(db_column='ReceiptDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vouchers'


class Worktypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkTypes'


class Workspaces(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=64)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=256, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Workspaces'


class Zonetypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    name = models.CharField(db_column='Name', unique=True, max_length=128)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZoneTypes'


class Zones(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    autoid = models.CharField(db_column='AutoId',unique=True ,max_length=64)
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    zonetypeid = models.ForeignKey(Zonetypes, models.DO_NOTHING, db_column='ZoneTypeId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=128)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=512, blank=True, null=True)  # Field name made lowercase.
    fullid = models.TextField(db_column='FullId')  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
    geometry = models.TextField(db_column='Geometry', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='DeletedAt', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.CharField(db_column='DeletedBy', max_length=128, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zones'


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'


class RoyaltyPresentationsPayments(models.Model):
    ddjjid = models.UUIDField(db_column='DDJJId')
    vepid = models.UUIDField(db_column='VepId', primary_key=True)
    montopagado = models.DecimalField(db_column='MontoPagado', max_digits=24, decimal_places=8)
    fechavencimiento = models.DateField(db_column='FechaVencimiento')
    fechapago = models.DateTimeField(db_column='FechaPago', null=True)
    aniopago = models.IntegerField(db_column='AnioPago')
    mespago = models.IntegerField(db_column='MesPago')
    mespagotexto = models.CharField(db_column='MesPagoTexto', max_length=32)
    tipopago = models.CharField(db_column='TipoPago', max_length=32)

    class Meta:
        managed = False
        db_table = 'view_royaltypresentationspayments'

class RoyaltyProductionResume(models.Model):
    ddjj_id = models.UUIDField(db_column='DDJJId', primary_key=True)
    prod_id = models.UUIDField(db_column='ProdId')
    producto_id = models.UUIDField(db_column='ProductoId', max_length=50)
    producto = models.TextField(db_column='Producto')
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=18, decimal_places=4)
    measurement_name = models.TextField(db_column='MeasurementName')
    declared_vnr = models.DecimalField(db_column='DeclaredVNR', max_digits=18, decimal_places=2)
    total_vnr = models.DecimalField(db_column='TotalVNR', max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'view_royaltypresentationsproduction'
        verbose_name = 'Resumen Producción Regalías'
        verbose_name_plural = 'Resumen Producción Regalías'