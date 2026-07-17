from store import create_collection
from search import search


def main():
    collection = create_collection()

    question = input("Ask a question: ")

    results = search(
        collection,
        question,
        n_results=3
    )

    print("\nTop Results:\n")

    for i, document in enumerate(results["documents"][0], start=1):
        print(f"Result {i}:\n")
        print(document)
        print("-" * 80)


if __name__ == "__main__":
    main()