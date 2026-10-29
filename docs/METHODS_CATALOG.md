# SPlusPy — فهرست استخراج‌شدهٔ API

این فایل به‌صورت ایستا از سورس پایتون تولید شده است. نام‌بردن از یک متد به معنی تضمین پشتیبانی endpoint سمت سرویس نیست. نام‌های دارای پیشوند `_` داخلی محسوب می‌شوند و عمداً در فهرست عمومی اصلی نمایش داده نشده‌اند.

## `_updates/entitycache.py`

### کلاس `EntityCache`

- `def set_self_user(self, id, bot, hash)`
- `def get(self, id)`
- `def extend(self, users, chats)`
- `def put(self, entity)`
- `def retain(self, filter)`

## `_updates/messagebox.py`

### توابع عمومی

- `def next_updates_deadline()`
- `def epoch()`

### کلاس `PtsInfo`

- `def from_update(cls, update)`

### کلاس `MessageBox`

- `def load(self, session_state, channel_states)`
- `def session_state(self)`
- `def is_empty(self) -> bool`
- `def check_deadlines(self)`
- `def force_get_difference(self, reason='reconnect')`
- `def reset_deadlines(self, entries, deadline)`
- `def reset_channel_deadline(self, channel_id, timeout)`
- `def set_state(self, state, reset=True)`
- `def try_set_channel_state(self, id, pts)`
- `def try_begin_get_diff(self, entry, reason)`
- `def end_get_diff(self, entry)`
- `def process_updates(self, updates, chat_hashes, result)`
- `def apply_pts_info(self, update, *, reset_deadlines)`
- `def get_difference(self)`
- `def apply_difference(self, diff, chat_hashes)`
- `def apply_difference_type(self, diff, chat_hashes)`
- `def end_difference(self)`
- `def get_channel_difference(self, chat_hashes)`
- `def apply_channel_difference(self, request, diff, chat_hashes)`
- `def end_channel_difference(self, request, reason: PrematureEndReason, chat_hashes)`

## `_updates/session.py`

### کلاس `EntityType`

- `def canonical(self)`

### کلاس `Entity`

- `def is_user(self)`
- `def is_group(self)`
- `def is_broadcast(self)`
- `def from_str(cls, string: str)`
- `def from_bytes(cls, blob)`

## `admin.py`

### کلاس `ChatAdmin`

- `async def ban_user(self, chat, user, until_date=None)`
- `async def mute_user(self, chat, user, until_date=None)`
- `async def unmute_user(self, chat, user)`
- `async def purge_messages(self, chat, limit=100, *, revoke=True)`
- `async def bulk_action(self, chat, action, user_ids, *, delay=0.5)`
- `async def get_admin_log(self, chat, *, limit=100)`

## `afk.py`

### کلاس `AFKManager`

- `def is_afk(self) -> bool`
- `def message(self) -> str`
- `def since(self) -> Optional[float]`
- `def duration(self) -> Optional[str]`
- `def replied_count(self) -> int`
- `def set(self, message: Optional[str]=None, *, auto_disable: Optional[bool]=None) -> None`
- `def disable(self) -> None`
- `def process(self, event: Any) -> Any`

## `client/soroushclient.py`

### کلاس `SoroushClient`

- `def http_robot(self) -> Optional['Robot']`
- `async def connect(self)`

## `client/telegrambaseclient.py`

### کلاس `SoroushPlusBaseClient`

- `def loop(self: 'SoroushClient') -> asyncio.AbstractEventLoop`
- `def disconnected(self: 'SoroushClient') -> asyncio.Future`
- `def flood_sleep_threshold(self)`
- `def flood_sleep_threshold(self, value)`
- `def fsm(self: 'SoroushClient')`
- `def fsm(self: 'SoroushClient', manager)`
- `def plugins(self: 'SoroushClient')`
- `def load_plugin(self: 'SoroushClient', plugin)`
- `def unload_plugin(self: 'SoroushClient', plugin)`
- `def reload_plugin(self: 'SoroushClient', plugin)`
- `def load_plugins_from(self: 'SoroushClient', path, recursive: bool=True)`
- `def unload_all_plugins(self: 'SoroushClient') -> int`
- `def scheduler(self: 'SoroushClient')`
- `def afk(self: 'SoroushClient')`
- `def mirror(self: 'SoroushClient')`
- `async def connect(self: 'SoroushClient') -> None`
- `def is_connected(self: 'SoroushClient') -> bool`
- `def disconnect(self: 'SoroushClient')`
- `def set_proxy(self: 'SoroushClient', proxy: typing.Union[tuple, dict])`

## `crypto/aes.py`

### کلاس `AES`

- `def decrypt_ige(cipher_text, key, iv)`
- `def encrypt_ige(plain_text, key, iv)`

## `crypto/aesctr.py`

### کلاس `AESModeCTR`

- `def encrypt(self, data)`
- `def decrypt(self, data)`

## `crypto/authkey.py`

### کلاس `AuthKey`

- `def key(self)`
- `def key(self, value)`
- `def calc_new_nonce_hash(self, new_nonce, number)`

## `crypto/cdndecrypter.py`

### کلاس `CdnDecrypter`

- `async def prepare_decrypter(client, cdn_client, cdn_redirect)`
- `def get_file(self)`
- `def check(data, cdn_hash)`

## `crypto/factorization.py`

### کلاس `Factorization`

- `def factorize(cls, pq)`
- `def gcd(a, b)`

## `crypto/rsa.py`

### توابع عمومی

- `def get_byte_array(integer)`
- `def add_key(pub, *, old)`
- `def encrypt(fingerprint, data, *, use_old=False)`

## `enums.py`

### کلاس `MessageMediaType`

- `def from_media(cls, media)`
- `def from_message(cls, message)`
- `def is_image(self)`
- `def is_video(self)`
- `def is_audio(self)`
- `def is_document(self)`
- `def is_sticker(self)`
- `def is_animation(self)`
- `def is_media(self)`

## `errors/__init__.py`

### توابع عمومی

- `def rpc_message_to_error(rpc_error, request)`

## `events/__init__.py`

### توابع عمومی

- `def register(event: 'typing.Optional[typing.Union[EventBuilder, typing.Type[EventBuilder]]]'=None) -> 'typing.Callable'`
- `def unregister(callback: 'typing.Callable', event: 'typing.Optional[typing.Union[EventBuilder, typing.Type[EventBuilder]]]'=None) -> int`
- `def is_handler(callback: 'typing.Callable') -> bool`
- `def list(callback: 'typing.Callable') -> typing.List['EventBuilder']`

## `events/album.py`

### کلاس `AlbumHack`

- `def extend(self, messages)`
- `async def deliver_event(self)`

### کلاس `Album`

- `def build(cls, update, others=None, self_id=None)`
- `def filter(self, event)`

## `events/chataction.py`

### کلاس `ChatAction`

- `def build(cls, update, others=None, self_id=None)`

## `events/common.py`

### توابع عمومی

- `def name_inner_event(cls)`

### کلاس `EventBuilder`

- `def build(cls, update: 'typing.Any', others: 'typing.Optional[typing.List]'=None, self_id: 'typing.Optional[int]'=None) -> 'typing.Optional[EventCommon]'`
- `async def resolve(self, client: 'SoroushClient') -> None`
- `async def filter(self, event: 'EventCommon') -> 'typing.Optional[EventCommon]'`

### کلاس `EventCommon`

- `def client(self) -> 'SoroushClient'`
- `def stringify(self)`
- `def to_dict(self)`

## `events/messagedeleted.py`

### کلاس `MessageDeleted`

- `def build(cls, update, others=None, self_id=None)`

## `events/messageedited.py`

### کلاس `MessageEdited`

- `def build(cls, update, others=None, self_id=None)`

## `events/messageread.py`

### کلاس `MessageRead`

- `def build(cls, update, others=None, self_id=None)`
- `def filter(self, event)`

## `events/newmessage.py`

### کلاس `NewMessage`

- `def build(cls, update, others=None, self_id=None)`
- `def filter(self, event)`

## `events/raw.py`

### کلاس `Raw`

- `async def resolve(self, client)`
- `def build(cls, update, others=None, self_id=None)`
- `def filter(self, event)`

## `events/userupdate.py`

### کلاس `UserUpdate`

- `def build(cls, update, others=None, self_id=None)`

## `extensions/binaryreader.py`

### کلاس `BinaryReader`

- `def read_byte(self)`
- `def read_int(self, signed=True)`
- `def read_long(self, signed=True)`
- `def read_float(self)`
- `def read_double(self)`
- `def read_large_int(self, bits, signed=True)`
- `def read(self, length=-1)`
- `def get_bytes(self)`
- `def tgread_bytes(self)`
- `def tgread_string(self)`
- `def tgread_bool(self)`
- `def tgread_date(self)`
- `def tgread_object(self)`
- `def tgread_vector(self)`
- `def close(self)`
- `def tell_position(self)`
- `def set_position(self, position)`
- `def seek(self, offset)`

## `extensions/html.py`

### توابع عمومی

- `def parse(html: str) -> Tuple[str, List[TypeMessageEntity]]`
- `def unparse(text: str, entities: Iterable[TypeMessageEntity]) -> str`

### کلاس `HTMLToSoroushPlusParser`

- `def handle_starttag(self, tag, attrs)`
- `def handle_data(self, text)`
- `def handle_endtag(self, tag)`

## `extensions/markdown.py`

### توابع عمومی

- `def parse(message, delimiters=None, url_re=None)`
- `def unparse(text, entities, delimiters=None, url_fmt=None)`

## `extensions/messagepacker.py`

### کلاس `MessagePacker`

- `def append(self, state)`
- `def extend(self, states)`
- `async def get(self)`

## `filters.py`

### کلاس `FilterModule`

- `def private(self) -> Filter`
- `def group(self) -> Filter`
- `def channel(self) -> Filter`
- `def me(self) -> Filter`
- `def text(self) -> 'TextFilter'`
- `def link(self) -> Filter`
- `def media(self) -> Filter`
- `def photo(self) -> Filter`
- `def video(self) -> Filter`
- `def document(self) -> Filter`
- `def audio(self) -> Filter`
- `def voice(self) -> Filter`
- `def sticker(self) -> Filter`
- `def animation(self) -> Filter`
- `def new_chat_members(self) -> Filter`
- `def left_chat_member(self) -> Filter`
- `def command(self, commands: 'typing.Union[str, typing.List[str]]', prefixes: 'typing.Union[str, typing.List[str]]'='/') -> CommandFilter`
- `def regex(self, pattern: str) -> RegexFilter`
- `def word(self, words: 'typing.Union[str, typing.List[str]]') -> WordFilter`
- `def callback_data(self, data: 'typing.Optional[str]'=None, *, pattern: 'typing.Optional[str]'=None) -> CallbackDataFilter`

## `fsm.py`

### کلاس `FSMStorage`

- `def get_state(self, chat_id: int, user_id: int) -> str`
- `def set_state(self, chat_id: int, user_id: int, state: str) -> None`
- `def get_data(self, chat_id: int, user_id: int) -> Dict[str, Any]`
- `def set_data(self, chat_id: int, user_id: int, data: Dict[str, Any]) -> None`
- `def update_data(self, chat_id: int, user_id: int, data: Dict[str, Any]) -> None`
- `def clear(self, chat_id: int, user_id: int) -> None`
- `def reset(self, chat_id: int, user_id: int) -> None`

### کلاس `FSMState`

- `def add_transition(self, transition: 'FSMTransition') -> None`
- `def transitions(self) -> List['FSMTransition']`

### کلاس `FSMTransition`

- `def matches(self, event: Any) -> bool`

### کلاس `FSMContext`

- `def state(self) -> str`
- `async def set_state(self, state: str) -> None`
- `def get_data(self) -> Dict[str, Any]`
- `async def set_data(self, data: Dict[str, Any]) -> None`
- `async def update_data(self, **kwargs: Any) -> None`
- `async def clear(self) -> None`
- `def data(self) -> Dict[str, Any]`

### کلاس `FSMManager`

- `def add_state(self, name: str, handler: Optional[Callable]=None, on_enter: Optional[Callable]=None, on_exit: Optional[Callable]=None, initial: bool=False) -> FSMState`
- `def set_initial_state(self, name: str) -> None`
- `def set_fallback_state(self, name: str) -> None`
- `def set_global_handler(self, handler: Callable) -> None`
- `def add_transition(self, source: str, target: str, trigger: Optional[Union[str, Callable]]=None, on_before: Optional[Callable]=None, on_after: Optional[Callable]=None) -> FSMTransition`
- `def get_state(self, chat_id: int, user_id: int) -> str`
- `async def set_state(self, chat_id: int, user_id: int, state: str) -> None`
- `async def set_data(self, chat_id: int, user_id: int, data: Dict[str, Any]) -> None`
- `def get_data(self, chat_id: int, user_id: int) -> Dict[str, Any]`
- `def clear(self, chat_id: int, user_id: int) -> None`
- `def get_context(self, chat_id: int, user_id: int) -> FSMContext`
- `async def process_event(self, client: Any, event: Any) -> bool`

## `helpers.py`

### توابع عمومی

- `def generate_random_long(signed=True)`
- `def ensure_parent_dir_exists(file_path)`
- `def add_surrogate(text)`
- `def del_surrogate(text)`
- `def within_surrogate(text, index, *, length=None)`
- `def strip_text(text, entities)`
- `def retry_range(retries, force_retry=True)`
- `def generate_key_data_from_nonce(server_nonce, new_nonce)`
- `def get_running_loop()`

## `http_api/callbackquery.py`

### کلاس `HTTPCallbackQuery`

- `def chat_id(self) -> Optional[int]`
- `def message_id(self) -> Optional[int]`
- `async def answer(self, text: Optional[str]=None, show_alert: Optional[bool]=None, url: Optional[str]=None, cache_time: Optional[int]=None) -> bool`

## `http_api/errors.py`

### توابع عمومی

- `def raise_for_status(error_code: int, description: str)`

## `http_api/keyboards.py`

### کلاس `InlineKeyboardBuilder`

- `def add_button(self, text: str, *, url: Optional[str]=None, callback_data: Optional[str]=None, web_app: Optional[Dict[str, Any]]=None, login_url: Optional[Dict[str, Any]]=None, switch_inline_query: Optional[str]=None, switch_inline_query_current_chat: Optional[str]=None, switch_inline_query_chosen_chat: Optional[Dict[str, Any]]=None, pay: Optional[bool]=None, callback_game: Optional[Dict[str, Any]]=None, copy_text: Optional[Dict[str, Any]]=None) -> 'InlineKeyboardBuilder'`
- `def add_url(self, text: str, url: str) -> 'InlineKeyboardBuilder'`
- `def add_callback(self, text: str, callback_data: str) -> 'InlineKeyboardBuilder'`
- `def add_row(self, buttons: Sequence[InlineKeyboardButton]) -> 'InlineKeyboardBuilder'`
- `def new_row(self) -> 'InlineKeyboardBuilder'`
- `def add(self, text: str, **kwargs: Any) -> 'InlineKeyboardBuilder'`
- `def row(self, *buttons: InlineKeyboardButton) -> 'InlineKeyboardBuilder'`
- `def adjust(self, *sizes: int) -> 'InlineKeyboardBuilder'`
- `def paginate(items: Sequence[Any], page: int, max_per_page: int, *, button_factory: Optional[Callable[[Any], InlineKeyboardButton]]=None, prev_text: str='◀ Prev', next_text: str='Next ▶', prev_callback: str='page:prev', next_callback: str='page:next', page_info_text: str='─ {page}/{total} ─') -> 'InlineKeyboardBuilder'`
- `def build(self) -> InlineKeyboardMarkup`
- `def as_markup(self) -> InlineKeyboardMarkup`

