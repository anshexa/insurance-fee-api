from tortoise import Model, fields


class InsuranceFee(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField(null=False)
    cost = fields.DecimalField(max_digits=12, decimal_places=2)  # цифр после запятой 2
    cargo_id = fields.OneToOneField('models.Cargo', related_name='insurance_fee')

    class Meta:
        table = 'insurance_fee'


class Cargo(Model):
    id = fields.IntField(pk=True)
    declared_value = fields.DecimalField(max_digits=12, decimal_places=2)  # цифр после запятой 2
    cargo_type_id = fields.ForeignKeyField('models.CargoType', related_name='cargo')


class CargoType(Model):
    id = fields.IntField(pk=True)
    cargo_type = fields.CharField(max_length=50, null=False, unique=True)

    class Meta:
        table = 'cargo_type'
