# Mã hóa thay thế bằng cộng k = STT theo danh sách (Z26)

def ma_hoa(van_ban):
    ket_qua = ""
    for stt, ky_tu in enumerate(van_ban, start=22):  
        if ky_tu.isalpha(): 
            if ky_tu.isupper():
                co_so = ord('A')
            else:
                co_so = ord('a')
            # công thức cộng k = STT rồi mod 26
            ky_tu_ma = chr((ord(ky_tu) - co_so + stt) % 26 + co_so)
            ket_qua += ky_tu_ma
        else:
            ket_qua += ky_tu
    return ket_qua

def giai_ma(van_ban_ma):
    ket_qua = ""
    for stt, ky_tu in enumerate(van_ban_ma, start=22):
        if ky_tu.isalpha():
            if ky_tu.isupper():
                co_so = ord('A')
            else:
                co_so = ord('a')
            ky_tu_goc = chr((ord(ky_tu) - co_so - stt) % 26 + co_so)
            ket_qua += ky_tu_goc
        else:
            ket_qua += ky_tu
    return ket_qua


# TEST
ban_ro = "van cong anh duy"
ban_ma = ma_hoa(ban_ro)
print("Bản rõ :", ban_ro)
print("Bản mã :", ban_ma)
print("Giải mã:", giai_ma(ban_ma))
