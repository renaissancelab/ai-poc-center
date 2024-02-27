#!/usr/bin/env python3

from towhee import AutoPipes, AutoConfig

if __name__ == '__main__':
    config = AutoConfig.load_config('sentence_embedding')
    config.model = 'paraphrase-albert-small-v2'
    config.device = 0
    sentence_embedding = AutoPipes.pipeline('sentence_embedding', config=config)

    # generate embedding for one sentence
    embedding = sentence_embedding('how are you?').get()
    # batch generate embeddings for multi-sentences
    embeddings = sentence_embedding.batch(['how are you?', 'how old are you?'])
    embeddings = [e.get() for e in embeddings]
