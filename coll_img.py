## 用来生成组织图片的
from PIL import Image

# 打开两张图片
img1 = Image.open(r"imgs\left.png")  # 图片1
img2 = Image.open(r"imgs\right.png")  # 图片2

# 获取两张图片的尺寸
width1, height1 = img1.size
width2, height2 = img2.size

# 选择较小的高度作为基准高度
new_height = min(height1, height2)

# 计算缩放后的宽度，保持图片比例
new_width1 = int((new_height / height1) * width1)
new_width2 = int((new_height / height2) * width2)

# 将图片按比例缩放
img1_resized = img1.resize((new_width1, new_height), Image.Resampling.LANCZOS)
img2_resized = img2.resize((new_width2, new_height), Image.Resampling.LANCZOS)

# 创建一个新的图片，宽度为两张图片的宽度之和，高度为基准高度
total_width = new_width1 + new_width2
new_img = Image.new('RGB', (total_width, new_height))

# 将两张图片拼接在一起
new_img.paste(img1_resized, (0, 0))  # 将第一张图片放在左边
new_img.paste(img2_resized, (new_width1, 0))  # 将第二张图片放在右边

# 保存或展示结果
new_img.save('output.jpg')  # 保存为新图片
new_img.show()  # 展示拼接结果
