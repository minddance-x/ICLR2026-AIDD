# ICLR 2026 AIDD 论文精选

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Papers](https://img.shields.io/badge/Papers-132-blue.svg)](#论文列表)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

> 🔬 从 ICLR 2026 的 5356 篇接收论文中，精选出 **132 篇** AI 辅助药物发现 (AIDD) 领域的核心论文。

## 📊 项目简介

ICLR 2026 共接收 5356 篇论文，信息量庞大。本项目旨在为 AIDD 领域的研究者提供一份**精选论文列表**，节省文献调研时间。

我们通过多轮筛选，从全部接收论文中提取出与以下方向相关的工作：

- 蛋白质结构预测与设计
- 小分子生成与优化
- 分子对接与相互作用预测
- 分子动力学模拟
- 药物发现应用
- 生物序列建模（RNA/DNA/抗体）

## 🗂️ 项目结构

```
ICLR2026-AIDD/
├── README.md                 # 项目说明
├── requirements.txt          # Python 依赖
├── LICENSE                   # MIT 许可证
├── data/
│   └── iclr2026_aidd_papers_refined.csv  # 132篇精选论文
├── scripts/
│   ├── fetch_papers.py       # 获取论文元数据
│   ├── filter_papers.py      # 关键词筛选
│   └── download_pdfs.py      # 批量下载 PDF
└── docs/
    └── notebooklm_guide.md   # NotebookLM 使用指南
```

## 🤖 使用 NotebookLM 生成综述

本项目的核心目标是将筛选后的论文导入 **Google NotebookLM**，让 AI 帮你快速生成领域综述。

### 快速开始

1. 下载论文 PDF（运行 `python scripts/download_pdfs.py`）
2. 访问 [Google NotebookLM](https://notebooklm.google.com/)
3. 创建新笔记本，上传 PDF 文件
4. 使用 [`docs/notebooklm_guide.md`](./docs/notebooklm_guide.md) 中的提示词进行提问

### 推荐提问流程

```
第一步：总体概览 → 了解主要研究方向
第二步：分主题分析 → 深入各子领域
第三步：技术对比 → 横向比较方法论
第四步：数据集基准 → 了解评测标准
第五步：未来展望 → 把握研究趋势
第六步：生成综述 → 输出完整报告
```

详细提示词模板见 👉 [NotebookLM 使用指南](./docs/notebooklm_guide.md)


## 📈 论文分布

| 主题 | 数量 | 代表性工作 |
|------|------|-----------|
| 🧬 蛋白质设计 | ~35 | SimpleFold, ProteinAE, Constrained Diffusion |
| 🧪 小分子生成 | ~30 | FragFM, SynCoGen, MolEditRL |
| 🔗 分子对接 | ~20 | h-MINT, SigmaDock, PoseX |
| ⚛️ 分子动力学 | ~15 | ATOM, MarS-FM, BioMD |
| 💊 药物发现 | ~15 | DrugTrail, SYNC |
| 🧬 生物序列 | ~10 | PatchDNA, AntigenLM |

## 🔥 技术趋势

1. **扩散模型 (Diffusion Models)**：约 40% 的论文采用
2. **Flow Matching**：作为扩散模型的替代方案逐渐兴起
3. **全原子建模 (All-Atom)**：多篇论文强调原子级精度
4. **可合成性约束**：生成分子的实际可合成性成为研究热点

## 🚀 快速开始

### 安装依赖

```bash
git clone https://github.com/minddance-x/ICLR2026-AIDD.git
cd ICLR2026-AIDD
pip install -r requirements.txt
```

### 使用脚本

```bash
# 1. 获取全部论文元数据（需要网络连接）
python scripts/fetch_papers.py

# 2. 筛选 AIDD 相关论文
python scripts/filter_papers.py

# 3. 下载论文 PDF（可选）
python scripts/download_pdfs.py
```

### 直接使用精选列表

如果只需要论文列表，无需运行脚本：

```python
import pandas as pd
df = pd.read_csv('data/iclr2026_aidd_papers_refined.csv')
print(f"共 {len(df)} 篇论文")
```

## 📝 论文列表

完整论文列表见 [`data/iclr2026_aidd_papers_refined.csv`](./data/iclr2026_aidd_papers_refined.csv)

每篇论文包含以下字段：
- `title`: 论文标题
- `authors`: 作者
- `abstract`: 摘要
- `keywords`: 关键词
- `pdf_link`: PDF 下载链接

### Top 10 论文

| 论文标题 | PDF |
|---------|-----|
| h-MINT: Modeling Pocket-Ligand Binding | [PDF](https://openreview.net/pdf?id=ajywV0kKXk) |
| SigmaDock: Fragment-Based SE(3) Diffusion Docking | [PDF](https://openreview.net/pdf?id=Vgm77U4ojX) |
| ATOM: Pretrained Neural Operator for Molecular Dynamics | [PDF](https://openreview.net/pdf?id=e9cV4xSjbR) |
| FragFM: Fragment-Level Discrete Flow Matching | [PDF](https://openreview.net/pdf?id=tr6vRn2aPg) |
| PoseX: AI for Protein Ligand Cross-Docking | [PDF](https://openreview.net/pdf?id=qqzxKudD4T) |
| Pallatom-Ligand: All-Atom Diffusion for Ligand-Binding Proteins | [PDF](https://openreview.net/pdf?id=uMD75SDTTA) |
| BioMD: All-atom Biomolecular Dynamics Simulation | [PDF](https://openreview.net/pdf?id=LQDeJk6NOr) |
| SimpleFold: Simpler Protein Folding | [PDF](https://openreview.net/pdf?id=FileqNzZzn) |
| SYNC: Synthesizability in Structure-Based Drug Design | [PDF](https://openreview.net/pdf?id=y1tPw4Uuzg) |
| DrugTrail: Explainable Drug Discovery | [PDF](https://openreview.net/pdf?id=MMLAvR1juf) |

## 🛠️ 筛选方法

三层筛选策略：

1. **关键词初筛**：基于 39 个 AIDD 核心关键词匹配
2. **噪声去除**：排除视频生成、图像编辑等无关领域
3. **人工校验**：逐一检查边缘案例

筛选流程：**5356 → 538 → 210 → 132**

## 📖 引用

如果本项目对您有帮助，欢迎 Star ⭐

```bibtex
@misc{iclr2026-aidd,
  author = {MindDance},
  title = {ICLR 2026 AIDD Paper Selection},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/minddance-x/ICLR2026-AIDD}
}
```

## 📄 License

MIT License

---

*Made with ❤️ by [MindDance](https://github.com/minddance-x)*
