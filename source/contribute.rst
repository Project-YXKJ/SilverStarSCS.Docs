.. |SS-SCS-Docs| replace:: SilverStar SCS Documentation

==================
Contribute to Docs
==================

The |SS-SCS-Docs| welcomes contributors! There are lots of ways to help out,
including:

* Reading the book and giving feedback
* Reviewing new contributions
* Revising existing content
* Writing new content
* Translate the book

Documentation types
===================

This project consists of four distinct documentation types with specific
purposes. The project aspires to follow the `Diátaxis process`_
for creating quality documentation. When proposing new additions to the project please pick the
appropriate documentation type.

.. _Diátaxis process: https://diataxis.fr/

Tutorials
---------

Tutorials are focused on teaching the reader new concepts by accomplishing a
goal. They are opinionated step-by-step guides. They do not include extraneous
warnings or information.

Guides
------

Guides are focused on accomplishing a specific task and can assume some level of
pre-requisite knowledge. These are similar to tutorials, but have a narrow and
clear focus and can provide lots of caveats and additional information as
needed. They may also discuss multiple approaches to accomplishing the task.

Explanations 
------------
Explanations are focused on understanding and information. These explore a
specific topic without a specific goal in mind.


Specifications
--------------

Specifications are reference documentation focused on comprehensively documenting
an product.


Translations
============

*TODO*

We use `Weblate`_ to manage translations of this project.
Please visit the `packaging.python.org`_ project on Weblate to contribute.

.. tip::

   Any translations of this project should follow `reStructuredText syntax`_.

.. _Weblate: https://weblate.org/
.. _packaging.python.org: https://hosted.weblate.org/projects/
.. _reStructuredText syntax: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Adding a language
-----------------

If your language is not listed on `packaging.python.org`_, click the button
:guilabel:`Start new translation` at the bottom of the language list and add
the language you want to translate.

Following reStructuredText syntax
---------------------------------

If you are not familiar with reStructuredText (RST) syntax, please read `this guide`_
before translating on Weblate.

**Do not translate the text in reference directly**

  When translating the text in reference, please do not translate them directly.

  | Wrong: Translate the following text directly:

  .. code-block:: rst

      `some ref`_ -> `TRANSLATED TEXT HERE`_

  | Right: Translate the following text with your own language and add the original reference:

  .. code-block:: rst

      `some ref`_ -> `TRANSLATED TEXT HERE <some ref_>`_

.. _this guide: https://docutils.sourceforge.io/docs/user/rst/quickref.html

Building the book locally
==========================

Though not required to contribute, it may be useful to build this docs locally
in order to test your changes. In order to build this docs locally, you'll
need:

1. `uv`_ is used for Python package and project manager.
2. `Nox`_ is used for automating development tasks.
   
   .. code-block:: bash

      uv tool install nox

To build the docs, run the following ``nox`` command in the project’s root folder:

.. code-block:: bash
   
   nox -rs docs

After the process has completed you can find the HTML output in the
``./build`` directory. You can open the ``index.html`` file to view the
docs in web browser.

.. _uv: https://docs.astral.sh/uv/
.. _Nox: https://nox.readthedocs.io/en/stable/

Style guide
===========

Audience
--------

The audience of this guide is anyone who uses SilverStar SCS product.

In particular, keep in mind that not all people who use SilverStar SCS see themselves
as developers. The audience of this document includes operators, maintenance personnel,
as well as professionals.

Voice and tone
--------------

When writing this guide, strive to write with a voice that's approachable and
humble, even if you have all the answers.

Imagine you're working on a project with someone you know to be smart and skilled.
You like working with them and they like working with you. That person
has asked you a question and you know the answer. How do you respond? *That* is
how you should write this guide.

When writing the guide, adjust your tone for the seriousness and difficulty of
the topic. If you're writing an introductory tutorial, it's OK to make a joke,
but if you're covering a sensitive specification, you might want to avoid jokes
altogether.

Conventions and mechanics
-------------------------

**Write to the reader**
  When giving recommendations or steps to take, address the reader as *you*
  or use the imperative mood.

  | Wrong: To install it, the user runs…
  | Right: You can install it by running…
  | Right: To install it, run…

**State assumptions**
  Avoid making unstated assumptions. Reading on the web means that any page of
  the book may be the first page of the book that the reader ever sees.
  If you're going to make assumptions, then say what assumptions that you're
  going to make.

**Cross-reference generously**
  The first time you mention a tool or practice, link to the part of the
  guide that covers it, or link to a relevant document elsewhere. Save the
  reader a search.

**Respect naming practices**
  When naming tools, sites, people, and other proper nouns, use their preferred
  capitalization.

  | Wrong: Pip uses…
  | Right: pip uses…
  |
  | Wrong: …hosted on github.
  | Right: …hosted on GitHub.

**Headings**
  Write headings that use words the reader is searching for. A good way to
  do this is to have your heading complete an implied question. For example, a
  reader might want to know *How do I install MyLibrary?* so a good heading
  might be *Install MyLibrary*.

  In section headings, use sentence case. In other words, write headings as you
  would write a typical sentence.

  | Wrong: Things You Should Know About Python
  | Right: Things you should know about Python

**Numbers**
  In body text, write numbers one through nine as words. For other numbers or
  numbers in tables, use numerals.

.. _contributors:

Contributions 
==============
Here is a list of the contributors who have worked on this. 
Big shout-out to them!

* Zhang XiaoLei `snowzxl <https://github.com/snowzxl>`_
* Xia Tian `xiatian-xjtu <https://github.com/xiatian-xjtu>`_
* Zhang YuPeng `yupeng-zhang <https://github.com/yupeng-zhang>`_
