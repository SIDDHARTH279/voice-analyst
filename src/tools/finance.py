import yfinance as yf

def _pct(x):
    return round(x * 100,2) if x is not None else None

def get_financials(ticker: str) -> dict:

    try:
        info = yf.Ticker(ticker).info
        if not info or info.get('currentPrice') is None:
            return {'error': 'no market data'}

        market_cap = info.get('marketCap')
        return {
            "name": info.get("longName"),
            "sector": info.get("sector"),
            "price": info.get("currentPrice"),
            "market_cap_cr": round(market_cap / 1e7) if market_cap else None,
            "pe_ratio": info.get("trailingPE"),
            "revenue_growth_pct": _pct(info.get("revenueGrowth")),
            "profit_margin_pct": _pct(info.get("profitMargins")),
            "debt_to_equity": info.get("debtToEquity"),
        }

    except Exception as e:
        return {'error': f'No market data ({e})'}


if __name__ == '__main__':
    print(get_financials("TCS.NS"))
    print(get_financials("FAKE123"))