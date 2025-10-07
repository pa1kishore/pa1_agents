"""
Tool for querying Vertex AI RAG corpora and retrieving relevant information.
"""

import logging
import os
import re
from google.adk.tools.tool_context import ToolContext
from vertexai import rag
logger = logging.getLogger(__name__)

GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
RAG_CORPUS_LOCATION = os.getenv("RAG_CORPUS_LOCATION")
RAG_CORPUS_ID = os.getenv("RAG_CORPUS_ID")
DEFAULT_DISTANCE_THRESHOLD =0.8
DEFAULT_TOP_K=10
RAG_CORPUS_NAME = os.getenv("RAG_CORPUS_NAME")

def get_corpus_resource_name(corpus_name: str) -> str:
    """
    Convert a corpus name to its full resource name if needed.
    Handles various input formats and ensures the returned name follows Vertex AI's requirements.

    Args:
        corpus_name (str): The corpus name or display name

    Returns:
        str: The full resource name of the corpus
    """
    print(f"Getting resource name for corpus: {corpus_name}")

    # # If it's already a full resource name with the projects/locations/ragCorpora format
    # if re.match(r"^projects/[^/]+/locations/[^/]+/ragCorpora/[^/]+$", corpus_name):
    #     return corpus_name

    # # Check if this is a display name of an existing corpus
    # try:
    #     # List all corpora and check if there's a match with the display name
    #     corpora = rag.list_corpora()
    #     for corpus in corpora:
    #         print(f"====>corpus name {corpus.name}")
    #         if hasattr(corpus, "display_name") and corpus.display_name == corpus_name:
    #             return corpus.name
    # except Exception as e:
    #     print(f"Error when checking for corpus display name: {str(e)}")
    #     # If we can't check, continue with the default behavior
    #     pass

    # # If it contains partial path elements, extract just the corpus ID
    # if "/" in corpus_name:
    #     # Extract the last part of the path as the corpus ID
    #     corpus_id = corpus_name.split("/")[-1]
    # else:
    #     corpus_id = corpus_name

    # # Remove any special characters that might cause issues
    # corpus_id = re.sub(r"[^a-zA-Z0-9_-]", "_", corpus_id)

    # Construct the standardized resource name
    
    return f"projects/{GOOGLE_CLOUD_PROJECT}/locations/{RAG_CORPUS_LOCATION}/ragCorpora/{RAG_CORPUS_ID}"


def check_corpus_exists(corpus_name: str, tool_context: ToolContext) -> bool:
    """
    Check if a corpus with the given name exists.

    Args:
        corpus_name (str): The name of the corpus to check
        tool_context (ToolContext): The tool context for state management

    Returns:
        bool: True if the corpus exists, False otherwise
    """
    # Check state first if tool_context is provided
    # if tool_context!=None and tool_context.state !=None and tool_context.state.get(f"corpus_exists_{corpus_name}"):
    #     return True

    # try:
    #     # Get full resource name
    #     corpus_resource_name = get_corpus_resource_name(corpus_name)

    #     # List all corpora and check if this one exists
    #     corpora = rag.list_corpora()
    #     for corpus in corpora:
    #         if (
    #             corpus.name == corpus_resource_name
    #             or corpus.display_name == corpus_name
    #         ):
    #             # Update state
    #             tool_context.state[f"corpus_exists_{corpus_name}"] = True
    #             # Also set this as the current corpus if no current corpus is set
    #             if not tool_context.state.get("current_corpus"):
    #                 tool_context.state["current_corpus"] = corpus_name
    #             return True

    #     return False
    # except Exception as e:
    #     print(f"Error checking if corpus exists: {str(e)}")
    #     # If we can't check, assume it doesn't exist
    #     return False

    return True

def tool_rag_query(
    corpus_name: str,
    query: str,
    tool_context: ToolContext,
) -> dict:
    """
    Query a Vertex AI RAG corpus with a user question and return relevant information.

    Args:
        corpus_name (str): The name of the corpus to query. If empty, the current corpus will be used.
                          Preferably use the resource_name from list_corpora results.
        query (str): The text query to search for in the corpus
        tool_context (ToolContext): The tool context

    Returns:
        dict: The query results and status
    """
    try:

        # Check if the corpus exists
        if not check_corpus_exists(corpus_name, tool_context):
            return {
                "status": "error",
                "message": f"Corpus '{corpus_name}' does not exist. Please create it first using the create_corpus tool.",
                "query": query,
                "corpus_name": corpus_name,
            }

        # Get the corpus resource name
        corpus_resource_name = get_corpus_resource_name(corpus_name)
        if corpus_resource_name is None:
            return {
                "status": "error",
                "message": f"Corpus '{corpus_name}' does not exist. Failed to get corpus resource",
                "query": query,
                "corpus_name": corpus_name,
            }
        # Configure retrieval parameters
        rag_retrieval_config = rag.RagRetrievalConfig(
            top_k=DEFAULT_TOP_K,
            filter=rag.Filter(vector_distance_threshold=DEFAULT_DISTANCE_THRESHOLD),
        )

        # Perform the query
        print("Performing retrieval query...")
        response = rag.retrieval_query(
            rag_resources=[
                rag.RagResource(
                    rag_corpus=corpus_resource_name,
                )
            ],
            text=query,
            rag_retrieval_config=rag_retrieval_config,
        )

        # Process the response into a more usable format
        results = []
        if hasattr(response, "contexts") and response.contexts:
            for ctx_group in response.contexts.contexts:
                result = {
                    "source_uri": (
                        ctx_group.source_uri if hasattr(ctx_group, "source_uri") else ""
                    ),
                    "source_name": (
                        ctx_group.source_display_name
                        if hasattr(ctx_group, "source_display_name")
                        else ""
                    ),
                    "text": ctx_group.text if hasattr(ctx_group, "text") else "",
                    "score": ctx_group.score if hasattr(ctx_group, "score") else 0.0,
                }
                results.append(result)

        # If we didn't find any results
        if not results:
            return {
                "status": "warning",
                "message": f"No results found in corpus '{corpus_name}' for query: '{query}'",
                "query": query,
                "corpus_name": corpus_name,
                "results": [],
                "results_count": 0,
            }

        return {
            "status": "success",
            "message": f"Successfully queried corpus '{corpus_name}'",
            "query": query,
            "corpus_name": corpus_name,
            "results": results,
            "results_count": len(results),
        }

    except Exception as e:
        error_msg = f"Error querying corpus: {str(e)}"
        print(error_msg)
        return {
            "status": "error",
            "message": error_msg,
            "query": query,
            "corpus_name": corpus_name,
        }
    

# if __name__ == '__main__':
# #    toolContext = ToolContext()
#    res= tool_rag_query(corpus_name="atnt_corpus",query="how to setup voicemail",tool_context=None)
#    print(f' search tool response {res}')