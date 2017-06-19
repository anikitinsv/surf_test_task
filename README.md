# surf_test_task
Run:
Python 3.6.1

$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ cd book_rent
$ python manage.py runserver



http util is httpie packet.

API references:

now in db:
admin/surfstudio
guest/surfstudio


Get auth token for user:
$ http POST http://127.0.0.1:8000/get-auth-token/ username=guest password=surfstudio

HTTP/1.0 200 OK
Allow: POST, OPTIONS
Content-Length: 52
Content-Type: application/json
Date: Mon, 19 Jun 2017 07:09:18 GMT
Server: WSGIServer/0.2 CPython/3.6.1
X-Frame-Options: SAMEORIGIN

{
    "token": "dd7cb7d58af62716c16b0922c0061a11591f8b19"
}


Users:
    $ http GET http://127.0.0.1:8000/users/ 'Authorization: Token dd7cb7d58af62716c16b0922c0061a11591f8b19'

    HTTP/1.0 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Length: 87
    Content-Type: application/json
    Date: Mon, 19 Jun 2017 06:53:45 GMT
    Server: WSGIServer/0.2 CPython/3.6.1
    Token: dd7cb7d58af62716c16b0922c0061a11591f8b19
    Vary: Accept
    X-Frame-Options: SAMEORIGIN

- http://127.0.0.1:8000/users/ - get current authorizated user, return json, like:
    [
        {
            "created": "2017-06-18T20:57:06.616450Z",
            "id": 2,
            "login": 2,
            "money": 346.65000000000003
        }
    ]

Books:
- http://127.0.0.1:8000/books/ - return all books for authorizated user if book.rent_estimate_time > now
    example:

    $http GET http://127.0.0.1:8000/books/ 'Authorization: Token dd7cb7d58af62716c16b0922c0061a11591f8b19'

    HTTP/1.0 200 OK
    Allow: GET, POST, PUT, PATCH, HEAD, OPTIONS
    Content-Length: 650
    Content-Type: application/json
    Date: Mon, 19 Jun 2017 06:57:23 GMT
    Server: WSGIServer/0.2 CPython/3.6.1
    Token: dd7cb7d58af62716c16b0922c0061a11591f8b19
    Vary: Accept
    X-Frame-Options: SAMEORIGIN


    [
        {
            "author": [
                {
                    "first_name": "Petr",
                    "id": 2,
                    "second_name": "Petrovich",
                    "surname": "Petrov"
                }
            ],
            "book_name": "Bukvar",
            "count_month_rented": 4,
            "id": 2,
            "owner": 2,
            "rent_cost": 9.95,
            "rent_estimate_time": "2017-10-19T05:50:53.603487Z"
        },
        {
            "author": [
                {
                    "first_name": "Ivan",
                    "id": 1,
                    "second_name": "Ivanovich",
                    "surname": "Ivanov"
                }
            ],
            "book_name": "Bukvar",
            "count_month_rented": 2,
            "id": 3,
            "owner": 2,
            "rent_cost": 7.95,
            "rent_estimate_time": "2017-08-19T05:52:16.210191Z"
        },
        {
            "author": [
                {
                    "first_name": "Ivan",
                    "id": 1,
                    "second_name": "Ivanovich",
                    "surname": "Ivanov"
                }
            ],
            "book_name": "Bukvar",
            "count_month_rented": 7,
            "id": 4,
            "owner": 2,
            "rent_cost": 13.95,
            "rent_estimate_time": "2018-01-19T05:58:21.632617Z"
        }
    ]

- http://127.0.0.1:8000/books/<book_id> - return book, if owner == current_user. Rent_estimate_time is ignored.
  Example:

    $ http GET http://127.0.0.1:8000/books/2/ 'Authorization: Token dd7cb7d58af62716c16b0922c0061a11591f8b19'

    HTTP/1.0 200 OK
    Allow: GET, POST, PUT, PATCH, HEAD, OPTIONS
    Content-Length: 217
    Content-Type: application/json
    Date: Mon, 19 Jun 2017 06:19:23 GMT
    Server: WSGIServer/0.2 CPython/3.6.1
    Token: dd7cb7d58af62716c16b0922c0061a11591f8b19
    Vary: Accept
    X-Frame-Options: SAMEORIGIN

    [
        {
            "author": [
                {
                    "first_name": "Petr",
                    "id": 2,
                    "second_name": "Petrovich",
                    "surname": "Petrov"
                }
            ],
            "book_name": "Bukvar",
            "count_month_rented": 4,
            "id": 2,
            "owner": 2,
            "rent_cost": 9.95,
            "rent_estimate_time": "2017-10-19T05:50:53.603487Z"
        }
    ]

PUT operations:

$ http PUT http://127.0.0.1:8000/books/4/ 'Authorization: Token dd7cb7d58af62716c16b0922c0061a11591f8b19' count_month_rented=7

HTTP/1.0 200 OK
Allow: GET, POST, PUT, PATCH, HEAD, OPTIONS
Content-Length: 215
Content-Type: application/json
Date: Mon, 19 Jun 2017 07:06:47 GMT
Server: WSGIServer/0.2 CPython/3.6.1
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "author": [
        {
            "first_name": "Ivan",
            "id": 1,
            "second_name": "Ivanovich",
            "surname": "Ivanov"
        }
    ],
    "book_name": "Bukvar",
    "count_month_rented": 7,
    "id": 4,
    "owner": 2,
    "rent_cost": 13.95,
    "rent_estimate_time": "2018-01-19T07:06:47.629301"
}
