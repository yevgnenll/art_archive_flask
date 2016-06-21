### art_archive를 api로 설계

**우리 API는 다음 method를 사용합니다**

* **GET**: 서버에서 데이터를 찾아옵니다.
* **POST**: 서버에 데이터를 입력합니다.


### art_archive의 Endpoint


| Action | HTTP method | URI |
| ------------- | ------------- | ------------- |
| 작품의 list | GET | /api/images/?page=page&count=count |
| 작품 입력 | POST | /api/images/ |


### art_archive의 Resources


| Resource |  URI |
| ------------- | ------------- |
| 작품의 list |  /api/images/ |


#### 1. 작품 list 보여주기

* **URL**

/api/images/?user_id=<user_id>

* **Method**

    `GET`

* **URL Param**

**required:**<br>
user_id=[Integer] 해당 작품을 upload한 user_id<br>

1. user_id가 있는경우
    - 작품제목: title
    - 원본 이미지 url: image_url
    - 썸네일 이미지 url: thumbnail

    ex.) /api/images/?user_id=1


2. user_id가 없는경우
    요청실패: 아래의 Erro Response 참조


* **SUCCESS Response**

    * **code**: 200<br>
    **content**: 1페이지에 10개 이하의 데이터 전송
    <pre>   { 
            title: 작품의 제목[String] ,
            image_url: 작품 이미지[URL],
            thumbnail: 작품의 썸네일 이미지[URL],
            }
    </pre>

* **ERROR Response**
    

    * **code**: 404<br>
    **content**: <pre> { error: "Data doesn't exist" } </pre> 

    * **code**: 500<br>
    **content**: <pre> { error: "Internal Server Error" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/images/?user_id=1",
    dataType: "json",
    type : "GET",
    success : function(result) {
      console.log(result);
    }
  });

  
```

--------


#### 5. 작품 입력하기 api

작품 하나의 정보를 입력합니다. 


* **URL**

    /api/images/

* **Method**

    `POST`

* **URL Param**

    * **required:**<br>
    title=[String] <br>
    image_data=[Image] <br>
    user_id=[Integer]


* **SUCCESS Response**

    * **code**: 201<br>
    **content**:
    <pre> { result: "Created"} </pre>

* **ERROR Response**

    * **code**: 400<br>
    **content**: <pre> { error: "Bad Request" } </pre> 

    * **code**: 500<br>
    **content**: <pre> { error: "Internal Server Error" } </pre> 


* **Sample Code**

```
  $.ajax({
    url: "/api/images/",
    dataType: "json",
    type : "POST",
    data : {
        "title": "작품제목",
        "image_url": image file,
        "user_id": 1,
        }
    success : function(result) {
      console.log(result);
    }
  });

```
