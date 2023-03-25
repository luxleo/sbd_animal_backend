### what I learn[dev]
```text
1. github도 유저를 미리 만들고, is_active=False등의 방식으로
활성화 시키지 않은 상태에서 이메일 인증을 거쳐 활성화한다.
 - 잘못된 메일 주소를 검증하는 기능은 없는듯하고, 코드가 도착하지 않을시에
 이메일 주소업데이트 방식이나 resend방식을 지원한다.
 - response로 verfication code가 전송되서 간단하게 암호화 적용했다.
2. PK를 email field로 지정하려 했으나 가입 할때 마다 재정렬이 일어나서,
 - 비효율적일 거 같아 철회, username, email field 두개 모두로 로그인 가능하도록 할 것
3. email, password로 가입 먼저 진행후에 username, height,weight지정하는 걸로
4. 함수형 view에서 @api_view => @permission_classes => function => 이 순서로 지정해야
 - 정상적으로 적용된다.
5. custom authenticate 함수에서 CSRFCheck()를 호출하여 사용했을때 
 - response가 제공되지 않았다는 에러가 뜨면서 처리 되지 않아 기존의 authenticate
 - 함수를 그대로사용
6.query시 caching을 사용하여 불필요한 db hit 방지:
 - qs = User.objects.filter(id=8)
 - res = list(qs) => db 조회
 - user = res[0] => caching된 결과 그대로 사용
7. query_set.get(SOME_LOOK_UP) => 없으면 DoesNotExist Error발생
 - query_set.filter(SOME_LOOK_UP) 이용하자. (속도도 get의 추가로직이 없어 10% 빠름)
8. model field 수정 table삭제 할 필요없이 migrate가능하다.
9. pdb.set_trace() 로 view함수 디버깅한다.
10. django_debug_toolbar error: urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
 - 위와 같이 순서 바꿔서 해결했다. -> 모든 url이 읽어지고난후에 추가되서 임포트가 안돼었다고한다.
 - reference: https://github.com/jazzband/django-debug-toolbar/issues/568
11. mysql db 에서는 postgresql과 달리 distinct on api를 지원하지 않아
- 로직으로 구현하였다. ('/work_out/views.py/graph_log_list')
12. django.models.DateField(auto_now_add=True)에서
- 그냥 save시 인자로 넘긴 created_at은 무시 되므로
- create후에 instance.created_at = data["created_at"]으로 update후
- .save()호출 한다.
- for data in dummy_data:
    workout_type = data["workout_type"]
    new_log = Log.objects.create(athlete=some_user,workout_type=workout_type
    ,**data)
    new_log.created_at = data["created_at"]
    new_log.save()
13. settings.AUTH_USER_MODEL vs django.contrib.auth.get_user_model()의 차이
- 전자는 string을 반환하고 후자는 class를 반환한다.
14. template variable 을 string안에서 사용할때 {{}}로 감싸지 않는다.
- base.html
15. s3의 static, media root 수정 해주기 위해서 s3boto extended custom class
작성.
-  sbd_animal/storages.py
```

### what I learn[prod]
```text
1.docker compose 에서는 docker run 으로 실행할때와 달리
- cmd에 지속되는 작업이 없으면 exit with status 0로 종료하게된다.
- 방지하기위해 stdin_open=true로 설정 해준다
2. docker container 내에서 서로간 연결될때 로컬 호스트는
- 컨테이너 네임으로 접근한다.
3. docker container os check:
- uname -a
- cat /etc/issue
4. dockerfile build context는 dockerfile위치로 지정되어있고
- 부모 dir의 위치를 전달시 알아듣지 못하므로 
- docker build -t <tagName> -f dir/dir/Dockerfile 
- 등으로 컨텍스트를 전달하고자 하는 부모로 부터 시작한다.
- Dockerfile 내부의 COPY 등은 부모 경로로 부터 시작한다.
5. docker container 내에서 프로젝트 실행시
- settings.DEBUG는 internel_ips에 등록된 ip에서만 실행되는데
- 로컬 호스트에서 컨테이너 접근시 등록되어있지 않으면(서로 ip address가 다르므로)
- settings.DEBUG = False처리 된다.
6. docker container 자체적으로 ip를 가지고 settings.docker_dev.py
- 에서 socket module로 host ip를 container 내부의 internal_ips에 등록
- 하였지만 base.html template이 src="http:localhost"를 반환하기 때문에
- container 내부에서 돌아가는 react와 연결되는 것이 아니라 host의 5173포트에서
- 연결해야한다.
7. Dockerfile 이름은 appname.Dockerfile로 지을수 있고
- 해당 파일에 대한 dockeringnore 파일은 appname.Dockerfile.dockerignore로 작성 가능하다.
8. lightsail instance와 lightsail storage(bucket) 연결하는 과정에서
- cors issue가 있었는데. request header의 origin이 호스트 ip로 기록 되어서
- TemplateView에서 html파일 렌더링후 소스파일 까지 같이 보낸다고 생각하였으나 response header에 allow-origin
- 추가하여 해결하려했으나 그런 과정은 소스코드에 없었고
- storage를 s3로 바꾸어 cors 설정해서 해결하였다.
- lightsail storage는 아직 지원하지 않는다. 
9. data migrate local -> prod
- 1.python3 manage.py dumpdata --exclude contenttypes
- 2.python3 manage.py loaddata FILEPATH
- contenttypes가 기본으로 생성되므로 중복되어서 옮길때 삭제 해준다.
11. docker image build시 플랫폼을 바꾸어 주어야한다.
- 개발 환경은 macOS -> prod 환경은 linux 
12. 서로 다른 도메인간에 쿠키 설정을 위해서
- SAME_SITE=None, SECURE=True(https로만 통신)로 설정한다.
```

### todo:
```text
1. history에서 스크롤 다운시 nextpage return 하기
2. history에서 운동별로 조회하기
3. dashboard 1주일 ,1개월 ,6개월 순으로 데이터 로드하기 [O]
4. log,rep 수정 구현하기 [O]
5. email 보냈을때 verification code 불일치 하는거 해결하기 [O]
6. colab에서 더미데이터 만들때 percentile필드도 채워 넣기 [O]
7. response에 cache응답하기 []
8. dummy data 랜덤이 아니라 발전형으로 만들기 [O]
```
### todo[deploy]:
```text
1. mysql,s3 연결[0]
2-0. docker container 내의 django 앱에서 localhost로 부터 수신한 ip 표시[]
2-1. django Dockerfile, celery Dockerfile redis Dockerfile작성[]
2-2. env에 등록할 키들 따로 처리[O].
2-3. docker-compose for prod[O]
2-4. docker-compose push to docker hub[O]
3. lightsail instance 위에 docker-compose file 올리기[O]
4. client axios url 배포된 lightsail ip로 수정[O]
5. vercel에 client배포[O]
```

celery operation command:
celery -A sbd_animal worker -l INFO   

  

