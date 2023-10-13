# 시퀀스의 곱 연산 사용하기

l = [1,2,3,4,5]
print(l*5)
print(5*'abcde')

# 리스트의 리스트 선언하기
board = [['_']*3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

# 잘못된 선언
weird_board = [['_']*3]*3
print(weird_board)
# weird_board[][2]가 전부 'X'로 바뀐다
weird_board[1][2]='X'
print(weird_board)