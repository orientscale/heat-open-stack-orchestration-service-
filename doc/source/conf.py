# -*- coding: utf-8 -*-
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# Heat documentation build configuration file, created by
# sphinx-quickstart on Thu Dec 13 11:23:35 2012.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import glob
import os
import sys
import tempfile

from oslo_config import cfg

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
CONTRIB_DIR = os.path.join(ROOT, 'contrib')
PLUGIN_DIRS = glob.glob(os.path.join(CONTRIB_DIR, '*'))
ENV_DIR = os.path.join(ROOT, "etc", "heat", "environment.d")
TEMP_ENV_DIR = tempfile.mkdtemp()

for f in glob.glob(os.path.join(ENV_DIR, "*.yaml")):
    with open(f, "r") as fin:
        name = os.path.split(f)[-1]
        with open(os.path.join(TEMP_ENV_DIR, name), "w") as fout:
            fout.write(fin.read().replace("file:///", "file://%s/" % ROOT))

sys.path.insert(0, ROOT)
sys.path.insert(0, BASE_DIR)

cfg.CONF.import_opt('plugin_dirs', 'heat.common.config')
cfg.CONF.set_override(name='plugin_dirs', override=PLUGIN_DIRS)

cfg.CONF.import_opt('environment_dir', 'heat.common.config')
cfg.CONF.set_override(name='environment_dir', override=TEMP_ENV_DIR)

# This is required for ReadTheDocs.org, but isn't a bad idea anyway.
os.environ['DJANGO_SETTINGS_MODULE'] = 'openstack_dashboard.settings'

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.intersphinx',
              'sphinx.ext.doctest',
              'sphinxcontrib.apidoc',
              'openstackdocstheme',
              'oslo_config.sphinxconfiggen',
              'oslo_config.sphinxext',
              'oslo_policy.sphinxext',
              'oslo_policy.sphinxpolicygen',
              'ext.resources',
              'ext.tablefromtext',
              'stevedore.sphinxext']

intersphinx_mapping = {
    'types_typedecorator': ('https://docs.sqlalchemy.org', None),
}

# policy sample file generation
policy_generator_config_file = '../../etc/heat/heat-policy-generator.conf'
sample_policy_basename = '_static/heat'

# oslo_config.sphinxconfiggen options
config_generator_config_file = '../../config-generator.conf'
sample_config_basename = '_static/heat'

# openstackdocstheme options
openstackdocs_repo_name = 'openstack/heat'
openstackdocs_pdf_link = True
openstackdocs_use_storyboard = True

todo_include_todos = True

# openstackdocstheme external link helper projects
openstackdocs_projects = [
    'devstack',
    'diskimage-builder',
    'keystone',
    'keystoneauth',
    'nova',
    'oslo.reports',
    'python-barbicanclient',
    'python-heatclient',
    'python-openstackclient',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
copyright = u'(c) 2012- Heat Developers'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['**/#*', '**~', '**/#*#']

# The reST default role (used for this markup: `text`)
# to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'native'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['heat.']

primary_domain = 'py'
nitpicky = False


# -- Options for API documentation  -------------------------------------------

apidoc_module_dir = '../../heat'
apidoc_separate_modules = True
apidoc_excluded_paths = [
    'cmd',
    'cloudinit',
    'db/sqlalchemy/migrations/versions',
    'engine/resources/aws',
    'engine/resources/openstack',
    'hacking',
    'httpd',
    'locale',
    'tests',
    'version.py',
]


# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme_path = ['.']
# html_theme = '_theme'
html_theme = 'openstackdocs'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {"sidebar_mode": "toc"}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any paths that contain "extra" files, such as .htaccess or
# robots.txt.
html_extra_path = ['_extra']

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Heatdoc'


# -- Options for LaTeX output -------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual])
latex_documents = [
    ('index', 'doc-heat.tex', u'Heat Documentation',
     u'Heat Developers', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = False

# Disable usage of xindy https://bugzilla.redhat.com/show_bug.cgi?id=1643664
latex_use_xindy = False

latex_elements = {
    'makeindex': '',
    'printindex': '',
    'preamble': r'\setcounter{tocdepth}{3}',
}

# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('man/heat-api', 'heat-api',
     u'REST API service to the heat project.',
     [u'Heat Developers'], 1),
    ('man/heat-api-cfn', 'heat-api-cfn',
     u'CloudFormation compatible API service to the heat project.',
     [u'Heat Developers'], 1),
    ('man/heat-db-setup', 'heat-db-setup',
     u'Command line utility to setup the Heat database',
     [u'Heat Developers'], 1),
    ('man/heat-engine', 'heat-engine',
     u'Service which performs the actions from the API calls made by the user',
     [u'Heat Developers'], 1),
    ('man/heat-keystone-setup', 'heat-keystone-setup',
     u'Script which sets up keystone for usage by Heat',
     [u'Heat Developers'], 1),
    ('man/heat-keystone-setup-domain', 'heat-keystone-setup-domain',
     u'Script which sets up a keystone domain for heat users and projects',
     [u'Heat Developers'], 1),
    ('man/heat-manage', 'heat-manage',
     u'Script which helps manage specific database operations',
     [u'Heat Developers'], 1),
    ('man/heat-status', 'heat-status',
     u'Script to check status of Heat deployment.',
     [u'Heat Developers'], 1),

]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'Heat', u'Heat Documentation',
     u'Heat Developers', 'Heat', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'
