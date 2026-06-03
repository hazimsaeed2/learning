# EPAT LECTURE CHEAT SHEET — AGENT INSTRUCTIONS

> **You are an AI agent. This file contains your complete instructions.**
> When given a lecture transcript (or a lecture file), read this file first and then produce the cheat sheet exactly as described below. You do not need any other instructions.

---

## YOUR TASK

You will receive a lecture transcript file (`.txt` or similar).
Your job is to read it, understand everything in it, and produce a **single self-contained HTML cheat sheet file** that covers the entire lecture.

---

## OUTPUT FILE NAMING RULE

The output file name must match the lecture file name exactly, but with the extension changed to `.html`.

**Examples:**
| Lecture file | Output cheat sheet |
|---|---|
| `Week 8-1Tutorial Session - Doubt Solving on Python after DMP-01.txt` | `Week 8-1Tutorial Session - Doubt Solving on Python after DMP-01.html` |
| `Week 8-2DMP-02 Introduction to Object Oriented Programming.txt` | `Week 8-2DMP-02 Introduction to Object Oriented Programming.html` |
| `Week 9-1MMT-05 Some Lecture Title.txt` | `Week 9-1MMT-05 Some Lecture Title.html` |

Save the file in the **same folder** as the lecture transcript.

---

## WHO WILL READ THIS CHEAT SHEET

- A student who **did not attend the lecture at all**.
- Hasan (the owner) — reading the cheat sheet **5 years from now** to quickly remember everything.
- A complete beginner with no prior knowledge of the topic.

**The test:** If someone reads only this HTML file — nothing else — they must be able to understand every concept, follow every number, and run every piece of code taught in the lecture.

---

## EXPLAIN ALL SHORTHAND, ACRONYMS, TICKERS, AND JARGON

Assume the reader will forget abbreviations after 5 years. Do **not** assume they remember shorthand.

