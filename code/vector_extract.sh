#!/bin/bash
# Copyright   2017   Johns Hopkins University (Author: Daniel Garcia-Romero)
#             2017   Johns Hopkins University (Author: Daniel Povey)
#        2017-2018   David Snyder
#             2018   Ewald Enzinger
# Apache 2.0.
#
# See ../README.txt for more info on data required.
# Results (mostly equal error-rates) are inline in comments below.

. ./cmd.sh
. ./path.sh
set -e
mfccdir=`pwd`/mfcc
vaddir=`pwd`/mfcc


# The trials file is downloaded by local/make_voxceleb1.pl.
#voxceleb1_trials=data/voxceleb1_test/trials
#voxceleb1_root=/export/corpora/VoxCeleb1
#voxceleb2_root=/export/corpora/VoxCeleb2
nnet_dir=/home/kaldi_asr/kaldi/egs/voxceleb/v2/xvector_voxceleb/exp/xvector_nnet_1a
musan_root=/export/corpora/JHU/musan
data_train=/home/kaldi_asr/the_data/data_extract_xvector
stage=0


if [ $stage -le 1 ]; then
  # Make MFCCs and compute the energy-based VAD for each dataset
  for name in train; do
    steps/make_mfcc.sh --write-utt2num-frames true --mfcc-config conf/mfcc.conf --nj 1 --cmd "$train_cmd" \
      data/${name} exp/make_mfcc $mfccdir
    utils/fix_data_dir.sh data/${name}
    sid/compute_vad_decision.sh --nj 1 --cmd "$train_cmd" \
      data/${name} exp/make_vad $vaddir
    utils/fix_data_dir.sh data/${name}
  done
fi

stage=9

if [ $stage -le 9 ]; then
  # Extract x-vectors for centering, LDA, and PLDA training.
  sid/nnet3/xvector/extract_xvectors.sh --cmd "$train_cmd --mem 4G" --nj 1 \
    $nnet_dir /home/kaldi_asr/kaldi/egs/voxceleb/v2/data/train \
    $nnet_dir/xvectors_train

  # Extract x-vectors used in the evaluation.
  #sid/nnet3/xvector/extract_xvectors.sh --cmd "$train_cmd --mem 4G" --nj 40 \
    #$nnet_dir data/voxceleb1_test \
    #$nnet_dir/xvectors_voxceleb1_test
fi


