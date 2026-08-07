#!/usr/bin/env python3
"""Build the static site. Run:  python3 build.py

Edit the CONTENT section below to update the site, then re-run.
Every page shares the sidebar and nav defined in shell().
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

NAME = "Oluwatosin Akande"
ROLE = "PhD Candidate, Industrial and Systems Engineering"

# Profile links shown in the sidebar on every page.
# To add Google Scholar or ORCID later, just add a line here.
LINKS = [
    ("Email", "mailto:oaa323@lehigh.edu"),
    ("GitHub", "https://github.com/Akande-hub"),
    ("LinkedIn", "https://linkedin.com/in/tosin-akande-5b3994b9/"),
]

NAV = [
    ("Home", "index.html"),
    ("Research", "research.html"),
    ("Projects", "projects.html"),
    ("Talks", "talks.html"),
    ("Teaching &amp; Service", "teaching.html"),
    ("Awards", "awards.html"),
]


def shell(page_file, title, body):
    links = "\n".join(
        f'        <li><a href="{u}">{n}</a></li>' for n, u in LINKS
    )
    nav = "\n".join(
        '        <a href="{u}"{cls}>{n}</a>'.format(
            u=u, n=n, cls=' class="active"' if u == page_file else ""
        )
        for n, u in NAV
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} &middot; {NAME}</title>
<meta name="description" content="{NAME} - PhD candidate in Industrial and Systems Engineering at Lehigh University. Mathematical optimization, machine learning, inverse problems, and PDEs.">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="wrap">

  <aside class="sidebar">
    <img class="avatar" src="assets/avatar.jpg" alt="{NAME}">
    <h1>{NAME}</h1>
    <p class="role">{ROLE}</p>
    <div class="affil">
      <a href="https://engineering.lehigh.edu/ise">Industrial and Systems Engineering</a><br>
      Lehigh University<br>
      Bethlehem, PA, USA
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
      &copy; 2026 {NAME}
    </footer>
  </main>

</div>
</body>
</html>
"""


# ----------------------------------------------------------------------
# CONTENT
# ----------------------------------------------------------------------

HOME = """
    <h2 class="page-title">About</h2>

    <p class="lead">I'm a fourth-year PhD candidate in Industrial and Systems Engineering
    (<a href="https://engineering.lehigh.edu/ise">Lehigh ISE</a>) at Lehigh University,
    advised by Professor Akwum Onwunta. My research centres on mathematical optimization,
    machine learning, inverse problems, and partial differential equations.</p>

    <p>Before Lehigh, I earned a Master's degree in Mathematical Sciences from the African
    Institute for Mathematical Sciences (<a href="https://aims.ac.rw/">AIMS</a>) in Rwanda,
    and a Bachelor's degree in Pure and Applied Mathematics from Ladoke Akintola University
    of Technology (<a href="https://www.lautech.edu.ng/undergraduate-programmes">LAUTECH</a>)
    in Ogbomoso, Nigeria.</p>

    <p>I served as President of the
    <a href="https://www.linkedin.com/company/lehigh-informs-student-chapter/">Lehigh INFORMS
    Student Chapter</a> for 2025&ndash;2026, and as Vice President and Treasurer of the
    <a href="https://www.linkedin.com/company/nigerian-club-lehigh-university/">Lehigh University
    Graduate Association of Nigerian Students</a>.</p>

    <h3 class="section">Research Interests</h3>
    <p>Mathematical optimization &middot; Scientific computing &middot; Machine learning &middot;
    Inverse problems &middot; Medical image registration &middot; Partial differential equations</p>

    <h3 class="section">Selected Publications</h3>
""" + """
    <div class="entry">
      <span class="title">Deep learning methods for inverse problems using connections between
      proximal operators and Hamilton&ndash;Jacobi equations</span>
      <div class="authors"><span class="me">Oluwatosin Akande</span>, Gabriel P. Langlois, Akwum Onwunta</div>
      <div class="meta">Preprint, 2025 &middot;
      <a href="https://arxiv.org/abs/2512.23829">arXiv:2512.23829</a></div>
    </div>

    <div class="entry">
      <span class="title">Momentum-based minimization of the Ginzburg&ndash;Landau functional
      on Euclidean spaces and graphs</span>
      <div class="authors"><span class="me">Oluwatosin Akande</span>, Patrick Dondl, Kanan Gupta,
      Akwum Onwunta, Stephan Wojtowytsch</div>
      <div class="meta">Preprint, 2024 &middot;
      <a href="https://arxiv.org/abs/2501.00389">arXiv:2501.00389</a></div>
    </div>

    <p class="more"><a href="research.html">All publications &rarr;</a></p>

    <h3 class="section">Selected Projects</h3>

    <div class="project">
      <h4>Nonlinear Optimization</h4>
      <p>MATLAB implementations of line-search and trust-region methods, benchmarked on
      seven test problems with convergence plots and per-iteration logs.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/Nonlinear-Optimization">github.com/Akande-hub/Nonlinear-Optimization</a></div>
    </div>

    <div class="project">
      <h4>Home Credit Default Risk</h4>
      <p>Credit-default classification on a highly imbalanced dataset, with feature selection
      and metrics suited to class imbalance.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/Home-Credit-Default-Risk-ML">github.com/Akande-hub/Home-Credit-Default-Risk-ML</a></div>
    </div>

    <p class="more"><a href="projects.html">All projects &rarr;</a></p>
"""

