# Market Pulse

A micro-service powered by **FastAPI** + **Gemini AI** that analyzes market sentiment for any stock ticker using:
- Momentum indicators (via Twelve Data)
- Real-time news (via NewsAPI)
- An LLM-generated explanation (via Gemini)

The frontend is built with **Next.js** + **Recharts**, featuring a minimalist UI and a sparkline chart visualizing last 5-day price momentum.

---

## 🛠️ Tech Stack

### 🔧 Backend
- **FastAPI** (async micro-service)
- **Gemini API** (LLM inference)
- **Twelve Data API** (stock momentum)
- **NewsAPI** (latest stock-related news)
- **CORS middleware** (for frontend integration)

### 💻 Frontend
- **Next.js** (React-based SSR framework)
- **TailwindCSS** (utility-first styling)
- **Axios** (API calls)
- **Recharts** (sparkline chart for momentum)

---

## 🚀 Features

- 🔍 Enter any stock ticker (e.g. `MSFT`, `AAPL`)
- 📈 View last 5-day momentum score as a sparkline
- 📰 Get top 5 recent news articles related to the stock
- 🧠 Receive a natural-language summary (Bullish / Bearish / Neutral) powered by Gemini AI
- 🌐 Fully async API with CORS support

---

## 📦 Project Structure

```
market-pulse/
├── src/
│   ├── main.py           # FastAPI entry point
│   ├── momentum.py       # Twelve Data integration
│   ├── news.py           # NewsAPI integration
│   ├── llm.py            # Gemini LLM request handler
│   └── cache.py          # (Optional) API result caching
├── frontend/
│   ├── app/page.js       # Next.js frontend UI
│   └── components/...    # (Optional) reusable components
```

---

## 🔑 API Spec

| Type     | Provider       |
|----------|----------------|
| Momentum | Twelve Data     |
| News     | NewsAPI         |
| LLM      | Gemini (Google) |

---

## ⚖️ Design Trade-Offs

- Used Twelve Data over Alpha Vantage for better free limits and JSON structure
- Used Gemini Flash 2.5 for faster, lightweight LLM reasoning
- Momentum is calculated with simple 5-day return score for clarity
- No DB used — pure micro-service with optional in-memory caching

---

## 🧪 Running Locally

### Backend
```bash
cd backend
python -m venv venv && source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

---

## 🧠 Future Work

- [ ] Add sentiment analysis from news headlines
- [ ] Support intraday or weekly momentum options
- [ ] Cache responses using Redis or SQLite
- [ ] Add ticker suggestions/autocomplete
- [ ] Add Docker support for easier deployment
- [x] Deploy to Vercel + Render with CI/CD

---

## 📄 License

MIT — feel free to fork and build on it!

---

## ✨ Author

Built with ❤️ by **[Rahul A B](https://github.com/klrab3490)**

