import datetime


class Form33StringClass():
    def __init__(self, trademark_number, trademark_class):
        self.trademark_number = trademark_number
        self.trademark_class = trademark_class
        self.day = datetime.datetime.now().strftime("%A") + " " + datetime.datetime.now().strftime("%d")
        self.month = datetime.datetime.now().strftime("%B")
        self.year = datetime.datetime.now().strftime("%Y")
        self.form_33_string = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Trade Marks Act</title>
        <style>
            .letter_margin {
                margin: auto 25%;
                line-height: 25px;
            }
            header{
                text-align: center;
            }
            .intro {
                text-align: center;
                font-style: italic;
            }
            .request{

            }
            .office_address{
                width: 50%;
                margin-left: 10%;
            }
            .address_row{
                display: flex;
                align-items: baseline;
            }

            .re-address_row{
                /* float: right; */
                display: flex;
                justify-content: flex-end;
            }
            .re_address{
                width: 60%;

            }
            .to_registrar{
                display: flex;
                align-items: baseline;
            }

            .registrar_paragraph {
                margin-left: 10%;
            }

            .underlined{
                text-decoration: underline;
            }
            .trademark_class{

            }
            .trademark_number{

            }
        </style>
    </head>
    <body>
        <table>
            <tr>
                <header>
                    <h1>TRADE MARKS ACT</h1>
                    <h2>FORM 33</h2>
                </header>
            </tr>
            <tr >
                <div class="intro letter_margin">
                    <p>
                        Form of Request to the Registrar by a Registered Proprietor or a Registered User of a Trade Mark, or a person  about  to be so registered, to enter, alter, or substitute an Address  for  service  as  part  of  his  Registration (Regulations 15, 82. 86 and 102)
                    </p>
                </div>
            </tr>
            <tr>
                <div class="request letter_margin">
                    <p >

                        Request is made by: <br><br>


                        A company incorporated in <br>

                        Carrying on business as manufacturers and merchants at:<br><br><br>


                        who is about to be registered as/who is the Registered Proprietor of Trade Mark(s)<br> No <span class="underlined trademark_number"> """+ str(trademark_number) +"""</span> registered in Class(es) <span class="underlined trademark_class"> """+str(trademark_class)+"""</span> <br>

                        for the inclusion/addition/alteration/substitution of an address for service in Nigeria in or to <br> the entry thereof so that the address for service in Nigeria may read:
                    </p>
                </div>
            </tr>

            <tr>
                <div class="letter_margin address_row">
                    <span>c/o</span>
                    <p class="office_address">
                                 ALLAN & OGUNKEYE

                        Legal Practitioners

                        Western House (7th Floor)

                        8/10 Broad Street, Lagos, Nigeria

                    </p>
                </div>
                <div class="letter_margin">
                    <p>DATED  this <span class="underlined weekday"> """+self.day+"""th </span> day of <span class="underlined month">""" +self.month+""" </span> <span class="underlined year"> """ +self.year+""" </span></p>
                </div>
            </tr>
            <br><br>
            <tr>
                <div class="letter_margin re-address_row">
                    <div class="">
                        <div>________________________</div>
                        <strong>ALLAN & OGUNKEYE</strong>
                        <p class="re_address">
                            Western House (7th Floor) <br>

                            8/10 Broad Street <br>

                            P.O. Box 51769, Ikoyi <br>

                            Lagos,Nigeria. <br>
                        </p>
                        <strong>AGENT FOR THE APPLICANT</strong>
                    </div>
                </div>
            </tr>

            <tr>
                <div class="letter_margin to_registrar">
                    <span>TO:</span>
                    <p class="registrar_paragraph">
                                  The Registrar of Trade Marks <br>

                                Trade Marks Registry <br>

                        Federal Ministry of Trade & Investment, <br>

                        Abuja, Nigeria. <br>
                    </p>
                </div>
            </tr>

        </table>
    </body>
</html>


"""
