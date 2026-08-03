import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Nome do servidor e descrição
SERVER_NAME = "Python-Adder-Server"
SERVER_VERSION = "1.0.0"

# Inicializa o servidor com a especificação stateless
# O SDK atualizado lida com a ausência de handshake de sessão automaticamente
app = Server(SERVER_NAME)

@app.list_tools()
async def list_tools() -> list[Tool]:
    """
    Lista as ferramentas disponíveis.
    Na nova spec 2026-07-28, a lista de ferramentas agora suporta cache (ttlMs),
    mas aqui definimos a estrutura básica.
    """
    return [
        Tool(
            name="soma",
            description="Soma dois números inteiros fornecidos pelo usuário.",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "integer", "description": "O primeiro número"},
                    "b": {"type": "integer", "description": "O segundo número"}
                },
                "required": ["a", "b"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """
    Executa a ferramenta chamada.
    Na nova arquitetura stateless, esta chamada ocorre sem dependência de sessão anterior.
    """
    if name == "soma":
        try:
            a = int(arguments.get("a", 0))
            b = int(arguments.get("b", 0))
            resultado = a + b
            
            # Retorna o resultado como conteúdo de texto
            return [TextContent(type="text", text=f"O resultado de {a} + {b} é {resultado}")]
        except (ValueError, TypeError) as e:
            return [TextContent(type="text", text=f"Erro ao somar: {str(e)}")]
    
    raise ValueError(f"Ferramenta desconhecida: {name}")

async def main():
    # O servidor é executado via stdio (padrão para CLI)
    # Não há configuração de sessão ou handshake inicial necessário
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())