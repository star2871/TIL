### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT * FROM playlist_track A ORDER BY PlaylistId  DESC LIMIT 5;
```
```
PlaylistId  TrackId
----------  -------
18          597
17          3290
17          2096
17          2095
17          2094
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT TrackID, Name FROM tracks B ORDER BY TrackId  ASC LIMIT 5;

``` 
```
PlaylistId  Name
----------  -----------------------
18          Now's The Time
17          The Zoo
17          Flying High Again
17          Crazy Train
17          I Don't Know
17          Looks That Kill
17          Live To Win
17          Ace Of Spades
17          Creeping Death
17          For Whom The Bell Tolls
```

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT PlaylistId, Name FROM A
JOIN B ON A.TrackId = B.TrackId
WHERE PlaylistId = 10 ORDER BY Name DESC LIMIT 5; 

``` 
```
PlaylistId  Name
----------  ------------------------
10          Women's Appreciation
10          White Rabbit
10          Whatever the Case May Be
10          What Kate Did
10          War of the Gods, Pt. 2
```

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*) 
FROM B INNER JOIN artists 
    ON B.Composer = artists.Name;
```
```
COUNT(*)
--------
402
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*) 
FROM B LEFT JOIN artists 
    ON B.Composer = artists.Name;

```
```
COUNT(*)
--------
3503
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
만약 A, B 테이블이 있다면 INNER JOIN은 두테이블의 교집합이고 LEFT JOIN은 B를 포함하지않는 A만을 나타내기 때문에 행의 개수가 다르다.
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceLineId, InvoiceId FROM invoice_items
ORDER BY InvoiceId ASC LIMIT 5;

```
```
InvoiceLineId  InvoiceId
-------------  ---------
1              1
2              1
3              2
4              2
5              2 
```

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceId, CustomerId FROM invoices
ORDER BY InvoiceId ASC LIMIT 5;

``` 
```
InvoiceId  CustomerId
---------  ----------
1          2
2          4
3          8
4          14
5          23
```


### 10. 각 invoice_items에 해당하는 invoices 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT invoice_items.InvoiceLineId, invoice_items.InvoiceId FROM invoices INNER JOIN invoice_items ON invoices.InvoiceId=invoice_items.InvoiceId ORDER BY invoice_items.InvoiceId DESC LIMIT 5;

``` 
```
InvoiceLineId  InvoiceId
-------------  ---------
2240           412
2239           411
2238           411
2237           411
2236           411
```

### 11. 각 invoices에 해당하는 customers 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT invoices.InvoiceId, invoices.CustomerId 
FROM invoices INNER JOIN customers
ON invoices.InvoiceId = customers.CustomerId
ORDER BY InvoiceId DESC LIMIT 5;
``` 
```
InvoiceId  CustomerId
---------  ----------
59         17
58         13
57         11
56         9
55         8
```

### 12. 각 invoice_items(상품)을 포함하는 invoices(송장)와 해당 invoices를 받을 customers(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT A.InvoiceLineId, A.InvoiceId, C.CustomerId
FROM invoice_items A 
    INNER JOIN invoices B
        ON A.InvoiceId = B.InvoiceId 
    INNER JOIN customers C
        ON B.CustomerId = C.CustomerId
ORDER BY A.InvoiceId DESC 
LIMIT 5;
```
```
InvoiceLineId  InvoiceId  CustomerId
-------------  ---------  ----------
2240           412        58
2226           411        44
2227           411        44
2228           411        44
2229           411        44
```


### 13. 각 customers가 주문한 invoice_items의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT C.CustomerId, count(*) AS '개수' FROM invoice_items A
INNER JOIN (
    SELECT * FROM invoices B
    INNER JOIN customers C
    ON B.CustomerId = C.CustomerId
) C
ON A.InvoiceId = C.InvoiceId
GROUP BY C.CustomerId
ORDER BY C.CustomerId ASC
LIMIT 5;
```
```
CustomerId  개수
----------  --
1           38
2           38
3           38
4           38
5           38
```


