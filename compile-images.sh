#!/bin/bash

# Strip .svg, then convert
find images/ -name '*.svg' |
  rev | cut -d. -f2- | rev |
  xargs -I{} -n1 inkscape --export-png={}.png {}.svg
