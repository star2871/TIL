### 한 개의 게시물에 여러 이미지 업로드하는 방법에 대해서 정리해 보았다. 먼저 간단하게 Django 세팅 후에 모델을 생성해주었다

# Django 세팅하기
```
# settings.py

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	...
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Pillow라는 파이썬 이미지 라이브러리도 설치해준다
```
pip install pillow
```

> ## Pillow는 여러 이미지 파일 포맷을 지원하고, 이미지 내부 데이타를 엑세스할 수 있게 하며 다양한 이미지 처리 기능을 제공한다. 또한, 이미지 크기를 변형하거나 회전 및 Transform, 그리고 필터링 등 다양한 이미지 프로세싱 작업들을 할 수 있다

# Model 만들기
## 게시글이 여러 이미지를 가지고 있는 1:N 구조의 모델을 생성했다.
```
class Post(BaseModel):
    id = models.AutoField(primary_key=True)
    to_date = models.DateField()
    title = models.CharField(max_length=50)
    content = models.TextField()
    status = models.CharField(max_length=2)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __int__(self):
        return self.id

    class Meta:
        db_table = 'post'


# 이미지 업로드 경로
def image_upload_path(instance, filename):
    return f'{instance.post.id}/{filename}'


class PostImage(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to=image_upload_path)

    def __int__(self):
        return self.id

    class Meta:
        db_table = 'post_image'
```

# Serializer 만들기
```
# forms.py
class PostImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = PostImage
        fields = ['image']


class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

	# 게시글에 등록된 이미지들 가지고 오기
    def get_images(self, obj):
        image = obj.image.all() 
        return PostImageSerializer(instance=image, many=True, context=self.context).data

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        instance = Post.objects.create(**validated_data)
        image_set = self.context['request'].FILES
        for image_data in image_set.getlist('image'):
            PostImage.objects.create(post=instance, image=image_data)
        return instance
```

> ## Serializers.py 에는 이미지를 직렬화할 PostImageSerializer을 두고, Post에서 글과 이미지를 한번에 입력받아서 저장할 것이기 때문에 PostImageSerializer를 images 변수를 두어 가져온다.

> ## get_images 함수는 게시글에 등록된 이미지들을 가지고 오기 위해 생성해주었다. PostImage 모델에서 related_name='image'이라고 선언해주었기 때문에 post 인스턴스(obj)에서 바로 image을 사용해서 역참조를 할수 있다. PostImage 객체에 이미지 데이터를 담아서 반환해준다.

> ## create 메소드에서는 파일 형식으로 전달받은 데이터틀 images_data에 따로담아놓고 post 객체를 생성한다. images_data 변수 안에 담겨 있는 image 리스트들을 .getlist(‘image’) 를 통해서 접근하여 for문으로 image_data를 하나씩 꺼내온다. 그 후 좀 전에 생성한 post 객체와, image_data를 PostImage 객체에 담아 생성한다.

# View 작성하기
### 마지막으로 viewset을 사용해서 view를 작성해주고 url에도 라우터를 이용해서 추가해준다.
```
# views.py

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    pagination_class = CustomResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
    permission_classes = [IsSuperUserOrReadOnly]

# urls.py

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
```