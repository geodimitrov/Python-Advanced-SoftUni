#try to create as many func as possible to break down the code
def symbol_occurrences(data):
    symbol_occur = {}
    for symbol in data:
        if symbol not in symbol_occur:
            symbol_occur[symbol] = 1
        else:
            symbol_occur[symbol] += 1
    return symbol_occur

def print_result(symbol_occur):
    for symbol, occur in sorted(symbol_occur.items()):
        print (f"{symbol}: {occur} time/s")

#use map or list compreh to create list/tuple of symbols
symbols = tuple(map(str, input()))
symbols_count = symbol_occurrences(symbols)
print_result(symbols_count)