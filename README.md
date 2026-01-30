# ICLR 2026 AIDD 论文精选

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Papers](https://img.shields.io/badge/Papers-132-blue.svg)](#论文列表)

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

从这 132 篇论文中观察到的主要趋势：

1. **扩散模型 (Diffusion Models)**：约 40% 的论文采用，覆盖分子生成、蛋白质设计等任务
2. **Flow Matching**：作为扩散模型的替代方案逐渐兴起
3. **全原子建模 (All-Atom)**：多篇论文强调原子级精度
4. **可合成性约束**：生成分子的实际可合成性成为研究热点

## 📝 论文列表

完整论文列表见 [`iclr2026_aidd_papers_refined.csv`](./iclr2026_aidd_papers_refined.csv)

每篇论文包含以下字段：
- `title`: 论文标题
- `authors`: 作者
- `abstract`: 摘要
- `keywords`: 关键词
- `pdf_link`: PDF 下载链接
- `venue`: 会议信息

### Top 10 论文预览

| 论文标题 | PDF |
|---------|-----|
| h-MINT: Modeling Pocket-Ligand Binding with Hierarchical Molecular Interaction Network | [PDF](https://openreview.net/pdf?id=ajywV0kKXk) |
| SigmaDock: Untwisting Molecular Docking with Fragment-Based SE(3) Diffusion | [PDF](https://openreview.net/pdf?id=Vgm77U4ojX) |
| ATOM: A Pretrained Neural Operator for Multitask Molecular Dynamics | [PDF](https://openreview.net/pdf?id=e9cV4xSjbR) |
| FragFM: Hierarchical Framework for Efficient Molecule Generation | [PDF](https://openreview.net/pdf?id=tr6vRn2aPg) |
| PoseX: AI Defeats Physics-based Methods on Protein Ligand Cross-Docking | [PDF](https://openreview.net/pdf?id=qqzxKudD4T) |
| Pallatom-Ligand: an All-Atom Diffusion Model for Designing Ligand-Binding Proteins | [PDF](https://openreview.net/pdf?id=uMD75SDTTA) |
| BioMD: All-atom Generative Model for Biomolecular Dynamics Simulation | [PDF](https://openreview.net/pdf?id=LQDeJk6NOr) |
| SimpleFold: Folding Proteins is Simpler than You Think | [PDF](https://openreview.net/pdf?id=FileqNzZzn) |
| SYNC: Measuring and Advancing Synthesizability in Structure-Based Drug Design | [PDF](https://openreview.net/pdf?id=y1tPw4Uuzg) |
| DrugTrail: Explainable Drug Discovery via Structured Reasoning | [PDF](https://openreview.net/pdf?id=MMLAvR1juf) |

## 🚀 使用方法

```bash
# 克隆仓库
git clone https://github.com/minddance-x/ICLR2026-AIDD.git

# 查看论文列表
cd ICLR2026-AIDD
cat iclr2026_aidd_papers_refined.csv
```

## 🛠️ 筛选方法

我们采用三层筛选策略：

1. **关键词初筛**：基于 40+ 个 AIDD 核心关键词匹配标题、摘要和关键词
2. **噪声去除**：排除视频生成、图像编辑等无关领域的误匹配论文
3. **人工校验**：逐一检查边缘案例，剔除非 AIDD 核心论文

筛选流程：5356 → 538 → 210 → **132**

## 📖 引用

如果本项目对您有帮助，欢迎 Star ⭐ 和引用：

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
