"""Check the public site's structure, local links, and HTTP delivery."""
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import urlsplit
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent
PAGES = ['index.html', 'privacy.html', 'terms.html']


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.ids = []
        self.links = []
        self.h1 = 0
        self.main = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        self.h1 += tag == 'h1'
        self.main += tag == 'main'
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])


for name in PAGES:
    text = (ROOT / name).read_text()
    doc = Document()
    doc.feed(text)
    assert text.startswith('<!doctype html>'), name
    assert doc.h1 == 1 and doc.main == 1, name
    assert len(doc.ids) == len(set(doc.ids)), name
    assert any(t == 'html' and a.get('lang') == 'en' for t, a in doc.tags), name
    assert any(t == 'meta' and a.get('name') == 'viewport' for t, a in doc.tags), name
    assert not any(t in {'script', 'iframe', 'form'} for t, _ in doc.tags), name
    assert '[ADD YOUR MONITORED SUPPORT EMAIL BEFORE PUBLISHING]' not in text, name
    assert 'mailto:chen0625tung@gmail.com' in doc.links, name
    assert 'operated by River' in text, name
    for marker in ('Unpublished draft', 'before launch', 'must be reviewed', 'Draft status', '[ADD YOUR'):
        assert marker not in text, (name, marker)
    if name in {'privacy.html', 'terms.html'}:
        assert '<time datetime="2026-11-04">November 4, 2026</time>' in text, name
    if name == 'privacy.html':
        assert 'hosted on GitHub Pages' in text, name
        assert 'https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement' in doc.links, name
    for link in doc.links:
        target = urlsplit(link)
        if target.scheme or target.netloc:
            assert target.scheme in {'https', 'mailto'}, link
            if target.scheme == 'mailto':
                assert target.path == 'chen0625tung@gmail.com', link
            continue
        if target.path:
            path = (ROOT / target.path).resolve()
            assert path.is_relative_to(ROOT) and path.is_file(), link
        elif target.fragment:
            assert target.fragment in doc.ids, link
    print(f'PASS structure and local links: {name}')


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT)))
thread = Thread(target=server.serve_forever, daemon=True)
thread.start()
try:
    for name in PAGES + ['styles.css']:
        with urlopen(f'http://127.0.0.1:{server.server_port}/{name}') as response:
            assert response.status == 200
            assert response.read() == (ROOT / name).read_bytes()
            print(f'PASS HTTP 200 and exact contents: {name}')
finally:
    server.shutdown()
    server.server_close()
    thread.join()
print('All checks passed. No persistent server started. Visual rendering and Google acceptance are not tested.')
