# Candlestick Pattern Backtester

Tests how often classic candlestick patterns are followed by a move up or down, using real price history from Yahoo Finance.

The idea: books like Thomas Bulkowski's *Encyclopedia of Candlestick Charts* publish success rates for each pattern. This project checks those numbers myself, on Apple (AAPL) stock, with my own pattern detectors written in pandas.

## Results: AAPL daily candles, Dec 1980 – Oct 2026 (11,554 candles)

| Pattern | Times found | My % up | 95% range | Bulkowski % up |
|---|---|---|---|---|
| Three white soldiers | 117 | 85.5% | 79.1 – 91.9% | 82% |
| Three red, big green (three-line strike) | 113 | 77.0% | 69.2 – 84.8% | 84% |
| Morning star | 483 | 70.2% | 66.1 – 74.3% | 78% |
| Three green, big red (three-line strike) | 85 | 27.1% | 17.7 – 36.5% | 35% |

**What "up" means:** after a pattern appears, I draw a box around the pattern's candles (their highest high and lowest low). The result counts as **up** if price later closes above the box before it closes below it, and **down** otherwise.

**Takeaways**
- Three white soldiers did slightly better than Bulkowski's figure; the other three came in 7–8 points lower.
- One likely reason: my detectors don't yet check the trend before the pattern, or the price gaps Bulkowski's definitions use.
- I also tried 1-minute candles, but only 15–19 patterns appeared in a week of data, which is too few to trust.

## How it works

- `patterns.py` — detection functions built on pandas Series (`is_green`, `is_red`, `is_tall`, `three_red_big_green`, `three_green_big_red`, `morning_star`, `three_white_soldiers`), the `box` and `win_rate` helpers, and an `all_patterns` registry.
- `backtest.py` — downloads the full AAPL history with `yfinance`, runs every pattern in the registry, and prints how many were found and their % up.

## Run it

```bash
pip install -r requirements.txt
python backtest.py
```

## Next steps

- Add a trend filter before each pattern.
- Test more tickers and save results to CSV automatically.
- Run it live on a small home server and use only the patterns with the best track record as signals.

*Educational project, not financial advice.*
