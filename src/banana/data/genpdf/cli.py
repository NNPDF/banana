import click

from . import generate_pdf, install_pdf


@click.group()
def cli():
    pass


@cli.command("generate")
@click.argument("name")
@click.argument("labels", nargs=-1)
@click.option("-p", "--parent-pdf-set", default=None, help="parent pdf set")
@click.option("-m", "--members", is_flag=True, help="generate all the members")
@click.option("-i", "--install", is_flag=True, help="install into LHAPDF")
def cli_generate_pdf(name, labels, parent_pdf_set, members, install):
    """Generate a new PDF from a parent set with given flavors"""
    return generate_pdf(name, labels, parent_pdf_set, members, None, install)


@cli.command("install")
@click.argument("name")
def cli_install_pdf(name):
    """Install the PDF on LHAPDF directory"""
    return install_pdf(name)


if __name__ == "__main__":
    cli()
