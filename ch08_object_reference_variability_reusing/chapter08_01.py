# 8.1 변수는 상자가 아니다

a = [1,2,3]
b = a
a.append(4)
print(b)

# 변수는 오른쪽 부터 할당된다
class Gizmo:
    def __init__(self):
        print('Ginzo id: %d'% id(self))

x = Gizmo()
y = Gizmo()*10 # Gizmo는 생성되었지만 *10에서 에러가 나서 y에 어떤 변수도 할당되지 않았다.

