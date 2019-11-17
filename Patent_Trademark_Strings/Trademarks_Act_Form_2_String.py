import datetime


class Form2StringClass():
    def __init__(self,
                 trademark_class,
                 trademark_law,
                 business_name,
                 business_address):
        self.trademark_class = trademark_class
        self.trademark_law = trademark_law
        self.business_name = business_name
        self.business_address = business_address
        self.weekday = (datetime.datetime.now().strftime("%A") + " "
                        + datetime.datetime.now().strftime("%d"))
        self.month = datetime.datetime.now().strftime("%B")
        self.year = datetime.datetime.now().strftime("%Y")
        self.form_2_string = """

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
            .image_box_row{
                display: flex;
                justify-content: space-evenly;
            }
            .image_box{
                width: 100%;
                border: 1px solid black;
                margin: 1rem;
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
                    <h2>FORM 2</h2>
                </header>
            </tr>
            <tr >
                <div class="intro letter_margin">
                    <p>
                        (Application for Registration of Trade Mark in Part <br>

                        A of the Register)
                    </p>
                </div>
            </tr>
            <tr>
                <div class="image_box_row letter_margin">
                    <div class="image_box">
                        <img src="" alt="">
                    </div>
                    <div class="">
                        <p>
                            One representation to be fixed within this space and
                            four others to be sent on Forms 3.
                        </p>
                        <hr>
                        <p>
                            Representations of a large size may be folded, but
                            must then be mounted upon linen or other suitable
                            material and affixed hereto.
                        </p>
                    </div>
                </div>
            </tr>
            <tr>
                <div class="request letter_margin">
                    <p>
                        Application is hereby made for Registration in Part A of the Register of the accompanying <br>
                        Trade Mark in Class <span class="underlined">"""+trademark_class+"""</span> in respect of:
                        <span class="underlined">""" +trademark_law+"""</span><br><br>
                        in the name of: <span class="underlined">"""+business_name+"""</span><br><br>
                        whose trade or business address is: <span class="underlined">"""+business_address+"""</span><br><br>
                        by whom it is being used/proposed to be used, and who claim(s) to be the proprietor(s) <br>
                        thereof.
                    </p>
                </div>
            </tr>

            <tr>
                <div class="letter_margin">
                    <p>DATED  this <span class="underlined weekday"> """+self.weekday+"""</span> day of<span class="underlined month"> """+self.month+"""</span> <span class="underlined year"> """+self.year+"""</span></p>
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


        </table>
    </body>
</html>



    """
