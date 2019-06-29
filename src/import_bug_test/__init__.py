# -*- coding: utf-8 -*-

# Import Bug Test Add-on for Anki
#
# Copyright (C) 2019  Aristotelis P. <https://glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

"""
Module-level entry point for the add-on into Anki 2.0/2.1
"""

errors = []

try:
    from .abc import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("abc", repr(e)))

try:
    from .argparse import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("argparse", repr(e)))

try:
    from .ast import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("ast", repr(e)))

try:
    from .atexit import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("atexit", repr(e)))

try:
    from .audioop import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("audioop", repr(e)))

try:
    from .base64 import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("base64", repr(e)))

try:
    from .bdb import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("bdb", repr(e)))

try:
    from .binascii import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("binascii", repr(e)))

try:
    from .bisect import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("bisect", repr(e)))

try:
    from .bs4 import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("bs4", repr(e)))

try:
    from .builtins import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("builtins", repr(e)))

try:
    from .bz2 import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("bz2", repr(e)))

try:
    from .calendar import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("calendar", repr(e)))

try:
    from .cgi import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("cgi", repr(e)))

try:
    from .chunk import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("chunk", repr(e)))

try:
    from .cmd import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("cmd", repr(e)))

try:
    from .code import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("code", repr(e)))

try:
    from .codecs import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("codecs", repr(e)))

try:
    from .codeop import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("codeop", repr(e)))

try:
    from .collections import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("collections", repr(e)))

try:
    from .contextlib import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("contextlib", repr(e)))

try:
    from .copy import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("copy", repr(e)))

try:
    from .copyreg import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("copyreg", repr(e)))

try:
    from .csv import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("csv", repr(e)))

try:
    from .ctypes import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("ctypes", repr(e)))

try:
    from .datetime import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("datetime", repr(e)))

try:
    from .decorator import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("decorator", repr(e)))

try:
    from .difflib import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("difflib", repr(e)))

try:
    from .dis import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("dis", repr(e)))

try:
    from .distutils import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("distutils", repr(e)))

try:
    from .doctest import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("doctest", repr(e)))

try:
    from .dummy_threading import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("dummy_threading", repr(e)))

try:
    from .email import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("email", repr(e)))

try:
    from .encodings import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("encodings", repr(e)))

try:
    from .enum import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("enum", repr(e)))

try:
    from .errno import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("errno", repr(e)))

try:
    from .faulthandler import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("faulthandler", repr(e)))

try:
    from .fnmatch import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("fnmatch", repr(e)))

try:
    from .ftplib import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("ftplib", repr(e)))

try:
    from .functools import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("functools", repr(e)))

try:
    from .gc import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("gc", repr(e)))

try:
    from .genericpath import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("genericpath", repr(e)))

try:
    from .getopt import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("getopt", repr(e)))

try:
    from .getpass import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("getpass", repr(e)))

try:
    from .gettext import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("gettext", repr(e)))

try:
    from .glob import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("glob", repr(e)))

try:
    from .gzip import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("gzip", repr(e)))

try:
    from .hashlib import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("hashlib", repr(e)))

try:
    from .heapq import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("heapq", repr(e)))

try:
    from .hmac import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("hmac", repr(e)))

try:
    from .html import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("html", repr(e)))

try:
    from .http import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("http", repr(e)))

try:
    from .importlib import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("importlib", repr(e)))

try:
    from .inspect import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("inspect", repr(e)))

try:
    from .io import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("io", repr(e)))

try:
    from .ipaddress import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("ipaddress", repr(e)))

try:
    from .itertools import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("itertools", repr(e)))

try:
    from .json import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("json", repr(e)))

try:
    from .keyword import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("keyword", repr(e)))

try:
    from .linecache import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("linecache", repr(e)))

try:
    from .locale import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("locale", repr(e)))

try:
    from .logging import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("logging", repr(e)))

try:
    from .lzma import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("lzma", repr(e)))

try:
    from .markdown import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("markdown", repr(e)))