### کلاس `ReplyKeyboardBuilder`

- `def add_button(self, text: str, *, request_contact: Optional[bool]=None, request_location: Optional[bool]=None, request_poll: Optional[Dict[str, Any]]=None, web_app: Optional[Dict[str, Any]]=None) -> 'ReplyKeyboardBuilder'`
- `def add_contact_request(self, text: str) -> 'ReplyKeyboardBuilder'`
- `def add_location_request(self, text: str) -> 'ReplyKeyboardBuilder'`
- `def new_row(self) -> 'ReplyKeyboardBuilder'`
- `def add_row(self, buttons: Sequence[KeyboardButton]) -> 'ReplyKeyboardBuilder'`
- `def row(self, *buttons: KeyboardButton) -> 'ReplyKeyboardBuilder'`
- `def adjust(self, *sizes: int) -> 'ReplyKeyboardBuilder'`
- `def build(self) -> ReplyKeyboardMarkup`
- `def as_markup(self) -> ReplyKeyboardMarkup`

## `http_api/message.py`

### کلاس `HTTPMessage`

- `def text(self) -> Optional[str]`
- `def raw_text(self) -> Optional[str]`
- `def is_reply(self) -> bool`
- `def client(self) -> Optional['Robot']`
- `def media_type(self) -> Optional[str]`
- `def file(self)`
- `def chat_id(self) -> Optional[int]`
- `def sender_id(self) -> Optional[int]`
- `def is_private(self) -> bool`
- `def is_group(self) -> bool`
- `def is_channel(self) -> bool`
- `async def respond(self, *args: Any, **kwargs: Any) -> Optional['HTTPMessage']`
- `async def reply(self, *args: Any, **kwargs: Any) -> Optional['HTTPMessage']`
- `async def reply_text(self, text: str, **kwargs: Any) -> Optional['HTTPMessage']`
- `async def reply_photo(self, photo: Any, caption: Optional[str]=None, **kwargs: Any) -> Optional['HTTPMessage']`
- `async def reply_video(self, video: Any, caption: Optional[str]=None, **kwargs: Any) -> Optional['HTTPMessage']`
- `async def reply_audio(self, audio: Any, caption: Optional[str]=None, **kwargs: Any) -> Optional['HTTPMessage']`
- `async def reply_voice(self, voice: Any, caption: Optional[str]=None, **kwargs: Any) -> Optional['HTTPMessage']`
- `async def reply_document(self, document: Any, caption: Optional[str]=None, **kwargs: Any) -> Optional['HTTPMessage']`
- `async def reply_sticker(self, sticker: Any, **kwargs: Any) -> Optional['HTTPMessage']`
- `async def edit(self, *args: Any, **kwargs: Any) -> Optional['HTTPMessage']`
- `async def delete(self, **kwargs: Any) -> bool`
- `async def forward(self, to_chat_id: Any, **kwargs: Any) -> Optional['HTTPMessage']`
- `async def copy(self, to_chat_id: Any, **kwargs: Any) -> Optional['HTTPMessage']`
- `async def pin(self, **kwargs: Any) -> bool`
- `async def unpin(self, **kwargs: Any) -> bool`
- `async def react(self, emoji: str, **kwargs: Any) -> bool`
- `async def get_reply_message(self) -> Optional['HTTPMessage']`
- `async def download(self, file_name: Optional[str]=None, **kwargs: Any) -> Optional[str]`
- `async def download_media(self, *args: Any, **kwargs: Any) -> Optional[str]`
- `async def mark_read(self, **kwargs: Any) -> bool`
- `async def tag_member(self, user: Any, text: Optional[str]=None) -> Optional['HTTPMessage']`
- `async def get_chat(self) -> Optional[Any]`
- `async def get_sender(self) -> Optional[Any]`
- `async def get_input_chat(self) -> None`
- `async def get_input_sender(self) -> None`

## `http_api/robot.py`

### کلاس `Robot`

- `def fsm(self) -> Any`
- `def fsm(self, manager: Any) -> None`
- `def plugins(self) -> Any`
- `def load_plugin(self, plugin: Any) -> Any`
- `def unload_plugin(self, plugin: Any) -> bool`
- `def reload_plugin(self, plugin: Any) -> Any`
- `def load_plugins_from(self, path: Any, recursive: bool=True) -> Any`
- `def unload_all_plugins(self) -> int`
- `def scheduler(self) -> Any`
- `def afk(self) -> Any`
- `def mirror(self) -> Any`
- `async def close(self) -> None`
- `async def download_file(self, file_path: str, destination: Optional[str]=None) -> Optional[str]`
- `def on_message(self, filters: _FilterLike=None, **kwargs: Any) -> Callable`
- `def on_edited_message(self, filters: _FilterLike=None) -> Callable`
- `def on_callback_query(self, filters: _FilterLike=None, *, data: Optional[str]=None, pattern: Any=None) -> Callable`
- `def on_inline_query(self, filters: _FilterLike=None, *, pattern: Any=None) -> Callable`
- `def on_raw_update(self, types: Any=None) -> Callable`
- `def on_error(self, exception_class: type) -> Callable`
- `def add_middleware(self, middleware: Any, index: Optional[int]=None) -> None`
- `def remove_middleware(self, middleware: Any) -> bool`
- `def add_event_handler(self, callback: Callable, event: Any) -> None`
- `def remove_event_handler(self, callback: Callable, event: Any=None) -> int`
- `def run(self) -> None`
- `def add_shutdown_hook(self, hook: Callable) -> None`
- `async def start(self) -> None`
- `async def stop(self) -> None`
- `async def start_webhook(self, host: str='0.0.0.0', port: int=8080, path: str='/webhook') -> None`
- `def run_webhook(self, host: str='0.0.0.0', port: int=8080, path: str='/webhook') -> None`
- `async def getMe(self) -> api_types.User`
- `async def getUpdates(self, offset: Optional[int]=None, limit: Optional[int]=None, timeout: Optional[int]=None, allowed_updates: Optional[List[str]]=None) -> List[api_types.Update]`
- `async def setWebhook(self, url: str, certificate: Optional[Any]=None, ip_address: Optional[str]=None, max_connections: Optional[int]=None, allowed_updates: Optional[List[str]]=None, drop_pending_updates: Optional[bool]=None, secret_token: Optional[str]=None) -> bool`
- `async def deleteWebhook(self, drop_pending_updates: Optional[bool]=None) -> bool`
- `async def getWebhookInfo(self) -> api_types.WebhookInfo`
- `async def sendMessage(self, chat_id: Union[int, str], text: str, parse_mode: Optional[str]=None, entities: Optional[List[Dict[str, Any]]]=None, link_preview_options: Optional[Dict[str, Any]]=None, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, reply_to_message_id: Optional[int]=None, reply_markup: Optional[Any]=None, message_thread_id: Optional[int]=None) -> api_types.Message`
- `async def sendPhoto(self, chat_id: Union[int, str], photo: Any, caption: Optional[str]=None, parse_mode: Optional[str]=None, caption_entities: Optional[List[Dict[str, Any]]]=None, has_spoiler: Optional[bool]=None, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, reply_to_message_id: Optional[int]=None, reply_markup: Optional[Any]=None, message_thread_id: Optional[int]=None) -> api_types.Message`
- `async def sendAudio(self, chat_id: Union[int, str], audio: Any, caption: Optional[str]=None, parse_mode: Optional[str]=None, caption_entities: Optional[List[Dict[str, Any]]]=None, duration: Optional[int]=None, performer: Optional[str]=None, title: Optional[str]=None, thumbnail: Optional[Any]=None, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, reply_to_message_id: Optional[int]=None, reply_markup: Optional[Any]=None, message_thread_id: Optional[int]=None) -> api_types.Message`
- `async def sendDocument(self, chat_id: Union[int, str], document: Any, caption: Optional[str]=None, parse_mode: Optional[str]=None, caption_entities: Optional[List[Dict[str, Any]]]=None, disable_content_type_detection: Optional[bool]=None, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, reply_to_message_id: Optional[int]=None, reply_markup: Optional[Any]=None, message_thread_id: Optional[int]=None) -> api_types.Message`
- `async def sendVideo(self, chat_id: Union[int, str], video: Any, duration: Optional[int]=None, width: Optional[int]=None, height: Optional[int]=None, thumbnail: Optional[Any]=None, caption: Optional[str]=None, parse_mode: Optional[str]=None, caption_entities: Optional[List[Dict[str, Any]]]=None, has_spoiler: Optional[bool]=None, supports_streaming: Optional[bool]=None, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, reply_to_message_id: Optional[int]=None, reply_markup: Optional[Any]=None, message_thread_id: Optional[int]=None) -> api_types.Message`
- `async def sendAnimation(self, chat_id: Union[int, str], animation: Any, duration: Optional[int]=None, width: Optional[int]=None, height: Optional[int]=None, thumbnail: Optional[Any]=None, caption: Optional[str]=None, parse_mode: Optional[str]=None, caption_entities: Optional[List[Dict[str, Any]]]=None, has_spoiler: Optional[bool]=None, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, reply_markup: Optional[Any]=None, message_thread_id: Optional[int]=None) -> api_types.Message`
- `async def sendVoice(self, chat_id: Union[int, str], voice: Any, caption: Optional[str]=None, parse_mode: Optional[str]=None, caption_entities: Optional[List[Dict[str, Any]]]=None, duration: Optional[int]=None, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, reply_to_message_id: Optional[int]=None, reply_markup: Optional[Any]=None, message_thread_id: Optional[int]=None) -> api_types.Message`
- `async def sendVideoNote(self, chat_id: Union[int, str], video_note: Any, duration: Optional[int]=None, length: Optional[int]=None, thumbnail: Optional[Any]=None, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, reply_to_message_id: Optional[int]=None, reply_markup: Optional[Any]=None, message_thread_id: Optional[int]=None) -> api_types.Message`
- `async def sendMediaGroup(self, chat_id: Union[int, str], media: List[Dict[str, Any]], disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, message_thread_id: Optional[int]=None) -> List[api_types.Message]`
- `async def sendLocation(self, chat_id: Union[int, str], latitude: float, longitude: float, horizontal_accuracy: Optional[float]=None, live_period: Optional[int]=None, heading: Optional[int]=None, proximity_alert_radius: Optional[int]=None, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, reply_markup: Optional[Any]=None, message_thread_id: Optional[int]=None) -> api_types.Message`
- `async def sendContact(self, chat_id: Union[int, str], phone_number: str, first_name: str, last_name: Optional[str]=None, vcard: Optional[str]=None, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, reply_markup: Optional[Any]=None, message_thread_id: Optional[int]=None) -> api_types.Message`
- `async def editMessageText(self, chat_id: Union[int, str], message_id: int, text: str, parse_mode: Optional[str]=None, entities: Optional[List[Dict[str, Any]]]=None, link_preview_options: Optional[Dict[str, Any]]=None, reply_markup: Optional[Any]=None) -> api_types.Message`
- `async def editMessageCaption(self, chat_id: Union[int, str], message_id: int, caption: Optional[str]=None, parse_mode: Optional[str]=None, caption_entities: Optional[List[Dict[str, Any]]]=None, reply_markup: Optional[Any]=None) -> api_types.Message`
- `async def editMessageMedia(self, chat_id: Union[int, str], message_id: int, media: Dict[str, Any], reply_markup: Optional[Any]=None) -> api_types.Message`
- `async def editMessageReplyMarkup(self, chat_id: Union[int, str], message_id: int, reply_markup: Optional[Any]=None) -> api_types.Message`
- `async def deleteMessage(self, chat_id: Union[int, str], message_id: int) -> bool`
- `async def deleteMessages(self, chat_id: Union[int, str], message_ids: List[int]) -> bool`
- `async def forwardMessage(self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None) -> api_types.Message`
- `async def copyMessage(self, chat_id: Union[int, str], from_chat_id: Union[int, str], message_id: int, caption: Optional[str]=None, parse_mode: Optional[str]=None, caption_entities: Optional[List[Dict[str, Any]]]=None, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, reply_markup: Optional[Any]=None) -> int`
- `async def getChat(self, chat_id: Union[int, str]) -> api_types.Chat`
- `async def getUserProfilePhotos(self, user_id: int, offset: Optional[int]=None, limit: Optional[int]=None) -> api_types.UserProfilePhotos`
- `async def pinChatMessage(self, chat_id: Union[int, str], message_id: int, disable_notification: Optional[bool]=None) -> bool`
- `async def unpinChatMessage(self, chat_id: Union[int, str], message_id: Optional[int]=None) -> bool`
- `async def sendChatAction(self, chat_id: Union[int, str], action: str, message_thread_id: Optional[int]=None) -> bool`
- `async def answerCallbackQuery(self, callback_query_id: str, text: Optional[str]=None, show_alert: Optional[bool]=None, url: Optional[str]=None, cache_time: Optional[int]=None) -> bool`
- `async def answerInlineQuery(self, inline_query_id: str, results: List[Any], cache_time: Optional[int]=None, is_personal: Optional[bool]=None, next_offset: Optional[str]=None, switch_pm_text: Optional[str]=None, switch_pm_parameter: Optional[str]=None) -> bool`
- `async def setMyCommands(self, commands: List[api_types.BotCommand], scope: Optional[Any]=None, language_code: Optional[str]=None) -> bool`
- `async def deleteMyCommands(self, scope: Optional[Any]=None, language_code: Optional[str]=None) -> bool`
- `async def getMyCommands(self, scope: Optional[Any]=None, language_code: Optional[str]=None) -> List[api_types.BotCommand]`
- `async def sendSticker(self, chat_id: Union[int, str], sticker: Any, disable_notification: Optional[bool]=None, protect_content: Optional[bool]=None, reply_parameters: Optional[Dict[str, Any]]=None, reply_to_message_id: Optional[int]=None, reply_markup: Optional[Any]=None, message_thread_id: Optional[int]=None) -> api_types.Message`
- `async def getStickerSet(self, name: str) -> api_types.StickerSet`
- `async def getFile(self, file_id: str) -> api_types.File`
- `async def get_message(self, chat_id: Union[int, str], message_id: int) -> Optional[HTTPMessage]`

## `http_api/types.py`

### کلاس `InlineKeyboardButton`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `InlineKeyboardMarkup`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `KeyboardButton`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `ReplyKeyboardMarkup`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `ReplyKeyboardRemove`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `ForceReply`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `BotCommand`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `BotCommandScopeDefault`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `BotCommandScopeAllPrivateChats`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `BotCommandScopeAllGroupChats`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `BotCommandScopeAllChatAdministrators`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `BotCommandScopeChat`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `BotCommandScopeChatAdministrators`

- `def to_dict(self) -> Dict[str, Any]`

### کلاس `BotCommandScopeChatMember`

- `def to_dict(self) -> Dict[str, Any]`

## `http_api/utils.py`

### توابع عمومی

- `def escape_markdown(text: str, entity_type: str=None) -> str`
- `def escape_html(text: str) -> str`

## `methods/account/end_takeout.py`

