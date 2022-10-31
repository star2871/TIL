# django 정참조 & 역참조
## Models.py
```
class Product(models.Model):
    name           = models.CharField(max_length=50)
    price          = models.DecimalField(max_digits=10, decimal_places=2)  
    sub_category   = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    label          = models.ManyToManyField('Label', through='ProductLabel')
   
class Category(models.Model):
    name     = models.CharField(max_length=50)
    category = models.ForeignKey('Menu', on_delete=models.CASCADE)
   
class SubCategory(models.Model):
    name     = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
```

## QuerySet 정참조&역참조
> ## 정참조
> ### 내가 참조하는 table 접근
> #### 해당 객체가 다른 객체의 ForeignKey를 가지고 있거나 1:1 관계인 상황에서 참조 하는 경우
> ```
> >> a = Product.objects.get(id=1)
> >> b = a.sub_category.name
> >> print(b)
> >> # output '배쓰 밤'
> ```
> #### `select_related()` 없이 바로 `relation` 중인 객체 정보를 볼 수 있다.
> #### 그럼 어떤 상황에 왜 `select_related()`를 사용하는 걸까?
> #### Hit(Database에 query를 요청하는 횟수)를 최소화하여 성능을 높인다.
> #### 한번의 Hit로 관계데이터를 가져오는 것과 같다.

> ## select_related
> ```
> >> a = Product.objects.select_related('sub_category').get(id=1)
> >> a.sub_category.name
> >> # output '배쓰 밤'
> ```

> ## 역참조
> ### 나를 참조하는 table 접근
> #### 다른 객체가 ForeignKey를 가지고 있거나 N:N 관계인 상황, 해당 객체를 참조하고 있는 다른 객체를 참조하려는 경우
> ```
> >> a = Category.objects.get(id=1)
> >> b = a.subcategory_set.all()[0].name
> >> # output '배쓰 밤'
> ```
> ### `너무나 헷갈리는 역참조, 역참조의 상황 생각해보기`
> 1. #### Subcategory는 여러 Product를 가진다.
> 2. #### Product는 Subcategory를 참조한다.
> 3. #### Product마다 정참조의 방식으로 주인인 Subcategory의 정보(name)을 얻을 수 있다.
> 4. #### Subcategory의 data를 기준으로 하나의 SubCategory가 소유한 Product를 얻으려면
> 5. #### product_id를 기준으로 filter를 걸 수는 있으나 Product table에 대한 QuerySet만 얻을 수 있다.
> 6. #### SubCategory data와 Product data를 동시에 가진 QuerySet을 얻으려면 어떻게 해야할까?
