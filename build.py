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
LINKS = [
    ("Email", "mailto:oaa323@lehigh.edu"),
    ("Google Scholar", "https://scholar.google.com/citations?user=tNDgo-8AAAAJ&hl=en"),
    ("GitHub", "https://github.com/Akande-hub"),
    ("LinkedIn", "https://www.linkedin.com/in/akandeoluwatosin/"),
]

NAV = [
    ("Home", "index.html"),
    ("Experience", "experience.html"),
    ("Research", "research.html"),
    ("Projects", "projects.html"),
    ("Talks", "talks.html"),
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
    advised by Professor Akwum Onwunta. My dissertation, <em>PDEs and Machine Learning with
    Applications in Medical Imaging</em>, develops optimization and deep learning methods for
    inverse problems and imaging.</p>

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

    <h3 class="section">Education</h3>

    <div class="entry">
      <span class="title">Ph.D. in Industrial and Systems Engineering</span>
      <div class="meta">2023 &ndash; present &middot; Lehigh University, USA</div>
      <p>Advisor: Prof. Akwum Onwunta. Dissertation: <em>PDEs and Machine Learning with
      Applications in Medical Imaging</em>. Committee: Prof. Luis Nunes Vicente,
      Prof. Daniel P. Robinson, Prof. Andreas Mang.</p>
    </div>

    <div class="entry">
      <span class="title">M.Sc. in Mathematical Sciences</span>
      <div class="meta">2021 &ndash; 2022 &middot; African Institute for Mathematical Sciences, Rwanda</div>
      <p>Advisor: Prof. Dedunje Biatat V.A. Thesis: <em>Artificial Neural Networks Under
      Constraint</em>. Committee: Prof. Blaise Tchapnda, Prof. Marcellin Atemkeng.</p>
    </div>

    <div class="entry">
      <span class="title">B.Tech. in Pure and Applied Mathematics</span>
      <div class="meta">2013 &ndash; 2019 &middot; Ladoke Akintola University of Technology, Nigeria</div>
      <p>Grade: 4.52/5.0. First Class Honors.</p>
    </div>

    <h3 class="section">Research Interests</h3>
    <p>Mathematical optimization &middot; Scientific computing &middot; Machine learning &middot;
    Inverse problems &middot; Medical imaging &middot; Partial differential equations</p>

    <h3 class="section">Selected Publications</h3>

    <div class="entry">
      <span class="title">Deep learning methods for inverse problems using connections between
      proximal operators and Hamilton&ndash;Jacobi equations</span>
      <div class="authors"><span class="me">Oluwatosin Akande</span>, Gabriel P. Langlois, Akwum Onwunta</div>
      <div class="meta">Under second review at <em>SIAM Journal on Applied Mathematics</em>, 2025 &middot;
      <a href="https://arxiv.org/abs/2512.23829">arXiv:2512.23829</a></div>
    </div>

    <div class="entry">
      <span class="title">Momentum-based minimization of the Ginzburg&ndash;Landau functional
      on Euclidean spaces and graphs</span>
      <div class="authors"><span class="me">Oluwatosin Akande</span>, Patrick Dondl, Kanan Gupta,
      Akwum Onwunta, Stephan Wojtowytsch</div>
      <div class="meta">Under review at <em>Journal of Computational Physics</em>, 2024 &middot;
      <a href="https://arxiv.org/abs/2501.00389">arXiv:2501.00389</a></div>
    </div>

    <p class="more"><a href="research.html">All publications &rarr;</a></p>

    <h3 class="section">Ongoing Projects</h3>

    <div class="project">
      <h4>Learned Proximal Networks</h4>
      <p>Learning proximal operators directly with input-convex neural networks, and using
      the learned prior for reconstruction in inverse problems.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/learned-proximal-networks">github.com/Akande-hub/learned-proximal-networks</a></div>
    </div>

    <div class="project">
      <h4>Learned Proximal Networks for High-Dimensional Hamilton&ndash;Jacobi PDEs</h4>
      <p>Numerics for the SIAP revision: learning a convex potential whose gradient is the
      proximal operator, then recovering the prior without per-query inversion.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/lpn_for_nonconvex_control">github.com/Akande-hub/lpn_for_nonconvex_control</a></div>
    </div>

    <p class="more"><a href="projects.html">All projects &rarr;</a></p>
"""

EXPERIENCE = """
    <h2 class="page-title">Experience</h2>

    <h3 class="section">Research</h3>

    <div class="entry">
      <span class="title">Graduate Research Assistant &mdash;
      <a href="https://engineering.lehigh.edu/ise">Industrial and Systems Engineering</a>,
      Lehigh University</span>
      <div class="meta">2023 &ndash; present &middot; Advised by Prof. Akwum Onwunta</div>
      <p>My dissertation, <em>PDEs and Machine Learning with Applications in Medical Imaging</em>,
      develops optimization methods with provable guarantees and applies them to inverse
      problems and imaging. Current work learns proximal operators with input-convex neural
      networks and connects them to Hamilton&ndash;Jacobi equations, giving a route to
      reconstruction that avoids solving an optimization problem at every query. Earlier work
      analysed momentum-based minimization of the Ginzburg&ndash;Landau functional on
      Euclidean spaces and graphs.</p>
    </div>

    <div class="entry">
      <span class="title">Research Visit &mdash; Department of Mathematics, University of Utah</span>
      <div class="meta">May &ndash; June 2024 &middot; Salt Lake City, UT, USA</div>
    </div>

    <h3 class="section">Teaching</h3>

    <div class="entry">
      <span class="title">Teaching Assistant &mdash; DSCI 311: Optimization and Mathematical
      Foundations for Data Science</span>
      <div class="meta">Summer 2025, Summer 2026 &middot; Lehigh University, PA, USA</div>
      <ul class="plain tight">
        <li>Onboarded 40 master's students to the required class tools (Jupyter Notebooks,
        Google Colab, Slack, Git, and LaTeX) and provided technical troubleshooting and
        debugging support.</li>
        <li>Led two hours of weekly practice sessions plus an additional office hour.</li>
        <li>Prepared six major homework projects, implementing LaTeX/Overleaf protocols and
        standardizing version control for student submissions.</li>
        <li>Facilitated office hours and Slack discussions, resolving questions on
        optimization theory and debugging code in Google Colab.</li>
        <li>Graded assignments covering linear algebra, deterministic and stochastic
        optimization, and statistics, meeting compressed summer session deadlines.</li>
      </ul>
    </div>

    <div class="entry">
      <span class="title">Adjunct Lecturer &mdash; Dominion University, Nigeria</span>
      <div class="meta">Fall 2020, Spring 2021, Fall 2022, Spring 2023 &middot;
      Elementary Mathematics, Mathematical Methods, Advanced Calculus</div>
      <ul class="plain tight">
        <li>Instructed undergraduate students across three mathematics courses.</li>
        <li>Prepared lecture notes and graded all coursework, exams, and assessments.</li>
        <li>Mentored students needing additional support to bridge gaps in technical skills.</li>
        <li>Supervised two final-year student dissertations.</li>
      </ul>
    </div>

    <h3 class="section">Leadership &amp; Service</h3>
    <ul class="plain">
      <li><span class="year">2025&ndash;26</span> President,
      <a href="https://www.linkedin.com/company/lehigh-informs-student-chapter/">Lehigh INFORMS
      Student Chapter</a>, ISE Department, Lehigh University, Bethlehem, PA, USA.</li>

      <li><span class="year">2024&ndash;26</span> Vice President and Treasurer,
      <a href="https://www.linkedin.com/company/nigerian-club-lehigh-university/">Lehigh
      University Graduate Association of Nigerian Students</a>, PA, USA.</li>

      <li><span class="year">2024</span> Volunteer, Graduate International Student Orientation,
      Lehigh University, Bethlehem, PA, USA.</li>

      <li><span class="year">2022</span> Volunteer, AIMS Teacher Training Partnership Program,
      Kigali, Rwanda.</li>

      <li><span class="year">2017&ndash;19</span> Welfare Officer and President, Mathematics
      Students Fellowship, Department of Mathematics, LAUTECH.</li>

      <li><span class="year">2017&ndash;18</span> Director of Studies, Christ Apostolic Youth
      Fellowship (CACYOF), LAUTECH.</li>

      <li><span class="year">2016&ndash;19</span> Volunteer, free community development services
      and medical outreaches, CACYOF outreach programs, LAUTECH.</li>
    </ul>

    <h3 class="section">Reviewing</h3>
    <ul class="plain">
      <li>Lehigh Rising Scholars Journal (LRSJ)</li>
    </ul>

    <h3 class="section">Professional Affiliations</h3>
    <ul class="plain">
      <li><span class="year">2023&ndash;</span> Institute for Operations Research and the
      Management Sciences (INFORMS)</li>

      <li><span class="year">2023&ndash;</span> Society for Industrial and Applied Mathematics
      (SIAM)</li>
    </ul>

    <h3 class="section">Skills</h3>
    <ul class="plain">
      <li><strong>Programming</strong> &mdash; Python, R, MATLAB, SQL</li>
      <li><strong>ML &amp; data science</strong> &mdash; scikit-learn, PyTorch, TensorFlow,
      NumPy, pandas, SciPy</li>
      <li><strong>Optimization</strong> &mdash; Gurobi, MOSEK, FEniCS</li>
      <li><strong>Tools</strong> &mdash; Git, Docker, LaTeX</li>
    </ul>
