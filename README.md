18.08.20
models.py -> 모델명의 첫 글자는 무조건 대문자!
-> class 로 정해줌
예) class Designer(models.Model):
        image = models.ImageField(upload_to = 'images/')
        name = models.CharField(max_length = 50)
        address = models.CharField(max_length = 255)
        ...
-> python manage.py makemigrations
-> python mange.py migrate

db가 알아 듣도록 번역하기(makemigrations(+특정 app))-> 번역한 내용을 db에 적용(migratee)

username = cminji
ps=0703