### کلاس `EndTakeout`

- `async def end_takeout(self: 'SoroushClient', success: bool) -> bool`

## `methods/account/takeout.py`

### کلاس `Takeout`

- `def takeout(self: 'SoroushClient', finalize: bool=True, *, contacts: bool=None, users: bool=None, chats: bool=None, megagroups: bool=None, channels: bool=None, files: bool=None, max_file_size: bool=None) -> 'SoroushClient'`

## `methods/auth/edit_2fa.py`

### کلاس `Edit2fa`

- `async def edit_2fa(self: typing.Any, current_password: typing.Optional[str]=None, new_password: typing.Optional[str]=None, *, hint: str='', email: typing.Optional[str]=None, email_code_callback: typing.Optional[typing.Callable[[int], typing.Union[str, typing.Awaitable[str]]]]=None) -> bool`

## `methods/auth/log_out.py`

### کلاس `LogOut`

- `async def log_out(self: typing.Any) -> bool`

## `methods/auth/qr_login.py`

### کلاس `QrLogin`

- `async def qr_login(self: typing.Any, ignored_ids: typing.Optional[typing.List[int]]=None) -> typing.Any`

## `methods/auth/send_code_request.py`

### کلاس `SendCodeRequest`

- `async def send_code_request(self: typing.Any, phone: str, *, code_callback: typing.Optional[typing.Callable[[], typing.Union[str, int]]]=None, _retry_count: int=0) -> typing.Any`

## `methods/auth/sign_in.py`

### کلاس `SignIn`

- `async def sign_in(self: typing.Any, phone: typing.Optional[str]=None, code: typing.Optional[typing.Union[str, int]]=None, *, password: typing.Optional[str]=None, phone_code_hash: typing.Optional[str]=None) -> typing.Any`

## `methods/auth/sign_up.py`

### کلاس `SignUp`

- `async def sign_up(self: typing.Any, code: typing.Union[str, int], first_name: str, last_name: str='', *, phone: typing.Optional[str]=None, phone_code_hash: typing.Optional[str]=None) -> typing.Any`

## `methods/auth/start.py`

### کلاس `Start`

- `def start(self: typing.Any, phone: typing.Union[typing.Callable[[], typing.Union[str, typing.Awaitable[str]]], str]=lambda: input('Please enter your phone: '), password: typing.Union[typing.Callable[[], typing.Union[str, typing.Awaitable[str]]], str]=lambda: getpass.getpass('Please enter your password: '), *, code_callback: typing.Optional[typing.Callable[[], typing.Union[str, int, typing.Awaitable[typing.Union[str, int]]]]]=None, first_name: str='New User', last_name: str='', max_attempts: int=3) -> typing.Any`

## `methods/buttons/build_reply_markup.py`

### کلاس `BuildReplyMarkup`

- `def build_reply_markup(buttons: 'typing.Optional[hints.MarkupLike]') -> 'typing.Optional[types.TypeReplyMarkup]'`

## `methods/chats/action.py`

### کلاس `Action`

- `def action(self: 'SoroushClient', entity: 'hints.EntityLike', action: 'typing.Union[str, types.TypeSendMessageAction]', *, delay: float=4, auto_cancel: bool=True) -> 'typing.Union[_ChatAction, typing.Coroutine]'`

## `methods/chats/edit_admin.py`

### کلاس `EditAdmin`

- `async def edit_admin(self: 'SoroushClient', entity: 'hints.EntityLike', user: 'hints.EntityLike', *, change_info: bool=None, post_messages: bool=None, edit_messages: bool=None, delete_messages: bool=None, ban_users: bool=None, invite_users: bool=None, pin_messages: bool=None, add_admins: bool=None, manage_call: bool=None, anonymous: bool=None, is_admin: bool=None, title: str=None) -> types.Updates`

## `methods/chats/edit_permissions.py`

### کلاس `EditPermissions`

- `async def edit_permissions(self: 'SoroushClient', entity: 'hints.EntityLike', user: 'typing.Optional[hints.EntityLike]'=None, until_date: 'hints.DateLike'=None, *, view_messages: bool=True, send_messages: bool=True, send_media: bool=True, send_stickers: bool=True, send_gifs: bool=True, send_games: bool=True, send_inline: bool=True, embed_link_previews: bool=True, send_polls: bool=True, change_info: bool=True, invite_users: bool=True, pin_messages: bool=True) -> types.Updates`

## `methods/chats/get_admin_log.py`

### کلاس `GetAdminLog`

- `async def get_admin_log(self: 'SoroushClient', *args, **kwargs) -> 'hints.TotalList'`

## `methods/chats/get_participants.py`

### کلاس `GetParticipants`

- `async def get_participants(self: 'SoroushClient', *args, **kwargs) -> 'hints.TotalList'`

## `methods/chats/get_permissions.py`

### کلاس `GetPermissions`

- `async def get_permissions(self: 'SoroushClient', entity: 'hints.EntityLike', user: 'hints.EntityLike'=None) -> 'typing.Optional[custom.ParticipantPermissions]'`

## `methods/chats/get_profile_photos.py`

### کلاس `GetProfilePhotos`

- `async def get_profile_photos(self: 'SoroushClient', *args, **kwargs) -> 'hints.TotalList'`

## `methods/chats/get_stats.py`

### کلاس `GetStats`

- `async def get_stats(self: 'SoroushClient', entity: 'hints.EntityLike', message: 'typing.Union[int, types.Message]'=None)`

## `methods/chats/iter_admin_log.py`

### کلاس `IterAdminLog`

- `def iter_admin_log(self: 'SoroushClient', entity: 'hints.EntityLike', limit: float=None, *, max_id: int=0, min_id: int=0, search: str=None, admins: 'hints.EntitiesLike'=None, join: bool=None, leave: bool=None, invite: bool=None, restrict: bool=None, unrestrict: bool=None, ban: bool=None, unban: bool=None, promote: bool=None, demote: bool=None, info: bool=None, settings: bool=None, pinned: bool=None, edit: bool=None, delete: bool=None, group_call: bool=None) -> _AdminLogIter`
- `async def get_admin_log(self: 'SoroushClient', *args, **kwargs) -> 'hints.TotalList'`

## `methods/chats/iter_participants.py`

### کلاس `IterParticipants`

- `def iter_participants(self: 'SoroushClient', entity: 'hints.EntityLike', limit: float=None, *, search: str='', filter: 'types.TypeChannelParticipantsFilter'=None, aggressive: bool=False) -> _ParticipantsIter`
- `async def get_participants(self: 'SoroushClient', *args, **kwargs) -> 'hints.TotalList'`

## `methods/chats/iter_profile_photos.py`

### کلاس `IterProfilePhotos`

- `def iter_profile_photos(self: 'SoroushClient', entity: 'hints.EntityLike', limit: int=None, *, offset: int=0, max_id: int=0) -> _ProfilePhotoIter`
- `async def get_profile_photos(self: 'SoroushClient', *args, **kwargs) -> 'hints.TotalList'`

## `methods/chats/kick_participant.py`

### کلاس `KickParticipant`

- `async def kick_participant(self: 'SoroushClient', entity: 'hints.EntityLike', user: 'typing.Optional[hints.EntityLike]')`

## `methods/chats/leave_chat.py`

### کلاس `LeaveChat`

- `async def leave_chat(self: 'SoroushClient', entity: 'hints.EntityLike')`

## `methods/dialogs/conversation.py`

### کلاس `Conversation`

- `def conversation(self: 'SoroushClient', entity: 'hints.EntityLike', *, timeout: float=60, total_timeout: float=None, max_messages: int=100, exclusive: bool=True, replies_are_responses: bool=True) -> custom.Conversation`

## `methods/dialogs/delete_dialog.py`

### کلاس `DeleteDialog`

- `async def delete_dialog(self: 'SoroushClient', entity: 'hints.EntityLike', *, revoke: bool=False)`

## `methods/dialogs/edit_folder.py`

### کلاس `EditFolder`

- `async def edit_folder(self: 'SoroushClient', entity: 'hints.EntitiesLike'=None, folder: typing.Union[int, typing.Sequence[int]]=None, *, unpack=None) -> types.Updates`

## `methods/dialogs/get_dialogs.py`

### کلاس `GetDialogs`

- `async def get_dialogs(self: 'SoroushClient', *args, **kwargs) -> 'hints.TotalList'`

## `methods/dialogs/get_drafts.py`

### کلاس `GetDrafts`

- `async def get_drafts(self: 'SoroushClient', entity: 'hints.EntitiesLike'=None) -> 'hints.TotalList'`

## `methods/dialogs/iter_dialogs.py`

### کلاس `IterDialogs`

- `def iter_dialogs(self: 'SoroushClient', limit: float=None, *, offset_date: 'hints.DateLike'=None, offset_id: int=0, offset_peer: 'hints.EntityLike'=types.InputPeerEmpty(), ignore_pinned: bool=False, ignore_migrated: bool=False, folder: int=None, archived: bool=None) -> _DialogsIter`

## `methods/dialogs/iter_drafts.py`

### کلاس `IterDrafts`

- `def iter_drafts(self: 'SoroushClient', entity: 'hints.EntitiesLike'=None) -> _DraftsIter`

## `methods/downloads/download_file.py`

### کلاس `DownloadFile`

- `async def download_file(self: 'SoroushClient', input_location: 'hints.FileLike', file: 'hints.OutFileLike'=None, *, part_size_kb: float=None, file_size: int=None, progress_callback: 'hints.ProgressCallback'=None, dc_id: int=None, key: bytes=None, iv: bytes=None) -> typing.Optional[bytes]`

## `methods/downloads/download_media.py`

### کلاس `DownloadMedia`

- `async def download_media(self: 'SoroushClient', message: 'hints.MessageLike', file: 'hints.FileLike'=None, *, thumb: 'typing.Union[int, types.TypePhotoSize]'=None, progress_callback: 'hints.ProgressCallback'=None) -> typing.Optional[typing.Union[str, bytes]]`

## `methods/downloads/download_profile_photo.py`

### کلاس `DownloadProfilePhoto`

- `async def download_profile_photo(self: 'SoroushClient', entity: 'hints.EntityLike', file: 'hints.FileLike'=None, *, download_big: bool=True) -> typing.Optional[str]`

## `methods/downloads/iter_download.py`

### کلاس `IterDownload`

- `def iter_download(self: 'SoroushClient', file: 'hints.FileLike', *, offset: int=0, stride: int=None, limit: int=None, chunk_size: int=None, request_size: int=MAX_CHUNK_SIZE, file_size: int=None, dc_id: int=None)`

## `methods/extra/add_contact.py`

### کلاس `AddContact`

- `async def add_contact(self: 'SoroushClient', phone: str, first_name: str, last_name: str='')`

## `methods/extra/archive_chat.py`

### کلاس `ArchiveChat`

- `async def archive_chat(self: 'SoroushClient', chat_id: 'hints.EntityLike')`

## `methods/extra/ban_chat_member.py`

### کلاس `BanChatMember`

- `async def ban_chat_member(self: 'SoroushClient', chat_id: 'hints.EntityLike', user_id: 'hints.EntityLike')`

## `methods/extra/block_user.py`

### کلاس `BlockUser`

- `async def block_user(self: 'SoroushClient', user_id: 'hints.EntityLike')`

## `methods/extra/copy_message.py`

### کلاس `CopyMessage`

- `async def copy_message(self: 'SoroushClient', chat_id: 'hints.EntityLike', from_chat_id: 'hints.EntityLike', message_id: int, **kwargs) -> 'types.Message'`

## `methods/extra/create_channel.py`

### کلاس `CreateChannel`

- `async def create_channel(self: 'SoroushClient', title: str, about: str='', megagroup: bool=False)`

## `methods/extra/create_group.py`

### کلاس `CreateGroup`

- `async def create_group(self: 'SoroushClient', title: str, users: 'typing.Sequence[hints.EntityLike]')`

## `methods/extra/delete_all_private.py`

### کلاس `DeleteAllPrivate`

- `async def delete_all_private(self: 'SoroushClient', revoke: bool=True, delay: float=1.0, on_progress: typing.Callable[[int, int, str], typing.Any]=None) -> dict`

## `methods/extra/delete_contacts.py`

### کلاس `DeleteContacts`

- `async def delete_contacts(self: 'SoroushClient', user_ids: 'typing.Union[hints.EntityLike, typing.Sequence[hints.EntityLike]]')`

## `methods/extra/get_active_sessions.py`

### کلاس `GetActiveSessions`

- `async def get_active_sessions(self: 'SoroushClient')`

## `methods/extra/get_all_groups.py`

### کلاس `GetAllGroups`

- `async def get_all_groups(self: 'SoroushClient') -> typing.List[dict]`

## `methods/extra/get_chat.py`

### کلاس `GetChat`

- `async def get_chat(self: 'SoroushClient', chat_id: 'hints.EntityLike')`

## `methods/extra/get_chat_history.py`

### کلاس `GetChatHistory`

- `async def get_chat_history(self: 'SoroushClient', chat_id: 'hints.EntityLike', limit: int=20, offset_id: int=0, **kwargs)`

## `methods/extra/get_chat_info.py`

### کلاس `GetChatInfo`

- `async def get_chat_info(self: 'SoroushClient', chat_id)`

## `methods/extra/get_chat_members.py`

### کلاس `GetChatMembers`

- `async def get_chat_members(self: 'SoroushClient', chat_id: 'hints.EntityLike', limit: int=0, **kwargs)`

## `methods/extra/get_contacts.py`

### کلاس `GetContacts`

- `async def get_contacts(self: 'SoroushClient')`

## `methods/extra/get_full_chat.py`

### کلاس `GetFullChat`

- `async def get_full_chat(self: 'SoroushClient', chat_id)`

## `methods/extra/get_full_user.py`

### کلاس `GetFullUser`

- `async def get_full_user(self: 'SoroushClient', user_id)`

## `methods/extra/get_user.py`

### کلاس `GetUser`

- `async def get_user(self: 'SoroushClient', user_id)`

## `methods/extra/get_users.py`

### کلاس `GetUsers`

- `async def get_users(self: 'SoroushClient', user_ids: 'typing.Union[hints.EntityLike, typing.Sequence[hints.EntityLike]]')`

## `methods/extra/is_public_chat.py`

### کلاس `IsPublicChat`

- `async def is_public_chat(self: 'SoroushClient', chat_id: 'hints.EntityLike') -> bool`

## `methods/extra/join_chat.py`

### کلاس `JoinChat`

- `async def join_chat(self: 'SoroushClient', chat: 'hints.EntityLike')`

## `methods/extra/leave_all.py`

### کلاس `LeaveAll`

- `async def leave_all(self, delay: float=0.5) -> dict`

## `methods/extra/pin_chat_message.py`

### کلاس `PinChatMessage`

- `async def pin_chat_message(self: 'SoroushClient', chat_id: 'hints.EntityLike', message_id: int, notify: bool=False)`

## `methods/extra/promote_chat_member.py`

### کلاس `PromoteChatMember`

- `async def promote_chat_member(self: 'SoroushClient', chat_id: 'hints.EntityLike', user_id: 'hints.EntityLike', privileges: 'types.ChatAdminRights'=None, title: str='', **kwargs)`

## `methods/extra/read_chat_history.py`

### کلاس `ReadChatHistory`

- `async def read_chat_history(self: 'SoroushClient', chat_id: 'hints.EntityLike') -> bool`