Rules:
- On first use, always expand the full meaning, then show the short form in brackets.
- After that, you may use the short form alone.
- If an acronym appears in a section title or a formula label before the body explains it, decode it in the first sentence immediately below that title.
- If the lecture uses a ticker, symbol, exchange code, or function shorthand, explain what it refers to in plain English.
- If the lecture uses technical words like CAGR, OHLCV, VWAP, SMA, LMA, UTC, IST, drawdown, or Sharpe, explain them the first time they appear.
- If the lecture uses something like `^NSEI`, explain it like this: `^NSEI` = Yahoo Finance ticker symbol for the Nifty 50 index (India's benchmark large-cap stock market index).

Examples:
- **Good:** "Simple Moving Average (SMA) = the average of the last N prices."
- **Good:** "OHLCV = Open, High, Low, Close, Volume — the 5 standard market data columns."
- **Good:** "UTC (Coordinated Universal Time) is the base time zone used by many data APIs."
- **Bad:** "Compute SMA on OHLCV, then convert UTC to IST."  
  This assumes the reader remembers 4 separate terms.

Add a small **TERMINOLOGY / DECODING THE SHORTHAND** box wherever the lecture uses many short forms.

---

## WHAT TO IGNORE IN THE TRANSCRIPT

Lecture transcripts are full of noise. **Strip all of this out — do not include it:**

- Filler talk: "okay", "so", "let me wait two seconds", "any questions?"
- Setup talk: "can you see my screen?", "is the font big enough?", "please confirm in the chat"
- Student Q&A chatter and back-and-forth that doesn't add new information
- Repetition — the instructor often says the same thing 3–4 times. Say it once, clearly.
- Personal introductions and session housekeeping

**Keep only:**
1. Concept definitions
2. All code shown (every line)
3. Step-by-step workflows
4. Formulas and calculation rules
5. "Why we do this" explanations — the reasoning behind things
6. Warnings, gotchas, and common mistakes
7. Comparisons ("A vs B" type explanations)

---

## THE #1 RULE — STEP-BY-STEP WORKED EXAMPLES WITH CONCRETE NUMBERS

> **This is the single most important instruction in this entire file.**
> Every concept, every formula, every code block MUST be accompanied by a **worked example using simple, concrete numbers** that the reader can follow step by step — just like watching someone solve a problem on a whiteboard.

### What "good" looks like (from the gold-standard Week 7-3 cheat sheet):

**Section 1 defines ALL numbers upfront in a table:**
```
Stock: AAPL | Total Shares: 100,000 | Decision Price: $150.00
Order Arrives: $150.30 | Average Fill: $150.80 | End Price: $151.00
Commission: $0.02/share | Executed: 80,000 | Unexecuted: 20,000
```

**Then EVERY later section plugs those SAME numbers into formulas with full arithmetic visible:**
```
Paper Return = S × (PN − PD)
             = 100,000 × ($151.00 − $150.00)
             = 100,000 × $1.00
             = $100,000

Execution Cost = X × (Pavg − P0)
               = 80,000 × ($150.80 − $150.30)
               = 80,000 × $0.50
               = $40,000
```

**The reader sees every multiplication, every subtraction, every intermediate result. Nothing is skipped.**

### What "bad" looks like (NEVER do this):

```
❌ "Calculate the rolling average for 21 days"
❌ "Use pct_change() to get returns"
❌ "Multiply position by returns"
❌ "The SMA crosses above the LMA → buy signal"
```

These tell the reader WHAT to do but never SHOW it being done with real numbers. The reader is left to imagine the calculation. **That is unacceptable.**

### What you MUST do instead:

```
✅ "Days 1–5 Close prices: 100, 102, 98, 105, 103
    SMA(3) on Day 3 = (100 + 102 + 98) / 3 = 300 / 3 = 100.00
    SMA(3) on Day 4 = (102 + 98 + 105) / 3 = 305 / 3 = 101.67
    SMA(3) on Day 5 = (98 + 105 + 103) / 3 = 306 / 3 = 102.00"

✅ "Return on Day 5 = (103 − 105) / 105 = −2 / 105 = −0.0190 = −1.90%"

✅ "Signal on Day 4: SMA(3)=101.67 > LMA(5)=101.60 AND yesterday SMA(3)=100.00 < LMA(5)=100.40 → CROSSOVER → signal = 1 (BUY)"
```

### The pattern:

1. **Section 1 (Core Example):** Define a small table of ~5–10 concrete values (prices, dates, shares, windows). These are your "sample data."
2. **Every other section:** Take those SAME numbers, plug them into the formula or code, and show every arithmetic step: input → intermediate → result.
3. **For code blocks:** After showing the code, show a mini-table of what the DataFrame looks like with those exact numbers — not "..." or "962 rows" but 5–6 specific rows with specific values.
4. **For comparisons:** Calculate BOTH sides with the same numbers so the reader sees the actual difference (e.g., simple return = −0.0190 vs log return = −0.0192).

### How many numbers is enough?

- For a **code-heavy lecture (DMP):** Define 5–8 days of price data with specific close prices. Use those prices in every rolling calculation, every return formula, every signal check.
- For a **formula-heavy lecture (MMT):** Define 8–12 named values (like the AAPL example above). Plug them into every formula.
- For a **tutorial session:** Use whatever sample data the instructor used.  Recreate the exact numbers from their demo.

**If a section has no worked example with concrete numbers, it is incomplete. Go back and add one.**

---

## HOW TO BUILD THE CHEAT SHEET — 6 STEPS

### STEP 1 — Read the transcript and extract the sample data
Before writing anything:
- What is the **main topic** of this lecture?
- What are the **top 5–8 concepts or skills** taught?
- What **specific numbers** did the instructor use? (prices, dates, shares, indicators, outputs) — Write them all down. These become your Core Example.
- If the instructor didn't use consistent numbers, **invent a simple set** (5–8 days of round-number prices) and use them everywhere.
- What **code** was demonstrated? List every code block.
- What were the **"aha" moments** — things students got wrong or found surprising?

---

### STEP 2 — Map the lecture structure into sections
Every lecture has a logical flow. Identify it, then make each topic a numbered HTML section:
```
Example: Libraries → Download Data → CSV files → Arrays vs Lists → Strategy → Returns → Vectorized vs Event-Driven
```
This becomes your section order in the HTML. Aim for **6–9 sections** total.

---

### STEP 3 — For every concept write: WHAT → WHY → HOW → WORKED EXAMPLE → TERMINOLOGY → GOTCHA
Every section (and sub-box within a section) must cover:
1. **WHAT is it?** — One plain English sentence. No jargon first.
2. **WHY does it matter?** — One sentence reason a trader/developer cares.
3. **HOW to use it** — Exact code with every line commented, OR step-by-step formula.
4. **WORKED EXAMPLE WITH NUMBERS** — This is mandatory. Take the Core Example numbers from Section 1, plug them in, and show every arithmetic step. Show the DataFrame rows. Show the intermediate values. Show the final result. The reader must be able to verify each step by hand.
5. **TERMINOLOGY DECODING** — Expand any acronym, ticker, shorthand, or jargon the first time it appears.
6. **GOTCHA / Common mistake** — What trips people up. These are gold.

**Rule: Distinguish a general rule from an example-specific outcome.**
- If the lecture demo ends with a specific value, direction, or signal (for example: final exit signal = `-1`), explicitly say whether that is a universal rule or just what happened in that sample path.
- Never turn an example-specific number or trade direction into a generic instruction unless the lecture clearly states it is always true.

> **Rule: "Never say 'calculate X' — always SHOW X being calculated with the numbers from Section 1."**
> **Rule: "Never write unexplained shorthand on first use."**

---

### STEP 4 — Build the Core Example section (Section 1, amber color)
This is the MOST IMPORTANT section. It defines every number used in the rest of the cheat sheet.

**For code-heavy lectures (DMP/Tutorial):**
Create a table of ~5–8 days of sample price data with specific Close prices. Example:
```
Day 1 (Jan 2): Close = 100.00
Day 2 (Jan 3): Close = 102.00
Day 3 (Jan 4): Close =  98.00
Day 4 (Jan 5): Close = 105.00
Day 5 (Jan 6): Close = 103.00
Day 6 (Jan 7): Close = 107.00
Day 7 (Jan 8): Close = 104.00
Day 8 (Jan 9): Close = 108.00
```
Plus strategy settings: Short MA window = 3, Long MA window = 5, etc.

**For formula-heavy lectures (MMT):**
Create a named-value table (like the AAPL TCA example): Symbol → Meaning → Value.

Then in EVERY subsequent section, reference this table:
- "Using our sample data from Section 1, Day 3 SMA(3) = (100 + 102 + 98) / 3 = 100.00"
- "Return on Day 5 = (103 − 105) / 105 = −0.0190 = −1.90%"

The reader should never have to wonder "what numbers would I plug in here?"

---

### STEP 5 — Write all code as complete, runnable snippets WITH sample output
Every code block must:
- Include all `import` statements needed to run it
- Have a **comment on every single line** explaining what it does
- Show the **expected output** below the code as an HTML table with the Core Example numbers — not "962 rows" but 5–8 specific rows with real values the reader can inspect
- If the code prints metrics, arrays, confusion matrices, model coefficients, shapes, or data types, show those exact outputs too — not just the table
- If the lecture covers forecasting, volatility, clustering, classification, or trade evaluation, show the model output on **real market data** whenever practical (real ticker, real dates, real predicted values, real chart)
- Use the **same variable names** as used in the lecture — do not rename things
- HTML-escape special characters: `<` → `&lt;`, `>` → `&gt;`, `&` → `&amp;`

**Special rule for model-driven lectures:**
- Never stop at the code. After the code, show what the model produced, what each output column/metric means, and how to interpret it in plain English.
- For example: ARIMA → actual vs forecast chart + forecast table; confusion matrix → 2×2 labeled grid + precision/recall; clustering → scatter plot with cluster meaning; volatility forecast → predicted vs realized volatility comparison.

---

### STEP 6 — Audit it once as a complete beginner
Before you finalize the HTML, pretend you know nothing about the topic and read it from top to bottom.

Ask these questions:
- If I skipped the lecture entirely, can I still tell what problem this topic solves?
- Do I know what every acronym, symbol, and metric means the first time I see it?
- If there is code, can I see what the code produced and why the output matters?
- If the topic is visual by nature, do I get a chart/diagram that makes the concept concrete?
- If a result is "good" or "bad", does the sheet explain compared to what benchmark or threshold?

If any answer is "no", the cheat sheet is incomplete. Fix it before saving.

---

### STEP 7 — End with a QUICK REFERENCE section (last section, gray color)
A 3-column grid containing:
- **Column 1:** All key functions/formulas in a compact table (function → what it does → gotcha)
- **Column 2:** Common mistakes table (mistake → what goes wrong → fix)
- **Column 3:** The core example's numbers at a glance + a step-by-step checklist of the lecture workflow + shorthand decoder (e.g. SMA, LMA, OHLCV, `^NSEI`)

Then a yellow **KEY TAKEAWAYS** bar: 4 boxes, one sentence each, the 4 most important things to remember.

Then a **FOOTER** with: the master formula or rule that summarizes the whole lecture in 1–2 lines.

---

## OUTPUT FORMAT — HTML ONLY

The output **must be a single self-contained `.html` file**. Anyone can open it in a browser (Chrome, Edge, Firefox) with no extra software. Do not produce Markdown or PDF.

### Base Style Reference
Model the visual design on `Week 7-3 MMT-04 The Algorithmic Trading Process.html` (in this same folder). That is the gold standard for layout, color, density, and typography.

---

### HTML Boilerplate (use this exact head/body structure)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[WEEK X-Y] — [LECTURE TOPIC] — Cheat Sheet</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body { font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
           font-size: 11px; line-height: 1.5; }
    @media print { body { font-size: 9px; } .page-break { page-break-before: always; } }
    h1 { font-size: 18px; }
    h2 { font-size: 13px; }
    h3 { font-size: 11px; }
    table { font-size: 10px; }
    pre  { font-size: 9px; line-height: 1.45; }
  </style>
