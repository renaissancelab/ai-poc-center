#!/usr/bin/env python3

from towhee import pipe, ops

if __name__ == '__main__':
    img_embedding = (
        pipe.input('url')
        .map('url', 'img', ops.image_decode.cv2()) # param1: input param2:
        .map('img', 'embedding', ops.image_embedding.timm(model_name='resnet50')) # resnet50 is model
        .output('embedding')
    )

    url = 'https://userblink.csdnimg.cn/31267e05470241e79669b6d283015a54.jpg'
    res = img_embedding(url).get()
    print(res)