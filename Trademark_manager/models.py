import datetime
from django.core.validators import URLValidator
from django.db import models
from Patent_Trademark_Strings.Trademarks_Act_Form_33_String import Form33StringClass
from Patent_Trademark_Strings.Trademarks_Act_Form_3_String import Form3StringClass
from Patent_Trademark_Strings.Trademarks_Act_Form_22_String import Form22StringClass
from Patent_Trademark_Strings.Trademarks_Act_Form_2_String import Form2StringClass
from Patent_Trademark_Strings.Trademarks_Act_Form_17_String import Form17StringClass
from Patent_Trademark_Strings.Trademarks_Act_Form_12_String import Form12StringClass
from Patent_Trademark_Strings.Trademarks_Act_Form_1_String import Form1StringClass



# Create your models here.
class Form_33_Model(models.Model):
    trademark_number = models.CharField(default='default number', max_length=30)
    trademark_class = models.CharField(default='default class', max_length=30)
    trademark_date = models.DateField(default=datetime.date.today)
    html = models.TextField(default=Form33StringClass(
            trademark_class=trademark_class.get_default(),
            trademark_number=trademark_number.get_default()
            ).form_33_string)

    def save(self, *args, **kwargs):
        self.html = Form33StringClass(
                    trademark_class=self.trademark_class,
                    trademark_number=self.trademark_number
                    ).form_33_string
        super(Form_33_Model, self).save(*args, **kwargs)


class Form_22_Model(models.Model):
    company_name = models.CharField(
                                default='default company_name',
                                max_length=300)
    corporate_law = models.CharField(
                                default='default corporate_law',
                                max_length=300)
    place_of_business = models.CharField(
                                default='default place_of_business',
                                max_length=300)
    trademark_number = models.CharField(
                                default='default number',
                                max_length=30)
    trademark_class = models.CharField(
                                default='default class',
                                 max_length=30)
    name_description_summary = models.CharField(
                                default='default name_description_summary',
                                max_length=300)
    trademark_date = models.DateField(default=datetime.date.today)
    html = models.TextField(default=Form22StringClass(
            company_name.get_default(),
            corporate_law.get_default(),
            place_of_business.get_default(),
            trademark_number.get_default(),
            trademark_class.get_default(),
            name_description_summary.get_default()
            ).form_22_string)

    def save(self, *args, **kwargs):
        self.html = Form22StringClass(
                company_name=self.company_name,
                corporate_law=self.corporate_law,
                place_of_business=self.place_of_business,
                trademark_number=self.trademark_number,
                trademark_class=self.trademark_class,
                name_description_summary=self.name_description_summary
                ).form_22_string
        super(Form_22_Model, self).save(*args, **kwargs)


class Form_17_Model(models.Model):
    company_name = models.CharField(
                                    default='default company_name',
                                    max_length=300)
    corporate_law = models.CharField(
                                    default='default corporate_law',
                                    max_length=300)
    place_of_business = models.CharField(
                                    default='default place_of_business',
                                    max_length=300)
    trademark_number = models.CharField(
                                    default='default number',
                                    max_length=30)
    trademark_class = models.CharField(
                                    default='default class',
                                     max_length=30)
    trademark_date = models.DateField(default=datetime.date.today)
    html = models.TextField(default=Form17StringClass(
            company_name.get_default(),
            corporate_law.get_default(),
            place_of_business.get_default(),
            trademark_number.get_default(),
            trademark_class.get_default()
            ).form_17_string)

    def save(self, *args, **kwargs):
        self.html = Form17StringClass(
                company_name=self.company_name,
                corporate_law=self.corporate_law,
                place_of_business=self.place_of_business,
                trademark_number=self.trademark_number,
                trademark_class=self.trademark_class
                ).form_17_string
        super(Form_17_Model, self).save(*args, **kwargs)


class Form_12_Model(models.Model):
    fee = models.CharField(
                            default='default fee',
                            max_length=300)
    trademark_number = models.CharField(
                                    default='default trademark_number',
                                    max_length=300)
    trademark_class = models.CharField(
                                    default='default trademark_class',
                                    max_length=300)
    address_line_1 = models.CharField(
                                    default='default address_line_1',
                                    max_length=300)
    address_line_2 = models.CharField(
                                    default='default address_line_2',
                                    max_length=300)
    address_line_3 = models.CharField(
                                    default='default address_line_3',
                                    max_length=300)
    trademark_date = models.DateField(default=datetime.date.today)
    html = models.TextField(default=Form12StringClass(
            fee.get_default(),
            trademark_number.get_default(),
            trademark_class.get_default(),
            address_line_1.get_default(),
            address_line_2.get_default(),
            address_line_3.get_default()
            ).form_12_string)

    def save(self, *args, **kwargs):
        self.html = Form12StringClass(
                    fee=self.fee,
                    trademark_number=self.trademark_number,
                    trademark_class=self.trademark_class,
                    address_line_1=self.address_line_1,
                    address_line_2=self.address_line_2,
                    address_line_3=self.address_line_3
                    ).form_12_string
        super(Form_12_Model, self).save(*args, **kwargs)


class Form_3_Model(models.Model):
    image_url = models.URLField(
                default='default/url/string', validators=[URLValidator()])
    html = models.TextField(
                default=Form3StringClass(image_url.get_default())
                .form_3_string)

    def save(self, *args, **kwargs):
        self.html = Form3StringClass(image_url=self.image_url).form_3_string
        super(Form_3_Model, self).save(*args, **kwargs)


class Form_2_Model(models.Model):
    trademark_class = models.CharField(
                             default='default class',
                             max_length=300)
    trademark_law = models.CharField(
                             default='default law',
                             max_length=300)
    business_name = models.CharField(
                             default='default name',
                             max_length=300)
    business_address = models.CharField(
                             default='default address',
                             max_length=300)
    html = models.TextField(default=Form2StringClass(
                    trademark_class=trademark_class.get_default(),
                    trademark_law=trademark_law.get_default(),
                    business_name=business_name.get_default(),
                    business_address=business_address.get_default()
                    ).form_2_string)

    def save(self, *args, **kwargs):
        self.html = Form2StringClass(
                    trademark_class=self.trademark_class,
                    trademark_law=self.trademark_law,
                    business_name=self.business_name,
                    business_address=self.business_address).form_2_string
        super(Form_2_Model, self).save(*args, **kwargs)


class Form_1_Model(models.Model):
    person_name = models.CharField(
                              default='default person name',
                              max_length=300)
    company_name = models.CharField(
                              default='default company_name',
                              max_length=300)
    company_name2 = models.CharField(
                              default='default company_name2',
                              max_length=300)
    corporate_law = models.CharField(
                              default='default corporate_law',
                              max_length=300)
    corporate_law2 = models.CharField(
                              default='default corporate_law2',
                              max_length=300)
    signature = models.CharField(
                              default='default signature',
                              max_length=300)
    html = models.TextField(default=Form1StringClass(
                person_name=person_name.get_default(),
                company_name=company_name.get_default(),
                company_name2=company_name2.get_default(),
                corporate_law=corporate_law.get_default(),
                corporate_law2=corporate_law2.get_default(),
                signature=signature.get_default()).form_1_string)

    def save(self, *args, **kwargs):
        self.html = Form1StringClass(
                    person_name=self.person_name,
                    company_name=self.company_name,
                    company_name2=self.company_name2,
                    corporate_law=self.corporate_law,
                    corporate_law2=self.corporate_law2,
                    signature=self.signature).form_1_string
        super(Form_1_Model, self).save(*args, **kwargs)
