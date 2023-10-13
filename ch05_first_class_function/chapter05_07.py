# 5.7 위치 매개변수에서 키워드 전용 매개변수까지

# **attrs를 통해서 key=value의 쌍에 대해서 dictionary로 인수를 전달한다.
# *를 통해서 튜플로 value만 전달한다.
def tag(name, *content, cls=None, **attrs):
    '''하나 이상의 HTML 태그를 생성한다'''
    print(name,content,cls,attrs)
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str =''.join(' %s="%s"'%(attr,value)
                          for attr, value
                          in sorted(attrs.items()))
    
    else:
        attr_str=''
    if content:
        return '\n'.join('<%s%s>%s</%s>'%(name,attr_str,c,name) for c in content)
    
    else:
        return '<%s%s />'%(name,attr_str)
    
print(tag('br')) # name에 전달
print(tag('p','hello')) # p는 name에 hello는 content에 전달
print(tag('p','hello','world')) # 첫번째 이후의 모든 인수는 content에 전달된다
print(tag('p','hello',id=33)) # 없는 변수인 id는 attr에 전달
print(tag('p','hello','world',cls='sidebar')) # cls를 통해서 2번째 인수부터 3번째 인수까지 content에 들어가고 cls에 대입됨
print(tag(content='testing',name='img')) # name=tag가 들어가지고 attrs={'content':'testing'}이 들어가짐
my_tag={'name':'img','title':'Sunset Boulevard','src':'sunset.jpg','cls':'framed'}
print(tag(**my_tag)) # key로 전달 받을 수 있는 인수(name, cls)를 제외한 모든 인수가 attr에 들어감