# 输入图像尺寸: n,c,h,w
# 卷积核大小：ih, iw, oc, stride=s
# 卷积后特征图尺寸：(h - ih) / s + 1, (w - iw) / s + 1, oc
# 输出特征尺寸: n, oc, (h - ih) / s + 1, (w - iw) / s + 1
# res = torch.zeors(n, oc, (h - ih) / s + 1, (w - iw) / s + 1)

def conv2d_nchw(input_data, weight_data, bias_data, stride=1, padding=0):
    # 输入数据的维度：[N, C, H, W]
    N, C, H, W = input_data.shape
    # 卷积核的维度：[O, C, K, K]
    O, _, K, K = weight_data.shape

    # 计算输出的高度和宽度
    out_h = (H - K + 2 * padding) // stride + 1
    out_w = (W - K + 2 * padding) // stride + 1

    for n in range(N):
        for o in range(O):
            for i in range(out_h):
                for j in range(out_w):
                    # 计算卷积结果
                    value = 0
                    for c in range(C):
                        for p in range(K):
                            for q in range(K):
                                value += input_data[c][i*stride+p][j*stride+q] * weight_data[o][c][p][q]
                    output_data[n][o][i][j] = value
