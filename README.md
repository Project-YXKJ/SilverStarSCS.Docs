# SilverStar-CSSM-Reference-Book



Documentation for SilverStar-CSSM

Built with [Sphinx](https://www.sphinx-doc.org/), and host on [Read the Docs](https://readthedocs.org/)

## Introduction

This is documentation of SilverStar's Control System for Sewing Machine, it is not written for a certain model product, but to explain the function, so here you can't find how to enter the setting interface or connection diagram of output and input ports.

This is an exploration of using Sphinx with Markdown.

Documentation is in the docs folder. It is published using Github pages, with a [github action](https://github.com/Project-YXKJ/SilverStar-CSSM-Reference-Book/blob/master/.github/workflows/main.yml).

https://serra.github.io/sphinx-with-markdown/

## Who need it?

Professionals who use the system.

## Build guide

### Setup

- 安装 Python
- 安装 Git

**Step 1.** 克隆本仓库, 创建虚拟环境(非必须, 但是建议)

[Installing packages using pip and virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

```bash
$ cd SilverStar-CSSM-Reference-Book
$ py -m venv env
```

### Activate virtual environment

**Step 2.** 激活虚拟环境, 并安装必要的包.

```bash
$ .\env\Scripts\activate
$ py -m pip install -r requirements.txt
```

### Render the documentation as HTML

**Step 3.** 输出本地 html, 打开 `docs/build/html/index.html` 查看

```bash
$ cd docs
$ make clean // 不是必须
$ make html
```

## Reference

[多语言](https://docs.readthedocs.io/en/stable/localization.html#projects-with-multiple-translations-sphinx-only)

[reStructuredText 语法参考](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)
