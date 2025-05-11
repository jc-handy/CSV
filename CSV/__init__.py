import csv,re
from csv import *

# Add CSV's "exported" values to those of the standard csv module.
__all__=csv.__all__+[
    'CSV_DIALECT_DESCRIPTION',
    'DEFAULT_DIALECT_SPEC',
    'dialect_string',
    'parse_dialect',
]

DEFAULT_DIALECT_SPEC=',"BMT\\FF'

CSV_DIALECT_DESCRIPTION=f"""\
    ## Formatting the Dialect String
    CSV formatting is a loose standard with dialectic flexability. These are
    the parameters involved:

    * SEP: Field separator character. (default: ,)
    * Q: Quote character. (default: ")
    * END: Line ending. This can be C for carraige return (\\r), N for
           newline (\\n), or B for both (\\r\\n). L for linefeed is the same
           as N for newline (\\n). Any other character is taken litterally
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
    string is {DEFAULT_DIALECT_SPEC!r}."""


quoting_map=dict(
  A=QUOTE_ALL,
  M=QUOTE_MINIMAL,
  N=QUOTE_NONNUMERIC,
  X=QUOTE_NONE
)

reverse_quoting_map={v:k for k,v in quoting_map.items()}

lineterminator_map=dict(
  B='\r\n',
  C='\r',
  L='\n',
  N='\n' # N functions as an alias for L.
)

reverse_lineterminator_map={v:k for k,v in lineterminator_map.items() if k!='N'}

def dialect_string(dialect,style='spec'):
  """Return a string that describes the given dialect as either a
  specification string (the default) or in a long, multi-line format."""
  
  if isinstance(dialect,str):
    d=get_dialect(dialect)
  if style=='long':
    s=f"""{dialect._name}:
  delimiter={dialect.delimiter!r}
  quotechar={dialect.quotechar!r}
  lineterminator={dialect.lineterminator!r}
  quoting={dialect.quoting!r}
  doublequote={dialect.doublequote!r}
  escapechar={dialect.escapechar!r}
  skipinitialspace={dialect.skipinitialspace!r}
  strict={dialect.strict!r}"""
  elif style=='spec':
    d=dialect
    lt=reverse_lineterminator_map.get(d.lineterminator,d.lineterminator)
    qt=reverse_quoting_map[d.quoting]
    dq='t' if d.doublequote else 'f'
    ss='t' if d.skipinitialspace else 'f'
    st='t' if d.strict else 'f'
    s=f"{d.delimiter}{d.quotechar}{lt}{qt}{dq}{d.escapechar}{ss}{st}"

  return s

# This regular expression matches a complete CSV dialect specification string.
re_dialect=re.compile(
  '^'
  '(?P<delimiter>.)'
  '(?P<quotechar>.)'
  '(?P<lineterminator>.)'
  '(?P<quoting>[AMNX])'
  '(?P<doublequote>[FT])'
  '(?P<escapechar>.)'
  '(?P<skipinitialspace>[FT])'
  '(?P<strict>[FT])'
  '$'
)

def parse_dialect(dialect_name,dialect_spec):
  """Parse a dialect string, register the dialect by name, and
  return the parsed dialect. See "Formatting the Dialect String" above
  for what dialect_spec looks like."""

  # Supply defaults for any unspecified elements of the dialect string.
  if len(dialect_spec)>len(DEFAULT_DIALECT_SPEC):
    raise Error(f"Dialect specification string too long: {dialect_spec!r}")
  if len(dialect_spec)<len(DEFAULT_DIALECT_SPEC):
    dialect_spec+=DEFAULT_DIALECT_SPEC[-(len(DEFAULT_DIALECT_SPEC)-len(dialect_spec)):]

  # Validate and parse the dialect string using a regular expression.
  m=re_dialect.match(dialect_spec)
  if m is None:
    raise Error(f"Bad dialect specification string: {dialect_spec!r}")

  # Cook this dialect spec's non-literal values.
  d=m.groupdict()
  try:
    d['quoting']=quoting_map[d['quoting']]
  except KeyError:
    raise Error(f"Bad \"quoting\" value in dialect specification string: {dialect_spec!r}")
  try:
    d['lineterminator']=lineterminator_map[d['lineterminator']]
  except KeyError:
    raise Error(f"Bad \"lineterminator\" value in dialect specification string: {dialect_spec!r}")
  if d['delimiter']=='n':
    d['delimiter']=None
  if d['escapechar']=='N':
    d['escapechar']=None
  d['doublequote']=d['doublequote']=='t'
  d['skipinitialspace']=d['skipinitialspace']=='t'
  d['lineterminator']=lineterminator_map.get(d['lineterminator'],d['lineterminator'])

  # Create our new dialect class, and register it.
  dialect_class=type(dialect_name,(Dialect,),{
    'delimiter':d['delimiter'],
    'quotechar':d['quotechar'],
    'escapechar':d['escapechar'],
    'doublequote':d['doublequote'],
    'skipinitialspace':d['skipinitialspace'],
    'lineterminator':d['lineterminator'],
    'quoting':d['quoting'],
  })
  register_dialect(dialect_name,dialect_class)
  return get_dialect(dialect_name)

