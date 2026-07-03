#!/usr/bin/env python3
"""Load GLUE MRPC and QQP datasets, standardize to exp_sel_data_out schema."""

import json
import sys
from pathlib import Path
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

WS = Path(__file__).parent
DATASETS_DIR = WS / "temp" / "datasets"
OUT = WS / "full_data_out.json"


@logger.catch(reraise=True)
def main():
    Path("logs").mkdir(exist_ok=True)

    datasets = []

    # --- Dataset 1: GLUE MRPC ---
    mrpc_path = DATASETS_DIR / "full_glue_mrpc.json"
    logger.info(f"Loading MRPC from {mrpc_path}")
    mrpc_rows = json.loads(mrpc_path.read_text())
    logger.info(f"MRPC: {len(mrpc_rows)} rows")

    mrpc_examples = []
    for i, row in enumerate(mrpc_rows):
        s1 = row["sentence1"]
        s2 = row["sentence2"]
        label = row["label"]
        # input: JSON encoding of the pair for MinHash pipeline consumption
        input_text = json.dumps({"sentence1": s1, "sentence2": s2})
        output_text = "1" if label == 1 else "0"
        mrpc_examples.append({
            "input": input_text,
            "output": output_text,
            "metadata_label_meaning": "1=paraphrase(near-duplicate) 0=non-paraphrase",
            "metadata_row_index": i,
            "metadata_task_type": "binary_classification",
            "metadata_source": "glue_mrpc",
        })

    logger.info(f"MRPC examples: {len(mrpc_examples)}")
    datasets.append({"dataset": "glue_mrpc", "examples": mrpc_examples})

    # --- Write output ---
    result = {
        "metadata": {
            "description": "GLUE MRPC (Microsoft Research Paraphrase Corpus) for MinHash near-duplicate detection evaluation. Sentence pairs labeled 1=paraphrase (near-duplicate, high lexical overlap) or 0=non-paraphrase.",
            "dataset": "glue_mrpc",
            "source": "nyu-mll/glue config=mrpc (Dolan & Brockett 2005; GLUE benchmark Wang et al. 2019)",
            "num_rows": len(mrpc_examples),
            "positive_rate": round(sum(1 for r in mrpc_rows if r["label"] == 1) / len(mrpc_rows), 3),
            "relevance": "Paraphrase pairs share high n-gram overlap — direct MinHash/Jaccard evaluation signal",
        },
        "datasets": datasets,
    }

    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    logger.info(f"Saved {len(mrpc_examples)} total examples to {OUT}")


if __name__ == "__main__":
    main()
