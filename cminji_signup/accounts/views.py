from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
#add
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token

# Create your views here.
def signup(request):
    if request.method == 'POST': #포스트 메소드 요청이고
        if request.POST['password1'] == request.POST['password2']: #패스워드 1, 2가 같으면
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) #만들고
            user.is_active = False #유저가 액티베이트 안돼있으면
            user.save() #저장
            current_site = get_current_site(request)
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_title = "계정 활성화 확인 이메일"
            mail_to = request.POST["email"]
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
            #auth.login(request, user) #이게 아마 로그인 바로 되게하는 기능같음 참고 블로그:https://ssungkang.tistory.com/entry/Django-10-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EB%A1%9C%EA%B7%B8%EC%9D%B8%EB%A1%9C%EA%B7%B8%EC%95%84%EC%9B%83-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
            #return redirect('accounts') #어카운트(/accounts)로 이동
            return render(request, 'accounts.html', { 'error': 'Please check your account activiation e-mail' }) 
    
    return render(request, 'signup.html') #아니면 signup 다시 보여줌

def login(request):
    if request.method == 'POST': # 먼저 이미 가입된 사람인지 확인
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: # 이미 가입된 사람이라면
            auth.login(request, user) # 로그인하고
            return redirect('accounts') # 어카운트로 이동시킴
        else: # 가입 안 되어있으면
            return render(request, 'login.html', {'error': 'username or password is incorrect.'}) # 에러 표시하고 로그인 페이지 새로고침
    else:
        return render(request, 'login.html') # POST요청아니면 로그인페이지 새로고침

def logout(request):
    auth.logout(request)
    return redirect('accounts')

def accounts(request):
    return render(request, 'accounts.html')

def userpage(request):
    if request.user.is_authenticated:
        return render(request, 'userpage.html')
    else:
        return render(request, 'accounts.html', { 'error': 'Only site member can access userpage.' })


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return render(request, 'accounts.html', { 'error': 'Your Accounts is activate'})
    else:
        return render(request, 'accounts.html', { 'error': '계정 활성화 오류'})
    return 
