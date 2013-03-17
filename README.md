orgtblfilter
============

A simple SPHINX-extension to convert Emacs orgtbl-mode tables to
ReST-Grid-Tables.


Description
-----------

The minor-mode "orgtbl-mode" in Emacs is a very simple, yet powerful
way to create tables in documents.

However, it's syntax is slightly different from what SPHINX
expects. So by installing this extension and configuring it in
*conf.py* by appending "orgtblfilter" to the extensions-list, you can
simply write orgtbl-mode tables, but they come out nicely formatted.

Example:


    |------+--------+--------------------------------------------|
    | Key  | Type   | Description                                |
    |------+--------+--------------------------------------------|
    |------+--------+--------------------------------------------|
    | type | string | "file"                                     |
    |------+--------+--------------------------------------------|
    | path | string | Path to a recording of scanner data by the |
    |      |        | `FileFilter`                               |
    |------+--------+--------------------------------------------|


will become

    +------+--------+--------------------------------------------+
    | Key  | Type   | Description                                |
    +======+========+============================================+
    | type | string | "file"                                     |
    +------+--------+--------------------------------------------+
    | path | string | Path to a recording of scanner data by the |
    |      |        | `FileFilter`                               |
    +------+--------+--------------------------------------------+


Please note the conversion of double-delimiter/header lines to a
header-line in grid-table syntax.

