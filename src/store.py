#store embedding in chromadb

import chromadb


def create_collection():
    """
    Create or load a ChromaDB collection.
    """
    #create local chromadb inside a folder "chroma_db"
    client = chromadb.PersistentClient(path="chroma_db")
    
    #the concept of a collection is the same as a table in SQL
    collection = client.get_or_create_collection(
        name="fannie_mae"
    )

    return collection

import chromadb

def store_chunks(collection, chunks, embeddings):
    """
    Store chunks and embeddings in ChromaDB.
    """

    collection.add(
        #creates automatic IDs
        ids=[str(i) for i in range(len(chunks))],
        documents=chunks,
        #save  vectors
        embeddings=embeddings.tolist()
    )