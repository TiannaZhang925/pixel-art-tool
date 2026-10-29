#!/usr/bin/env python3
"""照片像素化工具 - 把图片变成像素艺术风格"""

from PIL import Image
import argparse
import sys


def pixelate(image_path, output_path, pixel_size=10):
    """
    像素化图片

    Args:
        image_path: 输入图片路径
        output_path: 输出图片路径
        pixel_size: 像素块大小（越大越模糊）
    """
    # 打开图片
    img = Image.open(image_path)

    # 获取原图尺寸
    width, height = img.size

    # 缩小到目标尺寸
    small_width = width // pixel_size
    small_height = height // pixel_size

    # 防止缩小到 0
    small_width = max(1, small_width)
    small_height = max(1, small_height)

    # 缩小（使用 NEAREST 保持像素感）
    small_img = img.resize((small_width, small_height), Image.NEAREST)

    # 放大回原尺寸（使用 NEAREST 保持块状效果）
    pixelated_img = small_img.resize((width, height), Image.NEAREST)

    # 保存
    pixelated_img.save(output_path)
    print(f"✓ 像素化完成！已保存到: {output_path}")
    print(f"  像素块大小: {pixel_size}x{pixel_size}")
    print(f"  图片尺寸: {width}x{height}")


def main():
    parser = argparse.ArgumentParser(
        description="照片像素化工具 - 把图片变成像素艺术风格",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python pixelate.py photo.jpg                    # 默认像素化（10x10）
  python pixelate.py photo.jpg -o pixel.jpg       # 指定输出文件
  python pixelate.py photo.jpg -s 20              # 大像素块（20x20）
  python pixelate.py photo.jpg -s 5 -o out.png    # 小像素块 + PNG 格式
        """
    )

    parser.add_argument("input", help="输入图片路径")
    parser.add_argument("-o", "--output", help="输出图片路径（默认: input_pixelated.ext）")
    parser.add_argument("-s", "--size", type=int, default=10, help="像素块大小（默认: 10）")

    args = parser.parse_args()

    # 生成默认输出文件名
    if not args.output:
        import os
        base, ext = os.path.splitext(args.input)
        args.output = f"{base}_pixelated{ext}"

    # 执行像素化
    try:
        pixelate(args.input, args.output, args.size)
    except FileNotFoundError:
        print(f"✗ 错误: 找不到文件 '{args.input}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"✗ 错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
