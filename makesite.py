"""
Script to build a website from a bunch of markdown files.
Inspired by https://github.com/sunainapai/makesite
Tweaked for almarklein.org
Then for pygfx.org
"""

import os
import shutil
import webbrowser
import collections

import markdown
import pygments
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name


TITLE = "pygfx.org"

NAV = {
    "Main": "index",
    "Blog": "blog",
    "Sponsor": "sponsor",
    "Archive": "archive",
    # "Social": {
    #     'Twitter': 'https://twitter.com/pygfx',
    # },
}

NEWS = {}  # generated front-end

EXTERNAL_BLOG_POSTS = [
    {
        "title": "Rendering thick lines with dashes",
        "date": "2024-02-23",
        "url": "https://almarklein.org/line_rendering.html",
        "thumbnail": "https://almarklein.org/thumbs/line_rendering.jpg",
    },
    {
        "title": "GPU triangle tricks",
        "date": "2024-02-22",
        "url": "https://almarklein.org/triangletricks.html",
        "thumbnail": "https://almarklein.org/thumbs/triangletricks.jpg",
    },
    {
        "title": "On WebGPU, wgpu-py, and pygfx",
        "date": "2023-02-04",
        "url": "https://almarklein.org/wgpu.html",
        "thumbnail": "https://almarklein.org/thumbs/wgpu.jpg",
    },
    {
        "title": "Gamma and sRGB in visualisation",
        "date": "2022-09-29",
        "url": "https://almarklein.org/gamma.html",
        "thumbnail": "https://almarklein.org/thumbs/gamma.jpg",
    },
]

ExternalPage = collections.namedtuple("ExternalPage", ["title", "date", "url", "thumbnail"])
EXTERNAL_BLOG_POSTS = [ExternalPage(**x) for x in EXTERNAL_BLOG_POSTS]
EXTERNAL_BLOG_POSTS.sort(key=lambda p: p.date)


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(THIS_DIR, "output")
STATIC_DIR = os.path.join(THIS_DIR, "static")
PAGES_DIR = os.path.join(THIS_DIR, "pages")
POSTS_DIR = os.path.join(THIS_DIR, "posts")


REDIRECT = '<html><head><meta HTTP-EQUIV="REFRESH" content="0; url=URL"></head></html>'


def create_menu(page):
    """ Create the menu for the given page.
    """
    menu = ""

    if True:
        menuitems = []
        menuitems.append('<span class="header">Pages</span>')
        for title, target in NAV.items():
            if isinstance(target, str):
                if target.startswith(("https://", "http://", "/")):
                    menuitems.append(f"<a href='{target}'>{title}</a>")
                else:
                    menuitems.append(f"<a href='{target}.html'>{title}</a>")
                    if target == page.name:
                        menuitems[-1] = menuitems[-1].replace("<a ", '<a class="current" ')
            elif isinstance(target, dict):
                menuitems.append(f"<a href='{target.get('', '#')}.html'>{title}</a>")
                if target.get("", None) == page.name:
                    menuitems[-1] = menuitems[-1].replace("<a ", '<a class="current" ')
                if True:  # any(page.name == subtarget for subtarget in target.values()):
                    for subtitle, subtarget in target.items():
                        if not subtitle:
                            continue
                        if subtarget.startswith(("https://", "http://", "/")):
                            menuitems.append(f"<a class='sub' href='{subtarget}'>{subtitle}</a>")
                        else:
                            menuitems.append(
                                f"<a class='sub' href='{subtarget}.html'>{subtitle}</a>"
                            )
                            if subtarget == page.name:
                                menuitems[-1] = menuitems[-1].replace("class='", "class='current ")
            else:
                raise RuntimeError(f"Unexpected NAV entry {type(target)}")

        menu += "<div class='block1'>"
        menu += "<br>".join(menuitems)
        menu += "</div>"

    subtitles = [title for level, title in page.headers if level == 2]
    if subtitles:
        menuitems = []
        menuitems.append("<span class='header'>Current page</span>")
        menuitems += [
            f"<a class='sub' href='#{title.lower()}'>{title}</a>" for title in subtitles
        ]

        menu += "<br>"
        menu += "<div class='block2'>"
        menu += "<br>".join(menuitems)
        menu += "</div>"

    # if NEWS:
    #     menuitems = []
    #     menuitems.append('<br /><span class="header">News</span>')
    #     for title, url in NEWS.items():
    #         # menuitems.append(f"<a class='sub' href='{url}'>{title}</a>")
    #         menuitems.append(f"<a href='{url}'>{title}</a>")

    return menu


