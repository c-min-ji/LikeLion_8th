### 18.08.20
models.py -> 모델명의 첫 글자는 무조건 대문자!
-> class 로 정해줌
> 예) class Designer(models.Model):
        image = models.ImageField(upload_to = 'images/')
        name = models.CharField(max_length = 50)
        address = models.CharField(max_length = 255)
        ...
-> python manage.py makemigrations
-> python mange.py migrate

db가 알아 듣도록 번역하기(makemigrations(+특정 app))-> 번역한 내용을 db에 적용(migratee)

username = cminji
ps=0703

### 20.08.20`
### query set
- 객체가 엄청 많을 때는 어떻게 알려줄까?
- 한번에 넘겨주는 메소드가 있다!: <br>
        1. Model의 존재 알려주기<br>
        - from .models import Designer<br>
        2. Queryset을 Templates로 보내기<br>
        - def home(request):<br>
        designer = Designer.objects.all()
        <br>return render(request, 'home.html', {'designers': designers})

- 관계형 데베<br>
PK(primary Key)

404 - http Method


views.py의 pk 변수명과 urls.py의 변수명은 같아야한다


<!--이게 detail.html 아직 들어가면 오류 뜸 <a href="{% url 'update' designer.id %}" class="btn btn-sm btn-outline-secondary">정보 수정</a>
                            <a href="{% url 'delete' designer.id %}" class="btn btn-sm btn-outline-danger">정보 삭제</a>-->