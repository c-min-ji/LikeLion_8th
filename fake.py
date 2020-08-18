#파일명이 faker(즉, pip이름이랑 같으면)이면 에러난다
from faker import Faker

# 한국 ko_KR/중국 zh_CN/일본 ja_JP/영어 en_US/독일 de_DE/프랑스 fr_FR/스페인 es_ES
myfake = Faker()

# myfake.seed(n)은 왜 안되고 Faker.seed(n)은 되는 거지? 
# TypeError: Calling `.seed()` on instances is deprecated. Use the class method `Faker.seed()` instead. ㅉㅏ식..
Fake.seed(1)

for i in range(1, 10):
    print(myfake.name()) 
    print(myfake.address())
    print(myfake.text()) 
    print(myfake.sentence())
    print(myfake.random_number())

# faker로 글쓰는 법....(야매)
# views.py에 가서 def create(request): post.title 이랑 post.body 를 post.title = myfake.name()이런식으로 바꿔서 add post>제출하기 반복클릭..
# 글 안쓰는 대신 클릭해야하는 댓가가 따름....더 쉬운 방법이 있을 것같음...