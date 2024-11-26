import numpy as np

def conv2d(input_tensor, kernel, stride=1, padding=0):
    """
    二维卷积操作

    参数:
    input_tensor: 输入张量，形状为 (batch_size, in_channels, height, width)
    kernel: 卷积核，形状为 (out_channels, in_channels, kernel_height, kernel_width)
    stride: 步长，默认为 1
    padding: 填充，默认为 0

    返回:
    输出张量，形状为 (batch_size, out_channels, out_height, out_width)
    """
    batch_size, in_channels, in_height, in_width = input_tensor.shape
    out_channels, _, kernel_height, kernel_width = kernel.shape

    # 计算输出张量的尺寸
    out_height = (in_height - kernel_height + 2 * padding) // stride + 1
    out_width = (in_width - kernel_width + 2 * padding) // stride + 1

    # 填充输入张量
    if padding > 0:
        input_tensor = np.pad(input_tensor, ((0, 0), (0, 0), (padding, padding), (padding, padding)), mode='constant')

    # 初始化输出张量
    output_tensor = np.zeros((batch_size, out_channels, out_height, out_width))

    # 卷积操作
    for b in range(batch_size):
        for oc in range(out_channels):
            for ic in range(in_channels):
                for i in range(out_height):
                    for j in range(out_width):
                        # 计算卷积窗口的位置
                        h_start = i * stride
                        h_end = h_start + kernel_height
                        w_start = j * stride
                        w_end = w_start + kernel_width

                        # 提取输入张量的窗口
                        input_window = input_tensor[b, ic, h_start:h_end, w_start:w_end]

                        # 计算卷积
                        output_tensor[b, oc, i, j] += np.sum(input_window * kernel[oc, ic])

    return output_tensor

# 示例用法
if __name__ == "__main__":
    # 输入张量 (batch_size=1, in_channels=3, height=5, width=5)
    input_tensor = np.random.randn(1, 3, 5, 5)

    # 卷积核 (out_channels=2, in_channels=3, kernel_height=3, kernel_width=3)
    kernel = np.random.randn(2, 3, 3, 3)

    # 执行卷积操作
    output_tensor = conv2d(input_tensor, kernel, stride=1, padding=1)

    print("输入张量形状:", input_tensor.shape)
    print("卷积核形状:", kernel.shape)
    print("输出张量形状:", output_tensor.shape)
    print("输出张量:\n", output_tensor)