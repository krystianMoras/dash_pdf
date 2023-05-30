import base64
from dash import Dash, html
from dash_pdf import DashPdfDocument, DashPdfPage

app = Dash(__name__)


with open(r"../2105.14078(3).pdf", "rb") as pdf_file:
    encoded_string = base64.b64encode(pdf_file.read())
    # add "data:application/pdf;base64," to the front of encoded_string
    encoded_string = "data:application/pdf;base64," + \
        encoded_string.decode("utf-8")
    print(encoded_string[:100])

app.layout = html.Div([
    DashPdfDocument(id="my-pdf", file=encoded_string, children=[
        DashPdfPage(pageNumber=1, width=1000),
        html.P("Hello World"),
        DashPdfPage(pageNumber=2, width=1000),
        DashPdfPage(pageNumber=3, width=1000),
        DashPdfPage(pageNumber=4, width=1000),
        DashPdfPage(pageNumber=5, width=1000),
        DashPdfPage(pageNumber=6, width=1000),
        DashPdfPage(pageNumber=7, width=1000),
        DashPdfPage(pageNumber=8, width=1000),
        DashPdfPage(pageNumber=9, width=1000),
    ]),

])

if __name__ == "__main__":
    app.run_server(debug=True)

# add origin remote github
#
