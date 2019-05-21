from wtforms import fields, Form

class PackageDimensionsForm(Form):
    height = fields.IntegerField()
    weight = fields.IntegerField()
    length = fields.IntegerField()
    width = fields.IntegerField()


class MyRadioField(fields.RadioField):
    def pre_validate(self, form):
        pass

class BaseProductForm(Form):
    product_id = fields.StringField(_name='id')

    active = fields.BooleanField()
    attributes = fields.FieldList(fields.StringField(), min_entries=1, max_entries=5)
    caption = fields.StringField()
    deactivate_on = fields.DateField()
    description = fields.TextAreaField()
    images = fields.MultipleFileField()
    livemode = fields.BooleanField()
    product_metadata =fields.TextAreaField(_name='metadata')
    name = fields.StringField()
    package_dimensions = fields.FormField(PackageDimensionsForm)
    shippable = fields.BooleanField()
    product_type = MyRadioField(choices=[('service', 'service'), ('good','good')])
    url = fields.StringField()