"""

RESEARCH = """
    <h2 class="page-title">Research</h2>

    <p class="lead">My work sits at the intersection of mathematical optimization,
    machine learning, and partial differential equations &mdash; in particular, optimization
    methods with provable guarantees and their application to inverse problems and medical
    imaging.</p>

    <h3 class="section">Research Interests</h3>
    <ul class="plain">
      <li>Mathematical optimization &mdash; first- and second-order methods, momentum, convergence theory</li>
      <li>Inverse problems &mdash; proximal methods, regularization, learned reconstruction</li>
      <li>Machine learning &mdash; optimization for learning, deep learning for scientific problems</li>
      <li>Partial differential equations and scientific computing</li>
      <li>Medical imaging</li>
    </ul>

    <h3 class="section">Journal Publications</h3>

    <div class="entry">
      <span class="title">Deep learning methods for inverse problems using connections between
      proximal operators and Hamilton&ndash;Jacobi equations</span>
      <div class="authors"><span class="me">Oluwatosin Akande</span>, Gabriel P. Langlois, Akwum Onwunta</div>
      <div class="meta">Under second review at <em>SIAM Journal on Applied Mathematics</em>, 2025 &middot;
      <a href="https://arxiv.org/abs/2512.23829">arXiv:2512.23829</a></div>
    </div>

    <div class="entry">
      <span class="title">Momentum-based minimization of the Ginzburg&ndash;Landau functional
      on Euclidean spaces and graphs</span>
      <div class="authors"><span class="me">Oluwatosin Akande</span>, Patrick Dondl, Kanan Gupta,
      Akwum Onwunta, Stephan Wojtowytsch</div>
      <div class="meta">Under review at <em>Journal of Computational Physics</em>, 2024 &middot;
      <a href="https://arxiv.org/abs/2501.00389">arXiv:2501.00389</a></div>
    </div>

    <h3 class="section">Conference Publications</h3>

    <div class="entry">
      <span class="title">Methodological performance of data science in eco-sustainable
      design/engineering</span>
      <div class="authors"><span class="me">O. A. Akande</span>, A. M. Adeleye, A. T. Adeleye</div>
      <div class="meta">Proceedings of the 1st International Architectural Sciences and
      Applications Symposium (IArcSAS), 27&ndash;29 October 2021</div>
    </div>

    <h3 class="section">CV</h3>
    <p>A full CV is available on request &mdash; please
    <a href="mailto:oaa323@lehigh.edu">get in touch</a>. Publications are also listed on
    <a href="https://scholar.google.com/citations?user=tNDgo-8AAAAJ&amp;hl=en">Google Scholar</a>.</p>
