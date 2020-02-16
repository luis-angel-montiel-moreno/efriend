#!/bin/bash
EF_MKRU_PATH="agents_knowledge/MAIC_KR/universal"
EF_MKR_INI_PATH="agents_knowledge/MAIC_KR/ini"
EF_CNV_PATH="conversation_history"

cp $EF_MKR_INI_PATH/preguntasCine.ini $EF_MKRU_PATH/preguntasCine.clasp
cp $EF_CNV_PATH/ini/history.ini $EF_CNV_PATH/history.txt
cp $EF_MKR_INI_PATH/preguntas_original.clasp $EF_MKRU_PATH/questions_made.clasp
echo "Done."
