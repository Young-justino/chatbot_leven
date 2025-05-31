# 1. 학습데이터의 질문과 chat의 질문의 유사도를 레벤슈타인 거리를 이용해 구한다.
# 2. chat의 질문과 레벤슈타인 거리와 가장 유사한 학습데이터의 질문의 인덱스를 구한다.
# 3. 학습데이터의 인덱스의 답으로 chat의 답변을 채택한 뒤 출력한다.
import pandas as pd

# 문자열 a와 b 사이의 레벤슈타인 거리를 구하는 함수를 정의
def calc_distance(a, b):
    if a == b: return 0
    a_len = len(a)
    b_len = len(b)
    if a == "": return b_len
    if b == "": return a_len
    matrix = [[] for i in range(a_len+1)] # 리스트 컴프리헨션을 사용하여 1차원 초기화
    for i in range(a_len+1): # 0으로 초기화
        matrix[i] = [0 for j in range(b_len+1)]  # 리스트 컴프리헨션을 사용하여 2차원 초기화
    # 0일 때 초깃값을 설정
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[0][j] = j
    # 표 채우기 --- (※2)
    #print(matrix,'----------')
    for i in range(1, a_len+1):
        ac = a[i-1]
        # print(ac,'=============')
        for j in range(1, b_len+1):
            bc = b[j-1] 
            # print(bc)
            cost = 0 if (ac == bc) else 1  #  파이썬 조건 표현식 예:) result = value1 if condition else value2
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     # 문자 제거: 위쪽에서 +1
                matrix[i][j-1] + 1,     # 문자 삽입: 왼쪽 수에서 +1   
                matrix[i-1][j-1] + cost # 문자 변경: 대각선에서 +1, 문자가 동일하면 대각선 숫자 복사
            ])
            #print(matrix)
        #print(matrix,'----------끝')
    return matrix[a_len][b_len]

# 챗봇 클래스를 정의
class levenChatbot:
    # 챗봇 객체 초기화 메서드
    def __init__(self,filepath):
        self.questions, self.answers = self.load_data(filepath)
    
    # csv파일로부터 질문과 답변 데이터를 불러오는 메서드
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data["Q"].tolist()
        answers = data["A"].tolist()
        return questions, answers

    # chat의 질문과 레벤슈타인 거리가 가장 가까운 학습데이터 질문의 인덱스를 구하는 메서드
    def find_answer(self, input_sentence):
        # 사용자 입력과 기존 질문 사이의 레벤슈타인 거리를 계산
        distances = [calc_distance(input_sentence, question) for question in self.questions]
        # 가장 레벤슈타인 거리가 가까운 기존 질문의 인덱스를 찾음
        min_index = distances.index(min(distances))
        # 해당 인덱스에 해당하는 답변을 반환
        return self.answers[min_index]

# 데이터 파일의 경로를 지정합니다.
filepath = 'ChatbotData.csv'

# 챗봇 객체를 생성합니다
chatbot = levenChatbot(filepath)

# '종료'라는 입력이 나올 때까지 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프를 실행합니다.

while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_answer(input_sentence)
    print('Chatbot:', response)
    # csv파일로부터 질문과 답변 데이터를 불러오는 메서드
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data["Q"].tolist()
        answers = data["A"].tolist()
        return questions, answers

    # chat의 질문과 레벤슈타인 거리가 가장 가까운 학습데이터 질문의 인덱스를 구하는 메서드
    def find_answer(self, input_sentence):
        # 사용자 입력과 기존 질문 사이의 레벤슈타인 거리를 계산
        distances = [calc_distance(input_sentence, question) for question in self.questions]
        # 가장 레벤슈타인 거리가 가까운 기존 질문의 인덱스를 찾음
        min_index = distances.index(min(distances))
        # 해당 인덱스에 해당하는 답변을 반환
        return self.answers[min_index]

# 데이터 파일의 경로를 지정합니다.
filepath = 'ChatbotData.csv'

# 챗봇 객체를 생성합니다
chatbot = levenChatbot(filepath)

# '종료'라는 입력이 나올 때까지 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프를 실행합니다.

while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_answer(input_sentence)
    print('Chatbot:', response)