python preprocess.py -train_src cnetdata/cause-train.txt -train_tgt cnetdata/effect-train.txt -valid_src cnetdata/cause-val.txt -valid_tgt cnetdata/effect-val.txt -save_data cnetdata/demo
python train.py -data cnetdata/demo.train.pt -save_model cnetdemo-model 
#python translate.py -model poedemo-model_acc_16.03_ppl_1351.17_e13.pt -src poedata/tsrc-val.txt -output pred.txt -replace_unk -verbose
python translate.py -model cnetdemo-model_acc_36.71_ppl_47.63_e5.pt -src cnetdata/cause-val.txt -output pred.txt -replace_unk -verbose
cnetdemo-model_acc_36.71_ppl_47.63_e5.pt
# poedemo-model_acc_16.07_ppl_1351.41_e12.pt
# poedemo-model_acc_16.03_ppl_1351.17_e13.pt

