# 5.9 함수 애너테이션

def clip(text:str, max_len:'int > 0'=80) -> str:
    """max_len 앞이나 뒤의 마지막 공백에서 잘라낸 텍스트를 반환한다."""
    end=None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_before = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
        if end is None:
            end = len(text)
        return text[:end].rstrip()
    
# 해당 애너테이션은 어떤 기능도 수행하지 않으면서
# 함수 객체의 함수인 __annotations__속성에 전부 저장된다

from inspect import signature
sig = signature(clip)
print(sig.return_annotation)

for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13) # str문과 비슷하지만 문자열로 된 객체를 생성하여 반환함 ex) 'datetime.datetime(2017, 9, 27, 0, 0)'
    print(note, ':',param.name, '=', param.default)
    