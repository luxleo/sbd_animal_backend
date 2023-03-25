# 디렉터리 구조
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

# 
