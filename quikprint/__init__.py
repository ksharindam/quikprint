"""
Name = quikprint
Executable Command = quikprint
Package Name = quikprint
Python Module Name = quikprint
Debian Dependency = python3-pyqt5, cups
Description = Simple Qt frontend of Printing command lp
Changes :
v3.0    migrated from PyQt4 to PyQt5
v2.13   added : 4R (bordered) papersize to Brother_Inkjet
v2.12   fixed : Photo paper could not be set on Brother_Inkjet (USB)
v2.11   added : A6 paper size for HP Deskjet
v2.10   added : reverse page order button, removed all pages button
v2.9    added : brother inkjet printers support
v2.8    first page will be on top if all pages are printed
v2.7    collates copies if multiple copies are printed
v2.6    rangeEdit is focused after range button is clicked
v2.5    custom pagesize is remembered
v2.4    legal size paper added
v2.3    window height decreased
v2.2    bottom margin decreased
v2.1    button icons added
v2.0    ported to python3
v1.3    fixed : crash at startup if no printer added
v1.2    Selects filenames when not provided via cmdline args
        Even and odd pages icons added
...........................................................................
|   Copyright (C) 2019-2022 Arindam Chaudhuri <ksharindam@gmail.com>       |
|                                                                          |
|   This program is free software: you can redistribute it and/or modify   |
|   it under the terms of the GNU General Public License as published by   |
|   the Free Software Foundation, either version 3 of the License, or      |
|   (at your option) any later version.                                    |
|                                                                          |
|   This program is distributed in the hope that it will be useful,        |
|   but WITHOUT ANY WARRANTY; without even the implied warranty of         |
|   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          |
|   GNU General Public License for more details.                           |
|                                                                          |
|   You should have received a copy of the GNU General Public License      |
|   along with this program.  If not, see <http://www.gnu.org/licenses/>.  |
...........................................................................
"""
#TODO :
#      validate page range
#      reverse button should become unchecked when page set or range is changed

__version__ = '3.0'