</head>
<body class="bg-white p-4 max-w-6xl mx-auto">

  <!-- HEADER -->

  <!-- PAGE 1: Core Example + Sections 1–2 -->

  <!-- PAGE BREAK: <div class="page-break"></div> -->

  <!-- PAGE 2: Sections 3–5 (middle content, workflows, code) -->

  <!-- PAGE BREAK: <div class="page-break"></div> -->

  <!-- PAGE 3: Sections 6–7, Quick Reference, Takeaways, Footer -->

</body>
</html>
```

---

### Header Block (top of every cheat sheet)

```html
<header class="text-center border-b-4 border-blue-600 pb-3 mb-4">
  <h1 class="font-extrabold text-blue-900">[TOPIC IN CAPS] — COMPLETE CHEAT SHEET</h1>
  <p class="text-gray-600 mt-1">EPAT [Week X-Y] — [Session Name] | Instructor: [Name]</p>
  <p class="text-gray-700 mt-2">
    <strong>The Problem:</strong> [One sentence — what the student struggles with before this lecture]<br>
    <strong>Your Goal:</strong> [One sentence — what they can do after mastering this]
  </p>
</header>
```

---

### Section Wrapper (one per major topic)

```html
<section class="border-2 border-[COLOR]-500 rounded-lg p-3 mb-4 bg-[COLOR]-50">
  <h2 class="font-bold text-[COLOR]-900 mb-3 bg-[COLOR]-200 rounded px-2 py-1">N️⃣ SECTION TITLE</h2>
  <div class="grid grid-cols-2 gap-4">   <!-- use cols-3 for 3 equal boxes -->
    <div class="bg-white border-2 border-[COLOR]-300 rounded p-3">
      <h3 class="font-bold text-[COLOR]-800 mb-2">Sub-topic title</h3>
      <!-- content here -->
    </div>
    <div class="bg-white border-2 border-[COLOR]-300 rounded p-3">
      <!-- content here -->
    </div>
  </div>
