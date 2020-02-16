#!/bin/bash
# se debe correr no con sh script.sh sino bash script.sh
EF_MKR_INI_PATH="agents_knowledge/MAIC_KR/ini"
EF_MKRU_PATH="agents_knowledge/MAIC_KR/universal"
EF_MKRQT_PATH="agents_knowledge/MAIC_KR/quantitative"
EF_TMP_PATH="tmp"
EF_SRC_PATH="src"
EF_SRCU_PATH="src/universal"
EF_SRCQT_PATH="src/quantitative"
EF_CNV_PATH="conversation_history"

declare -i N=100
declare -i M=15
for ((j=1; j<=$N; j++))
do
  echo "Reinicia "
  echo $j  
  cp $EF_MKR_INI_PATH/preguntasCine.ini $EF_MKRU_PATH/preguntasCine.clasp
  cp $EF_CNV_PATH/ini/history.ini $EF_CNV_PATH/history.txt
  cp $EF_MKR_INI_PATH/preguntas_original.clasp $EF_MKRU_PATH/questions_made.clasp
  for ((i=1; i<=$M; i++))
  do
     echo "sesion #"  $i
     clingo $EF_MKRU_PATH/questions_made.clasp $EF_MKRU_PATH/likespCine.clasp > $EF_TMP_PATH/Cine.int
     echo "movies clasp done."
     python3 $EF_SRCU_PATH/cine_upd.py
     echo "movies py done."
     echo "Generating instance and solving DCP - Dialogue Composition Problem."
     gringo $EF_MKRU_PATH/opens.clasp $EF_MKRU_PATH/rec.clasp  $EF_MKRU_PATH/questions_made.clasp $EF_MKRQT_PATH/generate_dcp_instance_cuantitative.clasp -W none | grep [' ']v\( > $EF_TMP_PATH/vertices.out
     SALIDA=$(python3 $EF_SRCQT_PATH/cuentaVertices_quantitative.py)
     XERROR=$(expr match "$SALIDA" '.*WARNING.*')
     if [ $XERROR -gt 0 ]
     then
     	echo "Running in Default Mode."	
	echo "$SALIDA"
        python3 $EF_SRCQT_PATH/outDefault_quantitative.py 
     else 
	echo "Running in Standard Mode."
        clingo $EF_MKRU_PATH/opens.clasp $EF_MKRU_PATH/rec.clasp  $EF_MKRU_PATH/questions_made.clasp $EF_MKRQT_PATH/generate_dcp_instance_cuantitative.clasp $EF_MKRQT_PATH/dcp_knapsack_cuantitative.clasp -W none > $EF_TMP_PATH/Adial_cuantitative.int
        echo "DCP solution done."
        python3 $EF_SRCQT_PATH/outClaspToAdial_quantitative.py 
     fi
#    echo "Adial done."
     python3 $EF_SRCU_PATH/AdialToCdial.py
#    echo "Done"
     python3 $EF_SRC_PATH/s_inte_universal.py
#    echo "Dialogue Session done."
     python3 $EF_SRCU_PATH/filtra_chat.py
#    echo "Filter done."
     python3 $EF_SRCU_PATH/act_preg_hechas.py
#    echo "update-retrieval done."
     cat $EF_TMP_PATH/code.cnv >> $EF_CNV_PATH/history.txt
#    echo "history updated done."
#    echo "Cycle micro-chat done."
    sleep 1
  done
  python3 $EF_SRCU_PATH/cuenta_ses.py
  sleep 2
done