def create_blog_related_pages(posts):
    """ Create blog overview page and archive.
    """

    blogpages = {}

    # Generate overview page
    html = ["<h1>Blog</h1>"]

    html += ["\n\n<h2>Status updates</h2>"]
    for page in reversed(posts):
        text = page.md
        if "<!-- END_SUMMARY -->" in text:
            summary = text.split("<!-- START_SUMMARY -->")[-1].split(
                "<!-- END_SUMMARY -->"
            )[0]
        else:
            summary = text.split("## ")[0]
        summary = summary.split("-->")[-1]
        datespan = f"<span class='post-date-tags'>{page.date}</span>"

        html.append(f"<div style='border-top: 1px solid #ddd;'>{datespan}</div>")
        html.append(f'<a class="header" href="{page.name}.html"><h3>{page.title}</h3></a>')
        if page.thumbnail:
            html.append(f"<a href='{page.name}.html'><img src='{page.thumbnail}' class='thumb' /></a>")
        html.append("<p>" + summary )
        html.append(f"<a href='{page.name}.html'>Read more ...</a>")
        html.append("</p>")
        html.append("<br /><br /><div style='clear: both;'></div>")

    html += ["\n\n<h2>External blog posts</h2>"]
    for page in reversed(EXTERNAL_BLOG_POSTS):
        datespan = f"<span class='post-date-tags'>{page.date}</span>"
        html.append(f"<div style='border-top: 1px solid #ddd;'>{datespan}</div>")
        if page.thumbnail:
            html.append(f"<a href='{page.url}'><img src='{page.thumbnail}' class='thumb' /></a>")
        html.append(f'<a class="header" href="{page.url}"><h3>{page.title}</h3></a>')
        html.append("<br /><br /><div style='clear: both;'></div>")

    blogpages["overview"] = "\n".join(html)

    # Generate archive page
    year = ""
    html = ["<h1>Archive</h1>\n"]
    for page in reversed(posts):
        if page.date[:4] != year:
            year = page.date[:4]
            html.append(f"<h2>{year}</h2>")
        html.append(f'{page.date}: <a href="{page.name}.html">{page.title}</a><br />')
    blogpages["archive"] = "\n".join(html)

    # todo: Generate page for each tag

    return blogpages


def create_assets():
    """ Returns a dict of all the assets representing the website.
    """
    assets = {}

    # Load all static files
    for root, dirs, files in os.walk(STATIC_DIR):
        for fname in files:
            filename = os.path.join(root, fname)
            with open(filename, "rb") as f:
                assets[os.path.relpath(filename, STATIC_DIR)] = f.read()

    # Collect pages
    pages = {}
    for fname in os.listdir(PAGES_DIR):
        if fname.lower().endswith(".md"):
            name = fname.split(".")[0].lower()
            with open(os.path.join(PAGES_DIR, fname), "rb") as f:
                md = f.read().decode()
            pages[name] = Page(name, md)

    # Collect blog posts
    posts = []
    for fname in os.listdir(POSTS_DIR):
        if fname.lower().endswith(".md"):
            name = fname.split(".")[0].lower()
            assert name not in pages, f"blog post slug not allowed: {name}"
            with open(os.path.join(POSTS_DIR, fname), "rb") as f:
                md = f.read().decode()
            posts.append(Page(name, md))

    # Sort, select publishable, create shortlist
    posts.sort(key=lambda p: p.date)
    publishable_posts = [post for post in posts if post.date and not post.name.startswith("_")]

    # Get recent posts
    recent_posts = []
    recent_posts += publishable_posts[-1:]
    recent_posts += EXTERNAL_BLOG_POSTS[-1:]
    recent_posts_str = ",".join(str({"title": p.title, "date": p.date, "url": p.url}) for p in recent_posts)

    # Get template
    with open(os.path.join(THIS_DIR, "template.html"), "rb") as f:
        html_template = f.read().decode()

    with open(os.path.join(THIS_DIR, "style.css"), "rb") as f:
        css = f.read().decode()
    css += "/* Pygments CSS */\n" + HtmlFormatter(style="vs").get_style_defs(
        ".highlight"
    )

    # Generate posts
    for page in posts:
        page.prepare(pages.keys())
        title = page.title
        menu = create_menu(page)
        html = html_template.format(
            title=title, style=css, body=page.to_html(), menu=menu
        )
        print("generating post", page.name + ".html")
        assets[page.name + ".html"] = html.encode()

    # Generate pages
    for page in pages.values():
        page.prepare(pages.keys())
        title = TITLE if page.name == "index" else TITLE + " - " + page.title
        menu = create_menu(page)
        html = html_template.format(
            title=title, style=css, body=page.to_html(), menu=menu
        )
        print("generating page", page.name + ".html")
        if page.name == "index":
            js = f"var recent_blog_posts = [{recent_posts_str}];"
            html = html.replace("var recent_blog_posts = [];", js)
        assets[page.name + ".html"] = html.encode()

    # Generate special pages
    fake_md = ""  # "##index\n## archive\n## tags"
    for name, html in create_blog_related_pages(publishable_posts).items():
        name = "blog" if name == "overview" else name
        print("generating page", name + ".html")
        assets[f"{name}.html"] = html_template.format(
            title=TITLE, style=css, body=html, menu=create_menu(Page("", fake_md))
        ).encode()

    # Backwards compat with previous site
    for page in pages.values():
        assets["pages/" + page.name + ".html"] = REDIRECT.replace(
            "URL", f"/{page.name}.html"
        ).encode()

    # Fix backslashes on Windows
    for key in list(assets.keys()):
        if "\\" in key:
            assets[key.replace("\\", "/")] = assets.pop(key)

    return assets


