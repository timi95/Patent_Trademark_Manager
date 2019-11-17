import datetime

class Form17StringClass():
    def __init__(self,
                company_name,
                corporate_law,
                place_of_business,
                trademark_number,
                trademark_class):
                self.company_name = company_name
                self.corporate_law = corporate_law
                self.place_of_business = place_of_business
                self.trademark_number = trademark_number
                self.trademark_class = trademark_class
                self.weekday = (datetime.datetime.now().strftime("%A") + " "
                                + datetime.datetime.now().strftime("%d"))
                self.month = datetime.datetime.now().strftime("%B")
                self.year = datetime.datetime.now().strftime("%Y")
                self.weekday2 = (datetime.datetime.now().strftime("%A") + " "
                                 + datetime.datetime.now().strftime("%d"))
                self.month2 = datetime.datetime.now().strftime("%B")
                self.year2 = datetime.datetime.now().strftime("%Y")
                self.weekday3 = (datetime.datetime.now().strftime("%A") + " "
                                 + datetime.datetime.now().strftime("%d"))
                self.month3 = datetime.datetime.now().strftime("%B")
                self.year3 = datetime.datetime.now().strftime("%Y")
                self.form_17_string = """

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
                    <h2>FORM 17</h2>
                </header>
            </tr>
            <tr >
                <div class="intro letter_margin">
                    <p>
                        Request to the Registrar to register a subsequent Proprietor of a Trade Mark or Trade Marks
                        upon the same devolution of title (Regulation 74)
                    </p>
                </div>
            </tr>
            <tr>
                <div class="request letter_margin">
                    <p>
                        We <span class="underlined variable1"> """+company_name+"""</span>,<br>
                        are a company incorporated under the laws of <span class="underlined variable1"> """+corporate_law+"""</span> and carrying on <br>
                        business as manufacturers and merchants at <span class="underlined variable1"> """+place_of_business+"""</span> <br>
                        hereby request that our name may be entered in the Register of Trade Marks as Proprietor <br>
                        of Trade Mark(s) No.<span class="underlined variable1"> """+trademark_number+"""</span>*In Class <span class="underlined variable1"> """+trademark_class+"""</span> <br>
                        as from the <span class="underlined variable1"> """+self.weekday+"""</span> day of <span class="underlined variable1"> """+self.month+"""</span> 20<span class="underlined variable1"> """+self.year+"""</span> <br>
                        We are entitled to the Trade Mark(s) by virtue of Assignment Agreement/Instrument of<br>
                        Merger dated <span class="underlined variable1"> """+self.weekday2+"""</span> day of <span class="underlined variable1"> """+self.month2+"""</span> 20<span class="underlined variable1"> """+self.year2+"""</span><br>
                        The trade mark at the time of assignment was used in a business in the goods in question, and<br>
                        the assignment did not take place on or after the commencement of the Act otherwise than in<br>
                        connection with the goodwill of a business in the goods.<br>
                    </p>
                </div>
            </tr>

            <tr>
                <div class="letter_margin">
                    <p>DATED  this <span class="underlined weekday"> """+self.weekday3+"""</span>day of<span class="underlined month"> """+self.month3+"""</span> <span class="underlined year"> """+self.year3+"""</span></p>
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
                    <p class="">
                        To:<br>
                        The Registrar of Trade Marks ,<br>
                        Federal Ministry of Trade and Investment,<br>
                        Abuja, Nigeria.
                    </p>
                </div>
            </tr>

            <tr>
                <div class="letter_margin">
                    <p>
                        Note.-The instrument under which the Transferee claims should preferably accompany this <br>
                        Form.<br>
                        A request for the entry of an address for service of the subsequent proprietor may be made on<br>
                        an unstamped copy of Form 33, if it accompanies this Form.<br>
                    </p>
                </div>
            </tr>

            <div class="pagebreak"> </div>
            <hr>

            <tr>
                <div class="letter_margin">
                    <p>
                        *Additional numbers may be given in a signed Schedule on the back of the Form.
                    </p>
                </div>
            </tr>
        </table>
    </body>
</html>



    """
