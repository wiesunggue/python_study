# 5.8 매개변수에 대한 정보 읽기
# ????? 뭐지 이해못함

import bobo

@bobo.query('/')
def hello(person):
    return 'Hello %s!' %person


from clip import clip
from inspect import signature
