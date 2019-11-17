# Generated by Django 2.2.2 on 2019-11-08 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trademark_manager', '0003_auto_20191108_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form_12_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.CharField(default='default fee', max_length=300)),
                ('trademark_number', models.CharField(default='default trademark_number', max_length=300)),
                ('trademark_class', models.CharField(default='default trademark_class', max_length=300)),
                ('address_line_1', models.CharField(default='default address_line_1', max_length=300)),
                ('address_line_2', models.CharField(default='default address_line_2', max_length=300)),
                ('address_line_3', models.CharField(default='default address_line_3', max_length=300)),
                ('trademark_date', models.DateField(default=datetime.date.today)),
                ('html', models.TextField(default='\n\n<!DOCTYPE html>\n<html lang="en" dir="ltr">\n    <head>\n        <meta charset="utf-8">\n        <title>Trade Marks Act</title>\n        <style>\n            .letter_margin {\n                margin: auto 25%;\n                line-height: 25px;\n            }\n            header{\n                text-align: center;\n            }\n            .intro {\n                text-align: center;\n                font-style: italic;\n            }\n            .request{\n\n            }\n            .office_address{\n                width: 50%;\n                margin-left: 10%;\n            }\n            .address_row{\n                display: flex;\n                align-items: baseline;\n            }\n\n            .re-address_row{\n                /* float: right; */\n                display: flex;\n                justify-content: flex-end;\n            }\n            .re_address{\n                width: 100%;\n\n            }\n            .to_registrar{\n                display: flex;\n                align-items: baseline;\n            }\n\n            .registrar_paragraph {\n                margin-left: 10%;\n            }\n\n            .underlined{\n                text-decoration: underline;\n            }\n            .variable1{\n\n            }\n            .variable2{\n\n            }\n            @media print {\n                .pagebreak {\n                    clear: both;\n                    page-break-after: always;\n                }\n            }\n        </style>\n    </head>\n    <body>\n        <table>\n            <tr>\n                <header>\n                    <h1>TRADE MARKS ACT</h1>\n                    <h2>FORM 12</h2>\n                </header>\n            </tr>\n            <tr >\n                <div class="intro letter_margin">\n                    <p>\n                        Renewal of Registration of Trade Mark (Regulation 66)\n                    </p>\n                </div>\n            </tr>\n            <tr>\n                <div class="request letter_margin">\n                    <p>\n                        We, ALLAN & OGUNKEYE, Legal Practitioners of Western House (7 th Floor), 8/10 Broad <br>\n                        Street, Lagos hereby leave the prescribed fee of N<span class="underlined variable1"> default fee</span> for Renewal of Registration <br>\n                        of the Trade Mark No. <span class="underlined variable1"> default trademark_number</span> in Class <span class="underlined variable1"> default trademark_class</span> which we are directed by the <br>\n                        proprietor of the Trade Mark, that is to say by: <br><br>\n                        to pay.*\n                    </p>\n                </div>\n            </tr>\n\n            <tr>\n                <div class="letter_margin">\n                    <p>DATED  this <span class="underlined weekday"> Friday 08</span>day of<span class="underlined month"> November</span> <span class="underlined year"> 2019</span></p>\n                </div>\n            </tr>\n            <br><br>\n            <tr>\n                <div class="letter_margin re-address_row">\n                    <div class="">\n                        <div>________________________</div>\n                        <strong>ALLAN & OGUNKEYE</strong>\n                        <p class="re_address">\n                            Western House (7th Floor) <br>\n\n                            8/10 Broad Street <br>\n\n                            P.O. Box 51769, Ikoyi <br>\n\n                            Lagos,Nigeria. <br>\n                        </p>\n                        <strong>APPLICANT’S AGENT</strong>\n                    </div>\n                </div>\n            </tr>\n            <tr >\n                <div class="intro ">\n                    <p>\n                        The Statement on the back of this Form must be filled in, and signed.\n                    </p>\n                </div>\n            </tr>\n            <tr>\n                <div class="letter_margin to_registrar">\n                    <p class="">\n                        To:<br>\n                        The Registrar of Trade Marks ,<br>\n                        Federal Ministry of Trade and Investment,<br>\n                        Abuja, Nigeria.\n                    </p>\n                </div>\n            </tr>\n\n            <div class="pagebreak"> </div>\n            <hr>\n\n            <tr >\n                <div class="intro ">\n                    <p>\n                        (To appear on back of the Form)\n                    </p>\n                </div>\n            </tr>\n            <tr>\n                <div class="letter_margin">\n                    <p>\n                        The Registrar is requested to send notice of renewal of the Registration to the Registered <br>\n                        Proprietor at the following address:<br>\n                    </p>\n                </div>\n            </tr>\n            <tr>\n                <div class="letter_margin re-address_row">\n                        <div class="">\n                            <span class="variable2">default address_line_11</span><br><br>\n                            <span class="variable2">default address_line_2</span><br><br>\n                            <span class="variable2">default address_line_3</span><br><br>\n                        </div>\n                </div>\n            </tr>\n            <tr>\n                <div class="letter_margin">\n                    <p>DATED  this <span class="underlined weekday"> Friday 08</span>day of<span class="underlined month"> November\n                    </span> <span class="underlined year"> 2019</span></p>\n                </div>\n            </tr>\n            <br><br>\n            <tr>\n                <div class="letter_margin re-address_row">\n                    <div class="">\n                        <div>________________________</div>\n                        <strong>ALLAN & OGUNKEYE</strong>\n                        <p class="re_address">\n                            Western House (7th Floor) <br>\n\n                            8/10 Broad Street <br>\n\n                            P.O. Box 51769, Ikoyi <br>\n\n                            Lagos,Nigeria. <br>\n                        </p>\n                        <strong>APPLICANT’S AGENT</strong>\n                    </div>\n                </div>\n            </tr>\n        </table>\n    </body>\n</html>\n\n\n\n    ')),
            ],
        ),
    ]
