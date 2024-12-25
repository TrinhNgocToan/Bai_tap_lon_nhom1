import csv

def doc_danh_sach_tu_file():
    try:
        with open("ds_diem.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            global danh_sach_diem
            danh_sach_diem = list(reader)
            print("Đã đọc danh sách điểm từ file.")
    except FileNotFoundError:
        print("File ds_diem.csv chưa tồn tại!")



def luu_danh_sach_vao_file():
    with open("ds_diem.csv", mode="w", encoding="utf-8", newline="") as file:
        fieldnames = ["ten", "diem"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(danh_sach_diem)
        print("Đã lưu danh sách điểm vào file.")