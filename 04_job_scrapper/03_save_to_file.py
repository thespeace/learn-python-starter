def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w", encoding="utf-8") #파일 형태로 저장. (파일이름, 모드, 형식) 파일을 열어서 -
                                                           #엑셀파일은 열을 쉼표로 구분하고 새 행을 줄바꿈으로 구분해 준다.

    file.write("Position,Company,Location,URL\n") #파일 작성-

    for job in jobs:
        file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n") #job은 dictionary이기 때문에 대괄호로 key적어서 value 적어주기 / 파일 작성-

    file.close() #파일 저장.