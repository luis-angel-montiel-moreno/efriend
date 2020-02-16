#!/bin/bash
echo "Generando  modelo nivel bajo"
clingo select.clasp abiertos.clasp rec.clasp  preguntas_hechas.clasp genera_scrptE_new.clasp 
echo "done"






