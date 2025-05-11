# cvstool
The csvtool reads CSV data (or sometimes Excel data) and output's corresponding
CSV (by default) data (possibly using a different CSV dialect), shell variable
assignments, or ASCII table format.

## USAGE
Form 1: csvtool [OPTIONS] [value-1 ... value-n]<br>
Input MUST be formatted as parsable CSV.

Form 2: csvtool --infmt=excel [--worksheet=WORKSHEET] [OPTIONS] [value-1 ... value-n]<br>
Input MUST be an Excel spreadsheet. The first worksheet will be used unless named.

Form 3: csvtool --infmt=shell [OPTIONS] [value-1 ... value-n]<br>
Input MUST be lines of shell-escaped and -quoted values.

This command reads data from standard input in either CSV (by default), Excel,
or shell format and writes it to standard output as CSV (by default), shell, or
either of two tabular formats: table and markdown. The CSV dialects used for
reading and writing needn't be the same and can be specified using the
--reader (in the case of Form 1) and --writer options.

Regardless of which usage form is used, any data values given as command
line arguments supply a row of data that will be appear as the first
line of output. This is typically used to output column headings, (e.g.:
`'First name' Last\ name email account zipcode`), but it could just as
easily be a row of actual data. Just in case it's not obvious, any data
given on the command line in this way is not CSV-formatted. It is parsed
by your shell, so use proper escapes and quoting to distinguish one
argument (data value) from another.

The output format defaults to CSV (--outfmt=csv), but it can also be set to
shell, table, or markdown. If shell, each line of output is a list of
environment variable assignments separated by semicolons. This REQUIRES the
first line of input data to consist of column headings that are also valid
environment variable names. If --outfmt=table is used, consider using
--headings 1 (or 2 or whatever) to say how many lines of input should be
treated as column headings. (The default is 0.) "-box" (the default) or
"-ascii" can also be appended to "table" to determine whether box-drawing
characters or normal ASCII characters are used to separate one column from
another and heading rows from data rows. --outfmt=markdown is just like table
output, but output is Markdown-formatted.

## FIELDSPEC Syntax
A FIELDSPEC is made up of one or more ranges separated by commas. Each
range is one of "N" (the Nth field), "N-" (from the Nth to the last
field), or "N-M" (from the Nth to the Mth field, inclusive). Fields are
counted beginning with 1.

positional arguments:
* args:                 See the usage forms above. Command line arguments' meanings depend on what form
                        is being used.

options:
* --join JOINSPEC:      Join the given field range into a single field separated by a single character.
                        The first character of the JOINSPEC value is the field separator. The remainder
                        of JOINSPEC is the same field range syntax (FIELDSPEC) described below. Also,
                        --join renumbers fields as they are joined. So if `--join ' 1-2'` is given,
                        fields 1 and 2 are joined as field 1, and any subsequent fields are renumbered
                        beginning with 2. This is important to remember if you're also using the --keep
                        option because --keep is evaluated after --join.
* --lambda FUNC:        Give a lambda expression (minus the "lambda" keyword) accepting two arguments,
                        row number (starting with 1) and row (as a list). The function must return
                        either the row, possibly modified, or None, in which case the current row is
                        discarded entirely, and processing continues with the new row.
* --keep FIELDSPEC:     Output only these fields. See the **FIELDSPEC Syntax** section below. By default,
                        all fields are kept (of course).
* --headings N:         Set how many rows (lines) of heading data are in the input. (default: 0)
* --infmt {csv,excel,shell}: Set the input format. See the usage and description above for details.
                        (default: 'csv')
* --reader DIALECT:      Set the CSV reader's dialect. See **CSV Dialect Syntax** below. (default:
                        ',"BMT\\FF'
* --outfmt OUTFMT:       Set either csv, shell, table, table-ascii, table-box, table-nosep, or markdown
                        as the output format. See the usage and description above for details.
                        (default: 'csv')
* --writer DIALECT:      Set the CSV writer's dialect. See **CSV Dialect Syntax*** below. (default:
                        ',"BMT\\FF')
* --worksheet NAME_or_NUMBER: Give the name or number (starting with 0) of the worksheet to read if --excel
                        was used. If not given, the first worksheet will be read.
* --debug:              Turn on debugging output.
* --test:               Run internal tests (for debugging purposes only).
* --help, -h:           Show this help message and exit.

## CSV Dialect Syntax
CSV formatting is a loose standard with dialectic flexability. These are
the parameters involved:

* SEP: Field separator character. (default: ,)
* Q: Quote character. (default: ")
* END: Line ending. This can be C for carraige return (\r), N for
  newline (\n), or B for both (\r\n). L for linefeed is the same
  as N for newline (\n). Any other character is taken litterally
  and will be interpreted as end-of-line in an input file and will
  terminate each row written to an output file.
* QSTYLE: Quoting style. One of 'A' (all), 'M' (minimal, the default),
 'N' (non-numeric), or 'X' (none).
* DQUOTE: Represent a literal quote as two consecutive quotes. Either
  'T' (for True, the default) or 'F' (for False).
* ESC: The escape charater, which makes the next character a literal
  Use 'N' for no escaping. (default: None)
* SKIPWS: Skip whitespace immediately following a field separator. Either
  'T' (for True, the default) or 'F' (for False).
* STRICT: Raise exceptions on any little problem with the data. Either 'T'
  (for True) or 'F' (for False, the default).

The syntax of the string is SEP[Q[END[QSTYLE[DQUOTE[ESC[SKIPWS[STRICT]]]]]]].
Any values you don't specify take their default values. The default dialect
string is ',"BMT\\FF'.

