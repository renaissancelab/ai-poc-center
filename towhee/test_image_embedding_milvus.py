#!/usr/bin/env python3

import cv2
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
from towhee import ops, pipe, DataCollection
from towhee.types.image import Image
import pandas as pd
import numpy as np
import csv


# need run on gpu

def read_images(results):
    imgs = []
    for re in results:
        path = id_img[re.id]
        imgs.append(Image(cv2.imread(path), 'BGR'))
    return imgs


def read_csv(csv_path, encoding='utf-8-sig'):
    with open(csv_path, 'r', encoding=encoding) as f:
        data = csv.DictReader(f)
        for line in data:
            yield int(line['id']), line['path']


def create_milvus_collection(collection_name, dim):

    connections.connect(host='127.0.0.1', port='19530')

    if utility.has_collection(collection_name):
        utility.drop_collection(collection_name)

    fields = [
        FieldSchema(name='id', dtype=DataType.INT64, descrition='ids', is_primary=True, auto_id=False),
        FieldSchema(name='embedding', dtype=DataType.FLOAT_VECTOR, descrition='embedding vectors', dim=dim)
    ]
    schema = CollectionSchema(fields=fields, description='text image search')
    collection = Collection(name=collection_name, schema=schema)

    # create IVF_FLAT index for collection.
    index_params = {
        'metric_type': 'L2',
        'index_type': "IVF_FLAT",
        'params': {"nlist": 512}
    }
    collection.create_index(field_name="embedding", index_params=index_params)
    return collection


if __name__ == '__main__':
    # pre show
    df = pd.read_csv('reverse_image_search.csv')
    df.head()
    id_img = df.set_index('id')['path'].to_dict()

    # 1.image to embedding vector
    p = (
        pipe.input('path')
        .map('path', 'img', ops.image_decode.cv2('rgb'))
        .map('img', 'vec', ops.image_text_embedding.clip(model_name='clip_vit_base_patch16', modality='image'))
        .map('vec', 'vec', lambda x: x / np.linalg.norm(x))
        .output('img', 'vec')
    )
    DataCollection(p('./boy.jpeg')).show()
    # 2.text to embedding vector
    p2 = (
        pipe.input('text')
        .map('text', 'vec', ops.image_text_embedding.clip(model_name='clip_vit_base_patch16', modality='text'))
        .map('vec', 'vec', lambda x: x / np.linalg.norm(x))
        .output('text', 'vec')
    )
    DataCollection(p2("A teddybear on a skateboard in Times Square.")).show()

    # create collections and load image embedding into milvus
    collection = create_milvus_collection('text_image_search', 512)

    '''
    p3 = (
        pipe.input('csv_file')
        .flat_map('csv_file', ('id', 'path'), read_csv)
        .map('path', 'img', ops.image_decode.cv2())
        .map('img', 'vec', ops.image_text_embedding.clip(model_name='clip_vit_base_patch16', modality='image', device=0))
        .map('vec', 'vec', lambda x: x / np.linalg.norm(x))
        .map(('id', 'vec'), (), ops.ann_insert.milvus_client(host='127.0.0.1', port='19530', collection_name='text_image_search'))
        .output()
    )
    ret = p3('reverse_image_search.csv') 
    '''

    p3 = (
        pipe.input('file_name')
        .map('file_name', 'img', ops.image_decode.cv2())
        .map('img', 'vec', ops.image_text_embedding.clip(model_name='clip_vit_base_patch32', modality='image', device=0))
        .map('vec', 'vec', ops.towhee.np_normalize())
        .map(('vec', 'file_name'), (), ops.ann_insert.milvus_client(host='127.0.0.1', port='19530', collection_name='text_image_search'))
        .output()
    )

    for f_name in [
        'https://assets.raribleuserdata.com/prod/v1/image/t_image_cmp_preview/aHR0cHM6Ly9zdGF0aWMubWFudGxlLnh5ei9jaXRpemVuc29mbWFudGxlL2ltYWdlcy81MmRhNjcyODBiMWQ4NmI0MDNkNWZlNmQ4YjM5YmZlNjgzODlhZWJhLnBuZw==',
        'https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9zdGF0aWMubWFudGxlLnh5ei9jaXRpemVuc29mbWFudGxlL2ltYWdlcy81NTI1YjI1YzcwOGM4ZDA4ZTA2YTFhMTk5ZTg0M2YxNTA2OTYzODJjLnBuZw==',
        'https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9zdGF0aWMubWFudGxlLnh5ei9jaXRpemVuc29mbWFudGxlL2ltYWdlcy80MjgyMmZkOWM1NWU4MGMyMWJiNzkzMjdkMzIxNWZmYzI3ZGI0NTQxLnBuZw==']:
        p3(f_name)