RESEARCH = """
    <h2 class="page-title">Research</h2>

    <p class="lead">My work sits at the intersection of mathematical optimization,
    machine learning, and partial differential equations &mdash; in particular, optimization
    methods with provable guarantees and their application to inverse problems and imaging.</p>

    <h3 class="section">Research Interests</h3>
    <ul class="plain">
      <li>Mathematical optimization &mdash; first- and second-order methods, momentum, convergence theory</li>
      <li>Inverse problems &mdash; proximal methods, regularization, learned reconstruction</li>
      <li>Machine learning &mdash; optimization for learning, deep learning for scientific problems</li>
      <li>Partial differential equations and scientific computing</li>
      <li>Medical image registration</li>
    </ul>

    <h3 class="section">Publications &amp; Preprints</h3>

    <div class="entry">
      <span class="title">Deep learning methods for inverse problems using connections between
      proximal operators and Hamilton&ndash;Jacobi equations</span>
      <div class="authors"><span class="me">Oluwatosin Akande</span>, Gabriel P. Langlois, Akwum Onwunta</div>
      <div class="meta">Preprint, 2025 &middot;
      <a href="https://arxiv.org/abs/2512.23829">arXiv:2512.23829</a></div>
    </div>

    <div class="entry">
      <span class="title">Momentum-based minimization of the Ginzburg&ndash;Landau functional
      on Euclidean spaces and graphs</span>
      <div class="authors"><span class="me">Oluwatosin Akande</span>, Patrick Dondl, Kanan Gupta,
      Akwum Onwunta, Stephan Wojtowytsch</div>
      <div class="meta">Preprint, 2024 &middot;
      <a href="https://arxiv.org/abs/2501.00389">arXiv:2501.00389</a></div>
    </div>

    <h3 class="section">CV</h3>
    <p>A full CV is available on request &mdash; please
    <a href="mailto:oaa323@lehigh.edu">get in touch</a>.</p>
"""

PROJECTS = """
    <h2 class="page-title">Projects</h2>

    <p class="lead">Selected computational projects. Code for each is on
    <a href="https://github.com/Akande-hub">GitHub</a>.</p>

    <div class="project">
      <h4>Nonlinear Optimization <span class="tag">MATLAB</span></h4>
      <p>Implementations of line-search and trust-region methods for smooth nonlinear
      optimization &mdash; steepest descent, modified Newton, truncated Newton-CG,
      Cauchy-point, SR1, and Mor&eacute;&ndash;Sorensen solvers &mdash; benchmarked on seven
      test problems with convergence plots, per-iteration logs, and a written report.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/Nonlinear-Optimization">github.com/Akande-hub/Nonlinear-Optimization</a></div>
    </div>

    <div class="project">
      <h4>Home Credit Default Risk <span class="tag">Python</span></h4>
      <p>Credit-default classification on a reduced, highly imbalanced version of the Home
      Credit dataset, covering feature selection, categorical encoding, and evaluation
      metrics suited to class imbalance.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/Home-Credit-Default-Risk-ML">github.com/Akande-hub/Home-Credit-Default-Risk-ML</a></div>
    </div>

    <div class="project">
      <h4>Bike Sharing Demand Prediction <span class="tag">AutoGluon</span></h4>
      <p>Automated model training on AWS SageMaker to predict hourly bike-rental demand,
      including feature engineering, hyperparameter tuning, and Kaggle submission scoring.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/Udacity-Bike-Sharing">github.com/Akande-hub/Udacity-Bike-Sharing</a></div>
    </div>

    <div class="project">
      <h4>Coronary Heart Disease Risk <span class="tag">Python</span></h4>
      <p>Classification of coronary heart disease risk from clinical indicators on the
      South African heart-disease dataset.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/Coronary-Heart-Disease-Risk-SAheart-ML">github.com/Akande-hub/Coronary-Heart-Disease-Risk-SAheart-ML</a></div>
    </div>

    <div class="project">
      <h4>Scientific Computing in Python <span class="tag">Python</span></h4>
      <p>Numerical methods across ordinary differential equations, numerical linear algebra,
      data assimilation, data-driven optimization, and financial mathematics.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/Scientific-Computing-in-Python">github.com/Akande-hub/Scientific-Computing-in-Python</a></div>
    </div>

    <div class="project">
      <h4>Statistical Computing in R <span class="tag">R</span></h4>
      <p>Statistical machine learning, regression modelling and diagnostics, and methods for
      research design and analysis.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/Statistical-Computing-in-R">github.com/Akande-hub/Statistical-Computing-in-R</a></div>
    </div>
"""