</section>
```

---

### Color Coding — Use These Colors Consistently

| Section Type | COLOR to use | Example border class |
|---|---|---|
| Core Example / Key Numbers | `amber` | `border-amber-500 bg-amber-50` |
| Libraries / Setup / Imports | `blue` | `border-blue-500 bg-blue-50` |
| Data Download / APIs | `green` | `border-green-500 bg-green-50` |
| File I/O / Storage / CSV | `indigo` | `border-indigo-500 bg-indigo-50` |
| Concepts / Theory / Definitions | `orange` | `border-orange-500 bg-orange-50` |
| Strategy / Full Workflow / Steps | `purple` | `border-purple-500 bg-purple-50` |
| Returns / Math / Formulas | `teal` | `border-teal-500 bg-teal-50` |
| Comparison (A vs B) | `cyan` | `border-cyan-500 bg-cyan-50` |
| Warnings / Mistakes / Pitfalls | `red` | `border-red-500 bg-red-50` |
| Quick Reference (last section) | `gray` | `border-gray-600 bg-gray-100` |

---

### Code Block (dark background, green text)

```html
<pre class="bg-gray-900 text-green-400 rounded p-2 font-mono">
import yfinance as yf          # Download stock data from Yahoo Finance

df = yf.download(              # Fetch historical price data
    "^NSEI",                   # Ticker symbol for Nifty 50
    start="2017-01-01",        # Start date
    end="2020-01-01",          # End date
    multi_level_index=False    # Always add — keeps column names clean
)
# Output: DataFrame with 962 rows, columns: Open High Low Close Volume
</pre>
```

> Always HTML-escape code: `<` → `&lt;`, `>` → `&gt;`, `&` → `&amp;`

---

### Warning Box

```html
<div class="bg-red-100 rounded p-2 border-l-4 border-red-500">
  <p><strong>⚠️ WARNING — [Short label]:</strong> [What goes wrong and how to fix it]</p>
