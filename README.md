[프로젝트 설명 노션 링크](https://supreme-marimba-1b5.notion.site/SBD-ANIMAL-d8982e6459f846fc9420ed03b3e61847)
# 디렉터리 구조 /
```
├── backup_data # 개발환경 DB를 production 서버에 올리기 위한 백업 폴더입니다.
├── dev_db      # 개발환경 DB(docker 바인딩 volume을 위한 폴더)
│   ├── mysql
│   └── redis
├── prod_docker_compose # 로컬 및 서버에서 구동할 docker compose 
│   ├── prod
│   └── test
└── sbd_animal  # 프로젝트 root
    ├── config 
    ├── dist # admin Page (react build)
    ├── docs # 개발중 해결한 에러, 배운점 기록
    ├── media
    ├── sbd_admin_react # admin Page template(with react)
    ├── sbd_animal # API (with DRF)
    ├── settings # 개발,배포 세팅
    └── static
```

# 디렉터리 구조 /sbd_animal
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

