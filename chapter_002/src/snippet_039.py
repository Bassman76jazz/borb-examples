from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.image.unsplash import Unsplash

from decimal import Decimal
import keyring


def main():

    # set the unsplash API access key
    keyring.set_password("unsplash", "access_key", "<your access key here>")

    # create Document
    doc: Document = Document()

    # create Page
    page: Page = Page()

    # add Page to Document
    doc.append_page(page)

    # set a PageLayout
    layout: PageLayout = SingleColumnLayout(page)

    # add an Image from Unsplash
    # you can specify the keywords as well as the desired dimensions
    layout.add(Unsplash.get_image(["cherry", "blossom"], Decimal(400), Decimal(300)))

    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
