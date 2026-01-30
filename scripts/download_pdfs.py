"""
download_pdfs.py
批量下载论文 PDF 文件
"""

import pandas as pd
import requests
import os
import re
import time
from tqdm import tqdm
from pathlib import Path


def sanitize_filename(filename: str, max_length: int = 150) -> str:
    """清理文件名，移除非法字符"""
    cleaned = re.sub(r'[<>:"/\\|?*]', '', filename)
    return cleaned[:max_length]


def download_pdfs(input_file: str, output_dir: str = 'pdfs', 
                  delay: float = 0.5) -> dict:
    """
    批量下载论文 PDF
    
    Args:
        input_file: 包含论文信息的 CSV 文件
        output_dir: PDF 保存目录
        delay: 下载间隔（秒），避免请求过快
        
    Returns:
        下载统计信息
    """
    df = pd.read_csv(input_file)
    print(f"Papers to download: {len(df)}")
    
    Path(output_dir).mkdir(exist_ok=True)
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    })
    
    stats = {'success': 0, 'skipped': 0, 'failed': 0}
    
    for _, row in tqdm(df.iterrows(), total=len(df), desc="Downloading"):
        title = row['title']
        url = row['pdf_link']
        filename = f"{sanitize_filename(title)}.pdf"
        filepath = os.path.join(output_dir, filename)
        
        # 跳过已存在的文件
        if os.path.exists(filepath):
            stats['skipped'] += 1
            continue
        
        try:
            response = session.get(url, timeout=60)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                stats['success'] += 1
            else:
                stats['failed'] += 1
            time.sleep(delay)
        except Exception as e:
            print(f"\nError downloading {title}: {e}")
            stats['failed'] += 1
    
    print(f"\nDownload complete:")
    print(f"  Success: {stats['success']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Failed: {stats['failed']}")
    
    return stats


def main():
    input_file = 'data/iclr2026_aidd_papers_refined.csv'
    
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found.")
        return
    
    download_pdfs(input_file)


if __name__ == "__main__":
    main()
