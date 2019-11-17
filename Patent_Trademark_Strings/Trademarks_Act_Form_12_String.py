import datetime


class Form12StringClass():
    def __init__(self,
                 fee,
                 trademark_number,
                 trademark_class,
                 address_line_1,
                 address_line_2,
                 address_line_3):
        self.fee = fee
        self.trademark_number = trademark_number
        self.trademark_class = trademark_class
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.address_line_3 = address_line_3
        self.weekday = (datetime.datetime.now().strftime("%A") + " "
                        + datetime.datetime.now().strftime("%d"))
        self.month = datetime.datetime.now().strftime("%B")
        self.year = datetime.datetime.now().strftime("%Y")
        self.form_12_string = """

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
                width: 100%;

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
            .variable1{

            }
            .variable2{

            }
            @media print {
                .pagebreak {
                    clear: both;
                    page-break-after: always;
                }
            }
        </style>
    </head>
    <body>
        <table>
            <tr>
                <header>
                    <h1>TRADE MARKS ACT</h1>
                    <h2>FORM 12</h2>
                </header>
            </tr>
            <tr >
                <div class="intro letter_margin">
                    <p>
                        Renewal of Registration of Trade Mark (Regulation 66)
                    </p>
                </div>
            </tr>
            <tr>
                <div class="request letter_margin">
                    <p>
                        We, ALLAN & OGUNKEYE, Legal Practitioners of Western House (7 th Floor), 8/10 Broad <br>
                        Street, Lagos hereby leave the prescribed fee of N<span class="underlined variable1"> """+fee+"""</span> for Renewal of Registration <br>
                        of the Trade Mark No. <span class="underlined variable1"> """+trademark_number+"""</span> in Class <span class="underlined variable1"> """+trademark_class+"""</span> which we are directed by the <br>
                        proprietor of the Trade Mark, that is to say by: <br><br>
                        to pay.*
                    </p>
                </div>
            </tr>

            <tr>
                <div class="letter_margin">
                    <p>DATED  this <span class="underlined weekday"> """+self.weekday+"""</span>day of<span class="underlined month"> """+self.month+"""</span> <span class="underlined year"> """+self.year+"""</span></p>
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
                        <strong>APPLICANT’S AGENT</strong>
                    </div>
                </div>
            </tr>
            <tr >
                <div class="intro ">
                    <p>
                        The Statement on the back of this Form must be filled in, and signed.
                    </p>
                </div>
            </tr>
            <tr>
                <div class="letter_margin to_registrar">
                    <p class="">
                        To:<br>
                        The Registrar of Trade Marks ,<br>
                        Federal Ministry of Trade and Investment,<br>
                        Abuja, Nigeria.
                    </p>
                </div>
            </tr>

            <div class="pagebreak"> </div>
            <hr>

            <tr >
                <div class="intro ">
                    <p>
                        (To appear on back of the Form)
                    </p>
                </div>
            </tr>
            <tr>
                <div class="letter_margin">
                    <p>
                        The Registrar is requested to send notice of renewal of the Registration to the Registered <br>
                        Proprietor at the following address:<br>
                    </p>
                </div>
            </tr>
            <tr>
                <div class="letter_margin re-address_row">
                        <div class="">
                            <span class="variable2">"""+address_line_1+"""1</span><br><br>
                            <span class="variable2">"""+address_line_2+"""</span><br><br>
                            <span class="variable2">"""+address_line_3+"""</span><br><br>
                        </div>
                </div>
            </tr>
            <tr>
                <div class="letter_margin">
                    <p>DATED  this <span class="underlined weekday"> """+self.weekday+"""</span>day of<span class="underlined month"> """+self.month+"""
                    </span> <span class="underlined year"> """+self.year+"""</span></p>
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
                        <strong>APPLICANT’S AGENT</strong>
                    </div>
                </div>
            </tr>
        </table>
    </body>
</html>



    """
