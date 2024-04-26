from PIL import Image
import os
import math

def split_image_to_a4_and_create_pdf(image_path, num_splits, output_folder, dpi=900):
    # 设置Pillow的解压缩炸弹阈值
    Image.MAX_IMAGE_PIXELS = None

    # 计算A4纸的像素尺寸，假设300 DPI
    a4_width = int(11.69 * dpi)  # A4宽度，8.27英寸
    a4_height = int(8.27 * dpi)  # A4高度，11.69英寸

    # 创建输出目录
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 准备保存图片路径
    image_paths = []

    try:
        # 加载图片
        with Image.open(image_path) as img:
            width, height = img.size
            
            # 计算需要分割的行数和列数
            cols = int(math.sqrt(num_splits * (a4_width / a4_height)))
            rows = int(math.ceil(num_splits / cols))

            # 计算每个分割块的宽度和高度
            block_width = width // cols
            block_height = height // rows

            # 保持A4比例
            if block_width / block_height < (a4_width / a4_height):
                block_height = int(block_width * (a4_height / a4_width))
            else:
                block_width = int(block_height * (a4_width / a4_height))

            count = 0
            for i in range(rows):
                for j in range(cols):
                    left = j * block_width
                    top = i * block_height
                    right = left + block_width
                    bottom = top + block_height

                    if right > width or bottom > height or count >= num_splits:
                        continue

                    # 裁剪图片
                    cropped_img = img.crop((left, top, right, bottom))

                    # 指定保存路径
                    file_path = os.path.join(output_folder, f"split_{count+1}.png")
                    cropped_img.save(file_path)
                    image_paths.append(file_path)

                    count += 1
                    print(f"分割 {count}/{num_splits} 已保存至 {file_path}。")

            # 创建PDF
            if image_paths:
                images = [Image.open(x).convert('RGB') for x in image_paths]
                pdf_path = os.path.join(output_folder, "output.pdf")
                images[0].save(pdf_path, save_all=True, append_images=images[1:])
                print(f"所有图片已合并到PDF文件：{pdf_path}")

    except Exception as e:
        print(f"处理图片时出错: {e}")

# 调用函数
input_image_path = "D:\\test.png"
num_splits = 80
output_folder = f"{input_image_path}-output"
split_image_to_a4_and_create_pdf(input_image_path, num_splits, output_folder)
