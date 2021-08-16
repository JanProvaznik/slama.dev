#!/usr/bin/python3

import argparse
import glob
import os
import sys
from re import search, sub
from subprocess import DEVNULL, PIPE, Popen
from tempfile import NamedTemporaryFile  # for reading Xournal++ output
from typing import *


def crop_svg(contents: str, margin: float = 3) -> None:
    """Crop the specified .svg file.
    TODO: add support for cropping files that include text."""
    # set the default values for the coordinates we're trying to find
    inf = float("inf")
    min_x, min_y, max_x, max_y = inf, inf, -inf, -inf

    lines = contents.splitlines()
    paths_skipped = 0
    i = 0

    while i < len(lines):
        line = lines[i]

        if line.startswith(r"<path"):
            # skip the first two path tags
            if paths_skipped != 2:
                lines.pop(i)
                paths_skipped += 1
                continue

            path = search(r'<path(.+?)d="(.+?)"', line)
            coordinate_parts = path.group(2).strip().split(" ")

            # get only the coordinate numbers
            coordinates = [float(c) for c in coordinate_parts if not c.isalpha()]

            # check for min/max
            for x, y in zip(coordinates[::2], coordinates[1::2]):
                min_x, max_x = min(min_x, x), max(max_x, x)
                min_y, max_y = min(min_y, y), max(max_y, y)

        i += 1

    # adjust for margins
    min_x -= margin
    min_y -= margin
    max_x += margin
    max_y += margin

    # add/update svg values
    substitutions = (
        (r'<svg(.*)width="(.+?)pt', f'<svg\\1width="{max_x - min_x}pt'),  # width
        (r'<svg(.*)height="(.+?)pt', f'<svg\\1height="{max_y - min_y}pt'),  # height
        (r"<svg(.+)>", f'<svg\\1 x="{min_x}" y="{min_y}">'),  # min x and y
        (
            r'<svg(.*)viewBox="(.*?)"(.*)>',
            f'<svg\\1viewBox="{min_x} {min_y} {max_x - min_x} {max_y - min_y}"\\3>',
        ),  # viewbox
    )

    contents = "\n".join(lines)
    for pattern, replacement in substitutions:
        contents = sub(pattern, replacement, contents)

    return contents


def get_argument_parser() -> argparse.ArgumentParser:
    """Returns the ArgumentParser object for the script."""
    parser = argparse.ArgumentParser(
        description="Convert Xournal++ files to SVGs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # svg margins
    parser.add_argument(
        "-m",
        "--margins",
        dest="margins",
        metavar="M",
        type=int,
        default=15,
        help="the margins around the cropped Xournal++ files (in points, default 15)",
    )

    # compress
    parser.add_argument(
        "-c",
        "--compress",
        dest="compress",
        action="store_false",
        default=True,
        help="whether not to compress the SVG using Scour (on by default)",
    )

    # either convert all files or only specific files
    group = parser.add_mutually_exclusive_group(required=True)

    # all files
    group.add_argument(
        "-a",
        "--all-files",
        dest="files",
        default=[],
        action="store_const",
        const=glob.glob("*.xopp"),
        help="convert all .xopp files in the working directory",
    )

    # only specific files
    group.add_argument(
        "-i",
        "-f",
        "--files",
        dest="files",
        default=[],
        metavar="F",
        nargs="+",
        help="the name(s) of the .xopp file(s) to convert to SVG",
    )

    return parser


# get the parser and parse the commands
parser = get_argument_parser()
arguments = parser.parse_args()


# go through the specified markdown files
for i, name in enumerate(arguments.files):
    # check if the file exists
    if not os.path.exists(name):
        print(f"'{name}' not found, skipping.", flush=True)
        continue

    # get the svg from Xournal++, storing it in a temporary file
    tmp = NamedTemporaryFile(mode="w+", suffix=".svg")
    Popen(["xournalpp", f"--create-img={tmp.name}", name], stderr=DEVNULL).communicate()

    # crop the SVG
    cropped_svg = crop_svg(tmp.read())

    # possibly use scour to compress the SVG; else just output
    if arguments.compress:
        out = (
            Popen(["scour"], stdin=PIPE, stdout=PIPE, stderr=DEVNULL)
            .communicate(input=cropped_svg.encode())[0]
            .decode()
        )

    out_name = name[:-4] + "svg"
    with open(out_name, "w") as f:
        f.write(out)
        print(f"{name} -> {out_name}", flush=True)
