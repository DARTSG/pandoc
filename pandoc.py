import os
import subprocess
import sys
import glob
MD_EXTENSION = ".md"

PANDOC_CMD = 'pandoc -s --template pandoc.html "%s" --metadata pagetitle="%s" -o "%s"'


def get_md_files(folder):
    """Returns a list of all MD files within dir (recursively)"""
    return glob.glob(os.path.join(folder, r'**/*' + MD_EXTENSION), recursive=True)


def commands_to_run(files):
    commands = []
    for path in files:
        if path is None:
            continue

        folder, filename = os.path.split(path)
        title, _ = os.path.splitext(filename)
        output_path = os.path.join(folder, title + ".html")
        commands.append(PANDOC_CMD % (path, title, output_path))
    return commands


if __name__ == "__main__":
    files = get_md_files(".")
    commands = commands_to_run(files)
    for command in commands:
        subprocess.run(command, shell=True)
        # print(command)
