from . import (
    AccountMethods, AuthMethods, DownloadMethods, DialogMethods, ChatMethods,
    MessageMethods, UploadMethods, ButtonMethods, UpdateMethods,
    MessageParseMethods, UserMethods, SoroushPlusBaseClient
)
from .extra import ExtraMethods


class SoroushClient(
    AccountMethods, AuthMethods, DownloadMethods, DialogMethods, ChatMethods,
    MessageMethods, UploadMethods, ButtonMethods, UpdateMethods,
    MessageParseMethods, UserMethods, SoroushPlusBaseClient, ExtraMethods
):
    pass
