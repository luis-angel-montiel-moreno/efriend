#!/bin/bash
echo "Generando  modelo nivel bajo"
clingo abiertos.clasp rec.clasp  preguntas_hechas.clasp genera_scrptE.clasp longp_generate.clasp > Adial.int
echo "done"






