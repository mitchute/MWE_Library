import click
import shutil
import os

@click.option("--setup-project",
              is_flag=True,
              "Setup Project Files")
@click.argument("inputs")
def enstore(inputs,  setup_project):

    here = os.path.abspath(os.path.dirname(__file__))
    base_path = os.path.normpath(os.path.join(here, ".."))

    run_dir = click.format_filename(inputs)

    if setup_project:
        shutil.copytree(os.path.join(base_path, "resources"), run_dir)
