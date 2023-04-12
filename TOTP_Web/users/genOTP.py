
import datetime
from pyotp import TOTP

hmacKey = 'MYSCRET'

b = datetime.datetime(2023, 3, 22, 6, 00, 2)

def genOTP(serial):
    # TODO: thay secret = hmacKey + serial
    # secret = hmacKey+serial
    totp = TOTP(hmacKey)
    b_ts = int(b.timestamp())
    now_ts = int(datetime.datetime.now().timestamp())
    gmt = int(now_ts - b_ts)//30
    new_code = totp.at(b_ts, gmt)
    code = ''
    if code != new_code:
        code = new_code
    return code
