from ctypes import *
from ctypes.util import find_library

lib = CDLL(find_library('sips'))

class CallParm(Structure):
    _fields_ = [
        # reserve a l'api
        ("version", c_char*6),
        ("certificate_date", c_char*9),
        ("browser_type", c_char*129),
        
        # obligatoire
        ("merchant_id", c_char*16),
        ("amount", c_char*13),
        ("transaction_id", c_char*7),
        
        # calcule par l'api
        ("transmission_date", c_char*15),
        
        # facultatif a l'appel
        ("payment_means", c_char*129),
        ("header_flag", c_char*4),
        ("currency_code", c_char*4),
        ("merchant_country", c_char*3),
        ("language", c_char*3),
        ("normal_return_url", c_char*512),
        ("automatic_response_url", c_char*512),
        ("cancel_return_url", c_char*512),
        
        # facultatif a l'appel et a la conf
        ("normal_return_logo", c_char*51),
        ("cancel_return_logo", c_char*51),
        ("submit_logo", c_char*51),
        ("logo_id", c_char*33),
        ("logo_id2", c_char*33),
        ("card_list", c_char*129),
        ("transaction_condition", c_char*65),
        ("order_validity", c_char*3),
        ("bgcolor", c_char*7),
        ("block_align", c_char*13),
        ("block_order", c_char*33),
        ("textcolor", c_char*7),
        ("advert", c_char*33),
        ("background_id", c_char*33),
        ("merchant_language", c_char*3),
        ("receipt_complement", c_char*3073),
        ("caddie", c_char*2049),
        ("customer_id", c_char*20),
        ("customer_email", c_char*129),
        ("data", c_char*2049),
        ("return_context", c_char*257),
        ("templatefile", c_char*33),
        ("target", c_char*33),
        ("textfont", c_char*65),
        ("customer_ip_address", c_char*20),
        ("order_id", c_char*33),
        ("capture_day", c_char*3),
        ("capture_mode", c_char*21),
    ]


def init():
    cp = CallParm()
    lib.sips_init_func(byref(cp))
    return cp

def transaction_id():
    buf = create_string_buffer(7)
    lib.sips_transaction_id_func(buf)
    return buf.value

def call(cp, pathfile):
    error_buffer = c_char_p()
    error = lib.sips_call_func(byref(cp), pathfile, byref(error_buffer))
    if error:
        raise error_buffer.value

def remote_call(cp, pathfile):
    buffer = c_char_p()
    error_buffer = c_char_p()
    error = lib.sips_remote_call_func(byref(cp), pathfile, byref(buffer), byref(error_buffer))
    if error:
        raise error_buffer.value
    else:
        return buffer.value