</div>
```

### Tip Box

```html
<div class="bg-yellow-100 rounded p-2 border-l-4 border-yellow-400">
  <p><strong>💡 TIP:</strong> [Helpful insight or shortcut]</p>
</div>
```

---

### Page Layout — 3 Pages

Spread content across 3 logical print pages using `<div class="page-break"></div>`:

| Page | Content |
|---|---|
| Page 1 | Header + Core Example section (amber) + first 2 topic sections |
| Page 2 | Middle sections — the biggest workflow/strategy section goes here |
| Page 3 | Comparison sections + Quick Reference (gray) + Key Takeaways + Footer |

---

### Quick Reference Section (always last, gray)

```html
<section class="border-2 border-gray-600 rounded-lg p-3 bg-gray-100">
  <h2 class="font-bold text-gray-900 mb-3 bg-gray-300 rounded px-2 py-1">📋 QUICK REFERENCE — All In One Place</h2>
  <div class="grid grid-cols-3 gap-4">
    <!-- Col 1: Key functions table -->
    <!-- Col 2: Common mistakes table -->
    <!-- Col 3: Example numbers at a glance + step checklist -->
  </div>
  <div class="bg-yellow-100 rounded p-3 mt-3">
    <p class="font-bold text-yellow-900 mb-2">🎯 KEY TAKEAWAYS</p>
    <div class="grid grid-cols-4 gap-3">
      <p>1. [Most important thing]</p>
      <p>2. [Second most important]</p>
      <p>3. [Third]</p>
      <p>4. [Fourth]</p>
    </div>
  </div>
