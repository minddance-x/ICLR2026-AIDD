"""
filter_papers.py
基于关键词对论文进行多层筛选，提取 AIDD 相关论文
"""

import pandas as pd
import re
from pathlib import Path


# AIDD 核心关键词
ANCHOR_KEYWORDS = [
    r'drug discovery', r'drug design', r'molecule', r'molecular', r'protein',
    r'ligand', r'pocket', r'docking', r'admet', r'qsar', r'smiles', r'selfies',
    r'peptide', r'conformation', r'retrosynthesis', r'enzyme', r'antibody',
    r'biomolecule', r'binding affinity', r'genomic', r'bioinformatics',
    r'cheminformatics', r'crystallography', r'atomistic', r'molecular dynamics',
    r'pharmacology', r'therapeutic', r'residue', r'active site', r'epitope',
    r'antigen', r'genome', r'methylation', r'biological', r'biomedical',
    r'chemical', r'atom', r'force field', r'chemistry'
]

# 排除关键词（噪声来源）
EXCLUSION_PATTERNS = [
    r'video', r'image editing', r'image generation', r'image synthesis',
    r'autonomous driving', r'robotics', r'speech recognition',
    r'natural language', r'financial', r'urban', r'traffic', r'facial',
    r'portrait', r'weather', r'climate', r'novel view synthesis',
    r'computer vision', r'text-to-motion'
]


def build_regex(patterns: list) -> re.Pattern:
    """构建正则表达式"""
    pattern = '|'.join([fr'\b{p}' for p in patterns])
    return re.compile(pattern, re.IGNORECASE)


def is_aidd_paper(row: pd.Series, anchor_regex: re.Pattern, 
                   exclusion_regex: re.Pattern) -> bool:
    """判断论文是否与 AIDD 相关"""
    title = str(row['title']).lower()
    abstract = str(row['abstract']).lower()
    keywords = str(row['keywords']).lower()
    full_text = f"{title} {keywords} {abstract}"
    
    # 排除规则：如果命中排除词且标题中无强锚点词，则排除
    if exclusion_regex.search(full_text):
        strong_anchor = re.compile(
            r'\b(drug|molecule|molecular|protein|ligand|peptide)\b', 
            re.IGNORECASE
        )
        if not strong_anchor.search(title):
            return False
    
    # 必须命中至少一个锚点关键词
    if not anchor_regex.search(full_text):
        return False
    
    return True


def filter_papers(input_file: str, output_file: str) -> pd.DataFrame:
    """
    筛选 AIDD 相关论文
    
    Args:
        input_file: 输入 CSV 文件路径
        output_file: 输出 CSV 文件路径
        
    Returns:
        筛选后的 DataFrame
    """
    print(f"Loading {input_file}...")
    df = pd.read_csv(input_file).fillna('')
    print(f"Total papers: {len(df)}")
    
    anchor_regex = build_regex(ANCHOR_KEYWORDS)
    exclusion_regex = build_regex(EXCLUSION_PATTERNS)
    
    print("Filtering papers...")
    mask = df.apply(
        lambda row: is_aidd_paper(row, anchor_regex, exclusion_regex), 
        axis=1
    )
    filtered_df = df[mask].copy()
    
    print(f"Filtered papers: {len(filtered_df)}")
    
    # 保存结果
    filtered_df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Saved to {output_file}")
    
    return filtered_df


def main():
    input_file = 'data/iclr2026_all_papers.csv'
    output_file = 'data/iclr2026_aidd_papers.csv'
    
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found. Run fetch_papers.py first.")
        return
    
    filter_papers(input_file, output_file)


if __name__ == "__main__":
    main()
