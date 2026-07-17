from extract import extract_text
from clean import clean_text
from chunk import chunk_text
from embed import create_embeddings
from store import create_collection, store_chunks


def main():
    text = extract_text("data/fannie_mae.pdf")

    cleaned_text = clean_text(text)

    chunks = chunk_text(cleaned_text)

    print(f"Total chunks: {len(chunks)}")

    embeddings = create_embeddings(chunks)

    collection = create_collection()

    store_chunks(
        collection,
        chunks,
        embeddings
    )

    print("Index created successfully!")


if __name__ == "__main__":
    main()