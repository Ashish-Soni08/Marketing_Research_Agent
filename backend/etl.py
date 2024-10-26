from dotenv import dotenv_values
from llama_parse import LlamaParse
from llama_index.core import (SimpleDirectoryReader, 
                             VectorStoreIndex)

config = dotenv_values(".env")

def parse_document(pdf_document=["./sample_data/ozempic.pdf"], target_pages: str = None):

    parsing_instructions = """
    The provided document is a thin piece of folded paper that is part of every drug prescription box. 
    Usually the text is in VERY small print and typically provides information about dosages, side effects, storage instructions and much more. 
    Try to extract the key information so that it is easy to understand.
    """

    pdf_parser = LlamaParse(
    api_key=config["LLAMACLOUD_API_KEY"],
    result_type="text",  # markdown doesn't work with fast_mode to True
    parsing_instruction=parsing_instructions,
    num_workers=7,
    check_interval=2,
    max_timeout=2000,
    verbose=True,
    show_progress=True,
    language="en",
    invalidate_cache=False,
    do_not_cache=False,
    fast_mode=True,
    ignore_errors=True,
    split_by_page=True,
    disable_ocr=True,
    target_pages=target_pages  # for testing purposes use target_pages="0,80" to only parse the first and last page 
    )

    file_extractor = {".pdf": pdf_parser}

    documents = SimpleDirectoryReader(input_files=pdf_document, file_extractor=file_extractor).load_data()

    return documents

# Works
# documents = parse_document(target_pages="77")
# print(len(documents))
# print(documents[0])

# index = VectorStoreIndex(vector_store=documents)
# query_engine = index.query_engine()

# query = "What can I use Ozempic for?"
# response = query_engine.query(query)
# print(response)