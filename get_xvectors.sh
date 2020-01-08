#!/bin/bash
current_dir=`pwd`
current_dir_util="${current_dir}/utils/fix_data_dir.sh"
current_dir_xvec="${current_dir}/vector_extract.sh"
python wav_utt2spk.py $1 $2
python spk2utt.py $1 $2
bash $current_dir_util $2
bash $current_dir_xvec