try:
    from .marshal import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("marshal", repr(e)))

try:
    from .math import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("math", repr(e)))

try:
    from .mimetypes import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("mimetypes", repr(e)))

try:
    from .netrc import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("netrc", repr(e)))

try:
    from .ntpath import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("ntpath", repr(e)))

try:
    from .nturl2path import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("nturl2path", repr(e)))

try:
    from .opcode import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("opcode", repr(e)))

try:
    from .operator import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("operator", repr(e)))

try:
    from .optparse import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("optparse", repr(e)))

try:
    from .os import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("os", repr(e)))

try:
    from .pdb import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("pdb", repr(e)))

try:
    from .pickle import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("pickle", repr(e)))

try:
    from .pkgutil import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("pkgutil", repr(e)))

try:
    from .platform import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("platform", repr(e)))

try:
    from .plistlib import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("plistlib", repr(e)))

try:
    from .posixpath import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("posixpath", repr(e)))

try:
    from .pprint import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("pprint", repr(e)))

try:
    from .py_compile import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("py_compile", repr(e)))

try:
    from .pyaudio import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("pyaudio", repr(e)))

try:
    from .pydoc import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("pydoc", repr(e)))

try:
    from .pydoc_data import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("pydoc_data", repr(e)))

try:
    from .pyexpat import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("pyexpat", repr(e)))

try:
    from .PyQt5 import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("PyQt5", repr(e)))

try:
    from .queue import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("queue", repr(e)))

try:
    from .quopri import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("quopri", repr(e)))

try:
    from .random import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("random", repr(e)))

try:
    from .re import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("re", repr(e)))

try:
    from .reprlib import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("reprlib", repr(e)))

try:
    from .requests import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("requests", repr(e)))

try:
    from .select import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("select", repr(e)))

try:
    from .selectors import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("selectors", repr(e)))

try:
    from .send2trash import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("send2trash", repr(e)))

try:
    from .shlex import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("shlex", repr(e)))

try:
    from .shutil import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("shutil", repr(e)))

try:
    from .signal import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("signal", repr(e)))

try:
    from .sip import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("sip", repr(e)))

try:
    from .socket import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("socket", repr(e)))

try:
    from .socketserver import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("socketserver", repr(e)))

try:
    from .sqlite3 import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("sqlite3", repr(e)))

try:
    from .sre_compile import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("sre_compile", repr(e)))

try:
    from .sre_constants import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("sre_constants", repr(e)))

try:
    from .sre_parse import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("sre_parse", repr(e)))

try:
    from .ssl import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("ssl", repr(e)))

try:
    from .stat import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("stat", repr(e)))

try:
    from .string import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("string", repr(e)))

try:
    from .stringprep import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("stringprep", repr(e)))

try:
    from .struct import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("struct", repr(e)))

try:
    from .subprocess import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("subprocess", repr(e)))

try:
    from .sys import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("sys", repr(e)))

try:
    from .tarfile import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("tarfile", repr(e)))

try:
    from .tempfile import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("tempfile", repr(e)))

try:
    from .textwrap import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("textwrap", repr(e)))

try:
    from .threading import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("threading", repr(e)))

try:
    from .time import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("time", repr(e)))

try:
    from .token import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("token", repr(e)))

try:
    from .tokenize import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("tokenize", repr(e)))

try:
    from .traceback import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("traceback", repr(e)))

try:
    from .tracemalloc import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("tracemalloc", repr(e)))

try:
    from .types import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("types", repr(e)))

try:
    from .unicodedata import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("unicodedata", repr(e)))

try:
    from .unittest import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("unittest", repr(e)))

try:
    from .urllib import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("urllib", repr(e)))

try:
    from .uu import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("uu", repr(e)))

try:
    from .uuid import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("uuid", repr(e)))

try:
    from .warnings import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("warnings", repr(e)))

try:
    from .wave import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("wave", repr(e)))

try:
    from .weakref import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("weakref", repr(e)))

