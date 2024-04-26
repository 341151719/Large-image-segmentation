### Documentation for Image Splitting and PDF Merging Script

#### Overview

This Python script is designed to split a single large image into multiple smaller segments while maintaining the aspect ratio of A4 paper size. After splitting the image, each segment is saved as a PNG file in a designated output folder. Subsequently, all the segments are combined into a single PDF file, which is also saved in the same output folder.

#### Requirements

- Python 3.x
- Pillow Library: This can be installed using the command `pip install Pillow`.

#### How to Use

1. **Setup**: Ensure that Python and Pillow are installed on your system.
2. **Prepare Your Image**: Place the image you want to split in a known directory.
3. **Modify the Script**: Update the `input_image_path` and `num_splits` in the script to match your image location and desired number of splits.
4. **Run the Script**: Execute the script. It will create the output folder, save the split images, and generate the PDF.

#### Functions

- **split_image_to_a4_and_create_pdf(image_path, num_splits, output_folder, dpi=300)**:
  - `image_path`: Path to the input image.
  - `num_splits`: Desired number of image segments.
  - `output_folder`: Folder where the output files will be saved.
  - `dpi`: Dots per inch, set to 300 by default for high resolution.

#### Output

- **Output Folder**: Contains all the image segments as PNG files.
- **PDF File**: A single PDF file named `output.pdf` containing all the image segments.

### 图片分割与PDF合并脚本文档

#### 概述

此Python脚本旨在将单个大图像分割成多个小段，同时保持A4纸张尺寸的宽高比。分割图像后，每个段落以PNG文件格式保存在指定的输出文件夹中。随后，所有段落将合并成一个PDF文件，该文件也将保存在同一输出文件夹中。

#### 系统要求

- Python 3.x
- Pillow库：可使用命令 `pip install Pillow` 安装。

#### 使用说明

1. **设置**：确保系统中已安装Python和Pillow。
2. **准备图片**：将要分割的图片放置在已知目录中。
3. **修改脚本**：根据您的图片位置和期望的分割数量，更新脚本中的 `input_image_path` 和 `num_splits`。
4. **运行脚本**：执行脚本。它将创建输出文件夹，保存分割的图片，并生成PDF。

#### 函数

- **split_image_to_a4_and_create_pdf(image_path, num_splits, output_folder, dpi=300)**：
  - `image_path`：输入图像的路径。
  - `num_splits`：期望的图像分割段数。
  - `output_folder`：将保存输出文件的文件夹。
  - `dpi`：点每英寸，默认设置为300，以获得高分辨率。

#### 输出

- **输出文件夹**：包含所有图像段的PNG文件。
- **PDF文件**：一个名为 `output.pdf` 的PDF文件，包含所有图像段。
