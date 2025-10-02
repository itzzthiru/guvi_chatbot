import numpy as np
from sentence_transformers import SentenceTransformer

TEXT_PATH = "guvi.txt"
EMB_PATH = "guvi_embeddings.npy"
MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def main():
    with open(TEXT_PATH,"r",encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip()]
    model = SentenceTransformer(MODEL)
    print(f"Encoding {len(lines)} paragraphs...")
    embs = model.encode(lines, convert_to_numpy=True, show_progress_bar=True)
    np.save(EMB_PATH, embs)
    print("Saved to", EMB_PATH)

if __name__ == "__main__":
    main()
