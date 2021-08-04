from parse import parse_html

def test_parse_html():
    html = '''
<!DOCTYPE html>
<html>
<body>
<nav>
    <a href="/blog">Blog</a>
    <a href="/about">Here is my real website</a>
    <a href="https://dsmrt.com">Here is my real website</a>
    <a href="https://github.com/dsmrt">@dsmrt on github</a>
</nav>
<h1>Welcome</h1>
<p>My awesome website.</p>
</body>
</html>
'''
    # there should only be 2 valid anchor tags
    assert len(parse_html(html)) == 2