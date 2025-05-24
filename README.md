# docs
documentation website for the STEMAIDE kit. It guides you on how to build projects with the STEMAIDE kit.
# 📖 Project Documentation

Welcome to the official documentation site for the STEMAIDE kit! Built using [MkDocs](https://www.mkdocs.org/) and styled with the beautiful [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Docs Locally](#running-the-docs-locally)
- [Building Static Files](#building-static-files)
- [Deployment](#deployment)
- [Directory Structure](#directory-structure)
- [License](#license)

---

## 📌 About

This repository contains the technical documentation for the STEMAIDE kit. It is meant to guide developers, users, and contributors through setup, usage, and contribution guidelines.

---

## ✨ Features

- Built with [MkDocs](https://www.mkdocs.org/)
- Beautiful [Material Theme](https://squidfunk.github.io/mkdocs-material/)
- Fast local preview
- Static site generation
- Easy deployment to GitHub Pages

---

## ✅ Requirements

- Python 3.7+
- `pip` installed (Python package manager)
- Git (optional for GitHub deployment)

---

## ⚙️ Installation

Clone the repository (if not already done):

```bash
git clone https://github.com/your-username/your-docs-repo.git
cd your-docs-repo
```

### Install MkDocs and Material theme
```bash
pip install mkdocs mkdocs-material
```

## ▶️ Running the Docs Locally
- Use the following command to start a local server
```bash
mkdocs serve
```
- Your site will be available at: http://127.0.0.1:8000
Any changes you make in the `docs/` folder will auto-refresh in the browser.

## 🛠 Building Static Files
- To generate a static version of the documentation:
```bash
mkdocs build
```
- The static site will be built into the `site/` directory.

## 🚀 Deployment (GitHub Pages)

- To deploy the docs to GitHub Pages:

1. Ensure mkdocs.yml is configured with your site name and repo URL.

2. Run:
```bash
mkdocs gh-deploy
```
- This will push the site to the `gh-pages` branch of your repository.

## 📁 Directory Structure
```pgsql
.
├── docs/
│   ├── index.md
│   └── other-docs.md
├── mkdocs.yml
├── site/ (auto-generated after build)
└── README.md
```

## 📄 License
This project is licensed under the MIT License.