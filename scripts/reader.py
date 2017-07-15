import os
import json
import codecs

def investigate():
    keys = set()
    with codecs.open('sample.jsons', encoding='utf-8') as f:
        for line in f:
            entry = json.loads(line.strip())
            keys.update(set(entry.keys()))
        print keys
        
# investigate flat json structure
# {"end": "/c/af/pakistan", "surfaceStart": "Afghanistan", "weight": 1.0, "id": "/e/ff75ac33f095b9b2ee53ea6630e1a80be7e0a1b0", "rel": "/r/Antonym", "surfaceEnd": "Pakistan", "surfaceText": "[[Afghanistan]] is an antonym of [[Pakistan]]", "sources": ["/s/rule/synonym_section", "/s/web/de.wiktionary.org/wiki/Afghanistan"], "context": "/ctx/all", "dataset": "/d/wiktionary/de/af", "source_uri": "/and/[/s/rule/synonym_section/,/s/web/de.wiktionary.org/wiki/Afghanistan/]", "features": ["/c/af/afghanistan /r/Antonym -", "/c/af/afghanistan - /c/af/pakistan", "- /r/Antonym /c/af/pakistan"], "uri": "/a/[/r/Antonym/,/c/af/afghanistan/,/c/af/pakistan/]", "start": "/c/af/afghanistan", "license": "/l/CC/By-SA"}

# features:  ["/c/af/afghanistan /r/Antonym -", "/c/af/afghanistan - /c/af/pakistan", "- /r/Antonym /c/af/pakistan"]
# weight
# id /e/ff75ac33f095b9b2ee53ea6630e1a80be7e0a1b0
# surfaceText "[[Afghanistan]] is an antonym of [[Pakistan]]
# rel /r/Antonym
# end /c/af/pakistan
# surfaceStart Afghanistan
# start /c/af/afghanistan
# surfaceEnd Pakistan
# end /c/af/pakistan
# context /ctx/all

# filter strategy
## 1. start and end are all en concepts
## 2. relations are in our predefined list
## 3. extract all surface texts.
causeRels = ['Causes',
        'HasSubevent',
        'HasFirstSubevent',
        'HasPrerequisite',
        'CausesDesire',
        'MotivatedByGoal',
        'Entails']
def extract(fp, out_fp = None):
    if out_fp is None: 
        prefix, suffix = os.path.split(fp)
        out_fp = os.path.join(prefix, 'extract_'+suffix )
    with codecs.open(fp, encoding='utf-8') as f, \
            codecs.open(out_fp, 'w', encoding='utf-8') as outf:
        for line in f:
            entry = json.loads(line.strip())
            if 'start' in entry and \
                    'end' in entry and \
                    'rel' in entry:
                start = entry['start']
                end = entry['end']
                rel = os.path.split(entry['rel'])
                if start.startswith('/c/en/') and \
                        end.startswith('/c/en/') and \
                        rel in causeRels:
                            print line
                            outf.write(line)

def extract_dir(ddir):
    ddir = os.path.normpath(ddir)
    for fn in os.listdir(ddir):
        fn = os.path.join(ddir, fn)
        if os.path.isfile(fn) and os.path.splitext(fn)[-1]=='.jsons':
            extract(os.path.abspath(fn))

#extract_dir('/home/zhiyi/Projects/CausalLaw/data/ConceptNet/data/assertions')
#extract('/home/zhiyi/Projects/CausalLaw/data/ConceptNet/data/assertions/2015 part_00.jsons')

def extract_pairs(fp, src_fp, tgt_fp):
    with codecs.open(fp,encoding='utf-8') as f, codecs.open(src_fp, 'w', encoding='utf-8') as outf1, codecs.open(tgt_fp, 'w', encoding='utf-8') as outf2:
        for line in f:
            entry = json.loads(line.strip())
            if 'surfaceStart' not in entry and 'surfaceEnd' in entry:
                continue
            sstart = entry['surfaceStart']
            send = entry['surfaceEnd']
            if sstart and send:
                outf1.write(sstart+'\n')
                outf2.write(send+'\n')

extract_pairs('/home/zhiyi/Projects/CausalLaw/data/ConceptNet/data/extract_assertions/extract.jsons','/home/zhiyi/Projects/CausalLaw/forked/OpenNMT-py/cnetdata/cause.txt','/home/zhiyi/Projects/CausalLaw/forked/OpenNMT-py/cnetdata/effect.txt')