## `methods/extra/restrict_chat_member.py`

### کلاس `RestrictChatMember`

- `async def restrict_chat_member(self: 'SoroushClient', chat_id: 'hints.EntityLike', user_id: 'hints.EntityLike', permissions: 'types.ChatBannedRights'=None, **kwargs)`

## `methods/extra/search_messages.py`

### کلاس `SearchMessages`

- `async def search_messages(self: 'SoroushClient', chat_id: 'hints.EntityLike'=None, query: str='', limit: int=20, filter_type: 'typing.Union[types.TypeMessagesFilter, typing.Type[types.TypeMessagesFilter]]'=None, **kwargs)`

## `methods/extra/send_audio.py`

### کلاس `SendAudio`

- `async def send_audio(self: 'SoroushClient', chat_id: 'hints.EntityLike', audio: 'hints.FileLike', caption: str=None, reply_to_message_id: int=None, **kwargs) -> 'types.Message'`

## `methods/extra/send_document.py`

### کلاس `SendDocument`

- `async def send_document(self: 'SoroushClient', chat_id: 'hints.EntityLike', document: 'hints.FileLike', caption: str=None, reply_to_message_id: int=None, **kwargs) -> 'types.Message'`

## `methods/extra/send_photo.py`

### کلاس `SendPhoto`

- `async def send_photo(self: 'SoroushClient', chat_id: 'hints.EntityLike', photo: 'hints.FileLike', caption: str=None, reply_to_message_id: int=None, **kwargs) -> 'types.Message'`

## `methods/extra/send_reaction.py`

### کلاس `SendReaction`

- `async def send_reaction(self: 'SoroushClient', chat_id: 'hints.EntityLike', message_id: int, emoji: str, **kwargs)`

## `methods/extra/send_video.py`

### کلاس `SendVideo`

- `async def send_video(self: 'SoroushClient', chat_id: 'hints.EntityLike', video: 'hints.FileLike', caption: str=None, reply_to_message_id: int=None, **kwargs) -> 'types.Message'`

## `methods/extra/send_voice.py`

### کلاس `SendVoice`

- `async def send_voice(self: 'SoroushClient', chat_id: 'hints.EntityLike', voice: 'hints.FileLike', caption: str=None, reply_to_message_id: int=None, **kwargs) -> 'types.Message'`

## `methods/extra/set_chat_description.py`

### کلاس `SetChatDescription`

- `async def set_chat_description(self: 'SoroushClient', chat_id: 'hints.EntityLike', description: str='')`

## `methods/extra/set_chat_photo.py`

### کلاس `SetChatPhoto`

- `async def set_chat_photo(self: 'SoroushClient', chat_id: 'hints.EntityLike', photo: 'hints.FileLike')`

## `methods/extra/set_chat_title.py`

### کلاس `SetChatTitle`

- `async def set_chat_title(self: 'SoroushClient', chat_id: 'hints.EntityLike', title: str)`

## `methods/extra/terminate_session.py`

### کلاس `TerminateSession`

- `async def terminate_session(self: 'SoroushClient', session_hash: bytes)`

## `methods/extra/unarchive_chat.py`

### کلاس `UnarchiveChat`

- `async def unarchive_chat(self: 'SoroushClient', chat_id: 'hints.EntityLike')`

## `methods/extra/unban_chat_member.py`

### کلاس `UnbanChatMember`

- `async def unban_chat_member(self: 'SoroushClient', chat_id: 'hints.EntityLike', user_id: 'hints.EntityLike')`

## `methods/extra/unblock_user.py`

### کلاس `UnblockUser`

- `async def unblock_user(self: 'SoroushClient', user_id: 'hints.EntityLike')`

## `methods/extra/unpin_all_chat_messages.py`

### کلاس `UnpinAllChatMessages`

- `async def unpin_all_chat_messages(self: 'SoroushClient', chat_id: 'hints.EntityLike')`

## `methods/extra/unpin_chat_message.py`

### کلاس `UnpinChatMessage`

- `async def unpin_chat_message(self: 'SoroushClient', chat_id: 'hints.EntityLike', message_id: int=None)`

## `methods/extra/update_profile.py`

### کلاس `UpdateProfile`

- `async def update_profile(self: 'SoroushClient', first_name: str=None, last_name: str=None, about: str=None)`

## `methods/extra/update_profile_photo.py`

### کلاس `UpdateProfilePhoto`

- `async def update_profile_photo(self: 'SoroushClient', photo: 'hints.FileLike')`

## `methods/extra/update_username.py`

### کلاس `UpdateUsername`

- `async def update_username(self: 'SoroushClient', username: str)`

## `methods/messageparse/parse_mode.py`

### کلاس `ParseMode`

- `def parse_mode(self: 'SoroushClient')`
- `def parse_mode(self: 'SoroushClient', mode: str)`

## `methods/messages/delete_messages.py`

### کلاس `DeleteMessages`

- `async def delete_messages(self: 'SoroushClient', entity: 'hints.EntityLike', message_ids: 'typing.Union[hints.MessageIDLike, typing.Sequence[hints.MessageIDLike]]', *, revoke: bool=True) -> 'typing.Sequence[types.messages.AffectedMessages]'`

## `methods/messages/edit_message.py`

### کلاس `EditMessage`

- `async def edit_message(self: 'SoroushClient', entity: 'typing.Union[hints.EntityLike, types.Message]', message: 'typing.Union[int, types.Message, types.InputMessageID, str]'=None, text: str=None, *, parse_mode: str=(), attributes: 'typing.Sequence[types.TypeDocumentAttribute]'=None, formatting_entities: typing.Optional[typing.List[types.TypeMessageEntity]]=None, link_preview: bool=True, file: 'hints.FileLike'=None, thumb: 'hints.FileLike'=None, force_document: bool=False, buttons: typing.Optional['hints.MarkupLike']=None, supports_streaming: bool=False, schedule: 'hints.DateLike'=None) -> 'types.Message'`

## `methods/messages/forward_messages.py`

### کلاس `ForwardMessages`

- `async def forward_messages(self: 'SoroushClient', entity: 'hints.EntityLike', messages: 'typing.Union[hints.MessageIDLike, typing.Sequence[hints.MessageIDLike]]', from_peer: 'hints.EntityLike'=None, *, background: bool=None, with_my_score: bool=None, silent: bool=None, as_album: bool=None, schedule: 'hints.DateLike'=None, drop_author: bool=None, drop_media_captions: bool=None) -> 'typing.Sequence[types.Message]'`

## `methods/messages/get_messages.py`

### کلاس `GetMessages`

- `async def get_messages(self: 'SoroushClient', *args, **kwargs) -> typing.Union['hints.TotalList', typing.Optional['types.Message']]`

## `methods/messages/iter_messages.py`

### کلاس `IterMessages`

- `def iter_messages(self: 'SoroushClient', entity: 'hints.EntityLike', limit: float=None, *, offset_date: 'hints.DateLike'=None, offset_id: int=0, max_id: int=0, min_id: int=0, add_offset: int=0, search: str=None, filter: 'typing.Union[types.TypeMessagesFilter, typing.Type[types.TypeMessagesFilter]]'=None, from_user: 'hints.EntityLike'=None, wait_time: float=None, ids: 'typing.Union[int, typing.Sequence[int]]'=None, reverse: bool=False, reply_to: int=None, scheduled: bool=False) -> 'typing.Union[_MessagesIter, _IDsIter]'`

## `methods/messages/pin_message.py`

### کلاس `PinMessage`

- `async def pin_message(self: 'SoroushClient', entity: 'hints.EntityLike', message: 'typing.Optional[hints.MessageIDLike]', *, notify: bool=False, pm_oneside: bool=False)`

## `methods/messages/send_message.py`

### کلاس `SendMessage`

- `async def send_message(self: 'SoroushClient', entity: 'hints.EntityLike', message: 'hints.MessageLike'='', *, reply_to: 'typing.Union[int, types.Message]'=None, attributes: 'typing.Sequence[types.TypeDocumentAttribute]'=None, parse_mode: typing.Optional[str]=(), formatting_entities: typing.Optional[typing.List[types.TypeMessageEntity]]=None, link_preview: bool=True, file: 'typing.Union[hints.FileLike, typing.Sequence[hints.FileLike]]'=None, thumb: 'hints.FileLike'=None, force_document: bool=False, clear_draft: bool=False, buttons: typing.Optional['hints.MarkupLike']=None, silent: bool=None, background: bool=None, supports_streaming: bool=False, schedule: 'hints.DateLike'=None, comment_to: 'typing.Union[int, types.Message]'=None, nosound_video: bool=None, send_as: typing.Optional['hints.EntityLike']=None, message_effect_id: typing.Optional[int]=None) -> 'types.Message'`

## `methods/messages/send_read_acknowledge.py`

### کلاس `SendReadAcknowledge`

- `async def send_read_acknowledge(self: 'SoroushClient', entity: 'hints.EntityLike', message: 'typing.Union[hints.MessageIDLike, typing.Sequence[hints.MessageIDLike]]'=None, *, max_id: int=None, clear_mentions: bool=False, clear_reactions: bool=False) -> bool`

## `methods/messages/unpin_message.py`

### کلاس `UnpinMessage`

- `async def unpin_message(self: 'SoroushClient', entity: 'hints.EntityLike', message: 'typing.Optional[hints.MessageIDLike]'=None, *, notify: bool=False)`

## `methods/updates/add_event_handler.py`

### کلاس `AddEventHandler`

- `def add_event_handler(self: 'SoroushClient', callback: 'typing.Callable', event: 'typing.Union[EventBuilder, typing.Type[EventBuilder]]') -> None`
- `def add_middleware(self: 'SoroushClient', middleware: 'BaseMiddleware', index: 'typing.Optional[int]'=None) -> None`
- `def remove_middleware(self: 'SoroushClient', middleware: 'BaseMiddleware') -> bool`

## `methods/updates/on_channel.py`

### کلاس `OnChannel`

- `def on_channel(self: 'SoroushClient', filters=None)`

## `methods/updates/on_chat_action.py`

### کلاس `OnChatAction`

- `def on_chat_action(self: 'SoroushClient', filters=None)`

## `methods/updates/on_deleted_messages.py`

### کلاس `OnDeletedMessages`

- `def on_deleted_messages(self: 'SoroushClient', filters=None)`

## `methods/updates/on_edited_message.py`

### کلاس `OnEditedMessage`

- `def on_edited_message(self: 'SoroushClient', filters=None)`

## `methods/updates/on_error.py`

### کلاس `OnError`

- `def on_error(self: 'SoroushClient', exception_class)`

## `methods/updates/on_group.py`

### کلاس `OnGroup`

- `def on_group(self: 'SoroushClient', filters=None)`

## `methods/updates/on_me.py`

### کلاس `OnMe`

- `def on_me(self: 'SoroushClient', filters=None)`

## `methods/updates/on_message.py`

### کلاس `OnMessage`

- `def on_message(self: 'SoroushClient', filters=None)`

## `methods/updates/on_raw_update.py`

### کلاس `OnRawUpdate`

- `def on_raw_update(self: 'SoroushClient', types=None)`

## `methods/updates/on_user_status.py`

### کلاس `OnUserStatus`

- `def on_user_status(self: 'SoroushClient', filters=None)`

## `methods/updates/remove_event_handler.py`

### کلاس `RemoveEventHandler`

- `def remove_event_handler(self: 'SoroushClient', callback: 'typing.Callable', event: 'typing.Optional[typing.Union[EventBuilder, typing.Type[EventBuilder]]]'=None) -> int`

## `methods/updates/run_until_disconnected.py`

### کلاس `RunUntilDisconnectedSync`

- `def run_until_disconnected(self: 'SoroushClient')`

## `methods/uploads/send_file.py`

### کلاس `SendFile`

- `async def send_file(self: 'SoroushClient', entity: 'hints.EntityLike', file: 'typing.Union[hints.FileLike, typing.Sequence[hints.FileLike]]', *, caption: typing.Union[str, typing.Sequence[str]]=None, force_document: bool=False, mime_type: str=None, file_size: int=None, clear_draft: bool=False, progress_callback: 'hints.ProgressCallback'=None, reply_to: 'hints.MessageIDLike'=None, attributes: 'typing.Sequence[types.TypeDocumentAttribute]'=None, thumb: 'hints.FileLike'=None, allow_cache: bool=True, parse_mode: str=(), formatting_entities: typing.Optional[typing.Union[typing.List[types.TypeMessageEntity], typing.List[typing.List[types.TypeMessageEntity]]]]=None, voice_note: bool=False, video_note: bool=False, buttons: typing.Optional['hints.MarkupLike']=None, silent: bool=None, background: bool=None, supports_streaming: bool=False, schedule: 'hints.DateLike'=None, comment_to: 'typing.Union[int, types.Message]'=None, ttl: int=None, nosound_video: bool=None, send_as: typing.Optional['hints.EntityLike']=None, message_effect_id: typing.Optional[int]=None, **kwargs) -> typing.Union[typing.List[typing.Any], typing.Any]`

## `methods/uploads/upload_file.py`

### کلاس `UploadFile`

- `async def upload_file(self: 'SoroushClient', file: 'hints.FileLike', *, part_size_kb: float=None, file_size: int=None, file_name: str=None, use_cache: type=None, key: bytes=None, iv: bytes=None, progress_callback: 'hints.ProgressCallback'=None) -> 'types.TypeInputFile'`

## `methods/users/get_entity.py`

### کلاس `GetEntity`

- `async def get_entity(self: 'SoroushClient', entity: 'hints.EntitiesLike') -> typing.Union['hints.Entity', typing.List['hints.Entity']]`

## `methods/users/get_input_entity.py`

### کلاس `GetInputEntity`

- `async def get_input_entity(self: 'SoroushClient', peer: 'hints.EntityLike') -> 'types.TypeInputPeer'`

## `methods/users/get_me.py`

### کلاس `GetMe`

- `async def get_me(self: 'SoroushClient', input_peer: bool=False) -> 'typing.Union[types.User, types.InputPeerUser]'`

## `methods/users/get_peer_id.py`

### کلاس `GetPeerId`

- `async def get_peer_id(self: 'SoroushClient', peer: 'hints.EntityLike', add_mark: bool=True) -> int`

## `methods/users/is_bot.py`

### کلاس `IsBot`

- `async def is_bot(self: 'SoroushClient') -> bool`

## `methods/users/is_user_authorized.py`

### کلاس `IsUserAuthorized`

- `async def is_user_authorized(self: 'SoroushClient') -> bool`

## `middleware.py`

### کلاس `BaseMiddleware`

- `async def on_pre_process(self, client: Any, event: Any, data: Dict[str, Any]) -> None`
- `async def on_post_process(self, client: Any, event: Any, data: Dict[str, Any]) -> None`

### کلاس `MiddlewareManager`

- `def middlewares(self) -> List[BaseMiddleware]`
- `def add(self, middleware: BaseMiddleware, index: Optional[int]=None) -> None`
- `def remove(self, middleware: BaseMiddleware) -> bool`
- `def clear(self) -> None`
- `async def process_pre(self, client: Any, event: Any, data: Optional[Dict[str, Any]]=None) -> Dict[str, Any]`
- `async def process_post(self, client: Any, event: Any, data: Dict[str, Any]) -> None`

## `mirror.py`

### کلاس `MirrorRule`

