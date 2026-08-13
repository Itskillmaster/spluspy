import getpass
import inspect
import logging
import os
import sys
import typing
import warnings

from .. import utils, helpers, errors, password as pwd_mod
from .._updates import SessionState
from ..tl import functions, types

_log = logging.getLogger(__name__)


class AuthMethods:

    def start(
            self: typing.Any,
            phone: typing.Union[typing.Callable[[], typing.Union[str, typing.Awaitable[str]]], str] = lambda: input('Please enter your phone: '),
            password: typing.Union[typing.Callable[[], typing.Union[str, typing.Awaitable[str]]], str] = lambda: getpass.getpass('Please enter your password: '),
            *,
            code_callback: typing.Optional[typing.Callable[[], typing.Union[str, int, typing.Awaitable[typing.Union[str, int]]]]] = None,
            first_name: str = 'New User',
            last_name: str = '',
            max_attempts: int = 3) -> typing.Any:
        if code_callback is None:
            def code_callback() -> str:
                return input('Please enter the code you received: ')
        elif not callable(code_callback):
            raise ValueError(
                'The code_callback parameter needs to be a callable '
                'function that returns the code you received by SoroushPlus.'
            )

        if not phone:
            raise ValueError('No phone number provided.')

        coro = self._start(
            phone=phone,
            password=password,
            code_callback=code_callback,
            first_name=first_name,
            last_name=last_name,
            max_attempts=max_attempts
        )
        return (
            coro if self.loop.is_running()
            else self.loop.run_until_complete(coro)
        )

    async def _check_for_updates(self: typing.Any):
        try:
            import aiohttp
            from ..version import __version__
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    'https://pypi.org/pypi/SplusPy/json',
                    timeout=aiohttp.ClientTimeout(total=3)
                ) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        latest = data.get('info', {}).get('version', '')
                        if latest:
                            cur = tuple(int(x) for x in __version__.split('.'))
                            new = tuple(int(x) for x in latest.split('.'))
                            if new > cur:
                                _log.warning(
                                    '\033[93m⚠️  A new version of SplusPy (v%s) is available! '
                                    'You are running v%s. Please update: '
                                    'pip install --upgrade SplusPy\033[0m',
                                    latest, __version__
                                )
        except Exception:
            pass

    async def _start(
            self: typing.Any, phone, password, code_callback, first_name, last_name, max_attempts) -> typing.Any:
        self.loop.create_task(self._check_for_updates())

        if not self.is_connected():
            await self.connect()

        if await self.is_user_authorized():
            try:
                me = await self.get_me()
                if me is not None and hasattr(me, 'phone'):
                    if phone and not callable(phone) and utils.parse_phone(str(phone)) != getattr(me, 'phone', None):
                        warnings.warn(
                            'the session already had an authorized user so it did '
                            'not login to the user account using the provided phone; '
                            'if you were expecting a different user, check whether '
                            'you are accidentally reusing an existing session'
                        )
            except Exception as e:
                _log.debug('Failed to verify existing session user: %s', e)

            return self

        while callable(phone):
            value = phone()
            if inspect.isawaitable(value):
                value = await value

            phone = utils.parse_phone(str(value)) or phone

        attempts = 0
        two_step_detected = False

        await self.send_code_request(str(phone), code_callback=code_callback)
        while attempts < max_attempts:
            try:
                value = code_callback()
                if inspect.isawaitable(value):
                    value = await value

                if not value:
                    raise errors.PhoneCodeEmptyError(request=None)

                await self.sign_in(str(phone), code=value)
                break
            except errors.SessionPasswordNeededError:
                two_step_detected = True
                break
            except errors.PhoneNumberInvalidError:
                if hasattr(self, '_phone_code_hash'):
                    typing.cast(typing.Any, self)._phone_code_hash.clear()
                self._authorized = False
                await self.disconnect()
                if hasattr(self, '_sender') and typing.cast(typing.Any, self)._sender and hasattr(typing.cast(typing.Any, self)._sender, 'auth_key'):
                    typing.cast(typing.Any, self)._sender.auth_key.key = None
                if hasattr(self, 'session') and typing.cast(typing.Any, self).session:
                    typing.cast(typing.Any, self).session.auth_key = None
                await self.connect()
                await self.send_code_request(str(phone), code_callback=code_callback)
                print('Connection was lost. A new code has been sent.', file=sys.stderr)
            except (errors.PhoneCodeEmptyError,
                    errors.PhoneCodeExpiredError,
                    errors.PhoneCodeHashEmptyError,
                    errors.PhoneCodeInvalidError):
                print('Invalid code. Please try again.', file=sys.stderr)

            attempts += 1
        else:
            raise RuntimeError(
                '{} consecutive sign-in attempts failed. Aborting'
                .format(max_attempts)
            )

        me = None
        if two_step_detected:
            if not password:
                raise ValueError(
                    "Two-step verification is enabled for this account. "
                    "Please provide the 'password' argument to 'start()'."
                )

            if callable(password):
                for _ in range(max_attempts):
                    try:
                        value = password()
                        if inspect.isawaitable(value):
                            value = await value

                        me = await self.sign_in(phone=str(phone), password=str(value))
                        break
                    except errors.PasswordHashInvalidError:
                        print('Invalid password. Please try again', file=sys.stderr)
            else:
                me = await self.sign_in(phone=str(phone), password=str(password))

        signed, name = 'Signed in successfully as ', utils.get_display_name(me) if me else 'User'
        tos = '; remember to not break the ToS or you will risk an account ban!'
        try:
            print(signed, name, tos, sep='')
        except UnicodeEncodeError:
            print(signed, str(name).encode('utf-8', errors='ignore')
                  .decode('ascii', errors='ignore'), tos, sep='')

        return self

    def _parse_phone_and_hash(self, phone, phone_hash):
        parsed_phone = utils.parse_phone(str(phone)) if phone else getattr(self, '_phone', None)
        if not parsed_phone:
            raise ValueError(
                'Please make sure to call send_code_request first.'
            )

        p_hash = phone_hash or getattr(self, '_phone_code_hash', {}).get(parsed_phone, None)
        if not p_hash:
            raise ValueError('You also need to provide a phone_code_hash.')

        return parsed_phone, p_hash

    async def sign_in(
            self: typing.Any,
            phone: typing.Optional[str] = None,
            code: typing.Optional[typing.Union[str, int]] = None,
            *,
            password: typing.Optional[str] = None,
            phone_code_hash: typing.Optional[str] = None) -> typing.Any:
        me = None
        if not (phone and code):
            try:
                me = await self.get_me()
            except Exception as e:
                _log.debug('get_me failed, checking auth state: %s', e)
                if await self.is_user_authorized():
                    return None
            if me:
                return me

        request: typing.Any = None
        if phone and not code and not password:
            return await self.send_code_request(phone)
        elif code:
            phone_str, p_hash = self._parse_phone_and_hash(phone, phone_code_hash)
            request = functions.auth.SignInRequest(
                str(phone_str), str(p_hash), str(code)
            )
        elif password:
            pwd = await self(functions.account.GetPasswordRequest())
            check_req = pwd_mod.compute_check(pwd, password)
            request = typing.cast(typing.Any, check_req)
        else:
            raise ValueError(
                'You must provide a phone and a code the first time, '
                'and a password only if an RPCError was raised before.'
            )

        try:
            result = await self(request)
        except errors.PhoneCodeExpiredError:
            if phone and hasattr(self, '_phone_code_hash'):
                typing.cast(typing.Any, self)._phone_code_hash.pop(phone, None)
            raise
        except errors.PhoneNumberInvalidError:
            self._authorized = None
            if await self.is_user_authorized():
                try:
                    me = await self.get_me()
                except Exception as e:
                    _log.debug('get_me failed after auth check: %s', e)
                    me = None
                if me:
                    return await self._on_login(me)
                try:
                    state = await self(functions.updates.GetStateRequest())
                    difference = await self(functions.updates.GetDifferenceRequest(
                        pts=state.pts, date=state.date, qts=state.qts))
                    if isinstance(difference, types.updates.Difference):
                        state = difference.state
                    elif isinstance(difference, types.updates.DifferenceSlice):
                        state = difference.intermediate_state
                    elif isinstance(difference, types.updates.DifferenceTooLong):
                        state.pts = difference.pts
                    if hasattr(self, '_message_box'):
                        typing.cast(typing.Any, self)._message_box.load(
                            SessionState(0, 0, False, state.pts, state.qts,
                                         int(state.date.timestamp()), state.seq, 0),
                            [])
                except Exception as e:
                    _log.debug('Failed to initialize message box during login: %s', e)
                return None
            raise

        if isinstance(result, types.auth.AuthorizationSignUpRequired):
            self._tos = getattr(result, 'terms_of_service', None)
            raise errors.PhoneNumberUnoccupiedError(request=request)

        return await self._on_login(result.user)

    async def sign_up(
            self: typing.Any,
            code: typing.Union[str, int],
            first_name: str,
            last_name: str = '',
            *,
            phone: typing.Optional[str] = None,
            phone_code_hash: typing.Optional[str] = None) -> typing.Any:
        raise ValueError('Third-party applications cannot sign up for SoroushPlus.')

    async def _on_login(self, user):
        if hasattr(self, '_mb_entity_cache'):
            typing.cast(typing.Any, self)._mb_entity_cache.set_self_user(user.id, getattr(user, 'bot', False), getattr(user, 'access_hash', 0))
        self._authorized = True

        state = await self(functions.updates.GetStateRequest())
        difference = await self(functions.updates.GetDifferenceRequest(pts=state.pts, date=state.date, qts=state.qts))

        if isinstance(difference, types.updates.Difference):
            state = difference.state
        elif isinstance(difference, types.updates.DifferenceSlice):
            state = difference.intermediate_state
        elif isinstance(difference, types.updates.DifferenceTooLong):
            state.pts = difference.pts

        if hasattr(self, '_message_box'):
            typing.cast(typing.Any, self)._message_box.load(SessionState(0, 0, False, state.pts, state.qts, int(state.date.timestamp()), state.seq, 0), [])

        return user

    async def send_code_request(
            self: typing.Any,
            phone: str,
            *,
            code_callback: typing.Optional[typing.Callable[[], typing.Union[str, int]]] = None,
            _retry_count: int = 0) -> typing.Any:
        parsed_phone = utils.parse_phone(str(phone)) or getattr(self, '_phone', None)
        phone_hash = getattr(self, '_phone_code_hash', {}).get(parsed_phone) if hasattr(self, '_phone_code_hash') else None

        if not phone_hash:
            try:
                result = await self(functions.auth.SendCodeRequest(
                    str(parsed_phone), typing.cast(typing.Any, self).api_id, typing.cast(typing.Any, self).api_hash, types.CodeSettings()))
            except errors.AuthRestartError:
                if _retry_count > 2:
                    raise
                return await self.send_code_request(
                    str(parsed_phone), code_callback=code_callback, _retry_count=_retry_count+1)

            if isinstance(result, types.auth.SentCodeSuccess):
                raise RuntimeError('logged in right after sending the code')

            if hasattr(result, 'phone_code_hash') and result.phone_code_hash and phone_hash is None:
                if not hasattr(self, '_phone_code_hash'):
                    typing.cast(typing.Any, self)._phone_code_hash = {}
                typing.cast(typing.Any, self)._phone_code_hash[parsed_phone] = result.phone_code_hash
        else:
            pass

        self._phone = parsed_phone

        if hasattr(result, 'phone_code_hash'):
            if not hasattr(self, '_phone_code_hash'):
                typing.cast(typing.Any, self)._phone_code_hash = {}
            typing.cast(typing.Any, self)._phone_code_hash[parsed_phone] = result.phone_code_hash

        return result

    async def qr_login(self: typing.Any, ignored_ids: typing.Optional[typing.List[int]] = None) -> typing.Any:
        raise ValueError('QR login is not supported for self-bots.')

    async def log_out(self: typing.Any) -> bool:
        try:
            await self(functions.auth.LogOutRequest())
        except errors.RPCError as e:
            _log.debug('Logout failed: %s', e)
            return False

        if hasattr(self, '_mb_entity_cache'):
            typing.cast(typing.Any, self)._mb_entity_cache.set_self_user(None, None, None)
        self._authorized = False

        await self.disconnect()
        if hasattr(self, 'session') and typing.cast(typing.Any, self).session:
            await utils.maybe_async(typing.cast(typing.Any, self).session.delete())
            typing.cast(typing.Any, self).session = None
        return True

    async def edit_2fa(
            self: typing.Any,
            current_password: typing.Optional[str] = None,
            new_password: typing.Optional[str] = None,
            *,
            hint: str = '',
            email: typing.Optional[str] = None,
            email_code_callback: typing.Optional[typing.Callable[[int], typing.Union[str, typing.Awaitable[str]]]] = None) -> bool:
        if new_password is None and current_password is None:
            return False

        pwd = await self(functions.account.GetPasswordRequest())
        if hasattr(pwd, 'new_algo') and hasattr(pwd.new_algo, 'salt1'):
            pwd.new_algo.salt1 += os.urandom(32)
        assert isinstance(pwd, types.account.Password)
        if not getattr(pwd, 'has_password', False) and current_password:
            current_password = None

        if current_password:
            password = pwd_mod.compute_check(pwd, current_password)
        else:
            password = types.InputCheckPasswordEmpty()

        if new_password:
            new_password_hash = pwd_mod.compute_digest(
                typing.cast(typing.Any, pwd.new_algo), new_password)
        else:
            new_password_hash = b''

        try:
            await self(functions.account.UpdatePasswordSettingsRequest(
                password=password,
                new_settings=types.account.PasswordInputSettings(
                    new_algo=pwd.new_algo,
                    new_password_hash=new_password_hash,
                    hint=hint,
                    email=email,
                    new_secure_settings=None
                )
            ))
        except errors.EmailUnconfirmedError as e:
            if email_code_callback:
                code = email_code_callback(getattr(e, 'code_length', 5))
                if inspect.isawaitable(code):
                    code = await code

                code = str(code)
                await self(functions.account.ConfirmPasswordEmailRequest(code))

        return True

    async def __aenter__(self):
        return await self.start()

    async def __aexit__(self, *args):
        await self.disconnect()

    __enter__ = helpers._sync_enter
    __exit__ = helpers._sync_exit