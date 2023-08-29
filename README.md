# Awesome-Real-time-Semantic-Segmentation

# 图像融合(Image Fusion)


- [Citation](#citation)
- [实时语义分割方法(Real-time Semantic Segmentation Methods)](#实时语义分割方法Real-time Semantic Segmentation Methods)
  - [单分支网络(Single Branch Network)](#单分支网络Single Branch Network)
  - [双分支网络(Single Branch Network)](#单分支网络Single Branch Network)
  - [多分支网络(Two Branch Network)](#单分支网络Single Branch Network)
  - [单分支网络(Multi Branch Network)](#单分支网络Single Branch Network)
  - [U型网络(U-shape Network)](#U型网络U-shape Network)
- [数据集(Dataset)](#数据集dataset)
- [评估指标(Evaluation Metric)](#评估指标evaluation-metric)
## Citation
如果我们的总结对你有所帮助, 请引用以下论文：


## 实时语义分割方法(Real-time Semantic Segmentation Methods)
### 单分支网络(Single Branch Network)
<table>
    <thead>
      <tr>
        <th>方法</th>
        <th>标题</th>
        <th>论文</th>
        <th>代码</th>
        <th>发表期刊或会议</th>
        <th>基础框架</th>
        <th>应用场景</th>
        <th>发表年份</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td>ENet</td>
        <td>ENet: A Deep Neural Network Architecture for Real-Time Semantic Segmentation</td>
        <td><a href="https://arxiv.org/pdf/1606.02147.pdf">Paper</a></td>
        <td><a href="https://github.com/TimoSaemann/ENet">Code</a></td>
        <td>Arxiv</td>
        <td>CNN</td>
        <td>GPU</td>
        <td>2016</td>
    </tr>
    <tr>
        <td>DABNet</td>
        <td>DABNet: Depth-wise Asymmetric Bottleneck for Real-time Semantic Segmentation</td>
        <td><a href="https://arxiv.org/pdf/1907.11357.pdf">Paper</a></td>
        <td><a href="https://github.com/Reagan1311/DABNet">Code</a></td>
        <td>BMVC</td>
        <td>CNN</td>
        <td>GPU</td>
        <td>2019</td>
    </tr>
      <tr>
        <td>SegFormer</td>
        <td>SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers</td>
        <td><a href="https://proceedings.neurips.cc/paper/2021/file/64f1f27bf1b4ec22924fd0acb550c235-Paper.pdf">Paper</a></td>
        <td><a href="https://github.com/NVlabs/SegFormer">Code</a></td>
        <td>NeurIPS</td>
        <td>Transformer</td>
        <td>GPU</td>
        <td>2021</td>
    </tr>
    <tr>
        <td>SegNext</td>
        <td>SegNeXt: Rethinking Convolutional Attention Design for Semantic Segmentation</td>
        <td><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/08050f40fff41616ccfc3080e60a301a-Paper-Conference.pdf">Paper</a></td>
        <td><a href="https://github.com/Jittor/JSeg">Code</a></td>
        <td>NeurIPS</td>
        <td>CNN</td>
        <td>GPU</td>
        <td>2022</td>
    </tr>
    <tr>
        <td>AFFormer</td>
        <td></td>
        <td><a href="https://arxiv.org/pdf/2301.04648.pdf">Paper</a></td>
        <td><a href="https://github.com/dongbo811/AFFormer">Code</a></td>
        <td>AAAI</td>
        <td>Transformer</td>
        <td>GPU</td>
        <td>2023</td>
    </tr>
    </tbody>
    </table>
    
### 双分支网络(Two Branch Network)
<table>
    <thead>
      <tr>
        <th>方法</th>
        <th>标题</th>
        <th>论文</th>
        <th>代码</th>
        <th>发表期刊或会议</th>
        <th>基础框架</th>
        <th>应用场景</th>
        <th>发表年份</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td>BiSeNet</td>
        <td>BiSeNet: Bilateral Segmentation Network for Real-time Semantic Segmentation</td>
        <td><a href="https://openaccess.thecvf.com/content_ECCV_2018/papers/Changqian_Yu_BiSeNet_Bilateral_Segmentation_ECCV_2018_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/ycszen/BiSeNet">Code</a></td>
        <td>ECCV</td>
        <td>CNN</td>
        <td>GPU</td>
        <td>2018</td>
    </tr>
    <tr>
        <td>Fast-SCNN</td>
        <td>Fast-SCNN: Fast Semantic Segmentation Network</td>
        <td><a href="https://bmvc2019.org/wp-content/uploads/papers/0959-paper.pdf">Paper</a></td>
        <td><a href="https://github.com/Tramac/Fast-SCNN-pytorch">Code</a></td>
        <td>BMVC</td>
        <td>CNN</td>
        <td>GPU</td>
        <td>2019</td>
    </tr>
    </tbody>
    </table>
    

## 评估指标(Evaluation Metric)
### 通用评估指标(General evaluation metric)
通用评估指标位于：
### 遥感影像融合评估指标(Evaluation metric for pansharpening)
