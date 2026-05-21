"""Step 1: prove git deploy, process start, and HTTP bind on PORT."""

import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", "8000"))


def log(msg: str) -> None:
    print(f"[step01] {msg}", flush=True)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"hello")

    def log_message(self, fmt: str, *args) -> None:
        log(f"HTTP {self.address_string()} - {fmt % args}")


if __name__ == "__main__":
    log(f"importing mcp...")
    from dotdata_docs_mcp.server import mcp
    log(f"importing mcp successful")
    log("hello world")
    log(f"listening on 0.0.0.0:{PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
