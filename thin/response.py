from ctypes import *
from ctypes.util import find_library

from thin import lib

class ResponseParm(Structure):
    _fields_ = [
        # obligatoire et donc forcement renseigne
        # en provenance du serveur commercant
        ("merchant_id", c_char*16),
        ("amount", c_char*13),
        ("transaction_id", c_char*7),
        ("payment_means", c_char*13),
        ("transmission_date", c_char*15),
        
        # obligatoire et donc renseigne
        # genere par le serveur de paiement
        ("payment_time", c_char*7),
        ("payment_date", c_char*9),
        ("response_code", c_char*3),
        ("payment_certificate", c_char*13),
        ("authorisation_id", c_char*11),
        ("merchant_language", c_char*3),
        ("merchant_country", c_char*3),
        ("currency_code", c_char*4),
        ("card_number", c_char*8),
        ("language", c_char*3),
        
        # facultatif
        ("receipt_complement", c_char*3073),
        ("caddie", c_char*2049),
        ("customer_id", c_char*20),
        ("customer_email", c_char*129),
        ("transaction_condition", c_char*65),
        ("order_validity", c_char*3),
        ("data", c_char*2049),
        ("return_context", c_char*257),
        ("customer_ip_address", c_char*20),
        ("order_id", c_char*33),
        ("capture_day", c_char*3),
        ("capture_mode", c_char*21),
        ("bank_response_code", c_char*3),
        ("cvv_response_code", c_char*3),
        ("cvv_flag", c_char*2),
        ("complementary_code", c_char*3),
        ("complementary_info", c_char*256),
    ]

def remote_response(pathfile, message):
    rp = ResponseParm()
    error_buffer = c_char_p()
    error = lib.sips_remote_response_func(byref(rp),
                                          pathfile,
                                          message,
                                          byref(error_buffer))
    if error:
        raise error_buffer.value
    else:
        return rp
