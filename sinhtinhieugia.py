import numpy as np
import pandas as pd

# Cấu hình lấy mẫu và thời gian
sample_rate = 1000  # 1000 Hz (1 mẫu / 1 ms)
duration = 1.2      # 1.2 giây (1200 ms)
t_drop = 0.2        # Thả vật tại 200 ms
W = 500.0           # Trọng lượng chuẩn: 500 gram

# Thông số dao động cơ học thực tế 
f1, tau1, A1 = 45.0, 0.18, 220.0  # Dao động chính 45Hz
f2, tau2, A2 = 115.0, 0.08, 60.0  # Sóng hài bậc cao 115Hz
noise_level = 3.5                 # Biên độ nhiễu trắng (+/- gram)

# Trục thời gian
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
t_ms = t * 1000.0

dt = np.maximum(0, t - t_drop)
step_input = np.where(t >= t_drop, W, 0.0)

ringing = np.where(
    t >= t_drop,
    A1 * np.exp(-dt / tau1) * np.sin(2 * np.pi * f1 * dt) +
    A2 * np.exp(-dt / tau2) * np.sin(2 * np.pi * f2 * dt),
    0.0
)

# Nhiễu điện ngẫu nhiên
noise = np.random.normal(0, noise_level, len(t))
raw_weight = step_input + ringing + noise

# Lưu dữ liệu
df = pd.DataFrame({
    'Time_ms': np.round(t_ms, 1),
    'Raw_Weight_g': np.round(raw_weight, 2)
})

output_file = 'loadcell_data.csv'
df.to_csv(output_file, index=False)
print(f"Đã tạo file dữ liệu thành công: {output_file}")