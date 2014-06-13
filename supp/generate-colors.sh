#!/bin/bash

COUNT="$1"
FILE="$2"

function fill-in-the-gaps() {
  awk -v "c=$COUNT" 'BEGIN {prevval=-1} ; { for (i=prevval+1 ; i <= $1 - 1 ; ++i) print "... white" } ; {prevval=$1 } ; { print $1 " " $2 } ; {LASTVAL=$1} ; END {for (i=$1+1 ; i<c ; ++i) print "... white"}' "$@"
}

function data() {
  sort -n "$FILE" | fill-in-the-gaps
}


NUMLINES=$(data | wc -l)
NUMLINESLESSONE=$(($NUMLINES - 1))

echo -n '\begin{tabular}{'
seq 0 $NUMLINESLESSONE | awk '{if ($1 % 20 == 0) printf "|c" ; else printf "c"}'
echo '|}'


data | cut -d' ' -f 2 | xargs -n1 printf '\\cellcolor{%s} & ' | head -c -2
echo '\\ [5ex]'


echo "\\multicolumn{20}{|l|}{0} & "
seq 20 20 $NUMLINESLESSONE | xargs printf "\\multicolumn{20}{l|}{%d} & " | head -c -2
# awk '{if ($1 % 20 == 0) printf "\\multicolumn{20}{l|}{%d} & ", $1}' | head -c -2
echo '\\'


echo '\end{tabular}'
