import os
from toolbox_core import ToolboxSyncClient
from typing import List
 # Define the URL where your Toolbox server is running
TOOLBOX_URL = os.getenv("MCP_TOOLBOX_URL", "http://127.0.0.1:5000")

# Create the client instance
toolbox_client = ToolboxSyncClient(TOOLBOX_URL)
def get_sqlite_toolset() -> List:
    """
    Connects to the running Toolbox server and retrieves the configured tools.
    """
    # Create the client instance locally within the function if you prefer 
    # to keep the global scope clean, or use the global one defined above.
    # toolbox_client = ToolboxSyncClient(TOOLBOX_URL) 
    
    # Assuming toolbox_client is defined in the global scope as you had it:
    global toolbox_client 

    # Load the desired tools or toolsets

    try:
        # Calling load_toolset() without a name defaults to 'default-toolset'
        # which usually loads all tools defined in your YAML file.
        sqlite_tools = toolbox_client.load_toolset() 
        print(f"Successfully loaded {len(sqlite_tools)} tools from the Toolbox server.")
        return sqlite_tools

    except Exception as e:
        print(f"Failed to load tools from {TOOLBOX_URL}. Is the Toolbox server running? Error: {e}")
        # Return an empty list upon failure so the application doesn't crash
        return []