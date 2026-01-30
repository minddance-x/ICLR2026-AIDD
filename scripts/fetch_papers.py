"""
fetch_papers.py
从 OpenReview 获取 ICLR 2026 全部接收论文的元数据
"""

import openreview
import pandas as pd
from tqdm import tqdm


def fetch_iclr_papers(venue_id: str = "ICLR.cc/2026/Conference") -> pd.DataFrame:
    """
    从 OpenReview API 获取指定会议的全部论文
    
    Args:
        venue_id: OpenReview 会议 ID
        
    Returns:
        包含论文元数据的 DataFrame
    """
    print(f"Connecting to OpenReview API...")
    client = openreview.api.OpenReviewClient(baseurl='https://api2.openreview.net')
    
    print(f"Fetching papers from {venue_id}...")
    notes = client.get_all_notes(content={'venueid': venue_id})
    print(f"Retrieved {len(notes)} papers")
    
    papers = []
    for note in tqdm(notes, desc="Processing papers"):
        content = note.content
        paper = {
            'id': note.id,
            'title': content.get('title', {}).get('value', 'N/A'),
            'authors': ', '.join(content.get('authors', {}).get('value', [])),
            'abstract': content.get('abstract', {}).get('value', 'N/A'),
            'keywords': ', '.join(content.get('keywords', {}).get('value', [])),
            'pdf_link': f"https://openreview.net/pdf?id={note.id}",
            'venue': content.get('venue', {}).get('value', 'N/A'),
        }
        papers.append(paper)
    
    return pd.DataFrame(papers)


def main():
    df = fetch_iclr_papers()
    
    output_file = 'data/iclr2026_all_papers.csv'
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Saved {len(df)} papers to {output_file}")


if __name__ == "__main__":
    main()
