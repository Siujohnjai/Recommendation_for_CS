import sys
import os
from tempfile import TemporaryDirectory
import scrapbook as sb
import tensorflow as tf
import pickle
from utils.task_helper import *
from utils.general import *
from utils.data_helper import *
tf.get_logger().setLevel('ERROR') # only show error messages

from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
from recommenders.models.deeprec.deeprec_utils import prepare_hparams
from recommenders.models.deeprec.models.dkn import DKN
from recommenders.models.deeprec.io.dkn_iterator import DKNTextIterator

print(f"System version: {sys.version}")
print(f"Tensorflow version: {tf.__version__}")

class MySentenceCollection:
    def __init__(self, filename):
        self.filename = filename
        self.rd = None

    def __iter__(self):
        self.rd = open(self.filename, 'r', encoding='utf-8', newline='\r\n')
        return self

    def __next__(self):
        line = self.rd.readline()
        if line:
            return list(line.strip('\r\n').split(' '))
        else:
            self.rd.close()
            raise StopIteration

def train_word2vec(Path_sentences, OutFile_dir):
    OutFile_word2vec = os.path.join(OutFile_dir, r'word2vec.model')
    OutFile_word2vec_txt = os.path.join(OutFile_dir, r'word2vec.txt')
    create_dir(OutFile_dir)

    print('start to train word embedding...', end=' ')
    my_sentences = MySentenceCollection(Path_sentences)
    model = Word2Vec(my_sentences, size=50, window=10, min_count=1, workers=8, iter=5) # user more epochs for better accuracy

    model.save(OutFile_word2vec)
    model.wv.save_word2vec_format(OutFile_word2vec_txt, binary=False)
    print('\tdone . ')


if __name__ == '__main__':
    InFile_dir = 'inputs/'
    OutFile_dir = 'results/'
    create_dir(OutFile_dir)

    Path_PaperTitleAbs_bySentence = os.path.join(InFile_dir, 'doc_text.txt')
    Path_PaperFeature = os.path.join(OutFile_dir, 'doc_feature.txt')

    max_word_size_per_paper = 256
    word2idx = {}
    entity2idx = {}
    relation2idx = {}
    word2idx, entity2idx = gen_paper_content(
        Path_PaperTitleAbs_bySentence, Path_PaperFeature, word2idx, entity2idx, field=["Title"], doc_len=max_word_size_per_paper
    )
    word2idx_filename = os.path.join(OutFile_dir, 'word2idx.pkl')
    entity2idx_filename = os.path.join(OutFile_dir, 'entity2idx.pkl')

    OutFile_dir_KG = os.path.join(OutFile_dir, 'KG')
    create_dir(OutFile_dir_KG)

    gen_knowledge_relations(os.path.join(InFile_dir, 'RelatedFieldOfStudy.txt'), OutFile_dir_KG, entity2idx, relation2idx)
    Path_SentenceCollection = os.path.join(OutFile_dir, 'sentence.txt')
    gen_sentence_collection(
        Path_PaperTitleAbs_bySentence,
        Path_SentenceCollection,
        word2idx
    )

    Path_PaperReference = os.path.join(InFile_dir, 'PaperReferences.txt')
    Path_PaperAuthorAffiliations = os.path.join(InFile_dir, 'user_2_paper.txt')
    Path_Papers = os.path.join(InFile_dir, 'doc_text.txt')
    Path_Author2ReferencePapers = os.path.join(OutFile_dir, 'user_2_paper.tsv')

    author2paper_list = load_author_paperlist(Path_PaperAuthorAffiliations)
    paper2date = load_paper_date(Path_Papers)
    paper2reference_list = load_paper_reference(Path_PaperReference)

    author2reference_list = get_author_reference_list(author2paper_list, paper2reference_list, paper2date)

    output_author2reference_list(
        author2reference_list,
        Path_Author2ReferencePapers
    )

    OutFile_dir_DKN = os.path.join(OutFile_dir, 'data_source')
    create_dir(OutFile_dir_KG)

    with open(word2idx_filename, 'wb') as f:
        pickle.dump(word2idx, f)
    dump_dict_as_txt(word2idx, os.path.join(OutFile_dir, 'word2id.tsv'))
    with open(entity2idx_filename, 'wb') as f:
        pickle.dump(entity2idx, f)

    gen_experiment_splits(
        Path_Author2ReferencePapers,
        OutFile_dir_DKN,
        Path_PaperFeature,
        item_ratio=0.1,
        tag='small',
        process_num=2
    )

    train_word2vec(Path_Papers, OutFile_dir)

    data_path = os.path.join('data_source')

    yaml_file = os.path.join(data_path, r'dkn.yaml')
    train_file = os.path.join(data_path, r'train.txt')
    valid_file = os.path.join(data_path, r'valid.txt')
    test_file = os.path.join(data_path, r'test.txt')
    news_feature_file = os.path.join(data_path, r'doc_feature.txt')
    user_history_file = os.path.join(data_path, r'user_history.txt')
    wordEmb_file = os.path.join(data_path, r'word_embeddings_500.npy')
    entityEmb_file = os.path.join(data_path, r'entity2vec_50.npy')

    epochs = 20
    save_epoch = 1
    save_model = True
    history_size = 50
    batch_size = 100
    MODEL_DIR = os.path.join(data_path, r'save_dir')

    hparams = prepare_hparams(yaml_file,
                              news_feature_file=news_feature_file,
                              user_history_file=user_history_file,
                              wordEmb_file=wordEmb_file,
                              entityEmb_file=entityEmb_file,
                              epochs=epochs,
                              history_size=history_size,
                              batch_size=batch_size,
                              save_model=save_model,
                              save_epoch=save_epoch,
                              MODEL_DIR=MODEL_DIR)

    model = DKN(hparams, DKNTextIterator)
    model.fit(train_file, valid_file)

    output_sample = model.predict(test_file, test_file)
