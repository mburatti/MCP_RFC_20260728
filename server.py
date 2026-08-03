#!/usr/bin/env python3
"""
MCP Server Implementation - Spec 2026-07-28 (Stateless Architecture)

Features:
- Stateless Core: No session state maintained, no Mcp-Session-Id header required.
- Direct Request Processing: Each tool invocation receives explicit arguments and returns stateless results.
- Extended Math Tools: soma, subtracao, multiplicacao, divisao, potencia, raiz_quadrada, resto_divisao.
"""

import math
from mcp.server.fastmcp import FastMCP

# Create FastMCP server instance (Stateless Core Spec 2026-07-28)
mcp = FastMCP("Stateless-Math-Server-2026-07-28")

@mcp.tool()
def soma(a: float, b: float) -> str:
    """Soma dois números fornecidos pelo usuário statelessly."""
    return f"O resultado de {a} + {b} é {a + b}"

@mcp.tool()
def subtracao(a: float, b: float) -> str:
    """Subtrai o segundo número do primeiro (a - b)."""
    return f"O resultado de {a} - {b} é {a - b}"

@mcp.tool()
def multiplicacao(a: float, b: float) -> str:
    """Multiplica dois números."""
    return f"O resultado de {a} * {b} é {a * b}"

@mcp.tool()
def divisao(a: float, b: float) -> str:
    """Divide o primeiro número pelo segundo (a / b)."""
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return f"O resultado de {a} / {b} é {a / b}"

@mcp.tool()
def potencia(base: float, expoente: float) -> str:
    """Eleva a base ao expoente (base ^ expoente)."""
    return f"O resultado de {base} ^ {expoente} é {math.pow(base, expoente)}"

@mcp.tool()
def raiz_quadrada(a: float) -> str:
    """Calcula a raiz quadrada de um número positivo."""
    if a < 0:
        return "Erro: Não é possível calcular raiz quadrada de número negativo."
    return f"A raiz quadrada de {a} é {math.sqrt(a)}"

@mcp.tool()
def resto_divisao(a: int, b: int) -> str:
    """Calcula o resto da divisão inteira entre dois números (a % b)."""
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return f"O resto da divisão de {a} por {b} é {a % b}"

if __name__ == "__main__":
    mcp.run()
