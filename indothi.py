import matplotlib.pyplot as plt
import pandas as pd

# 1. Đọc dữ liệu từ file CSV
csv_file = 'loadcell_data.csv' 
df = pd.read_csv(csv_file)

# 2. Khởi tạo khung đồ thị
plt.figure(figsize=(13, 6), dpi=150)

# 3. Vẽ đường tín hiệu thô
plt.plot(
    df['Time_ms'],
    df['Raw_Weight_g'],
    color='#d95f02',
    linewidth=1.2,
    label='Tín hiệu thô (Raw Signal)',
)

# 4. Các đường mốc tham chiếu
plt.axvline(
    x=200,
    color='red',
    linestyle='--',
    linewidth=1.2,
    label='Thời điểm đặt vật (200 ms)',
)
plt.axhline(
    y=500,
    color='green',
    linestyle=':',
    linewidth=1.5,
    label='Trọng lượng thực (500g)',
)

# 5. Cấu hình trục và lưới hiển thị
plt.title(
    'Đồ thị tín hiệu thô Loadcell theo thời gian (ms)',
    fontsize=13,
    fontweight='bold',
)
plt.xlabel('Thời gian t (ms)', fontsize=11)
plt.ylabel('Trọng lượng (gram)', fontsize=11)
plt.xlim(0, 1200)
plt.ylim(-50, 800)

plt.minorticks_on()
plt.grid(True, which='major', linestyle='-', linewidth=0.7, alpha=0.7)
plt.grid(True, which='minor', linestyle=':', linewidth=0.4, alpha=0.4)
plt.legend(
    loc='upper right', frameon=True, facecolor='white', framealpha=0.9
)

plt.tight_layout()
plt.show()