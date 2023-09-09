# Awesome-Real-time-Semantic-Segmentation

# 实时语义分割(Real-time Semantic Segmentation)



- [实时语义分割方法(Real-time Semantic Segmentation Methods)](#实时语义分割方法)
  - [单分支网络(Single-branch Network)](#单分支网络)
  - [多分支网络(Two-branch Network)](#双分支网络)
  - [单分支网络(Multi-branch Network)](#多分支网络)
  - [U型网络(U-shape Network)](#U型网络)
  - [U型网络(U-shape Network)](#U型网络)
- [数据集(Dataset)](#数据集dataset)



## 实时语义分割方法(Real-time Semantic Segmentation Methods)
### 单分支网络(Single-branch Network)
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
        <th>数据集</th>
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
        <td>Desk GPU</td>
        <td>2016</td>
        <td>Cityscapes, CamVid, SUN</td>
    </tr>
    <tr>
        <td>DABNet</td>
        <td>DABNet: Depth-wise Asymmetric Bottleneck for Real-time Semantic Segmentation</td>
        <td><a href="https://arxiv.org/pdf/1907.11357.pdf">Paper</a></td>
        <td><a href="https://github.com/Reagan1311/DABNet">Code</a></td>
        <td>BMVC</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2019</td>
        <td>Cityscapes, CamVid</td>
    </tr>
      <tr>
        <td>SegFormer</td>
        <td>SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers</td>
        <td><a href="https://proceedings.neurips.cc/paper/2021/file/64f1f27bf1b4ec22924fd0acb550c235-Paper.pdf">Paper</a></td>
        <td><a href="https://github.com/NVlabs/SegFormer">Code</a></td>
        <td>NeurIPS</td>
        <td>Transformer</td>
        <td>Desk GPU</td>
        <td>2021</td>
        <td>Cityscapes, ADE20K, PascalContext, PascalVOC, COCO-Stuff, iSAID</td>
    </tr>
    <tr>
        <td>SegNext</td>
        <td>SegNeXt: Rethinking Convolutional Attention Design for Semantic Segmentation</td>
        <td><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/08050f40fff41616ccfc3080e60a301a-Paper-Conference.pdf">Paper</a></td>
        <td><a href="https://github.com/Jittor/JSeg">Code</a></td>
        <td>NeurIPS</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2022</td>
        <td>Cityscapes, ADE20K, PascalContext, PascalVOC, COCO-Stuff, iSAID</td>
    </tr>
    <tr>
        <td>AFFormer</td>
        <td>Head-Free Lightweight Semantic Segmentation with Linear Transformer</td>
        <td><a href="https://arxiv.org/pdf/2301.04648.pdf">Paper</a></td>
        <td><a href="https://github.com/dongbo811/AFFormer">Code</a></td>
        <td>AAAI</td>
        <td>Transformer</td>
        <td>Desk GPU</td>
        <td>2023</td>
        <td>Cityscapes, ADE20K, COCO-Stuff</td>     
    </tr>
    </tbody>
    </table>
    
### 双分支网络(Two-branch Network)
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
        <th>数据集</th>
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
        <td>Desk GPU</td>
        <td>2018</td>
        <td>Cityscapes, CamVid, COCO-Stuff</td>  
    </tr>
    <tr>
        <td>Fast-SCNN</td>
        <td>Fast-SCNN: Fast Semantic Segmentation Network</td>
        <td><a href="https://bmvc2019.org/wp-content/uploads/papers/0959-paper.pdf">Paper</a></td>
        <td><a href="https://github.com/Tramac/Fast-SCNN-pytorch">Code</a></td>
        <td>BMVC</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2019</td>
        <td>Cityscapes</td>  
    </tr>
    <tr>
        <td>BiSeNetV2</td>
        <td>BiSeNet V2: Bilateral Network with Guided Aggregation for Real-time Semantic Segmentation</td>
        <td><a href="https://arxiv.org/pdf/2004.02147.pdf">Paper</a></td>
        <td><a href="https://github.com/ycszen/BiSeNet">Code</a></td>
        <td>IJCV</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2021</td>
        <td>Cityscapes, CamVid, COCO-Stuff</td>  
    </tr>
    <tr>
        <td>STDC</td>
        <td>Rethinking BiSeNet For Real-time Semantic Segmentation</td>
        <td><a href="https://openaccess.thecvf.com/content/CVPR2021/papers/Fan_Rethinking_BiSeNet_for_Real-Time_Semantic_Segmentation_CVPR_2021_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/MichaelFan01/STDC-Seg">Code</a></td>
        <td>CVPR</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2021</td>
        <td>Cityscapes, CamVid</td>  
    </tr>
    <tr>
        <td>DDRNet</td>
        <td>Deep Dual-resolution Networks for Real-time and Accurate Semantic Segmentation of Traffic Scenes</td>
        <td><a href="https://arxiv.org/pdf/2101.06085.pdf">Paper</a></td>
        <td><a href="https://github.com/ydhongHIT/DDRNet">Code</a></td>
        <td>TIP</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2022</td>
        <td>Cityscapes, CamVid, COCO-Stuff</td>  
    </tr>
    <tr>
        <td>RTFormer</td>
        <td>Rethinking BiSeNet For Real-time Semantic Segmentation</td>
        <td><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/30e10e671c5e43edb67eb257abb6c3ea-Paper-Conference.pdf">Paper</a></td>
        <td><a href="https://github.com/PaddlePaddle/PaddleSeg/tree/release/2.8/configs/rtformer">Code</a></td>
        <td>NeurIPS</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2022</td>
        <td>Cityscapes, CamVid, ADE20K, COCO-Stuff</td>   
    </tr>
    <tr>
        <td>SeaFormer</td>
        <td>SEAFORMER: SQUEEZE-ENHANCED AXIAL TRANSFORMER FOR MOBILE SEMANTIC SEGMENTATION</td>
        <td><a href="https://arxiv.org/pdf/2301.13156">Paper</a></td>
        <td><a href="https://github.com/fudan-zvg/SeaFormer">Code</a></td>
        <td>ICLR</td>
        <td>Hybrid</td>
        <td>Mobile CPU</td>
        <td>2023</td>
        <td>Cityscapes, ADE20K, PascalContext, COCO-Stuff</td>         
    </tr>      
    </tbody>
    </table>

### 多分支网络(Multi Branch Network)
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
        <th>数据集</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td>ICNet</td>
        <td>ICNet for Real-Time Semantic Segmentation on High-Resolution Images</td>
        <td><a href="https://openaccess.thecvf.com/content_ECCV_2018/papers/Hengshuang_Zhao_ICNet_for_Real-Time_ECCV_2018_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/hszhao/ICNet">Code</a></td>
        <td>ECCV</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2018</td>
        <td>Cityscapes, CamVid, COCO-Stuff</td>  
    </tr>
    <tr>
        <td>ESPNet</td>
        <td>ESPNet: Efficient Spatial Pyramid of Dilated Convolutions for Semantic Segmentation</td>
        <td><a href="https://openaccess.thecvf.com/content_ECCV_2018/papers/Sachin_Mehta_ESPNet_Efficient_Spatial_ECCV_2018_paper.pdf">Paper</a></td>
        <td><a href="https://sacmehta.github.io/ESPNet/">Code</a></td>
        <td>ECCV</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2018</td>
        <td>Cityscapes, PascalVOC, Mapillary</td>  
    </tr>
    <tr>
        <td>DFANet</td>
        <td>DFANet: Deep Feature Aggregation for Real-Time Semantic Segmentation</td>
        <td><a href="https://openaccess.thecvf.com/content_CVPR_2019/papers/Li_DFANet_Deep_Feature_Aggregation_for_Real-Time_Semantic_Segmentation_CVPR_2019_paper.pdf">Paper</a></td>
        <td><a></a></td>
        <td>CVPR</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2019</td>
        <td>Cityscapes, CamVid</td> 
    </tr>
    <tr>
        <td>PIDNet</td>
        <td>PIDNet: A Real-time Semantic Segmentation Network Inspired by PID Controllers</td>
        <td><a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Xu_PIDNet_A_Real-Time_Semantic_Segmentation_Network_Inspired_by_PID_Controllers_CVPR_2023_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/XuJiacong/PIDNet">Code</a></td>
        <td>CVPR</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2023</td>
        <td>Cityscapes, CamVid,PASCAL Context</td>
    </tr>
    </tbody>
    </table>

### U型网络(U-shape Network)
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
        <th>数据集</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td>SwiftNet</td>
        <td>In Defense of Pre-trained ImageNet Architectures for Real-time Semantic Segmentation of Road-driving Images</td>
        <td><a href="https://openaccess.thecvf.com/content_CVPR_2019/papers/Orsic_In_Defense_of_Pre-Trained_ImageNet_Architectures_for_Real-Time_Semantic_Segmentation_CVPR_2019_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/orsic/swiftnet">Code</a></td>
        <td>CVPR</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2019</td>
        <td>Cityscapes, CamVid</td> 
    </tr>
    <tr>
        <td>ShelfNet</td>
        <td>ShelfNet for Fast Semantic Segmentation</td>
        <td><a href="https://openaccess.thecvf.com/content_ICCVW_2019/papers/CVRSUAD/Zhuang_ShelfNet_for_Fast_Semantic_Segmentation_ICCVW_2019_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/juntang-zhuang/ShelfNet-lw-cityscapes">Code</a></td>
        <td>ICCV(Workshop)</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2019</td>
        <td>Cityscapes, PascalContext, PascalVOC</td>
    </tr>
    <tr>
        <td>SFNet</td>
        <td>Semantic Flow for Fast and Accurate Scene Parsing</td>
        <td><a href="https://arxiv.org/pdf/2002.10120.pdf">Paper</a></td>
        <td><a href="https://github.com/lxtGH/SFSegNets">Code</a></td>
        <td>ECCV</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2020</td>
        <td>Cityscapes, CamVid, ADE20K, PascalContext</td>
    </tr>
    <tr>
        <td>HyperSeg</td>
        <td>HyperSeg: Patch-wise Hypernetwork for Real-time Semantic Segmentation</td>
        <td><a href="https://openaccess.thecvf.com/content/CVPR2021/papers/Nirkin_HyperSeg_Patch-Wise_Hypernetwork_for_Real-Time_Semantic_Segmentation_CVPR_2021_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/YuvalNirkin/hyperseg">Code</a></td>
        <td>CVPR</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2021</td>
        <td>Cityscapes, CamVid, PascalVOC</td>
    </tr>      
    <tr>
        <td>TopFormer</td>
        <td>TopFormer: Token Pyramid Transformer for Mobile Semantic Segmentation</td>
        <td><a href="https://openaccess.thecvf.com/content/CVPR2022/papers/Zhang_TopFormer_Token_Pyramid_Transformer_for_Mobile_Semantic_Segmentation_CVPR_2022_paper.pdf">Paper</a></td>
        <td><a href="https://github.com/hustvl/TopFormer">Code</a></td>
        <td>CVPR</td>
        <td>Hybrid</td>
        <td>Mobile CPU</td>
        <td>2022</td>
        <td>Cityscapes, ADE20K, PascalContext, COCO-Stuff</td>      
    </tr>
    </tbody>
    </table>

### NAS网络(NAS Network)
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
        <th>数据集</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td>DF-Seg</td>
        <td>Partial Order Pruning: for Best Speed/Accuracy Trade-off in Neural Architecture Search</td>
        <td><a href="https://openaccess.thecvf.com/content_CVPR_2019/papers/Li_Partial_Order_Pruning_For_Best_SpeedAccuracy_Trade-Off_in_Neural_Architecture_CVPR_2019_paper.pdf">Paper</a></td>
        <td><a ></a></td>
        <td>CVPR</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2019</td>
        <td>Cityscapes</td>
    </tr>
    <tr>
        <td>FasterSeg</td>
        <td>FASTERSEG: SEARCHING FOR FASTER REAL-TIME SEMANTIC SEGMENTATION</td>
        <td><a href="https://arxiv.org/pdf/1912.10917.pdf">Paper</a></td>
        <td><a href="https://github.com/VITA-Group/FasterSeg">Code</a></td>
        <td>ICLR</td>
        <td>CNN</td>
        <td>Desk GPU</td>
        <td>2020</td>
        <td>Cityscapes, CamVid, BDD</td>
    </tr>
    <tr>
        <td>RT-Seg</td>
        <td>Towards Real-Time Segmentation on the Edge</td>
        <td><a href="https://ojs.aaai.org/index.php/AAAI/article/view/25232">Paper</a></td>
        <td><a ></a></td>
        <td>AAAI</td>
        <td>CNN</td>
        <td>Mobile GPU</td>
        <td>2023</td>
        <td>Cityscapes, ADE20K, PascalVOC</td>
    </tr>
    <tr>
        <td>Pruning Parameterization</td>
        <td>Pruning Parameterization with Bi-level Optimization for Efficient Semantic Segmentation on the Edge</td>
        <td><a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Yang_Pruning_Parameterization_With_Bi-Level_Optimization_for_Efficient_Semantic_Segmentation_on_CVPR_2023_paper.pdf">Paper</a></td>
        <td><a ></a></td>
        <td>CVPR</td>
        <td>CNN</td>
        <td>Mobile GPU</td>
        <td>2023</td>
        <td>Cityscapes, ADE20K, PascalVOC</td>
    </tr>
    </tbody>
    </table>

## 数据集(Dataset)