- `async def resolve(self, client: Any) -> None`
- `def matches(self, chat_id: Any, chat_username: Any=None) -> bool`

### کلاس `MessageMirror`

- `def rules(self) -> List[MirrorRule]`
- `def is_running(self) -> bool`
- `def add(self, source: Any, destination: Any, *, forward: bool=False, filter: Any=None, caption: Optional[str]=None, enabled: bool=True) -> MirrorRule`
- `def remove(self, rule: Union[MirrorRule, int]) -> bool`
- `def remove_all(self) -> None`
- `def start(self) -> None`
- `def stop(self) -> None`

## `network/authenticator.py`

### توابع عمومی

- `async def do_authentication(sender)`
- `def get_int(byte_array, signed=True)`

## `network/connection/connection.py`

### کلاس `Connection`

- `async def connect(self, timeout=None, ssl=None)`
- `async def disconnect(self)`
- `def send(self, data)`
- `async def recv(self)`

### کلاس `PacketCodec`

- `def encode_packet(self, data)`
- `async def read_packet(self, reader)`

## `network/connection/http.py`

### کلاس `HttpPacketCodec`

- `def encode_packet(self, data)`
- `async def read_packet(self, reader)`

### کلاس `ConnectionHttp`

- `async def connect(self, timeout=None, ssl=None)`

## `network/connection/tcpabridged.py`

### کلاس `AbridgedPacketCodec`

- `def encode_packet(self, data)`
- `async def read_packet(self, reader)`

## `network/connection/tcpfull.py`

### کلاس `FullPacketCodec`

- `def encode_packet(self, data)`
- `async def read_packet(self, reader)`

## `network/connection/tcpintermediate.py`

### کلاس `IntermediatePacketCodec`

- `def encode_packet(self, data)`
- `async def read_packet(self, reader)`

### کلاس `RandomizedIntermediatePacketCodec`

- `def encode_packet(self, data)`
- `async def read_packet(self, reader)`

## `network/connection/tcpmtproxy.py`

### کلاس `MTProxyIO`

- `def init_header(secret, dc_id, packet_codec)`
- `async def readexactly(self, n)`
- `def write(self, data)`

### کلاس `TcpMTProxy`

- `def address_info(proxy_info)`
- `def normalize_secret(secret)`

## `network/connection/tcpobfuscated.py`

### کلاس `ObfuscatedIO`

- `def init_header(packet_codec)`
- `async def readexactly(self, n)`
- `def write(self, data)`

## `network/connection/websocket.py`

### کلاس `WebSocketReader`

- `async def readexactly(self, n)`

### کلاس `WebSocketWriter`

- `def write(self, data)`
- `async def drain(self)`
- `def close(self)`
- `async def wait_closed(self)`

### کلاس `ConnectionWebSocket`

- `async def disconnect(self)`

## `network/mtprotoplainsender.py`

### کلاس `MTProtoPlainSender`

- `async def send(self, request)`

## `network/mtprotosender.py`

### کلاس `MTProtoSender`

- `async def connect(self, connection)`
- `def is_connected(self)`
- `async def disconnect(self)`
- `def send(self, request, ordered=False)`
- `def disconnected(self)`

## `network/mtprotostate.py`

### کلاس `MTProtoState`

- `def reset(self)`
- `def update_message_id(self, message)`
- `def write_data_as_message(self, buffer, data, content_related, *, after_id=None)`
- `def encrypt_message_data(self, data)`
- `def decrypt_message_data(self, body)`
- `def update_time_offset(self, correct_msg_id)`

## `network/requeststate.py`

### کلاس `RequestState`

- `def reset_ids(self)`
- `def is_done(self) -> bool`

## `password.py`

### توابع عمومی

- `def check_prime_and_good_check(prime: int, g: int)`
- `def check_prime_and_good(prime_bytes: bytes, g: int)`
- `def is_good_large(number: int, p: int) -> bool`
- `def num_bytes_for_hash(number: bytes) -> bytes`
- `def big_num_for_hash(g: int) -> bytes`
- `def sha256(*p: bytes) -> bytes`
- `def is_good_mod_exp_first(modexp, prime) -> bool`
- `def xor(a: bytes, b: bytes) -> bytes`
- `def pbkdf2sha512(password: bytes, salt: bytes, iterations: int)`
- `def compute_hash(algo: types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow, password: str)`
- `def compute_digest(algo: types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow, password: str)`
- `def compute_check(request: types.account.Password, password: str)`

## `plugins.py`

### کلاس `Plugin`

- `def on_load(self, client: Any) -> None`
- `def on_ready(self, client: Any) -> None`
- `def on_unload(self, client: Any) -> None`

### کلاس `PluginManager`

- `def plugins(self) -> List[Plugin]`
- `def names(self) -> List[str]`
- `def get(self, name: str) -> Optional[Plugin]`
- `def load(self, plugin: Plugin) -> Plugin`
- `def unload(self, plugin: Union[Plugin, str]) -> bool`
- `def reload(self, plugin: Union[Plugin, str]) -> Plugin`
- `def unload_all(self) -> int`
- `def load_plugins_from(self, path: Union[str, pathlib.Path], recursive: bool=True) -> List[Plugin]`

## `requestiter.py`

### کلاس `RequestIter`

- `async def collect(self)`

## `resolvers.py`

### توابع عمومی

- `async def resolve_reply_sender(message) -> Optional[int]`

### کلاس `Target`

- `def id(self) -> Optional[int]`

### کلاس `TargetResolver`

- `async def resolve(self, target) -> Optional[Target]`
- `async def resolve_user_id(self, target) -> Optional[int]`

## `scheduler.py`

### کلاس `Job`

- `def is_recurring(self) -> bool`
- `def is_done(self) -> bool`
- `def cancel(self) -> bool`

### کلاس `Scheduler`

- `def is_running(self) -> bool`
- `def jobs(self) -> List[Job]`
- `def run_in(self, delay: Union[int, float, _dt.timedelta], callback: Optional[Callable]=None)`
- `def run_at(self, when: Union[_dt.datetime, int, float], callback: Optional[Callable]=None)`
- `def run_every(self, interval: Union[int, float, _dt.timedelta], callback: Optional[Callable]=None, *, times: Optional[int]=None)`
- `def cancel(self, job: Union[Job, int]) -> bool`
- `def clear(self) -> None`
- `def start(self) -> asyncio.Task`
- `async def stop(self, wait: bool=True, timeout: float=5.0) -> None`

## `sessions/abstract.py`

### کلاس `Session`

- `def clone(self, to_instance=None)`
- `def set_dc(self, dc_id, server_address, port)`
- `def dc_id(self)`
- `def server_address(self)`
- `def port(self)`
- `def auth_key(self)`
- `def auth_key(self, value)`
- `def takeout_id(self)`
- `def takeout_id(self, value)`
- `def get_update_state(self, entity_id)`
- `def set_update_state(self, entity_id, state)`
- `def get_update_states(self)`
- `def close(self)`
- `def save(self)`
- `def delete(self)`
- `def list_sessions(cls)`
- `def process_entities(self, tlo)`
- `def get_input_entity(self, key)`
- `def cache_file(self, md5_digest, file_size, instance)`
- `def get_file(self, md5_digest, file_size, cls)`

## `sessions/memory.py`

### کلاس `MemorySession`

- `def set_dc(self, dc_id, server_address, port)`
- `def dc_id(self)`
- `def server_address(self)`
- `def port(self)`
- `def auth_key(self)`
- `def tmp_auth_key(self)`
- `def auth_key(self, value)`
- `def tmp_auth_key(self, value)`
- `def takeout_id(self)`
- `def takeout_id(self, value)`
- `def get_update_state(self, entity_id)`
- `def set_update_state(self, entity_id, state)`
- `def get_update_states(self)`
- `def close(self)`
- `def save(self)`
- `def delete(self)`
- `def process_entities(self, tlo)`
- `def get_entity_rows_by_phone(self, phone)`
- `def get_entity_rows_by_username(self, username)`
- `def get_entity_rows_by_name(self, name)`
- `def get_entity_rows_by_id(self, id, exact=True)`
- `def get_input_entity(self, key)`
- `def cache_file(self, md5_digest, file_size, instance)`
- `def get_file(self, md5_digest, file_size, cls)`

## `sessions/postgresql_session.py`

### کلاس `PostgreSQLSession`

- `def set_dc(self, dc_id, server_address, port)`
- `def auth_key(self, value)`
- `def tmp_auth_key(self, value)`
- `def takeout_id(self, value)`
- `def get_update_state(self, entity_id)`
- `def set_update_state(self, entity_id, state)`
- `def get_update_states(self)`
- `def process_entities(self, tlo)`
- `def get_entity_rows_by_phone(self, phone)`
- `def get_entity_rows_by_username(self, username)`
- `def get_entity_rows_by_name(self, name)`
- `def get_entity_rows_by_id(self, id, exact=True)`
- `def cache_file(self, md5_digest, file_size, instance)`
- `def get_file(self, md5_digest, file_size, cls)`
- `def save(self)`
- `def close(self)`
- `def delete(self)`
- `def clone(self, to_instance=None)`

## `sessions/redis_session.py`

### کلاس `RedisSession`

- `def set_dc(self, dc_id, server_address, port)`
- `def auth_key(self, value)`
- `def tmp_auth_key(self, value)`
- `def takeout_id(self, value)`
- `def get_update_state(self, entity_id)`
- `def set_update_state(self, entity_id, state)`
- `def get_update_states(self)`
- `def process_entities(self, tlo)`
- `def get_entity_rows_by_phone(self, phone)`
- `def get_entity_rows_by_username(self, username)`
- `def get_entity_rows_by_name(self, name)`
- `def get_entity_rows_by_id(self, id, exact=True)`
- `def cache_file(self, md5_digest, file_size, instance)`
- `def get_file(self, md5_digest, file_size, cls)`
- `def save(self)`
- `def close(self)`
- `def delete(self)`
- `def clone(self, to_instance=None)`

## `sessions/sqlite.py`

### کلاس `SQLiteSession`

- `def clone(self, to_instance=None)`
- `def set_dc(self, dc_id, server_address, port)`
- `def auth_key(self, value)`
- `def tmp_auth_key(self, value)`
- `def takeout_id(self, value)`
- `def get_update_state(self, entity_id)`
- `def set_update_state(self, entity_id, state)`
- `def get_update_states(self)`
- `def save(self)`
- `def close(self)`
- `def delete(self)`
- `def list_sessions(cls)`
- `def process_entities(self, tlo)`
- `def get_entity_rows_by_phone(self, phone)`
- `def get_entity_rows_by_username(self, username)`
- `def get_entity_rows_by_name(self, name)`
- `def get_entity_rows_by_id(self, id, exact=True)`
- `def get_file(self, md5_digest, file_size, cls)`
- `def cache_file(self, md5_digest, file_size, instance)`

## `sessions/string.py`

### کلاس `StringSession`

- `def encode(x: bytes) -> str`
- `def decode(x: str) -> bytes`
- `def save(self: Session)`

## `sync.py`

### توابع عمومی

- `def syncify(*types)`

## `tl/core/gzippacked.py`

### کلاس `GzipPacked`

- `def gzip_if_smaller(content_related, data)`
- `def read(reader)`
- `def from_reader(cls, reader)`
- `def to_dict(self)`

## `tl/core/messagecontainer.py`

### کلاس `MessageContainer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/core/rpcresult.py`

### کلاس `RpcResult`

- `def from_reader(cls, reader)`
- `def to_dict(self)`

## `tl/core/tlmessage.py`

### کلاس `TLMessage`

- `def to_dict(self)`

## `tl/custom/adminlogevent.py`

### کلاس `AdminLogEvent`

- `def id(self)`
- `def date(self)`
- `def user_id(self)`
- `def action(self)`
- `def old(self)`
- `def new(self)`
- `def changed_about(self)`
- `def changed_title(self)`
- `def changed_username(self)`
- `def changed_photo(self)`
- `def changed_sticker_set(self)`
- `def changed_message(self)`
- `def deleted_message(self)`
- `def changed_admin(self)`
- `def changed_restrictions(self)`
- `def changed_invites(self)`
- `def changed_location(self)`
- `def joined(self)`
- `def joined_invite(self)`
- `def left(self)`
- `def changed_hide_history(self)`
- `def changed_signatures(self)`
- `def changed_pin(self)`
- `def changed_default_banned_rights(self)`
- `def stopped_poll(self)`
- `def started_group_call(self)`
- `def discarded_group_call(self)`
- `def user_muted(self)`
- `def user_unmutted(self)`
- `def changed_call_settings(self)`
- `def changed_history_ttl(self)`
- `def deleted_exported_invite(self)`
- `def edited_exported_invite(self)`
- `def revoked_exported_invite(self)`
- `def joined_by_invite(self)`
- `def changed_user_volume(self)`
- `def stringify(self)`

## `tl/custom/button.py`

### کلاس `Button`

- `def inline(text, data=None)`
- `def switch_inline(text, query='', same_peer=False)`
- `def url(text, url=None)`
- `def text(cls, text, *, resize=None, single_use=None, selective=None, persistent=None, placeholder=None)`
- `def request_location(cls, text, *, resize=None, single_use=None, selective=None, persistent=None, placeholder=None)`
- `def request_phone(cls, text, *, resize=None, single_use=None, selective=None, persistent=None, placeholder=None)`
- `def request_poll(cls, text, *, force_quiz=False, resize=None, single_use=None, selective=None, persistent=None, placeholder=None)`
- `def clear(selective=None)`
- `def force_reply(single_use=None, selective=None, placeholder=None)`
- `def buy(text)`
- `def game(text)`

## `tl/custom/chatgetter.py`

### کلاس `ChatGetter`

- `def chat(self)`
- `async def get_chat(self)`
- `def input_chat(self)`
- `async def get_input_chat(self)`
- `def chat_id(self)`
- `def is_private(self)`
- `def is_group(self)`
- `def is_channel(self)`

## `tl/custom/conversation.py`

### کلاس `Conversation`

- `async def send_message(self, *args, **kwargs)`
- `async def send_file(self, *args, **kwargs)`
- `def mark_read(self, message=None)`
- `def get_response(self, message=None, *, timeout=None)`
- `def get_reply(self, message=None, *, timeout=None)`
- `def get_edit(self, message=None, *, timeout=None)`
- `def wait_read(self, message=None, *, timeout=None)`
- `async def wait_event(self, event, *, timeout=None)`
- `def cancel(self)`
- `async def cancel_all(self)`

## `tl/custom/dialog.py`

### کلاس `Dialog`

- `async def send_message(self, *args, **kwargs)`
- `async def delete(self, revoke=False)`
- `async def archive(self, folder=1)`
- `def to_dict(self)`
- `def stringify(self)`

## `tl/custom/draft.py`

### کلاس `Draft`

- `def entity(self)`
- `def input_entity(self)`
- `async def get_entity(self)`
- `async def get_input_entity(self)`
- `def text(self)`
- `def raw_text(self)`
- `def is_empty(self)`
- `async def set_message(self, text=None, reply_to=0, parse_mode=(), link_preview=None)`
- `async def send(self, clear=True, parse_mode=())`
- `async def delete(self)`
- `def to_dict(self)`
- `def stringify(self)`

## `tl/custom/file.py`

### کلاس `File`

