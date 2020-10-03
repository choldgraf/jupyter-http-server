__version__ = "0.0.1"
def setup_http_server():
  return {
    'command': ['python3', '-m', 'http.server', '{port}'],
    'absolute_url': False,
    'launcher_entry': {
      'title': "HTTP Server"
    }
  }