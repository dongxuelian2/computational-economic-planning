#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p output/manuscript
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/manuscript manuscript/main.tex >output/manuscript/build.log
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=output/manuscript manuscript/main.tex >>output/manuscript/build.log
cp output/manuscript/main.pdf output/manuscript/aci-timing-manuscript.pdf
