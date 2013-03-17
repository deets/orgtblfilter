from orgtblfilter import is_separator, is_body, group_input, rewrite

def is_separator():
    for line, result in [
        ("|------|", 8),
        ("foobarbaz", 0),
        ("|--+--|\r\n", 7),
        ]:
        assert is_separator(line) == result, (line, result)


def test_body_classification():
    for line, size, result in [
        ("|-+-|", 5, True),
        ("     ", 5, False),
        ("|-+--|\r\n", 6, True),
        ]:
        assert is_body(line, size) == result, (line, size, result)


def test_input_grouping():
    lines = """This is a demo text

After a newline, another newline comes and then a simple table

|------+--------+--------------------------------|
| Key  | Type   | Description                    |
|------+--------+--------------------------------|
| ip   | string | IP-address of the ROD4 scanner |
| port | int    | Port of the ROD4 scanner       |
|------+--------+--------------------------------|

Again a newline.""".split("\n")
    groups = list(group_input(lines))
    assert len(groups) == 3, groups
    


def test_rewriting():
    input_text = """This is a demo text

After a newline, another newline comes and then a simple table

|------+--------+--------------------------------|
| Key  | Type   | Description                    |
|------+--------+--------------------------------|
| ip   | string | IP-address of the ROD4 scanner |
| port | int    | Port of the ROD4 scanner       |
|------+--------+--------------------------------|

Again a newline."""


    expected = """This is a demo text

After a newline, another newline comes and then a simple table

+------+--------+--------------------------------+
| Key  | Type   | Description                    |
+------+--------+--------------------------------+
| ip   | string | IP-address of the ROD4 scanner |
| port | int    | Port of the ROD4 scanner       |
+------+--------+--------------------------------+

Again a newline."""

    
    output_text = rewrite(input_text)
    assert output_text == expected, output_text
    


def test_header_rewriting():
    input_text = """This is a demo text

After a newline, another newline comes and then a simple table

|------+--------+--------------------------------|
| Key  | Type   | Description                    |
|------+--------+--------------------------------|
|------+--------+--------------------------------|
| ip   | string | IP-address of the ROD4 scanner |
| port | int    | Port of the ROD4 scanner       |
|------+--------+--------------------------------|

Again a newline."""


    expected = """This is a demo text

After a newline, another newline comes and then a simple table

+------+--------+--------------------------------+
| Key  | Type   | Description                    |
+======+========+================================+
| ip   | string | IP-address of the ROD4 scanner |
| port | int    | Port of the ROD4 scanner       |
+------+--------+--------------------------------+

Again a newline."""

    
    output_text = rewrite(input_text)
    assert output_text == expected, output_text
    
