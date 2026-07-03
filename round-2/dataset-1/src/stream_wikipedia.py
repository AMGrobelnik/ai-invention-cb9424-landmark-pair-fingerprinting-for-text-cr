#!/usr/bin/env python3
"""Stream 5000 English Wikipedia articles >300 words and save to temp/datasets/."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

OUTPUT_DIR = Path("/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/datasets")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TARGET = 5000
MIN_WORDS = 300

@logger.catch(reraise=True)
def main():
    from datasets import load_dataset
    logger.info("Streaming wikimedia/wikipedia en 20231101.en ...")
    ds = load_dataset("wikimedia/wikipedia", "20231101.en", split="train", streaming=True, trust_remote_code=False)

    articles = []
    checked = 0
    for row in ds:
        checked += 1
        text = row.get("text", "")
        words = text.split()
        if len(words) >= MIN_WORDS:
            articles.append({
                "id": row.get("id", str(checked)),
                "title": row.get("title", ""),
                "text": text,
                "url": row.get("url", ""),
                "word_count": len(words),
            })
            if len(articles) % 500 == 0:
                logger.info(f"Collected {len(articles)}/{TARGET} (checked {checked})")
        if len(articles) >= TARGET:
            break

    logger.info(f"Done: {len(articles)} articles from {checked} checked")

    out_path = OUTPUT_DIR / "wikipedia_en_5000.json"
    out_path.write_text(json.dumps(articles, ensure_ascii=False))
    logger.info(f"Saved to {out_path} ({out_path.stat().st_size / 1e6:.1f} MB)")

    # Also save mini (10 articles)
    mini_path = OUTPUT_DIR / "wikipedia_en_mini.json"
    mini_path.write_text(json.dumps(articles[:10], ensure_ascii=False))
    logger.info(f"Mini saved: {mini_path}")

if __name__ == "__main__":
    main()
