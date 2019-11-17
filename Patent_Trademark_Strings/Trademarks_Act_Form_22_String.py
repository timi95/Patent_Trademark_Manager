import datetime


class Form22StringClass():
    def __init__(self,
                company_name,
                corporate_law,
                place_of_business,
                trademark_number,
                trademark_class,
                name_description_summary):
                self.company_name = company_name
                self.corporate_law = corporate_law
                self.place_of_business = place_of_business
                self.trademark_number = trademark_number
                self.trademark_class = trademark_class
                self.name_description_summary = name_description_summary
                self.weekday = datetime.datetime.now().strftime("%A") + " " + datetime.datetime.now().strftime("%d")
                self.month = datetime.datetime.now().strftime("%B")
                self.year = datetime.datetime.now().strftime("%Y")
                self.weekday2 = datetime.datetime.now().strftime("%A") + " " + datetime.datetime.now().strftime("%d")
                self.month2 = datetime.datetime.now().strftime("%B")
                self.year2= datetime.datetime.now().strftime("%Y")
                self.form_22_string = """

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
                    <h2>FORM 22</h2>
                </header>
            </tr>
            <tr >
                <div class="intro letter_margin">
                    <p>
                        Request to enter change of Narne or Description of Registered Proprietor (or Registered <br>
                        User) of Trade Mark upon the Register (Regulations 86 and 102)
                    </p>
                </div>
            </tr>
            <tr>
                <div class="request letter_margin">
                    <p>
                        We <span class="underlined-dot variable1">"""+company_name+"""</span>,<br>
                        a company incorporated in <span class="underlined-dot variable1">"""+corporate_law+"""</span>  <br>
                        carrying on business as manufacturers and merchants at: <span class="underlined-dot variable1">"""+place_of_business+"""</span><br>


                        hereby request that our name(s) and description(s) may be entered in the Register of Trade <br>
                        Marks as proprietor of the Trade Mark(s) No"""+trademark_number+""" registered in Class """+trademark_class+""" <br><br>

                        We are entitled to the said Trade Mark. <br>
                        There has been no change in the actual proprietorship of the said trade Mark, but our name <br>
                        has been formally changed by virtue of certificate of change of name dated """+self.weekday+""" day of <br>
                        """+self.month+""" """+self.year+""" <br><br>

                        The entry at present standing in the Register gives our name and description all as <br>
                        follows:<span class="underlined-dot variable1">"""+name_description_summary+"""</span><br>
                    </p>
                </div>
            </tr>

            <tr>
                <div class="letter_margin">
                    <p>DATED  this <span class="underlined weekday"> """+self.weekday2+"""</span>day of<span class="underlined month"> """+self.month2+"""</span> <span class="underlined year"> """+self.year2+"""</span></p>
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

                        Abuja, Nigeria.
                    </p>
                </div>
            </tr>

            <tr>
                 <div class="letter_margin">
                     <p>*Additional numbers may be given on a signed Schedule on the back of the Form.</p>
                 </div>
            </tr>

            <div class="pagebreak"> </div>
            <tr>
                <span class="additional_number"></span> <br>
                <span class="additional_number2"></span> <br>
                <span class="additional_number3"></span> <br>
            </tr>
        </table>
    </body>
</html>



    """
