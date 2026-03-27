from fastmcp import FastMCP
import yfinance as yf
app = FastMCP("My MCP Server")
# 第一個工具；提供一個加法工具
@app.tool
def add(n1:int, n2:int)->int:
  """Add Two Numbers"""
  return n1+n2

# 第二個工具:提供股價
@app.tool()
def get_stock_price(ticker: str) -> str:
    """
    Get the latest stock price for a given ticker symbol.
    Example tickers: 'AAPL' for Apple, '2330.TW' for TSMC.
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if data.empty:
            return f"找不到股票代號: {ticker}"
        
        latest_price = data['Close'].iloc[-1]
        currency = stock.info.get('currency', 'USD')
        
        return f"{ticker} 的最新收盤價為 {latest_price:.2f} {currency}"
    except Exception as e:
        return f"發生錯誤: {str(e)}"
