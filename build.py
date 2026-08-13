#!/usr/bin/env python3
"""Build the static site from the YAML files in content/.

    python3 build.py

You should not normally need to run this by hand. Editing anything in content/
(through Pages CMS at app.pagescms.org, or directly on GitHub) triggers the
GitHub Action in .github/workflows/build.yml, which runs this script and commits
the regenerated HTML.

Text fields accept Markdown: **bold**, *italic*, and [links](https://example.com).
HTML entities such as &mdash; and &ndash; also work.
"""
import os
import yaml
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")

NAV = [
    ("Home", "index.html"),
    ("Experience", "experience.html"),
    ("Research", "research.html"),
    ("Projects", "projects.html"),
    ("Talks", "talks.html"),
    ("Awards", "awards.html"),
]

_md = markdown.Markdown(extensions=[])


def load(name):
    with open(os.path.join(CONTENT, name + ".yml"), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def md_inline(text):
    """Render Markdown but drop the wrapping <p> so it can sit inside a span."""
    if text is None:
        return ""
    html = _md.reset().convert(str(text).strip())
    if html.startswith("<p>") and html.endswith("</p>") and html.count("<p>") == 1:
        html = html[3:-4]
    return html


def md_block(text, indent="    "):
    """Render Markdown as one or more <p> blocks, indented to match the page."""
    if text is None:
        return ""
    html = _md.reset().convert(str(text).strip())
    lines = [indent + ln for ln in html.split("\n")]
    return "\n".join(lines)


def emphasise_name(text, site):
    """Wrap the site owner's name in <span class="me"> inside an author list.

    site.yml may list name_variants (e.g. "O. A. Akande") so abbreviated forms
    in a citation are highlighted too.
    """
    html = md_inline(text)
    names = [site["name"]] + list(site.get("name_variants") or [])
    for n in sorted(names, key=len, reverse=True):
        if n in html:
            return html.replace(n, '<span class="me">%s</span>' % n, 1)
    return html


def entry(title, meta=None, body=None):
    out = ['    <div class="entry">']
    out.append('      <span class="title">%s</span>' % title)
    if meta:
        out.append('      <div class="meta">%s</div>' % meta)
    if body:
        out.append(body)
    out.append("    </div>")
    return "\n".join(out)


def publication(pub, site):
    meta = md_inline(pub.get("venue"))
    if pub.get("link_url"):
        meta += ' &middot;\n      <a href="%s">%s</a>' % (pub["link_url"], pub["link_label"])
    return "\n".join([
        '    <div class="entry">',
        '      <span class="title">%s</span>' % md_inline(pub["title"]),
        '      <div class="authors">%s</div>' % emphasise_name(pub["authors"], site),
        '      <div class="meta">%s</div>' % meta,
        "    </div>",
    ])


def project(proj, key="description", show_tag=True):
    tag = ' <span class="tag">%s</span>' % proj["tag"] if (show_tag and proj.get("tag")) else ""
    return "\n".join([
        '    <div class="project">',
        "      <h4>%s%s</h4>" % (proj["name"], tag),
        "      <p>%s</p>" % md_inline(proj.get(key) or proj["description"]),
        '      <div class="repo"><a href="%s">%s</a></div>'
        % (proj["repo"], proj["repo"].replace("https://", "")),
        "    </div>",
    ])


def year_list(items, year_key="year", text_key="text"):
    out = ['    <ul class="plain">']
    for it in items:
        yr = it.get(year_key)
        prefix = '<span class="year">%s</span> ' % yr if yr else ""
        out.append("      <li>%s%s</li>" % (prefix, md_inline(it[text_key])))
    out.append("    </ul>")
    return "\n".join(out)


def section(title):
    return '    <h3 class="section">%s</h3>' % title


def page_title(title):
    return '    <h2 class="page-title">%s</h2>' % title


def shell(site, page_file, title, body):
    links = "\n".join(
        '        <li><a href="%s">%s</a></li>' % (l["url"], l["label"])
        for l in site["links"]
    )
    nav = "\n".join(
        '        <a href="%s"%s>%s</a>' % (u, ' class="active"' if u == page_file else "", n)
        for n, u in NAV
    )
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} &middot; {name}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="wrap">

  <aside class="sidebar">
    <img class="avatar" src="assets/avatar.jpg" alt="{name}">
    <h1>{name}</h1>
    <p class="role">{role}</p>
    <div class="affil">
      <a href="{dept_url}">{dept}</a><br>
      {university}<br>
      {location}
    </div>
    <ul class="links">
{links}
    </ul>
  </aside>

  <main class="main">
    <nav class="top">
{nav}
    </nav>

{body}

    <footer class="site">
      &copy; {year} {name}
    </footer>
  </main>

