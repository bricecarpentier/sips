#class ResponseParm(Structure):
#    _fields_ = [
#        # obligatoire et donc forcement renseigne
#        # en provenance du serveur commercant
#        ("merchant_id", c_char_p),
#        ("amount", c_char_p),
#        ("transaction_id", c_char_p),
#        ("payment_means", c_char_p),
#        ("transmission_date", c_char_p),
#        
#        # obligatoire et donc renseigne
#        # genere par le serveur de paiement
#        ("payment_time", c_char_p),
#        ("payment_date", c_char_p),
#        ("response_code", c_char_p),
#        ("payment_certificate", c_char_p),
#        ("authorisation_id", c_char_p),
#        ("merchant_language", c_char_p),
#        ("merchant_country", c_char_p),
#        ("currency_code", c_char_p),
#        ("card_number", c_char_p),
#        ("language", c_char_p),
#        
#        # facultatif
#        ("receipt_complement", c_char_p),
#        ("caddie", c_char_p),
#        ("customer_id", c_char_p),
#        ("customer_email", c_char_p),
#        ("transaction_condition", c_char_p),
#        ("order_validity", c_char_p),
#        ("data", c_char_p),
#        ("return_context", c_char_p),
#        ("customer_ip_address", c_char_p),
#        ("order_id", c_char_p),
#        ("capture_day", c_char_p),
#        ("capture_mode", c_char_p),
#        ("bank_response_code", c_char_p),
#        ("cvv_response_code", c_char_p),
#        ("cvv_flag", c_char_p),
#        ("complementary_code", c_char_p),
#        ("complementary_info", c_char_p),
#    ]
