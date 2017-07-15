python preprocess.py -train_src cnetdata/effect-train.txt -train_tgt cnetdata/cause-train.txt -valid_src cnetdata/effect-val.txt -valid_tgt cnetdata/cause-val.txt -save_data cnetdata/rdemo
python train.py -data cnetdata/rdemo.train.pt -save_model cnetrdemo-model 
#python translate.py -model poedemo-model_acc_16.03_ppl_1351.17_e13.pt -src poedata/tsrc-val.txt -output rpred.txt -replace_unk -verbose
python translate.py -model cnetmodel/cnetrdemo-model_acc_62.02_ppl_8.96_e12.pt -src cnetdata/effect-val.txt -output rpred.txt -replace_unk -verbose
# poedemo-model_acc_16.07_ppl_1351.41_e12.pt
# poedemo-model_acc_16.03_ppl_1351.17_e13.pt

