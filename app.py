import barcode 
hr=barcode.get_barcode_class('ean13')
Hr=hr("1254698752314")
qr=Hr.save('123')