"""

PROJECTS = """
    <h2 class="page-title">Projects</h2>

    <p class="lead">Code is on <a href="https://github.com/Akande-hub">GitHub</a>.</p>

    <h3 class="section">Ongoing</h3>

    <div class="project">
      <h4>Learned Proximal Networks <span class="tag">Python</span></h4>
      <p>Learning proximal operators directly with input-convex neural networks, and using
      the learned prior for reconstruction in inverse problems.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/learned-proximal-networks">github.com/Akande-hub/learned-proximal-networks</a></div>
    </div>

    <div class="project">
      <h4>Learned Proximal Networks for High-Dimensional Hamilton&ndash;Jacobi PDEs
      <span class="tag">Python</span></h4>
      <p>Numerics supporting the SIAP revision, building on
      <a href="https://openreview.net/pdf?id=kNPcOaqC5r">Fang, Buchanan and Sulam (ICLR 2024)</a>.
      The method learns a convex potential whose gradient is the proximal operator, then
      recovers the prior either by inverting that gradient per query or by fitting a second
      network &mdash; the latter matching a fully tuned inversion baseline without ever
      inverting.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/lpn_for_nonconvex_control">github.com/Akande-hub/lpn_for_nonconvex_control</a></div>
    </div>

    <h3 class="section">Other Projects</h3>

    <div class="project">
      <h4>Nonlinear Optimization <span class="tag">MATLAB</span></h4>
      <p>Implementations of line-search and trust-region methods for smooth nonlinear
      optimization &mdash; steepest descent, modified Newton, truncated Newton-CG,
      Cauchy-point, SR1, and Mor&eacute;&ndash;Sorensen solvers &mdash; benchmarked on seven
      test problems with convergence plots, per-iteration logs, and a written report.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/Nonlinear-Optimization">github.com/Akande-hub/Nonlinear-Optimization</a></div>
    </div>

    <div class="project">
      <h4>Scientific Computing in Python <span class="tag">Python</span></h4>
      <p>Numerical methods across ordinary differential equations, numerical linear algebra,
      data assimilation, data-driven optimization, and financial mathematics.</p>
      <div class="repo"><a href="https://github.com/Akande-hub/Scientific-Computing-in-Python">github.com/Akande-hub/Scientific-Computing-in-Python</a></div>
    </div>
