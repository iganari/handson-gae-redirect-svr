# Hands On App Engine Redirect Server 

## 概要

App Engine でリダイレクトサーバを構築するハンズオン

## 1. App Engine のデプロイ

```
export _gc_pj_id='Your Google Cloud Project ID'
```
```
gcloud app create --region asia-northeast1 --project ${_gc_pj_id}
```
```
gcloud app deploy redirect-google/app.yaml --project ${_gc_pj_id}
gcloud app browse -s redirect-yahoo --project ${_gc_pj_id}


gcloud app deploy redirect-yahoo/app.yaml --project ${_gc_pj_id}
gcloud app browse -s redirect-google --project ${_gc_pj_id}
```


![](./_img/01.png)



+ test

```
$ gcloud app browse -s redirect-yahoo --project ${_gc_pj_id}

Did not detect your browser. Go to this link to view your app:
https://redirect-yahoo-dot-{{ Your Google Cloud Project ID }}.an.r.appspot.com
```
```
$ curl -I https://redirect-yahoo-dot-{{ Your Google Cloud Project ID }}.an.r.appspot.com

HTTP/2 301 
content-type: text/html; charset=utf-8
location: https://www.yahoo.co.jp
x-cloud-trace-context: 42249280de62cf2bbecca09bdd9622a4;o=1
content-length: 233
date: Wed, 31 May 2023 21:59:00 GMT
server: Google Frontend

```

## 2. カスタムドメインの設定

WIP