- `def id(self)`
- `def name(self)`
- `def ext(self)`
- `def mime_type(self)`
- `def width(self)`
- `def height(self)`
- `def duration(self)`
- `def title(self)`
- `def performer(self)`
- `def emoji(self)`
- `def sticker_set(self)`
- `def size(self)`

## `tl/custom/message.py`

### کلاس `Message`

- `def client(self)`
- `def text(self)`
- `def text(self, value)`
- `def raw_text(self)`
- `def is_reply(self)`
- `def forward(self)`
- `async def forward_to(self, to_chat_id, **kwargs)`
- `def file(self)`
- `def media_type(self)`
- `def photo(self)`
- `def document(self)`
- `def audio(self)`
- `def voice(self)`
- `def video(self)`
- `def gif(self)`
- `def sticker(self)`
- `async def get_reply_message(self)`
- `async def respond(self, *args, **kwargs)`
- `async def reply(self, *args, **kwargs)`
- `async def edit(self, *args, **kwargs)`
- `async def delete(self, *args, **kwargs)`
- `async def tag_member(self, user, text: str=None)`
- `async def download_media(self, *args, **kwargs)`
- `async def reply_text(self, text, **kwargs)`
- `async def reply_photo(self, photo, caption=None, **kwargs)`
- `async def reply_video(self, video, caption=None, **kwargs)`
- `async def reply_audio(self, audio, caption=None, **kwargs)`
- `async def reply_voice(self, voice, caption=None, **kwargs)`
- `async def reply_document(self, document, caption=None, **kwargs)`
- `async def copy(self, to_chat_id, **kwargs)`
- `async def pin(self, **kwargs)`
- `async def unpin(self, **kwargs)`
- `async def react(self, emoji, **kwargs)`
- `async def download(self, file_name=None, **kwargs)`
- `async def mark_read(self, **kwargs)`

## `tl/custom/messagebutton.py`

### کلاس `MessageButton`

- `def client(self)`
- `def text(self)`
- `def data(self)`
- `def inline_query(self)`
- `def url(self)`
- `async def click(self, share_phone=None, share_geo=None, *, password=None, open_url=None)`

## `tl/custom/participantpermissions.py`

### کلاس `ParticipantPermissions`

- `def is_admin(self)`
- `def is_creator(self)`
- `def has_default_permissions(self)`
- `def is_banned(self)`
- `def has_left(self)`
- `def add_admins(self)`

## `tl/custom/qrlogin.py`

### کلاس `QRLogin`

- `async def recreate(self)`
- `def token(self) -> bytes`
- `def url(self) -> str`
- `def expires(self) -> datetime.datetime`
- `async def wait(self, timeout: float=None)`

## `tl/custom/sendergetter.py`

### کلاس `SenderGetter`

- `def sender(self)`
- `async def get_sender(self)`
- `def input_sender(self)`
- `async def get_input_sender(self)`
- `def sender_id(self)`

## `tl/custom/types.py`

### کلاس `FactCheck`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SuggestedPost`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/__init__.py`

### کلاس `DestroyAuthKeyRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DestroySessionRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetFutureSaltsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InitConnectionRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InvokeAfterMsgRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InvokeWithLayerRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PingRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PingDelayDisconnectRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReqDHParamsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReqPqRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReqPqMultiRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RpcDropAnswerRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetClientDHParamsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/account.py`

### کلاس `ChangeAuthorizationSettingsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CheckUsernameRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ConfirmPasswordEmailRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ConfirmPhoneRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetAuthorizationsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetAutoDownloadSettingsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetContactSignUpNotificationRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetContentSettingsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetGlobalPrivacySettingsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetNotifyExceptionsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetNotifySettingsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPasswordRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPasswordSettingsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPrivacyRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetRecentEmojiStatusesRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetSavedMusicIdsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetTmpPasswordRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetWallPapersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetWebAuthorizationsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RegisterDeviceRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReorderUsernamesRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReportPeerRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReportProfilePhotoRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResetAuthorizationRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResetWebAuthorizationRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResetWebAuthorizationsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SaveAutoDownloadSettingsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SaveMusicRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendConfirmPhoneCodeRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendVerifyPhoneCodeRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetAuthorizationTTLRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetContactSignUpNotificationRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetContentSettingsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetGlobalPrivacySettingsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetMainProfileTabRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetPrivacyRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleUsernameRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UnregisterDeviceRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBirthdayRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBusinessWorkHoursRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateEmojiStatusRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateGenderRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateNotifySettingsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePasswordSettingsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePersonalChannelRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateProfileRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateStatusRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateUserLocationRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateUsernameRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UploadWallPaperRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/auth.py`

### کلاس `BindTempAuthKeyRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CancelCodeRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CheckPasswordRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteAccountRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DropTempAuthKeysRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportAuthorizationRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportLoginTokenRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ImportAuthorizationRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ImportLoginTokenRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ImportWebTokenAuthorizationRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LogOutRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RequestPasswordRecoveryRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResendCodeRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResendDeleteAccountCodeRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResetAuthorizationsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendCodeRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendDeleteAccountCodeRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SignInRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SignUpRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/bots.py`

### کلاس `AllowSendMessageRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CanSendMessageRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InvokeWebViewCustomMethodRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/channels.py`

### کلاس `CheckUsernameRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ClickSponsoredMessageRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CreateChannelRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CreateForumTopicRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeactivateAllUsernamesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteChannelRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteMessagesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteTopicHistoryRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditAdminRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditBannedRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditForumTopicRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditPhotoRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditTitleRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetAdminedPublicChannelsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetChannelsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetForumTopicsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetForumTopicsByIDRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetFullChannelRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetGroupsForDiscussionRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetMessagesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetParticipantRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetParticipantsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetSendAsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetSponsoredMessagesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InviteToChannelRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JoinChannelRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LeaveChannelRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReadHistoryRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReadMessageContentsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReorderUsernamesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetDiscussionGroupRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleForumRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleJoinRequestRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleJoinToSendRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleMembershipMessageVisibilityRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleParticipantsHiddenRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TogglePreHistoryHiddenRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleSignaturesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleUsernameRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleViewForumAsMessagesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePinnedForumTopicRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateUsernameRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ViewSponsoredMessageRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/chatlists.py`

### کلاس `CheckChatlistInviteRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteExportedInviteRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditExportedInviteRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportChatlistInviteRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetExportedInvitesRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetLeaveChatlistSuggestionsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JoinChatlistInviteRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LeaveChatlistRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/conference.py`

### کلاس `BanConferenceParticipantRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CreateConferenceCallRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DiscardConferenceCallRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetActiveConferenceCallsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetBannedConferenceParticipantsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetConferenceCallRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JoinConferenceCallRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LeaveConferenceCallRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MuteConferenceParticipantRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RemoveConferenceParticipantRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResolveConferenceCallRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetConferenceRatingRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UnbanConferenceParticipantRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/contacts.py`

### کلاس `AddContactRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BlockRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteContactsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditCloseFriendsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetBirthdaysRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetBlockedRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetContactsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetTopPeersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ImportContactsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResolvePhoneRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResolveUsernameRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SearchRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UnblockRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/folders.py`

### کلاس `EditPeerFoldersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/help.py`

### کلاس `AcceptTermsOfServiceRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetAppConfigRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetConfigRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetCountriesListRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetNearestDcRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPeerColorsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPeerProfileColorsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPremiumPromoRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetSupportRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetTimezonesListRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/langpack.py`

### کلاس `GetDifferenceRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetLangPackRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetLanguagesRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetStringsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/messages.py`

### کلاس `AcceptUrlAuthRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AddChatUserRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CheckChatInviteRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ClearRecentReactionsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ClearRecentStickersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CreateChatRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteChatRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteChatUserRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteExportedChatInviteRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteHistoryRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteMessagesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteRevokedExportedChatInvitesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteScheduledMessagesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditChatAboutRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditChatDefaultBannedRightsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditChatPhotoRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditChatTitleRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditExportedChatInviteRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditMessageRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportChatInviteRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FaveStickerRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ForwardMessagesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetAllStickersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetArchivedStickersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetAttachMenuBotRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetAttachMenuBotsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetAvailableReactionsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetBotAppRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetBotCallbackAnswerRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetChatInviteImportersRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetChatsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetCommonChatsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetCustomEmojiDocumentsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetDhConfigRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetDialogFiltersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetDialogsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetDiscussionMessageRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetDocumentByHashRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetEmojiKeywordsDifferenceRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetEmojiStickersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetExportedChatInvitesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetExtendedMediaRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetFavedStickersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetFeaturedEmojiStickersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetFeaturedStickersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetFullChatRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetHistoryRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetInlineBotResultsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetMessageReactionsListRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetMessageReadParticipantsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetMessagesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetMessagesReactionsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetMessagesViewsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetOnlinesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPeerDialogsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPeerSettingsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPinnedDialogsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPollResultsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPollVotesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetRecentReactionsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetRecentStickersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetRepliesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetSavedGifsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetScheduledHistoryRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetStickerSetRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetStickersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetSuggestedDialogFiltersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetTopReactionsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetUnreadMentionsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetUnreadReactionsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetWebPageRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetWebPagePreviewRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `HideAllChatJoinRequestsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `HideChatJoinRequestRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `HidePeerSettingsBarRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ImportChatInviteRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InstallStickerSetRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MarkDialogUnreadRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MigrateChatRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ProlongWebViewRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReadDiscussionRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReadFeaturedStickersRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReadHistoryRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReadMentionsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReadMessageContentsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReadReactionsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReceivedMessagesRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReportRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReportSpamRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RequestAppWebViewRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RequestSimpleWebViewRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RequestUrlAuthRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RequestWebViewRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SaveDefaultSendAsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SaveDraftRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SaveGifRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SaveRecentStickerRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SearchRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SearchGlobalRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SearchStickerSetsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendInlineBotResultRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMediaRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMultiMediaRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendReactionRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendScheduledMessagesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendVoteRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendWebViewDataRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendWebViewResultMessageRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetChatAvailableReactionsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetDefaultReactionRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetTypingRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StartBotRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleBotInAttachMenuRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleDialogFilterTagsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleDialogPinRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleNoForwardsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TogglePeerTranslationsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TranscribeAudioRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TranslateTextRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UninstallStickerSetRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UnpinAllMessagesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateDialogFilterRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateDialogFiltersOrderRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePinnedMessageRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UploadMediaRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/payments.py`

### کلاس `ApplyGiftCodeRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CheckGiftCodeRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetGiveawayInfoRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPaymentFormRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPaymentReceiptRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetSavedInfoRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendPaymentFormRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ValidateRequestedInfoRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/phone.py`

### کلاس `AcceptCallRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ConfirmCallRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CreateGroupCallRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DiscardCallRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DiscardGroupCallRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EditGroupCallParticipantRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportGroupCallInviteRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetGroupCallRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetGroupParticipantsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JoinGroupCallRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JoinGroupCallPresentationRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LeaveGroupCallRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LeaveGroupCallPresentationRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReceivedCallRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RequestCallRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SaveCallDebugRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendSignalingDataRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SetCallRatingRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ToggleGroupCallStartSubscriptionRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/photos.py`

### کلاس `DeletePhotosRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`
- `def read_result(reader)`

### کلاس `GetUserPhotosRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateProfilePhotoRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UploadContactProfilePhotoRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UploadProfilePhotoRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/premium.py`

### کلاس `ApplyBoostRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetBoostsListRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetBoostsStatusRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetMyBoostsRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/stats.py`

### کلاس `GetBroadcastStatsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetMegagroupStatsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetMessagePublicForwardsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetMessageStatsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetStoryPublicForwardsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetStoryStatsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LoadAsyncGraphRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/stories.py`

### کلاس `ActivateStealthModeRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeleteStoriesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`
- `def read_result(reader)`

### کلاس `EditStoryRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportStoryLinkRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetAllStoriesRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPeerMaxIDsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`
- `def read_result(reader)`

### کلاس `GetPeerStoriesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetPinnedStoriesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetStoriesArchiveRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetStoriesByIDRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetStoryViewsListRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `IncrementStoryViewsRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReadStoriesRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`
- `def read_result(reader)`

### کلاس `ReportRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendReactionRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TogglePeerStoriesHiddenRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TogglePinnedRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`
- `def read_result(reader)`

## `tl/functions/thirdParty.py`

### کلاس `RequestRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TellRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/updates.py`

### کلاس `GetChannelDifferenceRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetDifferenceRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetStateRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/upload.py`

### کلاس `GetFileRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetWebFileRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SaveBigFilePartRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SaveFilePartRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/functions/users.py`

### کلاس `GetFullUserRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetSavedMusicRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetSavedMusicByIDRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GetUsersRequest`

