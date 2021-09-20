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

### 20.08.20
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
        - PK(primary Key)
        <br>- 404 - http Method
<br>-path convertor : 여러 객체의 url을 계층적으로 다룰 수 있도록 도와주는 도구
<br>-views.py의 pk 변수명과 urls.py의 변수명은 같아야한다


<!--이게 detail.html 아직 들어가면 오류 뜸 <a href="{% url 'update' designer.id %}" class="btn btn-sm btn-outline-secondary">정보 수정</a>
                            <a href="{% url 'delete' designer.id %}" class="btn btn-sm btn-outline-danger">정보 삭제</a>-->

### 21.08.20
<br>
nav바, 푸터 드뎌 계속 안만들어도 된다ㅜㅜ<br>
중복코트를 base.hrml에 만들어 놓고 미리 갖고 와서 새 페이지 만들기!!!<br>
<br>
base.html에 상속>타이틀 설정 > css도 설정 > block content
<br>
<br>

> {% extends 'base.html %} -> {% block title %}제목{% endblock %} -> {% block link %}{% static 'page/home.html(연결 파일) %}{% endblock %} -> {% block content %} {% endblock %}

### 25.08.20
<br>
GET / POST
get -> data를 'url'에 포함 시켜 전송, 길이 제약 ㅇ, 캐싱 가능(read에서 활용)
post -> 무조건 보안이 좋은 건 아닌데 겟보다는 좋다.길이 제약 x, 캐싱 불가(create, update에서 활용)
참고: HTTP Method/RESTful

#### create/update/delete/
create 새로운 객체를 생성해서 data를 저장
update 정보 수정이 필요한 객체를 찾아 data저장
둘 다 포스트 사용
delete 제거가 필요한 객체를 찾아 삭제
redirect - render의 차이점
render는 항상 요청과 함께 무슨 값을 반환하는 반면, redirect는 주소만 이동을 시켜줌
### 26.08.20
get/post
클라이언트에서 서버로 요청을 보내는 방법
리드는 겟
크리에이트나 업데이트는 포스트 권장
- 패키지 종속성 관리 : 내 패키지를 어떤 버전으로 사용하고 있는 지 알려주는 것

패키지 설치 : pip install -r requirements.txt
패키지 정의 : pip freeze > requirements.txt
