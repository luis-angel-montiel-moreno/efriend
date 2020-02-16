#!/bin/bash
EF_MKRU_PATH="agents_knowledge/MAIC_KR/universal"
EF_MKRQT_PATH="agents_knowledge/MAIC_KR/quantitative"
EF_TMP_PATH="tmp"
EF_SRC_PATH="src"
EF_SRCU_PATH="src/universal"
EF_SRCQT_PATH="src/quantitative"
EF_CNV_PATH="conversation_history"



clingo $EF_MKRU_PATH/questions_made.clasp $EF_MKRU_PATH/likespCine.clasp > $EF_TMP_PATH/Cine.int
echo "movies clasp done."
python3 $EF_SRCU_PATH/cine_upd.py
echo "movies py done."
echo "Generating instance and solving DCP - Dialogue Composition Problem."
clingo $EF_MKRU_PATH/opens.clasp $EF_MKRU_PATH/rec.clasp  $EF_MKRU_PATH/questions_made.clasp $EF_MKRQT_PATH/generate_dcp_instance_cuantitative.clasp $EF_MKRQT_PATH/dcp_knapsack_cuantitative.clasp -W none > $EF_TMP_PATH/Adial_cuantitative.int
echo "DCP solution done."
python3 $EF_SRCQT_PATH/outClaspToAdial_quantitative.py 
echo "Adial done."
python3 $EF_SRCU_PATH/AdialToCdial.py
echo "Done"
python3 $EF_SRC_PATH/inte_universal.py
echo "Dialogue Session done."
python3 $EF_SRCU_PATH/filtra_chat.py
echo "Filter done."
python3 $EF_SRCU_PATH/act_preg_hechas.py
echo "update-retrieval done."
cat $EF_TMP_PATH/code.cnv >> $EF_CNV_PATH/history.txt
echo "history updated done."
echo "Cycle micro-chat done."







