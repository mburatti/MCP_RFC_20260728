# MCP Sample Application (Stateless Architecture)

A Model Context Protocol (MCP) sample project implemented in Python using `FastMCP` and `mcp.client`. This project demonstrates a stateless MCP server exposing mathematical tools over `stdio` transport along with an asynchronous client.

---

## Features

- **Stateless MCP Server (`server.py`)**: Uses standard `stdio` transport without maintaining session states.
- **Asynchronous Client (`client.py`)**: Connects to the MCP server, discovers available tools dynamically, and executes tool calls.

---

## Setup & Installation

### Prerequisites

- Python 3.10+ (Python 3.14 supported)
- Virtual Environment (`.venv`)

### 1. Create and Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Option A: Using the Runner Script

Execute the provided bash script to automatically use the environment's Python interpreter:

```bash
chmod +x run_sample.sh
./run_sample.sh
```

### Option B: Running Manually

Activate your virtual environment and run the client:

```bash
python3 client.py
```

---

## Example Output

When running `client.py` or `./run_sample.sh`, the client will:
1. Start the MCP server via `stdio`.
2. Discover and print all available registered tools.
3. Invoke the `soma` tool with arguments `a=15` and `b=27`.

```text
Starting MCP Server (Stateless Mode 2026-07-28 Spec)...
Connected to MCP Server (Stateless Mode).

--- Discovered Tools (Stateless) ---
{
  "name": "soma",
  "description": "Soma dois números fornecidos pelo usuário statelessly.",
  ...
}
------------------------------------

Calling tool: soma(15, 27)...
Result: O resultado de 15.0 + 27.0 é 42.0

Client finished. Stateless server connection closed.
```
