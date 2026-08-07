# Akande-hub.github.io

Personal academic website for Oluwatosin Akande — https://akande-hub.github.io

## Editing

All content lives in `build.py`. Edit the text blocks near the bottom of that
file, then regenerate every page:

```
python3 build.py
```

This rewrites `index.html`, `research.html`, `projects.html`, `talks.html`,
`teaching.html`, and `awards.html`, keeping the sidebar and navigation
consistent across all of them.

- Profile links (Email, GitHub, LinkedIn, and any you add later such as
  Google Scholar or ORCID) are the `LINKS` list at the top of `build.py`.
- Navigation items are the `NAV` list.
- Styling is in `assets/style.css`.

`.nojekyll` tells GitHub Pages to serve these files directly instead of
running them through Jekyll.