- `async def resolve(self, client, utils)`
- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/tlobject.py`

### کلاس `TLObject`

- `def pretty_format(obj, indent=None)`
- `def serialize_bytes(data)`
- `def serialize_datetime(dt)`
- `def stringify(self)`
- `def to_dict(self)`
- `def to_json(self, fp=None, default=_json_default, **kwargs)`
- `def from_reader(cls, reader)`

### کلاس `TLRequest`

- `def read_result(reader)`
- `async def resolve(self, client, utils)`

## `tl/types/__init__.py`

### کلاس `AccessPointRule`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AccountDaysTTL`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ActiveConferenceCalls`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AppWebViewResultUrl`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AttachMenuBot`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AttachMenuBotIcon`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AttachMenuBotIconColor`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AttachMenuBots`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AttachMenuBotsBot`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AttachMenuBotsNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AttachMenuPeerTypeBotPM`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AttachMenuPeerTypeBroadcast`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AttachMenuPeerTypeChat`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AttachMenuPeerTypePM`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AttachMenuPeerTypeSameBotPM`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Authorization`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AutoDownloadSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AutoSaveException`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AutoSaveSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AvailableReaction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BadMsgNotification`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BadServerSalt`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BankCardOpenUrl`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BannedConferenceParticipants`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BaseThemeArctic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BaseThemeClassic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BaseThemeDay`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BaseThemeNight`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BaseThemeTinted`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BindAuthKeyInner`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Birthday`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Boost`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotApp`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotAppNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotCommand`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotCommandScopeChatAdmins`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotCommandScopeChats`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotCommandScopeDefault`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotCommandScopePeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotCommandScopePeerAdmins`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotCommandScopePeerUser`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotCommandScopeUsers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotInfo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotInlineMediaResult`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotInlineMessageMediaAuto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotInlineMessageMediaContact`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotInlineMessageMediaGeo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotInlineMessageMediaInvoice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotInlineMessageMediaVenue`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotInlineMessageMediaWebPage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotInlineMessageText`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotInlineResult`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotMenuButton`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotMenuButtonCommands`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotMenuButtonDefault`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotVerification`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BusinessAwayMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BusinessAwayMessageScheduleAlways`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BusinessAwayMessageScheduleCustom`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BusinessAwayMessageScheduleOutsideWorkHours`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BusinessGreetingMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BusinessIntro`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BusinessLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BusinessRecipients`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BusinessWeeklyOpen`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BusinessWorkHours`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CdnConfig`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CdnPublicKey`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Channel`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEvent`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionChangeAbout`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionChangeAvailableReactions`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionChangeBackgroundEmoji`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionChangeColor`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionChangeHistoryTTL`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionChangeLinkedChat`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionChangeLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionChangePhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionChangeStickerSet`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionChangeTitle`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionChangeUsername`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionChangeUsernames`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionCreateTopic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionDefaultBannedRights`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionDeleteMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionDeleteTopic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionDiscardGroupCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionEditMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionEditTopic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionExportedInviteDelete`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionExportedInviteEdit`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionExportedInviteRevoke`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionParticipantInvite`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionParticipantJoin`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionParticipantJoinByInvite`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionParticipantJoinByRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionParticipantLeave`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionParticipantMute`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionParticipantToggleAdmin`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionParticipantToggleBan`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionParticipantUnmute`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionParticipantVolume`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionPinTopic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionSendMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionStartGroupCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionStopPoll`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionToggleAntiSpam`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionToggleForum`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionToggleGroupCallSetting`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionToggleInvites`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionToggleNoForwards`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionTogglePreHistoryHidden`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionToggleSignatures`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionToggleSlowMode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventActionUpdatePinned`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelAdminLogEventsFilter`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelForbidden`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelFull`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelFullCustom`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelLocationEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelMessagesFilter`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelMessagesFilterEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipant`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantAdmin`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantBanned`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantCreator`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantLeft`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantSelf`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantsAdmins`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantsBanned`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantsBots`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantsContacts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantsKicked`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantsMentions`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantsRecent`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantsSearch`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Chat`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatAdminRights`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatAdminWithInvites`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatBannedRights`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatForbidden`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatFull`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatInvite`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatInviteAlready`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatInviteExported`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatInviteImporter`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatInvitePeek`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatInvitePublicJoinRequests`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatOnlines`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatParticipant`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatParticipantAdmin`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatParticipantCreator`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatParticipants`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatParticipantsForbidden`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatPhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatPhotoEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatReactionsAll`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatReactionsDisabled`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatReactionsNone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatReactionsSome`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatTheme`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatThemeUniqueGift`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ClientDHInnerData`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CodeSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ConferenceCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ConferenceCreated`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ConferenceParticipant`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Config`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Contact`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ContactBirthday`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ContactStatus`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DataJSON`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DcOption`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DefaultHistoryTTL`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DestroyAuthKeyFail`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DestroyAuthKeyNone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DestroyAuthKeyOk`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DestroySessionNone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DestroySessionOk`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DhGenFail`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DhGenOk`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DhGenRetry`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Dialog`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DialogFilter`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DialogFilterChatlist`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DialogFilterDefault`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DialogFilterSuggested`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DialogFolder`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DialogPeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DialogPeerFolder`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DisallowedGiftsSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Document`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DocumentAttributeAnimated`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DocumentAttributeAudio`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DocumentAttributeCustomEmoji`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DocumentAttributeFilename`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DocumentAttributeHasStickers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DocumentAttributeImageSize`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DocumentAttributeSticker`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DocumentAttributeVideo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DocumentEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DraftMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DraftMessageEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmailVerificationApple`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmailVerificationCode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmailVerificationGoogle`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmailVerifyPurposeLoginChange`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmailVerifyPurposeLoginSetup`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmailVerifyPurposePassport`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiGroup`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiKeyword`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiKeywordDeleted`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiKeywordsDifference`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiLanguage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiList`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiListNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiStatus`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiStatusEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiStatusUntil`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiURL`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EncryptedChat`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EncryptedChatDiscarded`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EncryptedChatEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EncryptedChatRequested`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EncryptedChatWaiting`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EncryptedFile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EncryptedFileEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EncryptedMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EncryptedMessageService`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportedChatlistInvite`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportedContactToken`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportedMessageLink`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportedStoryLink`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FileHash`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Folder`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FolderPeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ForumTopic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ForumTopicDeleted`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FutureSalt`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FutureSalts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Game`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GenderFemale`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GenderMale`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GeoPoint`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GeoPointEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GlobalPrivacySettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GroupCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GroupCallDiscarded`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GroupCallParticipant`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GroupCallParticipantVideo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GroupCallParticipantVideoSourceGroup`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GroupCallStreamChannel`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `HighScore`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `HttpWait`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ImportedContact`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InlineBotSwitchPM`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InlineBotWebView`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InlineQueryPeerTypeBotPM`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InlineQueryPeerTypeBroadcast`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InlineQueryPeerTypeChat`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InlineQueryPeerTypeMegagroup`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InlineQueryPeerTypePM`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InlineQueryPeerTypeSameBotPM`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputAppEvent`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotAppID`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotAppShortName`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineMessageGame`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineMessageID`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineMessageID64`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineMessageMediaAuto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineMessageMediaContact`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineMessageMediaGeo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineMessageMediaInvoice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineMessageMediaVenue`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineMessageMediaWebPage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineMessageText`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineResult`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineResultDocument`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineResultGame`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputBotInlineResultPhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputChannel`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputChannelEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputChannelFromMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputChatPhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputChatPhotoEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputChatUploadedPhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputChatlistDialogFilter`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputCheckPasswordEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputCheckPasswordSRP`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputClientProxy`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputConferenceCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputConferenceMediaTrack`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputConferenceParticipant`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputDialogPeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputDialogPeerFolder`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputDocument`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputDocumentEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputDocumentFileLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputEncryptedChat`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputEncryptedFile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputEncryptedFileBigUploaded`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputEncryptedFileEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputEncryptedFileLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputEncryptedFileUploaded`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputFile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputFileBig`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputFileLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputFolderPeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputGameID`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputGameShortName`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputGeoPoint`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputGeoPointEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputGroupCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputGroupCallStream`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputInvoiceMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputInvoicePremiumGiftCode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputInvoiceSlug`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputKeyboardButtonUrlAuth`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputKeyboardButtonUserProfile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaAreaVenue`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaContact`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaDice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaDocument`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaDocumentExternal`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaGame`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaGeoLive`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaGeoPoint`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaInvoice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaPayment`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaPhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaPhotoExternal`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaPoll`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaStory`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaUploadedDocument`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaUploadedPhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaVenue`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMediaWebPage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessageCallbackQuery`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessageEntityMentionName`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessageID`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagePinned`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessageReplyTo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterChatPhotos`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterContacts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterDocument`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterGeo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterGif`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterMusic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterMyMentions`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterPhoneCalls`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterPhotoVideo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterPhotos`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterPinned`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterRoundVideo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterRoundVoice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterUrl`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterVideo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputMessagesFilterVoice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputNotifyBroadcasts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputNotifyChats`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputNotifyForumTopic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputNotifyPeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputNotifyUsers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPaymentCredentials`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPaymentCredentialsApplePay`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPaymentCredentialsGooglePay`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPaymentCredentialsSaved`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPeerChannel`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPeerChannelFromMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPeerChat`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPeerEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPeerNotifySettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPeerPhotoFileLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPeerSelf`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPeerUser`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPeerUserFromMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPhoneCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPhoneContact`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPhotoEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPhotoFileLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPhotoLegacyFileLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyAbout`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyAddedByPhone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyBirthday`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyChatInvite`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyForwards`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyGender`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyPhoneCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyPhoneNumber`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyPhoneP2P`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyProfilePhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyReceiveMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeySavedMusic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyStatusTimestamp`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyKeyVoiceMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyValueAllowAll`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyValueAllowChatParticipants`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyValueAllowCloseFriends`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyValueAllowContacts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyValueAllowUsers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyValueDisallowAll`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyValueDisallowChatParticipants`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyValueDisallowContacts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputPrivacyValueDisallowUsers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputReplyToMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputReplyToStory`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputReportReasonChildAbuse`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputReportReasonCopyright`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputReportReasonFake`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputReportReasonGeoIrrelevant`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputReportReasonIllegalDrugs`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputReportReasonOther`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputReportReasonPersonalDetails`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputReportReasonPornography`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputReportReasonSpam`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputReportReasonViolence`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputSecureFile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputSecureFileLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputSecureFileUploaded`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputSecureValue`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputSingleMedia`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickerSetAnimatedEmoji`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickerSetAnimatedEmojiAnimations`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickerSetDice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickerSetEmojiDefaultStatuses`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickerSetEmojiDefaultTopicIcons`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickerSetEmojiGenericAnimations`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickerSetEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickerSetID`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickerSetItem`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickerSetPremiumGifts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickerSetShortName`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickerSetThumb`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickeredMediaDocument`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStickeredMediaPhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStorePaymentGiftPremium`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStorePaymentPremiumGiftCode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStorePaymentPremiumGiveaway`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputStorePaymentPremiumSubscription`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputTakeoutFileLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputTheme`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputThemeSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputThemeSlug`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputUser`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputUserEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputUserFromMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputUserSelf`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputWallPaper`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputWallPaperNoFile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputWallPaperSlug`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputWebDocument`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputWebFileAudioAlbumThumbLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputWebFileGeoPointLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InputWebFileLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Invoice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `IpPort`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `IpPortSecret`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JsonArray`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JsonBool`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JsonNull`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JsonNumber`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JsonObject`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JsonObjectValue`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JsonString`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButton`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonBuy`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonCallback`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonGame`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonRequestGeoLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonRequestPeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonRequestPhone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonRequestPoll`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonRow`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonSimpleWebView`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonSwitchInline`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonUrl`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonUrlAuth`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonUserProfile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `KeyboardButtonWebView`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LabeledPrice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LangPackDifference`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LangPackLanguage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LangPackString`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LangPackStringDeleted`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LangPackStringPluralized`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MaskCoords`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MediaAreaCoordinates`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MediaAreaGeoPoint`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MediaAreaSuggestedReaction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MediaAreaUrl`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MediaAreaVenue`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Message`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionBotAllowed`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionChannelCreate`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionChannelMigrateFrom`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionChatAddUser`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionChatCreate`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionChatDeletePhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionChatDeleteUser`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionChatEditPhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionChatEditTitle`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionChatJoinedByLink`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionChatJoinedByRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionChatMigrateTo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionContactReturned`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionContactSignUp`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionCustomAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionGameScore`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionGeoProximityReached`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionGiftCode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionGiftPremium`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionGiveawayLaunch`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionGiveawayResults`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionGroupCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionGroupCallScheduled`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionHistoryClear`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionInviteToGroupCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionPaymentSent`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionPaymentSentMe`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionPhoneCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionPinMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionProtectedMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionRequestedPeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionScreenshotTaken`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionSecureValuesSent`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionSecureValuesSentMe`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionSetChatTheme`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionSetChatWallPaper`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionSetMessagesTTL`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionSuggestProfilePhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionTopicCreate`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionTopicEdit`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionWebViewDataSent`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageActionWebViewDataSentMe`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityBankCard`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityBlockquote`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityBold`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityBotCommand`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityCashtag`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityCode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityCustomEmoji`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityEmail`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityHashtag`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityItalic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityMention`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityMentionName`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityPhone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityPre`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntitySpoiler`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityStrike`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityTextUrl`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityUnderline`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityUnknown`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEntityUrl`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageExtendedMedia`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageExtendedMediaPreview`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageFwdHeader`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaContact`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaDice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaDocument`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaGame`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaGeo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaGeoLive`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaGiveaway`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaInvoice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaPayment`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaPhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaPoll`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaStory`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaUnsupported`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaVenue`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageMediaWebPage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessagePeerReaction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessagePeerVote`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessagePeerVoteInputOption`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessagePeerVoteMultiple`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageRange`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageReactions`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageReplies`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageReplyHeader`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageReplyStoryHeader`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageService`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageViews`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MsgDetailedInfo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MsgNewDetailedInfo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MsgResendReq`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MsgsAck`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MsgsAllInfo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MsgsStateInfo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MsgsStateReq`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MyBoost`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `NearestDc`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `NewSessionCreated`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `NotificationSoundDefault`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `NotificationSoundLocal`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `NotificationSoundNone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `NotificationSoundRingtone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `NotifyBroadcasts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `NotifyChats`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `NotifyForumTopic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `NotifyPeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `NotifyUsers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PQInnerData`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PQInnerDataDc`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PQInnerDataTemp`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PQInnerDataTempDc`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Page`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockAnchor`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockAudio`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockAuthorDate`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockBlockquote`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockChannel`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockCollage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockCover`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockDetails`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockDivider`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockEmbed`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockEmbedPost`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockFooter`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockHeader`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockKicker`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockList`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockMap`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockOrderedList`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockParagraph`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockPhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockPreformatted`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockPullquote`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockRelatedArticles`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockSlideshow`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockSubheader`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockSubtitle`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockTable`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockTitle`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockUnsupported`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageBlockVideo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageCaption`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageListItemBlocks`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageListItemText`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageListOrderedItemBlocks`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageListOrderedItemText`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageRelatedArticle`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageTableCell`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PageTableRow`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ParticipantLocation`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PasswordKdfAlgoUnknown`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PaymentCharge`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PaymentFormMethod`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PaymentRequestedInfo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PaymentSavedCredentialsCard`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerBlocked`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerChannel`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerChat`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerColor`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerLocated`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerNotifySettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerSelfLocated`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerStories`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerUser`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneCallAccepted`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneCallDiscardReasonBusy`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneCallDiscardReasonDisconnect`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneCallDiscardReasonHangup`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneCallDiscardReasonMissed`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneCallDiscarded`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneCallEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneCallProtocol`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneCallRequested`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneCallWaiting`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneConnection`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneConnectionWebrtc`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Photo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhotoCachedSize`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhotoEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhotoPathSize`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhotoSize`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhotoSizeEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhotoSizeProgressive`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhotoStrippedSize`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Poll`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PollAnswer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PollAnswerVoters`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PollResults`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Pong`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PopularContact`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PostAddress`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PostInteractionCountersMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PostInteractionCountersStory`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PremiumGiftCodeOption`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PremiumGiftOption`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PremiumSubscriptionOption`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrepaidGiveaway`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyAbout`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyAddedByPhone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyBirthday`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyChatInvite`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyForwards`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyGender`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyPhoneCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyPhoneNumber`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyPhoneP2P`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyProfilePhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyReceiveMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeySavedMusic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyStatusTimestamp`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyKeyVoiceMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyValueAllowAll`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyValueAllowChatParticipants`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyValueAllowCloseFriends`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyValueAllowContacts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyValueAllowUsers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyValueDisallowAll`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyValueDisallowChatParticipants`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyValueDisallowContacts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyValueDisallowUsers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ProfileTabFiles`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ProfileTabGifs`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ProfileTabGifts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ProfileTabLinks`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ProfileTabMedia`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ProfileTabMusic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ProfileTabPosts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ProfileTabVoice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PublicForwardMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PublicForwardStory`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReactionCount`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReactionCustomEmoji`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReactionEmoji`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReactionEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReadParticipantDate`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReceivedNotifyMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RecentMeUrlChat`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RecentMeUrlChatInvite`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RecentMeUrlStickerSet`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RecentMeUrlUnknown`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RecentMeUrlUser`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReplyInlineMarkup`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReplyKeyboardForceReply`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReplyKeyboardHide`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReplyKeyboardMarkup`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RequestPeerTypeBroadcast`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RequestPeerTypeChat`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RequestPeerTypeUser`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResPQ`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RestrictionReason`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RpcAnswerDropped`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RpcAnswerDroppedRunning`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RpcAnswerUnknown`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RpcError`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SavedPhoneContact`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SearchResultPosition`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SearchResultsCalendarPeriod`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureCredentialsEncrypted`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureData`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureFile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureFileEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecurePasswordKdfAlgoSHA512`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecurePasswordKdfAlgoUnknown`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecurePlainEmail`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecurePlainPhone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureRequiredType`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureRequiredTypeOneOf`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureSecretSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValue`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueError`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueErrorData`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueErrorFile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueErrorFiles`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueErrorFrontSide`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueErrorReverseSide`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueErrorSelfie`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueErrorTranslationFile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueErrorTranslationFiles`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueHash`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypeAddress`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypeBankStatement`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypeDriverLicense`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypeEmail`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypeIdentityCard`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypeInternalPassport`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypePassport`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypePassportRegistration`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypePersonalDetails`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypePhone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypeRentalAgreement`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypeTemporaryRegistration`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SecureValueTypeUtilityBill`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendAsPeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageCancelAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageChooseContactAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageChooseStickerAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageEmojiInteraction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageEmojiInteractionSeen`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageGamePlayAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageGeoLocationAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageHistoryImportAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageRecordAudioAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageRecordRoundAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageRecordVideoAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageTypingAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageUploadAudioAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageUploadDocumentAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageUploadPhotoAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageUploadRoundAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendMessageUploadVideoAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ServerDHInnerData`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ServerDHParamsFail`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ServerDHParamsOk`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ShippingOption`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SimpleWebViewResultUrl`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SpeakingInGroupCallAction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SponsoredMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SponsoredWebPage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StarGift`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StarGiftAttributeBackdrop`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StarGiftAttributeModel`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StarGiftAttributeOriginalDetails`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StarGiftAttributePattern`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StarGiftUnique`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StarRefProgram`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StarsAmount`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StarsRating`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StarsTonAmount`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StatsAbsValueAndPrev`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StatsDateRangeDays`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StatsGraph`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StatsGraphAsync`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StatsGraphError`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StatsGroupTopAdmin`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StatsGroupTopInviter`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StatsGroupTopPoster`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StatsPercentValue`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StatsURL`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StickerKeyword`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StickerPack`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StickerSet`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StickerSetCovered`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StickerSetFullCovered`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StickerSetMultiCovered`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StickerSetNoCovered`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StoriesStealthMode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StoryFwdHeader`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StoryItem`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StoryItemDeleted`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StoryItemSkipped`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StoryView`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StoryViews`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextAnchor`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextBold`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextConcat`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextEmail`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextFixed`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextImage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextItalic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextMarked`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextPhone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextPlain`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextStrike`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextSubscript`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextSuperscript`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextUnderline`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextUrl`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TextWithEntities`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Theme`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ThemeSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Timezone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TlsBlockDomain`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TlsBlockGrease`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TlsBlockPublicKey`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TlsBlockRandom`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TlsBlockScope`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TlsBlockString`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TlsBlockZero`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TlsClientHello`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeerCategoryBotsInline`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeerCategoryBotsPM`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeerCategoryChannels`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeerCategoryCorrespondents`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeerCategoryForwardChats`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeerCategoryForwardUsers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeerCategoryGroups`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeerCategoryPeers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeerCategoryPhoneCalls`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateAttachMenuBots`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateAutoSaveSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBotCallbackQuery`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBotChatBoost`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBotChatInviteRequester`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBotCommands`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBotInlineQuery`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBotInlineSend`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBotMenuButton`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBotPrecheckoutQuery`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBotShippingQuery`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBotStopped`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBotWebhookJSON`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateBotWebhookJSONQuery`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChannel`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChannelAvailableMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChannelMessageForwards`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChannelMessageViews`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChannelParticipant`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChannelPinnedTopic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChannelPinnedTopics`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChannelReadMessagesContents`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChannelTooLong`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChannelUserTyping`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChannelViewForumAsMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChannelWebPage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChat`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChatDefaultBannedRights`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChatParticipant`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChatParticipantAdd`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChatParticipantAdmin`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChatParticipantDelete`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChatParticipants`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateChatUserTyping`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateConferenceCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateConferenceCallConnection`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateConferenceCallParticipant`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateConfig`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateContactsReset`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateDcOptions`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateDeleteChannelMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateDeleteMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateDeleteScheduledMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateDialogFilter`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateDialogFilterOrder`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateDialogFilters`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateDialogPinned`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateDialogUnreadMark`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateDraftMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateEditChannelMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateEditMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateEncryptedChatTyping`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateEncryptedMessagesRead`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateEncryption`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateFavedStickers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateFolderPeers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateGeoLiveViewed`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateGroupCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateGroupCallConnection`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateGroupCallParticipants`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateGroupInvitePrivacyForbidden`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateInlineBotCallbackQuery`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateLangPack`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateLangPackTooLong`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateLoginToken`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateMessageExtendedMedia`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateMessageID`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateMessagePoll`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateMessagePollVote`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateMessageReactions`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateMoveStickerSetToTop`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateNewAuthorization`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateNewChannelMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateNewEncryptedMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateNewMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateNewScheduledMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateNewStickerSet`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateNotifySettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePeerBlocked`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePeerHistoryTTL`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePeerLocated`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePeerSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePeerWallpaper`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePendingJoinRequests`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePhoneCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePhoneCallSignalingData`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePinnedChannelMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePinnedDialogs`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePinnedMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePrivacy`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatePtsChanged`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateReadChannelDiscussionInbox`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateReadChannelDiscussionOutbox`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateReadChannelInbox`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateReadChannelOutbox`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateReadFeaturedEmojiStickers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateReadFeaturedStickers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateReadHistoryInbox`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateReadHistoryOutbox`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateReadMessagesContents`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateReadStories`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateRecentEmojiStatuses`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateRecentReactions`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateRecentStickers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateSavedGifs`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateSavedRingtones`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateSentStoryReaction`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateServiceNotification`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateShort`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateShortChatMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateShortMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateShortSentMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateStickerSets`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateStickerSetsOrder`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateStoriesStealthMode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateStory`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateStoryID`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateTheme`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateTranscribedAudio`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateUser`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateUserEmojiStatus`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateUserName`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateUserPhone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateUserStatus`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateUserTyping`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateWebPage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdateWebViewResultSent`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Updates`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatesCombined`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UpdatesTooLong`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UrlAuthResultAccepted`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UrlAuthResultDefault`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UrlAuthResultRequest`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `User`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserFull`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserFullCustom`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserProfilePhoto`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserProfilePhotoEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserStatusEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserStatusLastMonth`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserStatusLastWeek`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserStatusOffline`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserStatusOnline`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserStatusRecently`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserTypeBusiness`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserTypeMxb`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserTypeNormal`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserTypeNotify`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserTypeUnknown`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Username`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `VideoSize`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `VideoSizeEmojiMarkup`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `VideoSizeStickerMarkup`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WallPaper`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WallPaperNoFile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WallPaperSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebAuthorization`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebDocument`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebDocumentNoProxy`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebPage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebPageAttributeStory`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebPageAttributeTheme`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebPageEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebPageNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebPagePending`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebViewMessageSent`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebViewResultUrl`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FactCheck`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SuggestedPost`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/account.py`

### کلاس `AuthorizationForm`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Authorizations`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AutoDownloadSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AutoSaveSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ContentSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmailVerified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmailVerifiedLogin`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiStatuses`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiStatusesNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Password`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PasswordInputSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PasswordSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PrivacyRules`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResetPasswordFailedWait`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResetPasswordOk`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResetPasswordRequestedWait`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SavedMusicIds`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SavedMusicIdsNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SavedRingtone`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SavedRingtoneConverted`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SavedRingtones`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SavedRingtonesNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentEmailCode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Takeout`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Themes`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ThemesNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TmpPassword`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WallPapers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WallPapersNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebAuthorizations`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/auth.py`

