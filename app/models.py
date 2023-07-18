from tortoise import Model, fields


class InsuranceFee(Model):
    id = fields.IntField(pk=True)
    cost = fields.DecimalField(max_digits=12, decimal_places=2)  # цифр после запятой 2
    cargo = fields.OneToOneField('models.Cargo', related_name='insurance_fee')  # tortoise к полю _id допишет: cargo_id

    class Meta:
        table = 'insurance_fee'  # задаем название таблицы


class Cargo(Model):
    id = fields.IntField(pk=True)
    declared_value = fields.DecimalField(max_digits=12, decimal_places=2)  # цифр после запятой 2
    cargo_type = fields.CharField(max_length=50, null=False)
    date = fields.DateField(null=False)