try:
    from .webbrowser import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("webbrowser", repr(e)))

try:
    from .xml import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("xml", repr(e)))

try:
    from .zipfile import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("zipfile", repr(e)))

try:
    from .zipimport import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("zipimport", repr(e)))

try:
    from .zlib import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("zlib", repr(e)))

try:
    from .certifi import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("certifi", repr(e)))

try:
    from .chardet import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("chardet", repr(e)))

try:
    from .grp import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("grp", repr(e)))

try:
    from .idna import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("idna", repr(e)))

try:
    from .posix import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("posix", repr(e)))

try:
    from .pwd import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("pwd", repr(e)))

try:
    from .termios import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("termios", repr(e)))

try:
    from .tty import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("tty", repr(e)))

try:
    from .urllib3 import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("urllib3", repr(e)))

try:
    from .certifi import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("certifi", repr(e)))

try:
    from .chardet import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("chardet", repr(e)))

try:
    from .grp import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("grp", repr(e)))

try:
    from .idna import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("idna", repr(e)))

try:
    from .posix import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("posix", repr(e)))

try:
    from .pwd import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("pwd", repr(e)))

try:
    from .readline import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("readline", repr(e)))

try:
    from .termios import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("termios", repr(e)))

try:
    from .tty import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("tty", repr(e)))

try:
    from .urllib3 import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("urllib3", repr(e)))

try:
    from .msvcrt import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("msvcrt", repr(e)))

try:
    from .netbios import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("netbios", repr(e)))

try:
    from .nt import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("nt", repr(e)))

try:
    from .pywintypes import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("pywintypes", repr(e)))

try:
    from .win32api import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("win32api", repr(e)))

try:
    from .win32file import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("win32file", repr(e)))

try:
    from .win32pipe import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("win32pipe", repr(e)))

try:
    from .win32wnet import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("win32wnet", repr(e)))

try:
    from .winerror import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("winerror", repr(e)))

try:
    from .winreg import answer_to_life_universe_and_everything
except Exception as e:
    errors.append(("winreg", repr(e)))



####

from anki.hooks import addHook

if errors:
    def showDebugInfo():
        from aqt import mw
        from anki import version as anki_version
        from aqt.utils import showInfo, showText
        
        txt = """
    <h2>Bug Status: Affected</h2>

    <p>It seems like your system is affected by a module import bug.</p>

    <p>To report your findings, please copy the debug info below and post it 
    <a href="https://github.com/glutanimate/review-heatmap/issues/43">here</a>. 
    Feel free to uninstall "Import Bug Test" one you're done</p>

    <p>Thanks so much again for helping with squashing this bug!</p>

    <p><b>Debug info</b>:</p>
    """
        txt += "<div style='white-space: pre-wrap'>"
        
        if not anki_version.startswith("2.0"):
            from aqt.utils import supportText
            txt += "\n" + supportText() + "\n"
            txt += "Add-ons:\n\n" + repr(mw.addonManager.allAddons()) + "\n\n"
        else:
            from aqt import appVersion
            from aqt.qt import QT_VERSION_STR, PYQT_VERSION_STR
            txt += '<p>' + "Version %s" % appVersion + '\n'
            txt += ("Qt %s PyQt %s\n\n") % (QT_VERSION_STR, PYQT_VERSION_STR)
            txt += "Add-ons:\n\n" + repr(mw.addonManager.files()) + "\n\n"
            
        txt += "\n\n".join(error[0] + ":\n" + error[1] for error in errors)
        
        txt += "</div>"
        
        kwargs = dict(title="Import Bug Test", type="html")
        
        if not anki_version.startswith("2.0"):
            kwargs["copyBtn"] = True
        
        showText(txt, **kwargs)
        

else:
    def showDebugInfo():
        from aqt.utils import showInfo
        showInfo("It seems like everything is working fine.<br>"
                "Feel free to uninstall Import Bug Test!",
                title="Import Bug Test")

addHook("profileLoaded", showDebugInfo)
