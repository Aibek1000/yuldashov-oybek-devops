import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def student_info():
    return (
        "DevOps Student Application\n\n"
        f"Name: {os.getenv('STUDENT_NAME', 'Oybek')}\n"
        f"Surname: {os.getenv('STUDENT_SURNAME', 'Yuldashov')}\n"
        f"Group: {os.getenv('STUDENT_GROUP', 'IT2-2307')}\n"
        f"Student ID: {os.getenv('STUDENT_ID', '41559')}\n\n"
        "Application is running successfully!\n"
    )


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        content = student_info().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    print(student_info(), flush=True)
    print("Server started on port 8000", flush=True)
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
