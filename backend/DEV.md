# Bookshelf API documentation

## Getting started




# Todo:

Add swagger definitions based on:
* https://medium.com/@sean_bradley/add-swagger-ui-to-your-python-flask-api-683bfbb32b36

Maybe interesting:
* https://github.com/flasgger/flasgger


# Testing:

## Manual Testing:

### Positiv working curls

```shell
curl http://127.0.0.1:5000/books\?page\=1
```

```shell
curl http://127.0.0.1:5000/book\/24
```

```shell
curl --location --request POST 'http://127.0.0.1:5000/book' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title": "book title",
	"author": "author name",
	"rating": 5
}'
```

```shell
curl http://127.0.0.1:5000/book\/28 -X PATCH -H "Content-Type: application/json" -d '{"rating": "3"}'
```

```shell
curl http://127.0.0.1:5000/book\/28 -X DELETE
```

## Error raising curls

**404**

```shell
curl http://127.0.0.1:5000/book\/300 -X DELETE
```

**400**

```shell
curl http://127.0.0.1:5000/book\/300 -X PATCH -H "Content-Type: application/json" -d '{"rating": "3"}'
```

**422**

```shell
curl --location --request POST 'http://127.0.0.1:5000/book/create' \
--header 'Content-Type: application/json' \
--data-raw '{
	"title": "book title",
	"author": "author name",
  "vogel": 0193
}'
```

**405**

```shell
curl http://127.0.0.1:5000/book\/300 -X POST -H "Content-Type: application/json" -d '{"rating": "3"}'
{
  "error": 405,
  "message": "Not allowed",
  "success": false
}
```
