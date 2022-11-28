from openbb_terminal.sdk import openbb
unu_df = openbb.stocks.options.unu()
print(type(unu_df[0]))