</div>
</body>
</html>
""".format(
        title=title, name=site["name"], desc=site["meta_description"].strip(),
        role=site["role"], dept_url=site["department_url"], dept=site["department"],
        university=site["university"], location=site["location"],
        links=links, nav=nav, body=body, year=site["footer_year"],
    )


# ----------------------------------------------------------------------
# Page bodies
# ----------------------------------------------------------------------

def build_home(site, home, research, projects):
    about = md_block(home["about"]).replace("<p>", '<p class="lead">', 1)
    p = [page_title("About"), "", about, ""]

    p.append(section("Education"))
    p.append("")
    for e in home["education"]:
        body = "      <p>%s</p>" % md_inline(e["detail"]) if e.get("detail") else None
        p.append(entry(e["degree"], e.get("meta"), body))
        p.append("")

    p.append(section("Research Interests"))
    p.append("    <p>%s</p>" % md_inline(home["interests"]))
    p.append("")

    n = int(home.get("selected_publications", 2))
    if n:
        p.append(section("Selected Publications"))
        p.append("")
        for pub in research["journal"][:n]:
            p.append(publication(pub, site))
            p.append("")
        p.append('    <p class="more"><a href="research.html">All publications &rarr;</a></p>')
        p.append("")

    m = int(home.get("selected_projects", 2))
    if m:
        p.append(section("Ongoing Projects"))
        p.append("")
        for proj in projects["ongoing"][:m]:
            p.append(project(proj, key="short_description", show_tag=False))
            p.append("")
        p.append('    <p class="more"><a href="projects.html">All projects &rarr;</a></p>')

    return "\n".join(p).rstrip()


def build_experience(site, exp):
    p = [page_title("Experience"), ""]

    p.append(section("Research"))
    p.append("")
    for r in exp["research"]:
        body = "      <p>%s</p>" % md_inline(r["detail"]) if r.get("detail") else None
        p.append(entry(md_inline(r["title"]), r.get("meta"), body))
        p.append("")

    p.append(section("Teaching"))
    p.append("")
    for t in exp["teaching"]:
        bullets = None
        if t.get("bullets"):
            lines = ['      <ul class="plain tight">']
            lines += ["        <li>%s</li>" % md_inline(b) for b in t["bullets"]]
            lines.append("      </ul>")
            bullets = "\n".join(lines)
        p.append(entry(md_inline(t["title"]), t.get("meta"), bullets))
        p.append("")

    p.append(section("Leadership &amp; Service"))
    p.append(year_list(exp["service"]))
    p.append("")

    p.append(section("Reviewing"))
    p.append('    <ul class="plain">')
    p += ["      <li>%s</li>" % md_inline(r) for r in exp["reviewing"]]
    p.append("    </ul>")
    p.append("")

    p.append(section("Professional Affiliations"))
    p.append(year_list(exp["affiliations"]))
    p.append("")

    p.append(section("Skills"))
    p.append('    <ul class="plain">')
    for s in exp["skills"]:
        p.append("      <li><strong>%s</strong> &mdash; %s</li>" % (s["label"], s["items"]))
    p.append("    </ul>")

    return "\n".join(p).rstrip()


def build_research(site, research):
    p = [page_title("Research"), "", md_block(research["intro"]).replace("<p>", '<p class="lead">', 1), ""]

    p.append(section("Research Interests"))
    p.append('    <ul class="plain">')
    p += ["      <li>%s</li>" % md_inline(i) for i in research["interests"]]
    p.append("    </ul>")
    p.append("")

    p.append(section("Journal Publications"))
    p.append("")
    for pub in research["journal"]:
        p.append(publication(pub, site))
        p.append("")

    if research.get("conference"):
        p.append(section("Conference Publications"))
        p.append("")
        for pub in research["conference"]:
            p.append(publication(pub, site))
            p.append("")

    p.append(section("CV"))
    p.append("    <p>%s</p>" % md_inline(research["cv_note"]))
    return "\n".join(p).rstrip()


def build_projects(site, projects):
    p = [page_title("Projects"), "",
         '    <p class="lead">%s</p>' % md_inline(projects["intro"]), ""]
    p.append(section("Ongoing"))
    p.append("")
    for proj in projects["ongoing"]:
        p.append(project(proj))
        p.append("")
    p.append(section("Other Projects"))
    p.append("")
    for proj in projects["other"]:
        p.append(project(proj))
        p.append("")
    return "\n".join(p).rstrip()


def build_talks(site, talks):
    p = [page_title("Talks &amp; Conferences"), ""]
    p.append(section("Invited &amp; Contributed Talks"))
    p.append('    <ul class="plain">')
    for t in talks["talks"]:
        p.append('      <li><span class="year">%s</span> <strong>%s</strong> %s</li>'
                 % (t["year"], md_inline(t["title"]), md_inline(t["venue"])))
    p.append("    </ul>")
    p.append("")
    p.append(section("Participation"))
    p.append(year_list(talks["participation"]))
    return "\n".join(p).rstrip()


def build_awards(site, awards):
    return "\n".join([page_title("Awards &amp; Honors"), "", year_list(awards["awards"])]).rstrip()


def main():
    site = load("site")
    home, exp = load("home"), load("experience")
    research, projects = load("research"), load("projects")
    talks, awards = load("talks"), load("awards")

    pages = [
        ("index.html", "Home", build_home(site, home, research, projects)),
        ("experience.html", "Experience", build_experience(site, exp)),
        ("research.html", "Research", build_research(site, research)),
        ("projects.html", "Projects", build_projects(site, projects)),
        ("talks.html", "Talks", build_talks(site, talks)),
        ("awards.html", "Awards &amp; Honors", build_awards(site, awards)),
    ]
    for fname, title, body in pages:
        with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as fh:
            fh.write(shell(site, fname, title, body))
        print("wrote", fname)
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print("wrote .nojekyll")


if __name__ == "__main__":
    main()