def main():
    """ Main function that exports the page to the file system.
    """
    # Create / clean output dir
    if os.path.isdir(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    os.mkdir(OUT_DIR)

    # Write all assets to the directory
    for fname, bb in create_assets().items():
        filename = os.path.join(OUT_DIR, fname)
        dirname = os.path.dirname(filename)
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        with open(filename, "wb") as f:
            f.write(bb)


class Page:
    """ Representation of a page. It takes in markdown and produces HTML.
    """

    def __init__(self, name, markdown):
        self.name = name
        self.md = markdown
        self.parts = []
        self.headers = []
        self.url = f"{name}.html"

        self.title = name
        if markdown.startswith("# "):
            self.title = markdown.split("\n")[0][1:].strip()

        self.date = None
        if "<!-- DATE:" in markdown:
            self.date = markdown.split("<!-- DATE:")[-1].split("-->")[0].strip() or None
        if self.date is not None:
            assert (
                len(self.date) == 10 and self.date.count("-") == 2
            ), f"Weird date in {name}.md"

        self.author = None
        if "<!-- AURTHOR:" in markdown:
            self.author = markdown.split("<!-- AURTHOR:")[-1].split("-->")[0].strip()

        self.tags = []
        if "<!-- TAGS:" in markdown:
            self.tags = [
                x.strip()
                for x in markdown.split("<!-- TAGS:")[-1].split("-->")[0].split(",")
            ]

        self.thumbnail = None
        for fname in ["thumbs/" + self.name + ".jpg"]:
            if os.path.isfile(os.path.join(THIS_DIR, "static", fname)):
                self.thumbnail = fname

    def prepare(self, page_names):
        # Convert markdown to HTML
        self.md = self._fix_links(self.md, page_names)
        self.md = self._highlight(self.md)
        self._split()  # populates self.parts and self.headers

    def _fix_links(self, text, page_names):
        """ Fix the markdown links based on the pages that we know.
        """
        for n in page_names:
            text = text.replace(f"]({n})", f"]({n}.html)")
            text = text.replace(f"]({n}.md)", f"]({n}.html)")
        return text

    def _highlight(self, text):
        """ Apply syntax highlighting.
        """
        lines = []
        code = []
        for i, line in enumerate(text.splitlines()):
            if line.startswith("```"):
                if code:
                    formatter = HtmlFormatter()
                    try:
                        lexer = get_lexer_by_name(code[0])
                    except Exception:
                        lexer = get_lexer_by_name("text")
                    lines.append(
                        pygments.highlight("\n".join(code[1:]), lexer, formatter)
                    )
                    code = []
                else:
                    code.append(line[3:].strip())  # language
            elif code:
                code.append(line)
            else:
                lines.append(line)
        return "\n".join(lines).strip()

    def _split(self):
        """ Split the markdown into parts based on sections.
        Each part is either text or a tuple representing a section.
        """
        text = self.md
        self.parts = parts = []
        self.headers = headers = []
        lines = []

        # Split in parts
        for line in text.splitlines():
            if line.startswith(("# ", "## ", "### ", "#### ", "##### ")):
                # Finish pending lines
                parts.append("\n".join(lines))
                lines = []
                # Process header
                level = len(line.split(" ")[0])
                title = line.split(" ", 1)[1]
                title_short = "".join(c for c in title if ord(c) < 256).strip()
                while "<i" in title_short:
                    i1 = title_short.find("<i")
                    i2 = title_short.find("</i>", i1)
                    title_short = title_short[:i1] + title_short[i2+4:]
                title_short = title_short.split("(")[0].split("<")[0].strip().replace("`", "")
                headers.append((level, title_short))
                parts.append((level, title_short, title))
            else:
                lines.append(line)
        parts.append("\n".join(lines))

        # Now convert all text to html
        for i in range(len(parts)):
            if not isinstance(parts[i], tuple):
                parts[i] = markdown.markdown(parts[i], extensions=[]) + "\n\n"

    def to_html(self):
        htmlparts = []
        for part in self.parts:
            if isinstance(part, tuple):
                level, title_short, title = part
                title_html = (
                    title.replace("``", "`")
                    .replace("`", "<code>", 1)
                    .replace("`", "</code>", 1)
                )
                ts = title_short.lower().replace(" ", "-")
                if part[0] == 1:
                    htmlparts.append(f"<span class='post-date-tags'>{self.date}</span>")
                    htmlparts.append("<h1>%s</h1>" % title_html)
                elif part[0] == 2 and title_short:
                    htmlparts.append(
                        "<a class='anch' name='{}' href='#{}'>".format(ts, ts)
                    )
                    htmlparts.append("<h%i>%s</h%i>" % (level, title_html, level))
                    htmlparts.append("</a>")
                else:
                    htmlparts.append("<h%i>%s</h%i>" % (level, title_html, level))
            else:
                htmlparts.append(part)
        return "\n".join(htmlparts)


if __name__ == "__main__":
    main()
    # webbrowser.open(os.path.join(OUT_DIR, "index.html"))
