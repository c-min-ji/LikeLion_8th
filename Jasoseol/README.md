## 27.08.20
# JssProject

ORM : 파이썬을 SQl문처럼 쓸 수 있게 번역해줌.<br>
* django project ->(sql)<-(orm) db<br>
* object : 사용자의 id, update date etc를 이루는 말

* ex) 어떤 object CRUD해조! 하면 데베가 요청받아서 삭제해주면 장고프로젝트는 삭제 완료 오케!
<hr>

-python manage.py makemigrations/ 데베가 알아들을 수 있는 번역파일 생성<br>
-python manage.py migrate/ 번역파일 생성뒤에 번역파일들을 참조하여 원하는 대로 데베구성을 해달라고 데베에게 말한다
<hr>

settings.py에 원하는 데베 연결가능(db종류: mtsql, oracle, postgresqpl...)
<hr>

### model만들 때, 쓰는 단어들 

- primary key: auto Field<br>
- 문자열 : CharField, TextField, SlugField<br>
- 숫자 : InntegerField, PositiveIntegerField, FloatField<br>
- 날짜/ 시간 : DateField, TimeField, DateTimeField<br>
- 참/ 거짓 : BooleanField, NullBooleanField<br>
- 파일 : FileField, ImageField, FilePathField
<hr>

model추가 혹은 변경사항생겼을 때, makemigrations


## 17.09.20
<hr>

> ModelForm<br>
모델에 대응하는 html폼을 만들어줌<br>
데이터를 생성하거나 업데이트가 간편<br>
폼을 다루는 법을 배워야함.

> django template filter 구글에 치고 공식문서 들어가보면 필요한 필터 볼 수 있셈!

### pk(primary key)
> 각각의 오브젝트가 가져야하는 단일 식별자 예) 주민등록번호, 학번...

자소설 3강에서 할 거 : 디테일, 수정, 삭제