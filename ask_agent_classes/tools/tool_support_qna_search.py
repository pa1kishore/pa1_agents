# """
# This tool, retuns information from AT&T Portal about AT&T products and services. This tool also returns steps for troubleshoot any user issues.
# """
# from google.adk.tools.tool_context import ToolContext
# import os
# import urllib.parse
# import requests
# import urllib3
# import json
# import logging
# from urllib3.exceptions import InsecureRequestWarning

# urllib3.disable_warnings(InsecureRequestWarning)
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
# search_api_host = os.getenv('SEARCH_API_BASE')
# if search_api_host is None or search_api_host.strip() =='':
#     search_api_host= 'https://services.att.com'
# # search_api_host= 'https://services.att.com'    

# def tool_support_qna_topdocs(query: str,tool_context: ToolContext) -> dict:
#     """
#     This tool, retuns information from AT&T Portal about AT&T products and services. This tool also returns steps for troubleshoot any user issues.

#     Args:
#         query (str): query to perform search in AT&T portal
#         tool_context (ToolContext): The tool context
        

#     Returns:
#         dict: A dictionary with keys 'success' (str) and 'message' (str),
#               additionally returns 'data' (list[dict]) documents sematically matching with user query and url (str) search api url if successful.
#     """
#     logger.info('Tool started tool_qna_search')
#     # Validate inputs
#     if query is None or query.strip() == '':

#         return {
#             "status": "error",
#             "message": "Tool input validation failed. User query is empty"
#         }
#     if '*' in query:
#         #query contain * search calls fails return without calling seach api or replace with something else
#         # logger.info('query cotains "*"')
#         return {
#             "status": "error",
#             "message": "Tool input validation failed. query cotains '*'"
#         }
#     # Pre-process any input parameters processing
#         # nothing
    

#     try:
#         headers = {
#             'Content-Type':"application/json",
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
#         }
#         # get data from backend
#         #API: https://services.att.com/search/v1/topdocs?app-id=sitesearch&rows=100&q=apple%20iphone%2016

#         url =f"{search_api_host}/search/v1/topdocs?app-id=sitesearch&rows=7&fl=chatURL,los,chunk_html,chunk_markdown,title&q={urllib.parse.quote_plus(query)}"
#         logger.info(f'Final search query {url}')
#         search_response = requests.request('GET', url, headers=headers, verify=False)
#         final_response ={
#             "status":"success"
#         }
#         if search_response.status_code ==200:
#             documents = json.loads(search_response.text)['response']['docs']
#             docs=[]
#             for doc in documents:
#                 content = doc['chunk_markdown'] if 'chunk_markdown' in doc else None
#                 if content is None:
#                     content = doc['chunk_html'] if 'chunk_html' in doc else None
#                 docs.append({
#                     "url": doc['chatURL'] if 'chatURL' in doc else None,
#                     "content": content,
#                     "title": doc['title'] if 'title' in doc else None,
#                 })
                
#             final_response['data'] = docs 
#         else:
#             logger.info(f"failed to get documents using tool_support_qna_topdocs tool status code: {search_response.status_code} ")
#             final_response = {
#                  "status": "error",
#                 "message": f"Error get data from search api status code: {search_response.status_code}",
#                 "url": url
#             }
#         # logger.info (f'Returning search restults {final_response}')
#         return final_response
#     except Exception as e:
#         return {
#             "status": "error",
#             "message": f"Error get data from search api: {str(e)}"
#         }
#     # Post-process any input parameters processing
#         #nothing




# # if __name__ == '__main__':
# #    res= tool_support_qna_search(query="how to setup voicemail",tool_context=None)
# #    logger.info(f' search tool response {res}')