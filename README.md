# 🎨 照片像素化工具

把普通照片变成复古像素艺术风格！

## 安装

```bash
pip install -r requirements.txt
```

## 使用

```bash
# 基础用法（默认 10x10 像素块）
python pixelate.py photo.jpg

# 指定输出文件
python pixelate.py photo.jpg -o pixel.jpg

# 大像素块（更模糊，更复古）
python pixelate.py photo.jpg -s 20

# 小像素块（细节更多）
python pixelate.py photo.jpg -s 5 -o out.png
```

## 参数说明

- `input`: 输入图片路径（必填）
- `-o, --output`: 输出图片路径（默认: `原文件名_pixelated.扩展名`）
- `-s, --size`: 像素块大小，默认 10（越大越模糊）

## 示例效果

| 原图 | 像素化 (s=10) | 像素化 (s=20) |
|------|---------------|---------------|
| ![原图](examples/original.jpg) | ![s=10](examples/pixel_10.jpg) | ![s=20](examples/pixel_20.jpg) |

## 原理

1. 将图片缩小到 `原尺寸 / 像素块大小`
2. 使用最近邻插值（NEAREST）保持块状效果
3. 放大回原尺寸，形成像素块

## License

MIT
