# 디렉터리 구조
```
├── __init__.py
├── __pycache__
├── accounts # API server : 유저 관리 (회원가입, 로그인)
├── beastTamers # back office API
├── bulletinBoard # API server : 문의 게시판
├── celery.py  # 이메일 레디스 비동기큐로 보내기 위한 celery
├── new_storage.py
├── storages.py # 배포 S3 storage 설정
├── urls.py
└── work_out # API server : 운동 타입, 로그 관리
```
