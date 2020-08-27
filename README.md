## 27.08.20

ORM : 파이썬을 SQl문처럼 쓸 수 있게 번역해줌.
django project ->(sql) db
                <-(orm)
object : 사용자의 id, update date etc

ex) 어떤 object CRUD해조! 하면 데베가 요청받아서 삭제해주면 장고프로젝트는 삭제 완료 오케!

python manage.py makemigrations/ 데베가 알아들을 수 있는 번역파일 생성
python manage.py migrate/ 번역파일 생성뒤에 번역파일들을 참조하여 원하는 대로 데베구성을 해달라고 데베에게 말한다

settings.py에 원하는 데베 연결가능(db종류: mtsql, oracle, postgresqpl...)

primary key: auto Field
문자열 : CharField, TextField, SlugField
숫자 : InntegerField, PositiveIntegerField, FloatField
날짜/ 시간 : DateField, TimeField, DateTimeField
참/ 거짓 : BooleanField, NullBooleanField
파일 : FileField, ImageField, FilePathField

model추가 혹은 변경사항생겼을떄makemigrations