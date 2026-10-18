
def is_green(df):
    body = (df["Close"] - df["Open"])
    return body > 0

def is_red(df):
    body = (df["Close"] - df["Open"])
    return body < 0

def box(df, n):
    top = df["High"].rolling(n).max()
    bottom = df["Low"].rolling(n).min()
    return top, bottom


def is_tall(df, days=10, factor=1.0):
    body = (df["Close"] - df["Open"]).abs()
    avg_body = body.rolling(days).mean().shift(1)
    return body > avg_body * factor

def three_red_big_green(df): #84% up bulkowski threee line strike 
    red=is_red(df)
  
    return (
        red.shift(3, fill_value=False)
        & red.shift(2, fill_value=False)
        & red.shift(1, fill_value=False)
        & (df["Close"] > df["Open"].shift(3))
    )

def three_green_big_red(df):  #
    green=is_green(df)
  
    return (
        green.shift(3, fill_value=False)
        & green.shift(2, fill_value=False)
        & green.shift(1, fill_value=False)
        & (df["Close"] < df["Open"].shift(3))
    )

def morning_star(df):
    red=is_red(df)
    green=is_green(df)
    midpoint = (df["Open"].shift(2) + df["Close"].shift(2)) / 2
    return (
        red.shift(2,fill_value=False)
        & (((df["Close"].shift(1) - df["Open"].shift(1)).abs())< (df["Close"].shift(2) - df["Open"].shift(2)).abs()/2)
        & green
        & (df["Close"]>=midpoint)
        )

def three_white_soldiers(df): #3 prasina psila
    tall=is_tall(df)
    green=is_green(df)
    return (
        green.shift(2, fill_value=False)
        & green.shift(1, fill_value=False)
        & green
        & tall
        & tall.shift(1, fill_value=False)
        & tall.shift(2, fill_value=False)
    )
def win_rate(df, found, top, bottom):
    up = 0
    down = 0
    for i in range(len(df)):
        if found.iloc[i]:
            for j in range(i + 1, len(df)):
                if df["Close"].iloc[j] > top.iloc[i]:
                    up = up + 1
                    break
                if df["Close"].iloc[j] < bottom.iloc[i]:
                    down = down + 1
                    break
    total = up + down
    if total == 0:
        return 0, 0
    return total, up / total * 100


all_patterns = {
    "three_red_big_green": (three_red_big_green,4),
    "three_green_big_red": (three_green_big_red,4),
    "morning_star": (morning_star,3),
    "three_white_soldiers": (three_white_soldiers,3),
    
}