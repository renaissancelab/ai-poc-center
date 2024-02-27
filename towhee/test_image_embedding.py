#!/usr/bin/env python3

from towhee import ops, pipe, DataCollection

if __name__ == '__main__':
    # create image embeddings and build index
    p = (
        pipe.input('file_name')
        .map('file_name', 'img', ops.image_decode.cv2())
        .map('img', 'vec', ops.image_text_embedding.clip(model_name='clip_vit_base_patch32', modality='image'))
        .map('vec', 'vec', ops.towhee.np_normalize())
        .map(('vec', 'file_name'), (), ops.ann_insert.faiss_index('./faiss', 512))
        .output()
    )

    for f_name in ['https://assets.raribleuserdata.com/prod/v1/image/t_image_cmp_preview/aHR0cHM6Ly9zdGF0aWMubWFudGxlLnh5ei9jaXRpemVuc29mbWFudGxlL2ltYWdlcy81MmRhNjcyODBiMWQ4NmI0MDNkNWZlNmQ4YjM5YmZlNjgzODlhZWJhLnBuZw==',
                   'https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9zdGF0aWMubWFudGxlLnh5ei9jaXRpemVuc29mbWFudGxlL2ltYWdlcy81NTI1YjI1YzcwOGM4ZDA4ZTA2YTFhMTk5ZTg0M2YxNTA2OTYzODJjLnBuZw==',
                   'https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9zdGF0aWMubWFudGxlLnh5ei9jaXRpemVuc29mbWFudGxlL2ltYWdlcy80MjgyMmZkOWM1NWU4MGMyMWJiNzkzMjdkMzIxNWZmYzI3ZGI0NTQxLnBuZw==']:
        p(f_name)

    # Flush faiss data into disk.
    p.flush()
    # search image by text
    decode = ops.image_decode.cv2('rgb')
    p = (
        pipe.input('text')
        .map('text', 'vec', ops.image_text_embedding.clip(model_name='clip_vit_base_patch32', modality='text'))
        .map('vec', 'vec', ops.towhee.np_normalize())
        # faiss op result format:  [[id, score, [file_name], ...]
        .map('vec', 'row', ops.ann_search.faiss_index('./faiss', 3))
        .map('row', 'images', lambda x: [decode(item[2][0]) for item in x])
        .output('text', 'images')
    )

    DataCollection(p('a girl')).show()

