#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p output/pdf
pandoc docs/research/aci_sharp_timing_theorem.md \
  --from markdown+tex_math_single_backslash --standalone \
  --pdf-engine=xelatex -V geometry:margin=1in -V fontsize=10pt \
  -V colorlinks=true -V urlcolor=blue \
  -o output/pdf/aci-sharp-timing-theorem.pdf