"""

TALKS = """
    <h2 class="page-title">Talks &amp; Conferences</h2>

    <h3 class="section">Invited &amp; Contributed Talks</h3>
    <ul class="plain">
      <li><span class="year">2026</span> <strong>Deep learning methods for inverse problems
      using connections between proximal operators and Hamilton&ndash;Jacobi equations.</strong>
      INFORMS Annual Meeting, 1&ndash;4 November 2026, San Francisco, CA, USA.</li>

      <li><span class="year">2026</span> <strong>Deep learning methods for inverse problems
      using connections between proximal operators and Hamilton&ndash;Jacobi equations.</strong>
      Modeling and Optimization: Theory and Applications (MOPTA), 18&ndash;19 August 2026,
      Lehigh University, Bethlehem, PA, USA.</li>

      <li><span class="year">2025</span> <strong>Momentum-based optimization in machine
      learning.</strong> INFORMS Chapter Research Collaboration, 13 November 2025, Industrial
      and Systems Engineering Department, Rutgers University, NJ, USA.</li>

      <li><span class="year">2024</span> <strong>Momentum-based minimization of the
      Ginzburg&ndash;Landau functional on Euclidean spaces and graphs.</strong>
      SIAM New York&ndash;New Jersey&ndash;Pennsylvania Section Conference,
      1&ndash;3 November 2024, Rochester Institute of Technology, NY, USA.</li>

      <li><span class="year">2022</span> <strong>Time-series analysis using spectral and
      wavelet analysis.</strong> AIMS Week, 20 April 2022, African Institute for Mathematical
      Sciences, Kigali, Rwanda.</li>
    </ul>

    <h3 class="section">Participation</h3>
    <ul class="plain">
      <li><span class="year">2024</span> Modeling and Optimization: Theory and Applications
      (MOPTA), 14&ndash;16 August 2024, Lehigh University, Bethlehem, PA, USA.</li>

      <li><span class="year">2024</span> Research visit, May&ndash;June 2024, Department of
      Mathematics, University of Utah, Salt Lake City, UT, USA.</li>
    </ul>
"""

AWARDS = """
    <h2 class="page-title">Awards &amp; Honors</h2>

    <ul class="plain">
      <li><span class="year">2026</span> <strong>Travel Award ($500)</strong>, Rossin College
      Professional Development Program, Lehigh University.</li>

      <li><span class="year">2026</span> <strong>Travel Award ($650)</strong>, 2026 INFORMS
      Annual Meeting.</li>

      <li><span class="year">2026</span> <strong>Travel Award ($400)</strong>, 2026 Northeast
      Region Workshop on PDEs and Applied Mathematics.</li>

      <li><span class="year">2024</span> <strong>SIAM-NNP Travel Award ($350)</strong>,
      2024 SIAM New York&ndash;New Jersey&ndash;Pennsylvania Section Conference.</li>

      <li><span class="year">2023</span> <strong>Rossin College Doctoral Fellowship
      (Dean's Fellow)</strong>, P.C. Rossin College of Engineering, Lehigh University, USA.</li>

      <li><span class="year">2023</span> <strong>Google &amp; Facebook M.Sc. Fellowship</strong>,
      African Master's in Machine Intelligence (AMMI).</li>

      <li><span class="year">2021</span> <strong>M.Sc. Fully Funded Fellowship</strong>,
      African Institute for Mathematical Sciences (AIMS), Rwanda.</li>

      <li><span class="year">2019</span> <strong>First Class Honors Merit Award</strong>,
      Department of Pure and Applied Mathematics, Ladoke Akintola University of Technology,
      Nigeria.</li>
    </ul>
"""

PAGES = [
    ("index.html", "Home", HOME),
    ("experience.html", "Experience", EXPERIENCE),
    ("research.html", "Research", RESEARCH),
    ("projects.html", "Projects", PROJECTS),
    ("talks.html", "Talks", TALKS),
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
