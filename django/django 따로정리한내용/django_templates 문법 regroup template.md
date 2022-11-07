regroup template 태그를 이용하여 모든 사용자의 리뷰 사진을 가져오고 그 사용자 마다의 리뷰 사진들을 각자쓴 목록들로 가져오는 기능을 추하였습니다.
```accounts/reviewlist.html
{% regroup reviews by user.username as dates_items %}

{% for date in dates_items %}

  <div class="changelog-day">

    <h3 class="changelog-heading">

      <b>{{ date.grouper }}</b>

    </h3>

    {% for changelog in date.list %}

      <img src="{{ changelog.image.url }}" alt="{{ changelog.image }}" style="border: 4px solid rgba(221, 177, 177, 0.396); border-radius: 1rem;">

    </p>

  {% endfor %}

</div>

{% endfor %}
```
이걸 사용해 보니 그룹화하여 제가 원하는 db 필들의 내용들을 가져올수 있었습니다.
또한 grouper를 통해 모든 유저들을 가져올수 있었습니다.

```accounts/views.py
def reviewlist(request):
    users = get_user_model().objects.all()
    reviews = Review.objects.order_by("pk")[:4]

    context = {
        "users": users,
        "reviews": reviews,
    }

    return render(request, "accounts/reviewlist.html", context)
```
