#!/bin/bash
echo "Generando  modelo nivel bajo"
clingo abiertos.clasp rec.clasp  preguntas_hechas.clasp genera_scrptE_new.clasp longp_generate.clasp 
echo "done"