### کلاس `Authorization`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AuthorizationSignUpRequired`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CodeTypeCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CodeTypeFlashCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CodeTypeFragmentSms`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CodeTypeMissedCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CodeTypeSms`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportedAuthorization`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LoggedOut`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LoginToken`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LoginTokenMigrateTo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `LoginTokenSuccess`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PasswordRecovery`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentCode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentCodeSuccess`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentCodeTypeApp`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentCodeTypeCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentCodeTypeEmailCode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentCodeTypeFirebaseSms`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentCodeTypeFlashCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentCodeTypeFragmentSms`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentCodeTypeMissedCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentCodeTypeSetUpEmailRequired`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentCodeTypeSms`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentDeleteAccountCode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/bots.py`

### کلاس `BotInfo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/channels.py`

### کلاس `AdminLogResults`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipant`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipants`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelParticipantsNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SendAsPeers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/chatlists.py`

### کلاس `ChatlistInvite`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatlistInviteAlready`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatlistUpdates`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportedChatlistInvite`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportedInvites`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/conference.py`

### کلاس `ConferenceCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/contacts.py`

### کلاس `Blocked`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BlockedSlice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ContactBirthdays`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Contacts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ContactsNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Found`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ImportedContacts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ResolvedPeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeersDisabled`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TopPeersNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/help.py`

### کلاس `AppConfig`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AppConfigNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AppUpdate`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ConfigSimple`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CountriesList`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CountriesListNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Country`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CountryCode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeepLinkInfo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DeepLinkInfoEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InviteText`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `NoAppUpdate`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PassportConfig`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PassportConfigNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerColorOption`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerColorProfileSet`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerColorSet`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerColors`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerColorsNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PremiumPromo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PromoData`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PromoDataEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RecentMeUrls`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Support`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SupportName`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TermsOfService`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TermsOfServiceUpdate`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TermsOfServiceUpdateEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TimezonesList`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TimezonesListNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserInfo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserInfoEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/messages.py`

### کلاس `AffectedFoundMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AffectedHistory`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AffectedMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AllStickers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AllStickersNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ArchivedStickers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AvailableReactions`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AvailableReactionsNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotApp`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotCallbackAnswer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BotResults`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatAdminsWithInvites`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatFull`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatInviteImporters`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Chats`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChatsSlice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CheckedHistoryImportPeer`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DhConfig`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DhConfigNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DialogFilters`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Dialogs`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DialogsNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DialogsSlice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DiscussionMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiGroups`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `EmojiGroupsNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportedChatInvite`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportedChatInviteReplaced`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportedChatInvites`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FavedStickers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FavedStickersNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FeaturedStickers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FeaturedStickersNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ForumTopics`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FoundStickerSets`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FoundStickerSetsNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `HighScores`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `HistoryImport`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `HistoryImportParsed`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `InactiveChats`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageEditData`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageReactionsList`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageViews`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Messages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessagesNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessagesSlice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerDialogs`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerSettings`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Reactions`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ReactionsNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RecentStickers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `RecentStickersNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SavedGifs`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SavedGifsNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SearchCounter`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SearchResultsCalendar`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SearchResultsPositions`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentEncryptedFile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SentEncryptedMessage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SponsoredMessages`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SponsoredMessagesEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StickerSet`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StickerSetInstallResultArchive`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StickerSetInstallResultSuccess`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StickerSetNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Stickers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StickersNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TranscribedAudio`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `TranslateResult`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `VotesList`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebPage`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/payments.py`

### کلاس `BankCardData`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CheckedGiftCode`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ExportedInvoice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GiveawayInfo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GiveawayInfoResults`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PaymentForm`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PaymentReceipt`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PaymentResult`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PaymentVerificationNeeded`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SavedInfo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ValidatedRequestedInfo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/phone.py`

### کلاس `ExportedGroupCallInvite`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GroupCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GroupCallStreamChannels`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GroupCallStreamRtmpUrl`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `GroupParticipants`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `JoinAsPeers`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhoneCall`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/photos.py`

### کلاس `Photo`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Photos`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PhotosSlice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/premium.py`

### کلاس `BoostsList`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `BoostsStatus`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MyBoosts`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/stats.py`

### کلاس `BroadcastStats`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MegagroupStats`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `MessageStats`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PublicForwards`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StoryStats`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/stickers.py`

### کلاس `SuggestedShortName`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/storage.py`

### کلاس `FileGif`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FileJpeg`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FileMov`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FileMp3`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FileMp4`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FilePartial`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FilePdf`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FilePng`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FileUnknown`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FileWebp`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/stories.py`

### کلاس `AllStories`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `AllStoriesNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `PeerStories`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Stories`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StoryViews`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `StoryViewsList`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/thirdParty.py`

### کلاس `Message`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Reply`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/update.py`

### کلاس `ThirdParty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/updates.py`

### کلاس `ChannelDifference`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelDifferenceEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `ChannelDifferenceTooLong`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `Difference`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DifferenceEmpty`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DifferenceSlice`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `DifferenceTooLong`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `State`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/upload.py`

### کلاس `CdnFile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `CdnFileReuploadNeeded`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `File`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `FileCdnRedirect`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `WebFile`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `tl/types/users.py`

### کلاس `SavedMusic`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `SavedMusicNotModified`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

### کلاس `UserFull`

- `def to_dict(self)`
- `def from_reader(cls, reader)`

## `utils.py`

### توابع عمومی

- `def chunks(iterable, size=100)`
- `def get_display_name(entity)`
- `def get_extension(media)`
- `def get_input_peer(entity, allow_self=True, check_hash=True)`
- `def get_input_channel(entity)`
- `def get_input_user(entity)`
- `def get_input_dialog(dialog)`
- `def get_input_document(document)`
- `def get_input_photo(photo)`
- `def get_input_chat_photo(photo)`
- `def get_input_geo(geo)`
- `def get_input_media(media, *, is_photo=False, attributes=None, force_document=False, voice_note=False, video_note=False, supports_streaming=False, ttl=None)`
- `def get_input_message(message)`
- `def get_input_group_call(call)`
- `def get_message_id(message)`
- `def get_attributes(file, *, attributes=None, mime_type=None, force_document=False, voice_note=False, video_note=False, supports_streaming=False, thumb=None)`
- `def sanitize_parse_mode(mode)`
- `def get_input_location(location)`
- `def is_image(file)`
- `def is_gif(file)`
- `def is_audio(file)`
- `def is_video(file)`
- `def is_list_like(obj)`
- `def parse_phone(phone)`
- `def parse_username(username)`
- `def get_inner_text(text, entities)`
- `def get_peer(peer)`
- `def get_peer_id(peer, add_mark=True)`
- `def resolve_id(marked_id)`
- `def resolve_bot_file_id(file_id)`
- `def pack_bot_file_id(file)`
- `def resolve_invite_link(link)`
- `def resolve_inline_message_id(inline_msg_id)`
- `def get_appropriated_part_size(file_size)`
- `def encode_waveform(waveform)`
- `def decode_waveform(waveform)`
- `def split_text(text, entities, *, limit=4096, max_entities=100, split_at=('\\n', '\\s', '.'))`
- `def stripped_photo_to_jpg(stripped)`
- `async def maybe_async(coro)`

