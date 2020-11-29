from urllib.parse import urlparse

from django.core.validators import RegexValidator
from django.db import models

# validator: vcard アプリケーションのURLを示すキーかどうか
vakudate_vcard_key = RegexValidator(
    regex=r"^vcard/",
    message=("This key isn't a vcard resource"),
)

# validator: URL が vcard アプリケーションのホスト名かどうか
validate_vcard_host = RegexValidator(
    regex=r"^http(s)?://(([0-9a-zA-Z]*.cloudfront.net)|(c.)?stat100.ameba.jp)/.*",
    message=("This url isn't a url of vcard resources"),
)


class Resource(models.Model):
    """
    vcardサーバから取得したリソースを管理するモデルクラス

    fields:
        key: オブジェクトキー
        url: オブジェクトキーを見つけるのに使ったURL
        fetched: データをGCSにfetchし終えてるならTrue
        created: 作成日時
    """

    key = models.CharField(
        max_length=1024,
        null=False,
        blank=True,
        db_index=True,
        unique=True,
        primary_key=True,
        validators=[vakudate_vcard_key],
    )
    url = models.URLField(
        max_length=1024,
        null=False,
        blank=False,
        validators=[validate_vcard_host],
    )
    fetched = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        """初期化処理 (URLからkeyを生成している)"""
        super().__init__(*args, **kwargs)

        # key = 格納されているオブジェクトのURLのパス部分
        # これが vcard/ から始まっていないといけない
        pathstr = urlparse(self.url).path
        if len(pathstr) > 6 and pathstr[:7] == "/vcard/":
            self.key = pathstr[1:]  # GCSのKeyに"/"は要らない
        else:
            raise ValueError("This url isn't a url of vcard resources")

    def __str__(self) -> str:
        """文字列値"""
        return self.key
