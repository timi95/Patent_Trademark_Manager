import datetime


class Form3StringClass():
    def __init__(self, image_url):
        self.image_url = image_url
        self.form_3_string = """

<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Trade Marks Act</title>
        <style>
            .letter_margin {
                margin: auto 15%;
                line-height: 25px;
            }
            header{
                text-align: center;
            }
            .intro {
                text-align: center;
                font-style: italic;
            }
            .centered_text {
                text-align: center;
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
                background-image: url("""+image_url+""");
                background-repeat: no-repeat;
                background-position: center;
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
                    <h2>FORM 3</h2>
                </header>
            </tr>
            <tr >
                <div class="intro letter_margin">
                    <p>
                        Additional Representation of Trade Mark to Accompany Application for <br>

                        Registration (Regulations 16 and 40)
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
                            One representation of the trade mark to
                            be affixed within this space. It must
                            correspond exactly in all respects with
                            the representation affixed to the
                            Application Form.
                        </p>
                        <hr>
                        <p>
                            Any representation larger than the
                            space provided may be folded but must
                            then be mounted upon linen or other
                            suitable material and affixed hereto.
                        </p>
                    </div>
                </div>
            </tr>
            <tr>
                <div class="letter_margin">
                    <p class="centered_text">
                        Four of these ADDITIONAL REPRESENTATIONS of the Trade Mark <br>

                        must accompany each Form of Application.
                    </p>
                </div>
            </tr>



        </table>
    </body>
</html>



    """
