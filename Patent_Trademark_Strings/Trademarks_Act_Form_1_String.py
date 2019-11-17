import datetime


class Form1StringClass():
    def __init__(self,
                 person_name,
                 company_name,
                 company_name2,
                 corporate_law,
                 corporate_law2,
                 signature):
        self.weekday = (datetime.datetime.now().strftime("%A") + " "
                        + datetime.datetime.now().strftime("%d"))
        self.month = datetime.datetime.now().strftime("%B")
        self.year = datetime.datetime.now().strftime("%Y")
        self.form_1_string = """

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
            .underlined-dot{
                border-bottom: 2px dotted #000;
                text-decoration: none;
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
                    <h2>FORM 1</h2>
                </header>
            </tr>
            <tr >
                <div class="intro letter_margin">
                    <p>
                        (Form of Authorization of Agent in a matter or <br>
                        Proceeding under the Act (Regulation 16)
                    </p>
                </div>
            </tr>
            <tr>
                <div class="request letter_margin">
                    <p>
                        I/We <span class="underlined-dot variable1">"""+person_name+"""</span>,<br>
                        of <span class="underlined-dot variable1">"""+company_name+"""</span>  <br>
                        <span class="underlined-dot variable1">"""+company_name2+"""</span><br>

                        have appointed ALLAN & OGUNKEYE Legal Practitioners, of Western House (7 th <br>
                        Floor), 8/10 Broad Street, Lagos. P.O. Box 51769 Ikoyi, Lagos, Nigeria to act as my/our <br>
                        agents for the prosecution on my/our behalf of the following matter or proceeding under <br>
                        the Trade Marks Act: <br><br>
                        in respect of the following trade mark(s) belonging to me/us: <br><br>

                        and request that all notices, requisitions and communications relating thereto may be sent <br>
                        to such agent at the above address. <br><br>

                        I/We revoke all previous authorizations, if any, in respect of the same matter or <br>
                        proceeding. <br><br>

                        We hereby declare that we are a company incorporated under the laws of <span class="underlined-dot variable1">"""+corporate_law+"""</span> <br>
                        <span class="underlined-dot variable1">"""+corporate_law2+"""</span>
                    </p>
                </div>
            </tr>

            <tr>
                <div class="letter_margin">
                    <p>DATED  this <span class="underlined weekday">"""+self.weekday+"""</span>day of<span class="underlined month"> """+self.month+"""</span> <span class="underlined year"> """+self.year+"""</span></p>
                </div>
            </tr>
            <br><br>
            <tr>
                <div class="letter_margin re-address_row">

                        <p class="re_address">
                            Signature.:<span class="underlined">"""+signature+"""</span> <br>
                            <strong> (Secretary/Director/Authorized Officer)</strong>
                        </p>
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

                        Federal Secretariat <br>

                        Garki, Abuja. <br>
                    </p>
                </div>
            </tr>

        </table>
    </body>
</html>



    """