</section>
```

### Footer (always last, below everything)

```html
<footer class="mt-3 text-center text-gray-600 border-t-2 border-gray-300 pt-2">
  <p><strong>THE MASTER FORMULA / RULE:</strong> [One-line summary of the whole lecture]</p>
  <p class="mt-1"><strong>THE ONE THING TO NEVER FORGET:</strong> [The single most critical rule]</p>
</footer>
```

---

## QUALITY CHECKLIST — Before You Finish

Before saving the file, verify every item:

**Worked Examples (MOST IMPORTANT):**
- [ ] Section 1 defines a table of concrete sample data (5–8 days of prices, or 8–12 named values)
- [ ] EVERY subsequent section plugs those Section 1 numbers into its formulas/code
- [ ] Every calculation shows full arithmetic: input → intermediate steps → final result (nothing skipped)
- [ ] Code block outputs show mini-tables with the actual sample numbers (not "962 rows..." but 5–8 specific rows)
- [ ] No section says "calculate X" without showing X calculated with specific numbers
- [ ] Comparisons (A vs B) compute BOTH sides with the same numbers so the reader sees the actual difference

**Terminology / Memory:**
- [ ] Every acronym, ticker, shorthand, and jargon term is expanded on first use
- [ ] Tickers/symbols are explained in plain English (example: `^NSEI` = Yahoo Finance ticker for Nifty 50)
- [ ] A reader returning after 5 years can decode all short forms without external help

**Content:**
- [ ] Every concept has: WHAT → WHY → HOW → WORKED EXAMPLE WITH NUMBERS → GOTCHA
- [ ] One core example runs consistently through all sections (same stock, same numbers)
- [ ] Every code snippet has all imports + every line commented + expected output shown
- [ ] Code outputs include exact printed metrics/arrays/shapes when the lecture uses them (not just a generic table)
- [ ] Common mistakes are called out explicitly with red warning boxes
- [ ] GOTCHAs are written as ASSUMPTION → REALITY → FIX when possible
- [ ] If someone reads only this file, they understand 100% of the lecture

**HTML:**
- [ ] File name matches the lecture file name with `.html` extension
- [ ] Tailwind CDN is in the `<head>`
- [ ] No raw `<`, `>`, `&` inside `<pre>` blocks — all HTML-escaped
- [ ] Uses 2–3 column grid layouts — NO long single-column walls of text
- [ ] Two `<div class="page-break"></div>` dividers splitting content into 3 pages
- [ ] Colors match the color-coding table above
- [ ] Quick Reference section is the last section (gray)
- [ ] Key Takeaways bar (yellow) is inside the Quick Reference section
- [ ] Footer is present with the master rule

**Visual Aids (NEW):**
- [ ] Every concept that is inherently visual has an inline SVG diagram (crossover chart, equity curve, rolling window, payoff diagram, etc.)
- [ ] SVGs use `viewBox` for responsive sizing and `class="w-full"` for container fit
- [ ] Chart legends and annotations are present — lines are labeled, key points are marked
- [ ] Visual style matches section color coding (green=buy, red=sell, blue=data)
- [ ] Forecasting / volatility / clustering / evaluation topics use real market data in visuals whenever practical
- [ ] The final sheet passes one full beginner audit read: no unexplained jumps, no missing outputs, no unexplained verdicts

---

## EPAT-SPECIFIC NOTES

- EPAT lectures use **Nifty 50** (`^NSEI`) or **Indian stocks** as examples. Keep them — don't change to US stocks.
- **DMP sessions** (Data, Modeling & Programming) — heavy on Python code, libraries, step-by-step workflows. Prioritize code blocks and workflows.
- **MMT sessions** (Market Microstructure & Trading) — heavy on formulas, concepts, analogies, metrics. Prioritize formula tables and analogy boxes.
- **Tutorial sessions** — mix of code demos and Q&A. Focus on the demo, ignore the Q&A noise.
- Always keep the exact **function names, variable names, and parameter names** used in the lecture. Do not rename or simplify them.

---

## VISUAL AIDS — INLINE SVG CHARTS & DIAGRAMS

> **Rule: If a concept is easier to understand with a picture than with words alone, add an inline SVG diagram.**

Many financial and algorithmic concepts are inherently visual. A crossover strategy makes no sense until you SEE two lines crossing. An equity curve shows performance at a glance. A rolling window becomes obvious with a sliding-bracket animation.

When the lecture is about **forecasting, volatility, model evaluation, clustering, or strategy performance**, prefer a chart built from **real market data** whenever practical rather than a purely toy illustration. Use toy numbers only when the lecture itself is purely conceptual or when the arithmetic must be hand-checkable.

### When to Add SVG Visuals

| Concept Type | What to Draw | Example |
|---|---|---|
| **Moving Average Crossover** | Price line + SMA + LMA with BUY/SELL markers and profit zone shading | Green/red dashed lines crossing, with vertical signal lines |
| **Rolling Window / Sliding Calculation** | Brackets sliding over data boxes showing which values enter the window | Colored rectangles over price boxes with arrows showing the slide |
| **Equity Curve / Cumulative Returns** | Strategy line vs buy-and-hold line over time | Two lines diverging, with annotations showing final returns |
| **Distribution / Histogram** | Bell curve or histogram showing return distribution | Bars with mean/std markers |
| **Options Payoff Diagram** | Payoff at expiry vs underlying price | Hockey-stick lines for calls/puts, combined for spreads |
| **Clustering / Classification** | Scatter plot with colored clusters or decision boundaries | Dots in groups with centroids marked |
| **Neural Network Architecture** | Layers of nodes with connections | Input → Hidden → Output nodes |
| **Time Series Forecast** | Actual vs predicted with confidence bands | Historical line + dotted forecast line |
| **Volatility Smile / Surface** | Strike vs IV curve | U-shaped curve with ATM marked |
| **Greeks Sensitivity** | How delta/gamma/theta/vega change with price/time | Line charts showing greek profiles |
| **Model Evaluation** | Confusion matrix, predicted vs actual, error bands, P&L range | 2×2 grid, forecast error chart, expected vs actual outcome |
| **Decision Rules / Trees** | Split logic, yes/no branching, no-trade band logic | Tree diagram, decision flow, threshold bands |

### SVG Best Practices

1. **Use `viewBox` for responsive sizing:** `<svg viewBox="0 0 620 250" class="w-full">` — scales to container width.
2. **Keep it self-contained:** No external images or fonts. Use `system-ui` for text.
3. **Color-code consistently:** Match section colors (green for buy, red for sell, blue for price data).
4. **Add a legend** at the bottom of every chart.
5. **Annotate key points** — don't just draw lines; label crossover points, extremes, and zones.
6. **Use dashed lines** for moving averages/forecasts to distinguish from raw data (solid).
7. **Keep file size reasonable:** 15–30 SVG lines per chart. Don't over-detail.
8. **Wrap in a styled container:** `<div class="bg-white border-2 border-[COLOR]-300 rounded p-3 mt-3">` with a bold title.
9. **Explain the verdict inside the visual:** if a chart implies "overfit", "stationary", "ATM is most active", or "forecast beat actual", label that conclusion directly on the SVG.

### SVG Template

```html
<div class="bg-white border-2 border-[COLOR]-300 rounded p-3 mt-3">
  <h3 class="font-bold text-[COLOR]-800 mb-2">📈 VISUAL: [Chart Title]</h3>
  <svg viewBox="0 0 620 250" class="w-full">
    <!-- Background -->
    <rect x="40" y="20" width="545" height="190" rx="4" fill="#f8fafc" stroke="#e2e8f0"/>
    <!-- Grid lines -->
    <!-- Data lines (polyline) -->
    <!-- Annotations (text, circles, arrows) -->
    <!-- Legend -->
  </svg>
</div>
```

---

*These are your complete instructions. You do not need anything else. Receive the transcript → produce the `.html` file.*


