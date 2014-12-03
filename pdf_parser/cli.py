import io
import sys

import click
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf


@click.command()
def main():
    """Parses PDFs."""
    fname = '/Users/jonathan/Desktop/simple1.pdf'
    caching = True
    maxpages = 0
    password = ''
    pagenos = set()
    rsrcmgr = PDFResourceManager(caching=caching)
    outfp = sys.stdout
    laparams = LAParams()
    device = TextConverter(rsrcmgr, outfp, laparams=laparams)
    fp = io.open(fname, 'rb')
    process_pdf(rsrcmgr, device, fp, pagenos, maxpages=maxpages,
                password=password, caching=caching, check_extractable=True)
    fp.close()
    # click.echo('hello')
