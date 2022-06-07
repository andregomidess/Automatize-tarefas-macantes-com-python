import pyperclip, re

honeRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?
# código de área
(\s|-|\.)?
# separador
(\d{3})
# primeiros 3 dígitos
(\s|-|\.)
# separador
(\d{4})
# últimos 4 dígitos
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extensão
)''', re.VERBOSE)