import numpy as np


KGE_METHOD = 'TransE'
ENTITY_EMBEDDING_DIM = 50


def read_map(file):
    entity2index_map = {}
    reader = open(file, encoding='utf-8')
    for line in reader:
        array = line.split('\t')
        if len(array) != 2:  # to skip the first line in entity2id.txt
            continue
        entity_id = array[0]
        index = int(array[1])
        entity2index_map[entity_id] = index
    reader.close()
    return entity2index_map


def get_neighbors_for_entity(file):
    reader = open(file, encoding='utf-8')
    entity2neighbor_map = {}
    for line in reader:
        array = line.strip().split('\t')
        if len(array) != 3:  # to skip the first line in triple2id.txt
            continue
        head = int(array[0])
        tail = int(array[1])
        if head in entity2neighbor_map:
            entity2neighbor_map[head].append(tail)
        else:
            entity2neighbor_map[head] = [tail]
        if tail in entity2neighbor_map:
            entity2neighbor_map[tail].append(head)
        else:
            entity2neighbor_map[tail] = [head]
    reader.close()
    return entity2neighbor_map


if __name__ == '__main__':
    # entity2index.txt (generated by news_preprocess.py) contains all entities appear in the dataset
    # entity2id.txt (generated by prepare_data_for_transx.py) contains all entities in the crawled knowledge graph
    entity2index = read_map('entity2id.txt')
    # entity2index = read_map('entity2index.txt')
    full_entity2index = read_map('entity2id.txt')
    entity2neighbor = get_neighbors_for_entity('triple2id.txt')

    full_embeddings = np.loadtxt(KGE_METHOD + '_entity2vec_' + str(ENTITY_EMBEDDING_DIM) + '.vec')
    entity_embeddings = np.zeros([len(entity2index) + 1, ENTITY_EMBEDDING_DIM])
    context_embeddings = np.zeros([len(entity2index) + 1, ENTITY_EMBEDDING_DIM])

    print('writing entity embeddings...')
    for entity, index in entity2index.items():
        if entity in full_entity2index:
            full_index = full_entity2index[entity]
            entity_embeddings[index] = full_embeddings[full_index]
            if full_index in entity2neighbor:
                context_full_indices = entity2neighbor[full_index]
                context_embeddings[index] = np.average(full_embeddings[context_full_indices], axis=0)

    np.save('entity_embeddings_' + KGE_METHOD + '_' + str(ENTITY_EMBEDDING_DIM), entity_embeddings)
    np.save('context_embeddings_' + KGE_METHOD + '_' + str(ENTITY_EMBEDDING_DIM), context_embeddings)
