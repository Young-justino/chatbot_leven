# 1. �н��������� ������ chat�� ������ ���絵�� ������Ÿ�� �Ÿ��� �̿��� ���Ѵ�.
# 2. chat�� ������ ������Ÿ�� �Ÿ��� ���� ������ �н��������� ������ �ε����� ���Ѵ�.
# 3. �н��������� �ε����� ������ chat�� �亯�� ä���� �� ����Ѵ�.
import pandas as pd

# ���ڿ� a�� b ������ ������Ÿ�� �Ÿ��� ���ϴ� �Լ��� ����
def calc_distance(a, b):
    if a == b: return 0
    a_len = len(a)
    b_len = len(b)
    if a == "": return b_len
    if b == "": return a_len
    matrix = [[] for i in range(a_len+1)] # ����Ʈ ����������� ����Ͽ� 1���� �ʱ�ȭ
    for i in range(a_len+1): # 0���� �ʱ�ȭ
        matrix[i] = [0 for j in range(b_len+1)]  # ����Ʈ ����������� ����Ͽ� 2���� �ʱ�ȭ
    # 0�� �� �ʱ갪�� ����
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[0][j] = j
    # ǥ ä��� --- (��2)
    #print(matrix,'----------')
    for i in range(1, a_len+1):
        ac = a[i-1]
        # print(ac,'=============')
        for j in range(1, b_len+1):
            bc = b[j-1] 
            # print(bc)
            cost = 0 if (ac == bc) else 1  #  ���̽� ���� ǥ���� ��:) result = value1 if condition else value2
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     # ���� ����: ���ʿ��� +1
                matrix[i][j-1] + 1,     # ���� ����: ���� ������ +1   
                matrix[i-1][j-1] + cost # ���� ����: �밢������ +1, ���ڰ� �����ϸ� �밢�� ���� ����
            ])
            #print(matrix)
        #print(matrix,'----------��')
    return matrix[a_len][b_len]

# ê�� Ŭ������ ����
class levenChatbot:
    # ê�� ��ü �ʱ�ȭ �޼���
    def __init__(self,filepath):
        self.questions, self.answers = self.load_data(filepath)
    
    # csv���Ϸκ��� ������ �亯 �����͸� �ҷ����� �޼���
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data["Q"].tolist()
        answers = data["A"].tolist()
        return questions, answers

    # chat�� ������ ������Ÿ�� �Ÿ��� ���� ����� �н������� ������ �ε����� ���ϴ� �޼���
    def find_answer(self, input_sentence):
        # ����� �Է°� ���� ���� ������ ������Ÿ�� �Ÿ��� ���
        distances = [calc_distance(input_sentence, question) for question in self.questions]
        # ���� ������Ÿ�� �Ÿ��� ����� ���� ������ �ε����� ã��
        min_index = distances.index(min(distances))
        # �ش� �ε����� �ش��ϴ� �亯�� ��ȯ
        return self.answers[min_index]

# ������ ������ ��θ� �����մϴ�.
filepath = 'ChatbotData.csv'

# ê�� ��ü�� �����մϴ�
chatbot = levenChatbot(filepath)

# '����'��� �Է��� ���� ������ ������� �Է¿� ���� ê���� ������ ����ϴ� ���� ������ �����մϴ�.

while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '����':
        break
    response = chatbot.find_answer(input_sentence)
    print('Chatbot:', response)
    # csv���Ϸκ��� ������ �亯 �����͸� �ҷ����� �޼���
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data["Q"].tolist()
        answers = data["A"].tolist()
        return questions, answers

    # chat�� ������ ������Ÿ�� �Ÿ��� ���� ����� �н������� ������ �ε����� ���ϴ� �޼���
    def find_answer(self, input_sentence):
        # ����� �Է°� ���� ���� ������ ������Ÿ�� �Ÿ��� ���
        distances = [calc_distance(input_sentence, question) for question in self.questions]
        # ���� ������Ÿ�� �Ÿ��� ����� ���� ������ �ε����� ã��
        min_index = distances.index(min(distances))
        # �ش� �ε����� �ش��ϴ� �亯�� ��ȯ
        return self.answers[min_index]

# ������ ������ ��θ� �����մϴ�.
filepath = 'ChatbotData.csv'

# ê�� ��ü�� �����մϴ�
chatbot = levenChatbot(filepath)

# '����'��� �Է��� ���� ������ ������� �Է¿� ���� ê���� ������ ����ϴ� ���� ������ �����մϴ�.

while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '����':
        break
    response = chatbot.find_answer(input_sentence)
    print('Chatbot:', response)