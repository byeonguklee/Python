import qrcode

with open('site_list.txt', 'r', encoding='UTF8') as f:
    read_lines = f.readlines() # f 파일 전체의 라인을 읽어온다.

    for line in read_lines: # 읽어온 값을 한 줄 씩 가져온다.
        line = line.strip() # 텍스트만 읽어온다.
        print(line)

    qr_data = line
    qr_image = qrcode.make(qr_data)

    qr_image.save(qr_data + '.png')