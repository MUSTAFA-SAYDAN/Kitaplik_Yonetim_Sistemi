def eksik_alan_kontrol(veri, gerekli_alanlar):
    for alan in gerekli_alanlar:
        if alan not in veri:
            return alan
    return None