#1.Tạo frame
import pandas as pd

data = {
    "Họ và tên": [
        "Nguyễn Văn An",
        "Trần Thị Bình",
        "Lê Hoàng Nam",
        "Phạm Minh Anh",
        "Hoàng Thị Lan",
        "Võ Quốc Bảo",
        "Đặng Thu Hà",
        "Bùi Đức Long",
        "Đỗ Ngọc Mai",
        "Ngô Thành Công"
    ],
    "Điểm chuyên cần": [9.0, 8.5, 7.5, 10.0, 8.0, 9.5, 7.0, 8.5, 9.0, 7.5],
    "Điểm giữa kỳ":   [8.5, 7.0, 6.5, 9.0, 7.5, 8.0, 6.0, 7.5, 9.5, 6.5],
    "Điểm cuối kỳ":   [9.0, 8.0, 7.0, 9.5, 8.5, 8.5, 6.5, 8.0, 9.0, 7.0]
}

df = pd.DataFrame(data)

#Tính điểm tổng kết

df["Tong_ket"] = (
    0.2 * df["Điểm chuyên cần"]
    + 0.3 * df["Điểm giữa kỳ"]
    + 0.5 * df["Điểm cuối kỳ"]
)

#Xếp loại

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

print(df)

#Thống kê
# Tính điểm tổng kết trung bình của lớp
diem_tb = df["Tong_ket"].mean()

# Tìm sinh viên có điểm tổng kết cao nhất
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]

# Tìm sinh viên có điểm tổng kết thấp nhất
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]

# Đếm số sinh viên đạt (điểm tổng kết >= 5)
so_sv_dat = (df["Tong_ket"] >= 5).sum()

# In kết quả
print("Điểm tổng kết trung bình của lớp:", round(diem_tb, 2))

print("\nSinh viên có điểm cao nhất:")
print(sv_cao_nhat[["Họ và tên", "Tong_ket"]])

print("\nSinh viên có điểm thấp nhất:")
print(sv_thap_nhat[["Họ và tên", "Tong_ket"]])

print("\nSố sinh viên đạt:", so_sv_dat)
print("Số sinh viên không đạt:", len(df) - so_sv_dat)
#Trực quan hoá

import matplotlib.pyplot as plt

#1 Lấy dữ liệu từ DataFrame df
ten_sv = df["Họ và tên"]
diem = df["Tong_ket"]

#2 Vẽ biểu đồ cột
plt.figure(figsize=(12, 6))
plt.bar(ten_sv, diem)

#3 Thiết lập tiêu đề và tên trục
plt.title("Điểm tổng kết của 10 sinh viên")
plt.xlabel("Tên sinh viên")
plt.ylabel("Điểm tổng kết")

#4 Giới hạn trục điểm từ 0 đến 10
plt.ylim(0, 10)

#5 Xoay tên sinh viên để dễ đọc
plt.xticks(rotation=45, ha="right")

#6 Hiển thị giá trị điểm trên đầu mỗi cột
for i, value in enumerate(diem):
    plt.text(i, value + 0.1, f"{value:.2f}",
             ha="center", va="bottom")

plt.tight_layout()
plt.show()
