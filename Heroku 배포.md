# Heroku 배포

## 1. 사전준비

### 1.1 Github Repo 생성

- 배포할 프로잭트 하나만 관리하고 있는 새로운 폴더로 진행해야 함.
  - 절대 TIL 안에 있는 프로젝트로 진행하면 안됨!

#### 1.1.1 Repo 생성

#### 1.1.2 .gitignore 등록

- `.gitignore.io`에서 `django`, `venv` 를 입력하고 결과값을 `.gitignore` 작성

#### 1.1.3 현재 install된 모듈들을 txt 파일로 저장

```bash
# 기존 프로잭트의 install 목록을 생성
$ pip freeze > requirements.txt
```

```bash
# 새로운 프로잭트에 requirements.txt 파일을 복사해 와서
$ pip install -r requirements.txt
```

#### 1.1.4 원격 저장소 업로드

```bash
$ pip install django-heroku
```

```python
# settings.py
...

import django_heroku
django_heroku(locals())
```

### 1.2 환경변수 관리
- 토큰값이 노출되는 것을 방지한다.
- DEBUG 값을 바꾸어 사용자가 우리 서버의 구조를 볼 수 없게 한다.

```bash
$ pip install python-decouple
```

```python
# settins.py
SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG')
```

- `.env` 생성

  ```
  SECRET_KEY='token key'
  DEBUG=True
  ```
  
- 파일 구조


![image-20191125130859239](C:%5CUsers%5Cstudent%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20191125130859239.png)

### 1.3 django-heroku



## 2. 배포 설정

### 2.1 Procfile

```bash
$ pip install gunicorn
```



- intall 목록 갱신

```bash
$ pip freeze > requirments.txt
```





- heroku cli 64bit 설치
- vs 코드를 껐다 키고

```bash
$ heroku login
```

```bash
$ heroku create

Creating app... done, ⬢ still-caverns-72924
https://still-caverns-72924.herokuapp.com/ | https://git.heroku.com/still-caverns-72924.git
```

```bash
$ git remote -v

heroku  https://git.heroku.com/still-caverns-72924.git (fetch)
heroku  https://git.heroku.com/still-caverns-72924.git (push)
origin  https://github.com/hasuikhs/django-deploy.git (fetch)
origin  https://github.com/hasuikhs/django-deploy.git (push)
```



```bash
$ heroku config:set SECRET_KEY='token key'
$)5a6은(는) 예상되지 않았습니다.

$ heroku config:set DEBUG=True
Setting DEBUG and restarting ⬢ still-caverns-72924... done, v3
DEBUG: True
```





![image-20191125111535573](C:%5CUsers%5Cstudent%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20191125111535573.png)

## 3. 배포

```bash
$ heroku config:set DISABLE_COLLECTSTATIC=1
```



```bash
$ git push heroku master
```



```bash
$ heroku run python manage.py makemigrations
```

- 오류 발생시

  ```bash
  $ heroku config:set DISABLE_COLLECTSTATIC=1
  ```

```bash
$ heroku run python manage.py migrate
```



```bash
$ heroku open
```

