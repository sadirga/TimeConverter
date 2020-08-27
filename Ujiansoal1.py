def TimeConverter(num):                             # buat nama function dan parameternya
    if type(num) == str or type(num) == float or num > 359999 or num < 0: # buat kondisi jika type data num adalah str atau float
        print('Invalid Value')                      # maka print (invalid value) atau jika num lebih dari 
                                                    # angka 359999 dan num kurang dari 0

    else:                                           # jika num tidak ada masalah maka
        hours = 0                                   # siapkan 2 variable integer dengan nilai 0
        minutes = 0
        seconds = num
        if seconds > 59:                            # Jika detik lebih dari 59
            minutes = seconds //60                  # detik akan di dibagi 60 (// agar hasilnya tidak float) dan di store ke menit
            seconds = seconds %60                   # detik akan di modulo 60 (agar memperlihatkan sisa)
        if minutes > 59:                            # lalu jika minutes > dari 59
            hours = minutes //60                    # menit akan di bagi 60 dan di store ke variable hours
            minutes = minutes%60                    # menit akan di modulo 60 (agar memperlihatkan sisa)
        print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')    

TimeConverter(3702)