TALKS = """
    <h2 class="page-title">Talks &amp; Conferences</h2>

    <h3 class="section">Invited &amp; Contributed Talks</h3>
    <ul class="plain">
      <li><span class="year">2025</span> <strong>Momentum-Based Optimization in Machine Learning.</strong>
      Rutgers University Industrial and Systems Engineering Research Collaboration, NJ, USA.</li>

      <li><span class="year">2024</span> <strong>Momentum-based minimization of the
      Ginzburg&ndash;Landau functional on Euclidean spaces and graphs.</strong>
      SIAM New York&ndash;New Jersey&ndash;Pennsylvania Section Conference,
      October 31 &ndash; November 2, Rochester Institute of Technology, NY, USA.</li>
    </ul>

    <h3 class="section">Conferences &amp; Visits</h3>
    <ul class="plain">
      <li><span class="year">2024</span> SIAM New York&ndash;New Jersey&ndash;Pennsylvania Section
      Conference, Rochester Institute of Technology, NY, USA.</li>

      <li><span class="year">2024</span> Modeling and Optimization: Theory and Applications
      (MOPTA), 14&ndash;16 August, Lehigh University, Bethlehem, PA, USA.</li>

      <li><span class="year">2024</span> Research visit, May&ndash;July,
      University of Utah, Salt Lake City, UT, USA.</li>

      <li><span class="year">2022</span> Data Science Workshop, African Institute for
      Mathematical Sciences (AIMS), Kigali, Rwanda.</li>
    </ul>
"""

TEACHING = """
    <h2 class="page-title">Teaching &amp; Service</h2>

    <h3 class="section">Teaching</h3>
    <ul class="plain">
      <li><span class="year">2025</span> <strong>Graduate Teaching Assistant</strong> &mdash;
      Optimization and Mathematical Foundations, Computer Science and Engineering,
      Lehigh University, PA, USA. (Summer)</li>

      <li><span class="year">2022&ndash;23</span> <strong>Assistant Lecturer</strong> &mdash;
      Mathematical Methods, Faculty of Computing Science,
      Dominion University Ibadan, Nigeria.</li>

      <li><span class="year">2020&ndash;21</span> <strong>Teaching Assistant</strong> &mdash;
      Elementary Mathematics I&ndash;III, Faculty of Computing Science,
      Dominion University Ibadan, Nigeria.</li>
    </ul>

    <h3 class="section">Service</h3>
    <ul class="plain">
      <li><span class="year">2025&ndash;26</span> President, Lehigh INFORMS Student Chapter,
      ISE Department, Lehigh University, Bethlehem, PA, USA.</li>

      <li><span class="year">2024&ndash;26</span> Vice President and Treasurer, Lehigh University
      Graduate Association of Nigerian Students, PA, USA.</li>

      <li><span class="year">2024</span> Volunteer, Graduate International Student Orientation,
      Lehigh University, Bethlehem, PA, USA.</li>

      <li><span class="year">2022</span> Volunteer, AIMS Teacher Training Partnership Program,
      Kigali, Rwanda.</li>

      <li><span class="year">2017&ndash;19</span> Welfare Officer and President, Mathematics
      Students Fellowship, Department of Mathematics, LAUTECH, Nigeria.</li>

      <li><span class="year">2017&ndash;18</span> Director of Studies, Christ Apostolic Youth
      Fellowship (CACYOF), LAUTECH, Nigeria.</li>

      <li><span class="year">2016&ndash;19</span> Volunteer, community development services and
      medical outreaches, CACYOF outreach programs, LAUTECH, Nigeria.</li>
    </ul>
"""

AWARDS = """
    <h2 class="page-title">Awards &amp; Honors</h2>

    <ul class="plain">
      <li><span class="year">2023</span> <strong>PC Rossin Fellowship</strong>, Department of
      Industrial and Systems Engineering, Lehigh University, USA.</li>

      <li><span class="year">2023</span> <strong>Google &amp; Facebook Scholarship Award (MSc)</strong>,
      African Masters of Machine Intelligence (AMMI), Senegal. <em>(declined)</em></li>

      <li><span class="year">2022</span> <strong>3rd Runner-Up, Accessible Healthcare</strong>,
      Microsoft Africa Development Center University Mentorship Program, Rwanda.</li>

      <li><span class="year">2021</span> <strong>Full Scholarship (MSc)</strong>, Next Einstein
      Initiative, African Institute for Mathematical Sciences (AIMS), Rwanda.</li>
    </ul>
"""

PAGES = [
    ("index.html", "Home", HOME),
    ("research.html", "Research", RESEARCH),
    ("projects.html", "Projects", PROJECTS),
    ("talks.html", "Talks", TALKS),
    ("teaching.html", "Teaching &amp; Service", TEACHING),
    ("awards.html", "Awards &amp; Honors", AWARDS),
]

if __name__ == "__main__":
    for fname, title, body in PAGES:
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as fh:
            fh.write(shell(fname, title, body))
        print("wrote", fname)
    # Tell GitHub Pages to serve these files as-is rather than run Jekyll.
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    print("wrote .nojekyll")
