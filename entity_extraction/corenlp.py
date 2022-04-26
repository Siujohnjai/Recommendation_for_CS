from stanza.server import CoreNLPClient
import os
import csv
import re
from time import time
# example text
# print('---')
# print('input text')
# print('')

# text = "Facebook is a company"

# print(text)

# set up the client
print('---')
print('starting up Java Stanford CoreNLP Server...')

# set up the client
# with CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','ner','parse','depparse','coref'], timeout=60000, memory='16G') as client:
with CoreNLPClient(annotators=['entitylink','openie'], timeout=300000, memory='16G', threads=32) as client:
    directory_in_str = "/data1/chwongcc/stanza/demo/corpus_full"
    directory = os.fsencode(directory_in_str)
        
    for file in os.listdir(directory):
        start = time()
        filename = os.fsdecode(file)
        print(filename)
        flag_vocab = False
        filename_wo_txt = filename[:-4]
        with open(f"{directory_in_str}/{filename}") as r:
            corpus = r.read().replace('\n', ' ').replace('\r', '')
            vocab = re.sub('[0-9]', '', filename_wo_txt)
            vocab_short = filename_wo_txt[filename_wo_txt.find("(")+1:filename_wo_txt.find(")")]

        # triples_corpus = client.annotate(corpus[0:8000])
        # print('Corpus: %s [...].' % corpus[0:800])
        # print('Found %s triples in the corpus.' % len(triples_corpus))
    
            # submit the request to the server
            ann = client.annotate(corpus[0:8000])
            # ann = client.annotate(text)

            # get the first sentence
            # sentence = ann.sentence[0]
            list_of_dict = []

            
            for sentence in ann.sentence:
                for triple in sentence.openieTriple:  
                    # print(triple)  
                    flag = False
                    triple_dict = {}
                    for j in triple.subjectTokens:
                        if (sentence.token[j.tokenIndex].pos == "PRP"):
                            # print(sentence.token[j.tokenIndex])
                            flag = True
                    
                    if flag:
                        continue

                    ## save triple to list
                    triple_dict['subject'] = triple.subject.lower()
                    triple_dict['relation'] = triple.relation.lower()
                    triple_dict['object'] = triple.object.lower()

                    if triple_dict['subject'] == vocab or triple_dict['subject'] == vocab_short:
                        flag_vocab = True

                    if triple_dict['object'] == vocab or triple_dict['object'] == vocab_short:
                        flag_vocab = True

                    triple_dict['subject_wikientity'] = []
                    triple_dict['relation_wikientity'] = []
                    triple_dict['object_wikientity'] = []
                    
                    for j in triple.subjectTokens:
                        triple_dict['subject_wikientity'].append(sentence.token[j.tokenIndex].wikipediaEntity)

                    for j in triple.relationTokens:
                        triple_dict['relation_wikientity'].append(sentence.token[j.tokenIndex].wikipediaEntity)

                    for j in triple.objectTokens:
                        triple_dict['object_wikientity'].append(sentence.token[j.tokenIndex].wikipediaEntity)

                    list_of_dict.append(triple_dict)

        end = time()
        
        print(len(list_of_dict)/(end - start))
            
        if flag_vocab:
            header = ['subject', 'relation', 'object', 'subject_wikientity', 'relation_wikientity', 'object_wikientity']
        
            with open(f'/data1/chwongcc/stanza/demo/openie_wikientity_csv_filtered_full_debug2/{filename[:-4]}.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = header)
                writer.writeheader()
                writer.writerows(list_of_dict)

                    # for token in sentence.token:
                    #     if token.word == triple.object:
                    #         print(token.word, token.wikipediaEntity)
            # print(sentence)
            # break
            # get the dependency parse of the first sentence
            # print('---')
            # print('tokens of first sentence')
            # tokens = sentence.token
            # for token in tokens:
            #     if token.wikipediaEntity != "O":    
            #         print(token.word, token.wikipediaEntity)    
            # print('---')
            # print('dependency parse of first sentence')
            # dependency_parse = sentence.basicDependencies
            # print(dependency_parse)
        
            # # get the constituency parse of the first sentence
            # print('---')
            # print('constituency parse of first sentence')
            # constituency_parse = sentence.parseTree
            # print(constituency_parse)

            # # get the first subtree of the constituency parse
            # print('---')
            # print('first subtree of constituency parse')
            # print(constituency_parse.child[0])

            # # get the value of the first subtree
            # print('---')
            # print('value of first subtree of constituency parse')
            # print(constituency_parse.child[0].value)

            # # get the first token of the first sentence
            # print('---')
            # print('first token of first sentence')
            # token = sentence.token[0]
            # print(token)

            # # get the part-of-speech tag
            # print('---')
            # print('part of speech tag of token')
            # token.pos
            # print(token.pos)

            # # get the named entity tag
            # print('---')
            # print('named entity tag of token')
            # print(token.ner)

            # # get an entity mention from the first sentence
            # print('---')
            # print('first entity mention in sentence')
            # print(sentence.mentions[0])

            # # access the coref chain
            # print('---')
            # print('coref chains for the example')
            # print(ann.corefChain)

            # # Use tokensregex patterns to find who wrote a sentence.
            # pattern = '([ner: PERSON]+) /wrote/ /an?/ []{0,3} /sentence|article/'
            # matches = client.tokensregex(text, pattern)
            # # sentences contains a list with matches for each sentence.
            # assert len(matches["sentences"]) == 3
            # # length tells you whether or not there are any matches in this
            # assert matches["sentences"][1]["length"] == 1
            # # You can access matches like most regex groups.
            # matches["sentences"][1]["0"]["text"] == "Chris wrote a simple sentence"
            # matches["sentences"][1]["0"]["1"]["text"] == "Chris"

            # # Use semgrex patterns to directly find who wrote what.
            # pattern = '{word:wrote} >nsubj {}=subject >obj {}=object'
            # matches = client.semgrex(text, pattern)
            # # sentences contains a list with matches for each sentence.
            # assert len(matches["sentences"]) == 3
            # # length tells you whether or not there are any matches in this
            # assert matches["sentences"][1]["length"] == 1
            # # You can access matches like most regex groups.
            # matches["sentences"][1]["0"]["text"] == "wrote"
            # matches["sentences"][1]["0"]["$subject"]["text"] == "Chris"
            # matches["sentences"][1]["0"]["$object"]["text"] == "sentence"

