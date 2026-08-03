#!/usr/bin/env python3
"""
MCP Client Implementation - Spec 2026-07-28 (Stateless Architecture)

Features:
- Stateless Connection: Operates without stateful session tracking or Mcp-Session-Id headers.
- Immediate Tool Execution: Requests carry input parameters statelessly.
"""

import asyncio
import os
from pathlib import Path
from mcp import StdioServerParameters, stdio_client
from mcp.client.session import ClientSession

# Locate script base directory and project virtualenv Python binary (Python 3.14 in .venv)
base_dir = Path(__file__).parent.resolve()
venv_python = (base_dir / ".venv" / "bin" / "python3.14").resolve()
if not venv_python.exists():
    venv_python = (base_dir / ".venv" / "bin" / "python3").resolve()

python_bin = str(venv_python)

env = dict(os.environ)
if venv_python.parent.exists():
    env["PATH"] = f"{venv_python.parent}:{env.get('PATH', '')}"

server_params = StdioServerParameters(
    command=python_bin,
    args=[str(base_dir / "server.py")],
    env=env
)

async def main():
    print("Starting MCP Server (Stateless Mode 2026-07-28 Spec)...")
    # 1. Establish Transport
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize connection handshake
            await session.initialize()
            print("Connected to MCP Server (Stateless Mode).")

            # 2. Discover Available Tools (Stateless)
            tools_response = await session.list_tools()
            print("\n--- Discovered Tools (Stateless) ---")
            for tool in tools_response.tools:
                print(tool.model_dump_json(indent=2))
            print("------------------------------------\n")

            # 3. Call Tool (Stateless Request)
            print("Calling tool: soma(15, 27)...")
            result = await session.call_tool(
                name="soma",
                arguments={"a": 15, "b": 27}
            )

            # 4. Process Response
            if result.content:
                for item in result.content:
                    if item.type == "text":
                        print(f"Result: {item.text}")
            else:
                print("No content returned.")

    print("\nClient finished. Stateless server connection closed.")

if __name__ == "__main__":
    asyncio.run(main())