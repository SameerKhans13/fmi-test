# slides_part2_a.py
# Slides 36 to 52: Statements Linkage, Cash Flow, and Financial Ratios

slides_36_to_52 = [
    # SLIDE 36
    {
        "id": 36,
        "module": "Module 3 · Statements Linkage",
        "title": "Income Statement: Operating Profit to PAT & EPS",
        "subtitle": "How EBIT flows through financing, taxes, and shares",
        "badge": "INCOME STATEMENT",
        "badge_type": "primary",
        "content_html": """
            <h3>The Bottom Half of the Income Statement</h3>
            <p>Once Operating Profit (EBIT) is established from core operations, non-operating capital structure charges and taxes are deducted:</p>
            <div class="table-responsive" style="margin-top:0.75rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <tr><th>Line Item</th><th>Meaning / Nature</th><th>Who Controls It?</th></tr>
                    <tr><td><strong>EBIT (Operating Profit)</strong></td><td>Core business earning before debt and taxes</td><td>Operations / Management</td></tr>
                    <tr><td><strong>− Finance Costs (Interest)</strong></td><td>Obligation to lenders on borrowed debt</td><td>Capital Structure choice</td></tr>
                    <tr><td><strong>= EBT (Profit Before Tax)</strong></td><td>Taxable accounting income</td><td>Pre-tax earnings</td></tr>
                    <tr><td><strong>− Corporate Income Tax</strong></td><td>Statutory tax liability (~25% in India)</td><td>Tax Authority (Govt)</td></tr>
                    <tr><td><strong>= PAT (Net Profit after Tax)</strong></td><td>Residual earnings belonging to shareholders</td><td>Shareholders</td></tr>
                    <tr><td><strong>÷ Number of Equity Shares</strong></td><td>Weighted average common shares outstanding</td><td>Capital base</td></tr>
                    <tr><td><strong>= EPS (Earnings Per Share)</strong></td><td>Net income earned per single share</td><td>Per-share metric</td></tr>
                </table>
            </div>
            <div class="callout callout-warning" style="margin-top:0.75rem;">
                <strong>⚠️ MCQ Exam Trap:</strong> Interest is a <em>financing cost</em>, not an operating cost! EBIT is completely independent of whether a company is funded 100% by equity or 100% by debt.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">From EBIT to Retained Earnings</h4>
                <div style="display:flex; flex-direction:column; gap:0.4rem; max-width:320px; margin:0 auto; font-size:0.85rem;">
                    <div style="background:#eff6ff; border:1px solid #93c5fd; padding:0.4rem 0.6rem; border-radius:6px; font-weight:bold; color:#1e40af; text-align:center;">
                        EBIT (Operating Profit)
                    </div>
                    <div style="text-align:center; color:#64748b; font-size:0.75rem;">↓ Deduct: Interest (Debt Lenders)</div>
                    <div style="background:#f1f5f9; border:1px solid #cbd5e1; padding:0.4rem 0.6rem; border-radius:6px; font-weight:bold; color:#334155; text-align:center;">
                        EBT (Profit Before Tax)
                    </div>
                    <div style="text-align:center; color:#64748b; font-size:0.75rem;">↓ Deduct: Tax (Government)</div>
                    <div style="background:#ecfdf5; border:1px solid #6ee7b7; padding:0.4rem 0.6rem; border-radius:6px; font-weight:bold; color:#065f46; text-align:center;">
                        PAT (Net Income)
                    </div>
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; margin-top:0.3rem;">
                        <div style="background:#fef3c7; border:1px solid #fde68a; padding:0.4rem; border-radius:6px; font-size:0.75rem; text-align:center; color:#92400e;">
                            <strong>Dividends</strong><br>Paid out to Owners
                        </div>
                        <div style="background:#dbeafe; border:1px solid #bfdbfe; padding:0.4rem; border-radius:6px; font-size:0.75rem; text-align:center; color:#1e40af;">
                            <strong>Retained Earnings</strong><br>Reinvested in B/S
                        </div>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 37
    {
        "id": 37,
        "module": "Module 3 · Statements Linkage",
        "title": "Balance Sheet Snapshot: Liquidity & Solvency",
        "subtitle": "Order of presentation and permanent funding structure",
        "badge": "BALANCE SHEET",
        "badge_type": "primary",
        "content_html": """
            <h3>The Balance Sheet Architecture</h3>
            <p>The Balance Sheet displays the financial position of a firm at a single specific point in time (snapshot), arranged in order of liquidity or permanence:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-top:0.75rem;">
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.75rem;">
                    <h4 style="color:#2563eb; font-size:0.95rem; margin-bottom:0.4rem;">Assets (Resources Controlled)</h4>
                    <ul style="font-size:0.85rem; line-height:1.6; margin-left:1.2rem;">
                        <li><strong>Non-Current Assets:</strong> Property, Plant & Equipment (PP&E), Intangibles (Goodwill, Patents), Long-Term Investments.</li>
                        <li><strong>Current Assets:</strong> Inventories (raw, WIP, finished), Trade Receivables (Debtors), Cash & Bank balances.</li>
                    </ul>
                </div>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.75rem;">
                    <h4 style="color:#059669; font-size:0.95rem; margin-bottom:0.4rem;">Liabilities & Equity (Claims)</h4>
                    <ul style="font-size:0.85rem; line-height:1.6; margin-left:1.2rem;">
                        <li><strong>Shareholders' Equity:</strong> Share Capital + Retained Earnings & Reserves.</li>
                        <li><strong>Non-Current Liabilities:</strong> Long-term loans, Debentures, Bonds (> 12 months).</li>
                        <li><strong>Current Liabilities:</strong> Trade Payables, Short-term bank overdraft, Accrued expenses.</li>
                    </ul>
                </div>
            </div>
            <div class="callout callout-info" style="margin-top:0.75rem;">
                <strong>💡 Net Working Capital:</strong> Current Assets − Current Liabilities = Working Capital required to fund day-to-day operations.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Liquidity Gradient of the Balance Sheet</h4>
                <div style="display:flex; justify-content:space-between; align-items:center; background:#f8fafc; padding:0.6rem; border-radius:8px; margin-bottom:0.5rem; font-size:0.85rem;">
                    <span style="color:#64748b; font-weight:bold;">Least Liquid</span>
                    <span style="color:#3b82f6; font-weight:bold;">── Increasing Liquidity ──▶</span>
                    <span style="color:#059669; font-weight:bold;">Most Liquid</span>
                </div>
                <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:0.4rem; text-align:center; font-size:0.8rem;">
                    <div style="background:#eff6ff; border:1px solid #bfdbfe; padding:0.5rem 0.2rem; border-radius:6px;">
                        <strong>Factory / Land</strong><br><span style="font-size:0.7rem; color:#64748b;">Years to sell</span>
                    </div>
                    <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:0.5rem 0.2rem; border-radius:6px;">
                        <strong>Inventory</strong><br><span style="font-size:0.7rem; color:#64748b;">Weeks to sell</span>
                    </div>
                    <div style="background:#fefce8; border:1px solid #fef08a; padding:0.5rem 0.2rem; border-radius:6px;">
                        <strong>Receivables</strong><br><span style="font-size:0.7rem; color:#64748b;">Days to collect</span>
                    </div>
                    <div style="background:#ecfdf5; border:1px solid #6ee7b7; padding:0.5rem 0.2rem; border-radius:6px;">
                        <strong>Bank Cash</strong><br><span style="font-size:0.7rem; color:#059669; font-weight:bold;">Immediate cash</span>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 38
    {
        "id": 38,
        "module": "Module 3 · Statements Linkage",
        "title": "Cash Flow Statement: The Three Pillars",
        "subtitle": "Operating, Investing, and Financing activities explained",
        "badge": "CASH FLOW",
        "badge_type": "success",
        "content_html": """
            <h3>Cash Flow Statement (CFS) Architecture</h3>
            <p>While the P&L reports accrual profits, the Cash Flow Statement tracks actual gross cash inflows and outflows across 3 distinct activity buckets:</p>
            <div style="display:flex; flex-direction:column; gap:0.5rem; margin-top:0.75rem;">
                <div style="background:#f0fdf4; border-left:4px solid #22c55e; padding:0.6rem;">
                    <strong style="color:#15803d;">1. Cash from Operating Activities (CFO):</strong>
                    <div style="font-size:0.85rem; color:#334155;">Cash generated from selling goods/services, after paying suppliers, staff, and taxes. The true engine of business sustainability. Must be positive for mature companies!</div>
                </div>
                <div style="background:#eff6ff; border-left:4px solid #3b82f6; padding:0.6rem;">
                    <strong style="color:#1d4ed8;">2. Cash from Investing Activities (CFI):</strong>
                    <div style="font-size:0.85rem; color:#334155;">Purchase or sale of long-term productive assets (Capex: plant, machinery, software) and strategic investments in other companies. Typically negative for growing firms investing in future capacity.</div>
                </div>
                <div style="background:#faf5ff; border-left:4px solid #a855f7; padding:0.6rem;">
                    <strong style="color:#7e22ce;">3. Cash from Financing Activities (CFF):</strong>
                    <div style="font-size:0.85rem; color:#334155;">Transactions with financial capital providers: Issuing new shares (+), borrowing debt (+), repaying debt principal (−), and paying dividends to equity holders (−).</div>
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The Cash Flow Trinity</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.5rem; text-align:center; font-size:0.8rem;">
                    <div style="background:#ecfdf5; border:1px solid #86efac; padding:0.6rem 0.3rem; border-radius:8px;">
                        <div style="font-size:1.5rem;">🏭</div>
                        <div style="font-weight:bold; color:#166534; margin:0.3rem 0;">CFO</div>
                        <div style="font-size:0.75rem; color:#14532d;">Core Business Sales & Bills</div>
                        <div style="margin-top:0.5rem; color:#15803d; font-weight:bold;">Healthy: (+)</div>
                    </div>
                    <div style="background:#eff6ff; border:1px solid #93c5fd; padding:0.6rem 0.3rem; border-radius:8px;">
                        <div style="font-size:1.5rem;">🏗️</div>
                        <div style="font-weight:bold; color:#1e40af; margin:0.3rem 0;">CFI</div>
                        <div style="font-size:0.75rem; color:#1e3a8a;">Capex & Equipment</div>
                        <div style="margin-top:0.5rem; color:#2563eb; font-weight:bold;">Growing: (−)</div>
                    </div>
                    <div style="background:#faf5ff; border:1px solid #d8b4fe; padding:0.6rem 0.3rem; border-radius:8px;">
                        <div style="font-size:1.5rem;">🏦</div>
                        <div style="font-weight:bold; color:#6b21a8; margin:0.3rem 0;">CFF</div>
                        <div style="font-size:0.75rem; color:#581c87;">Debt & Dividends</div>
                        <div style="margin-top:0.5rem; color:#9333ea; font-weight:bold;">Variable (+/−)</div>
                    </div>
                </div>
                <div style="text-align:center; margin-top:0.75rem; font-size:0.8rem; background:#f8fafc; padding:0.4rem; border-radius:6px; font-weight:bold;">
                    Net Change in Cash = CFO + CFI + CFF
                </div>
            </div>
        """
    },

    # SLIDE 39
    {
        "id": 39,
        "module": "Module 3 · Statements Linkage",
        "title": "Reconciling Net Income to Operating Cash Flow",
        "subtitle": "The exact indirect method step-by-step arithmetic",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>How Accrual Profit Converts to Cash Flow</h3>
            <p>Under the Indirect Method, we start with Net Income (PAT) and adjust for non-cash items and working capital changes:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <tr><th>Item</th><th>Adjustment</th><th>Why? Intuition</th></tr>
                    <tr><td><strong>Net Income (PAT)</strong></td><td>Starting Point</td><td>Includes accruals & non-cash items</td></tr>
                    <tr><td><strong>+ Depreciation & Amortisation</strong></td><td><span class="badge badge-success">ADD BACK</span></td><td>Non-cash expense; no actual cash left the bank account!</td></tr>
                    <tr><td><strong>− Increase in Debtors (Receivables)</strong></td><td><span class="badge badge-danger">SUBTRACT</span></td><td>Sales were recognized in P&L, but cash has not yet been received.</td></tr>
                    <tr><td><strong>− Increase in Inventory</strong></td><td><span class="badge badge-danger">SUBTRACT</span></td><td>Cash was spent to manufacture/buy goods that sit unsold.</td></tr>
                    <tr><td><strong>+ Increase in Creditors (Payables)</strong></td><td><span class="badge badge-success">ADD</span></td><td>We received goods/services without paying cash yet (free financing).</td></tr>
                </table>
            </div>
            <div class="callout callout-danger" style="margin-top:0.75rem;">
                <strong>🎯 Golden Working Capital Rule for MCQs:</strong><br>
                • Increase in Current Assets = <strong>Cash OUTFLOW</strong> (Subtract)<br>
                • Increase in Current Liabilities = <strong>Cash INFLOW</strong> (Add)
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The Cash Conversion Formula</h4>
                <div style="background:#f8fafc; border:2px dashed #cbd5e1; border-radius:8px; padding:0.8rem; font-size:0.85rem; line-height:1.8;">
                    <div style="font-weight:bold; color:#1e40af;">CFO = PAT</div>
                    <div style="color:#059669; font-weight:bold;">+ Non-Cash Expenses (Depreciation)</div>
                    <div style="color:#dc2626; font-weight:bold;">− Δ Current Assets (excluding cash)</div>
                    <div style="color:#059669; font-weight:bold;">+ Δ Current Liabilities</div>
                </div>
                <div style="margin-top:0.8rem; background:#eff6ff; padding:0.6rem; border-radius:6px; font-size:0.8rem; color:#1e3a8a;">
                    <strong>Worked Numerical Quick Check:</strong><br>
                    PAT = ₹10L | Depr = ₹2L | AR rose by ₹3L | AP rose by ₹1L<br>
                    <strong>CFO</strong> = 10 + 2 − 3 + 1 = <strong>₹10 Lakhs</strong>.
                </div>
            </div>
        """
    },

    # SLIDE 40
    {
        "id": 40,
        "module": "Module 3 · Statements Linkage",
        "title": "Why Profit != Cash: The Working Capital Trap",
        "subtitle": "How profitable companies go bankrupt (Overtrading)",
        "badge": "EXAM TRAP",
        "badge_type": "danger",
        "content_html": """
            <h3>The Myth of Profit Equal to Cash</h3>
            <p>Students frequently confuse high Net Profit with financial safety. A company can show massive accounting profits while running out of cash to pay bills tomorrow:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-top:0.75rem;">
                <div style="background:#fff1f2; border:1px solid #fecdd3; border-radius:8px; padding:0.75rem;">
                    <h4 style="color:#e11d48; font-size:0.9rem; margin-bottom:0.4rem;">High Profit, Negative Cash Flow</h4>
                    <p style="font-size:0.85rem; line-height:1.6; color:#475569;">
                        Company sells ₹1 Crore worth of goods on 180-day credit. Revenue is recognized immediately; Profit shows ₹25 Lakhs. But <strong>zero cash</strong> is collected. Company cannot pay employee salaries or rent!
                    </p>
                </div>
                <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:8px; padding:0.75rem;">
                    <h4 style="color:#16a34a; font-size:0.9rem; margin-bottom:0.4rem;">Low Profit, Positive Cash Flow</h4>
                    <p style="font-size:0.85rem; line-height:1.6; color:#475569;">
                        Company records heavy depreciation on machinery (slashing accounting profit), but collects cash immediately upfront from retail customers (e.g., supermarkets, airlines, telecom). Bank balance swells!
                    </p>
                </div>
            </div>
            <div class="callout callout-warning" style="margin-top:0.75rem;">
                <strong>⚠️ Terminology: Overtrading</strong> occurs when a business expands revenue too rapidly without sufficient working capital, causing liquidity collapse.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The Profit vs Cash Divergence</h4>
                <div style="display:flex; justify-content:space-around; align-items:center; text-align:center; padding:1rem 0;">
                    <div style="width:45%; background:#ecfdf5; border:2px solid #10b981; border-radius:8px; padding:0.75rem;">
                        <div style="font-size:1.8rem;">📈</div>
                        <div style="font-weight:bold; color:#065f46; font-size:1rem;">P&L Statement</div>
                        <div style="font-size:0.8rem; color:#047857; margin-top:0.3rem;">Accrual Accounting</div>
                        <div style="font-size:0.75rem; color:#475569; margin-top:0.5rem;">"We earned profit on paper"</div>
                    </div>
                    <div style="font-size:1.5rem; color:#94a3b8; font-weight:bold;">≠</div>
                    <div style="width:45%; background:#eff6ff; border:2px solid #3b82f6; border-radius:8px; padding:0.75rem;">
                        <div style="font-size:1.8rem;">🏦</div>
                        <div style="font-weight:bold; color:#1e40af; font-size:1rem;">Cash Flow</div>
                        <div style="font-size:0.8rem; color:#1d4ed8; margin-top:0.3rem;">Real Bank Balance</div>
                        <div style="font-size:0.75rem; color:#475569; margin-top:0.5rem;">"We can settle bills today"</div>
                    </div>
                </div>
                <div style="text-align:center; font-size:0.85rem; font-weight:bold; color:#b91c1c; margin-top:0.5rem;">
                    "Revenue is vanity, Profit is sanity, Cash is reality!"
                </div>
            </div>
        """
    },

    # SLIDE 41
    {
        "id": 41,
        "module": "Module 4 · Financial Ratios",
        "title": "Financial Ratios: Master Classification & Purpose",
        "subtitle": "The 5 diagnostic pillars of corporate financial health",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Why Compute Financial Ratios?</h3>
            <p>Raw rupee numbers in financial statements are meaningless in isolation. A profit of ₹50 Crore means nothing unless compared to sales volume or capital invested:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; margin-top:0.75rem; font-size:0.85rem;">
                <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:0.5rem; border-radius:6px;">
                    <strong style="color:#2563eb;">1. Liquidity Ratios:</strong> Can the firm pay short-term bills due in 30–90 days? (Current, Quick, Cash).
                </div>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:0.5rem; border-radius:6px;">
                    <strong style="color:#059669;">2. Efficiency / Turnover Ratios:</strong> How rapidly are assets converted into sales and cash? (Inventory, Receivables, Payables).
                </div>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:0.5rem; border-radius:6px;">
                    <strong style="color:#d97706;">3. Solvency / Leverage Ratios:</strong> Can the firm survive long-term debt and interest obligations? (D/E, Interest Coverage).
                </div>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:0.5rem; border-radius:6px;">
                    <strong style="color:#7c3aed;">4. Profitability & Returns:</strong> How much margin is left for owners per ₹1 of sales or capital? (GP, Net Margin, ROCE, ROE).
                </div>
            </div>
            <div class="callout callout-info" style="margin-top:0.75rem;">
                <strong>📋 Exam Advantage:</strong> Ratio formulas are <strong>GIVEN on your exam formula sheet</strong>! Your focus must be on <em>interpretation, movement drivers, and traps</em>.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The Five Diagnostic Families</h4>
                <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.8rem;">
                    <div style="display:flex; justify-content:space-between; background:#eff6ff; padding:0.4rem 0.6rem; border-radius:6px;">
                        <strong>💧 Liquidity:</strong>
                        <span>Current, Quick, Cash Ratio</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; background:#ecfdf5; padding:0.4rem 0.6rem; border-radius:6px;">
                        <strong>⚙️ Efficiency:</strong>
                        <span>Turnover Days & Cycles</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; background:#fffbeb; padding:0.4rem 0.6rem; border-radius:6px;">
                        <strong>🛡️ Solvency:</strong>
                        <span>Debt/Equity & Coverage</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; background:#faf5ff; padding:0.4rem 0.6rem; border-radius:6px;">
                        <strong>📊 Profitability:</strong>
                        <span>Margins & DuPont ROE</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; background:#fdf2f8; padding:0.4rem 0.6rem; border-radius:6px;">
                        <strong>💎 Valuation:</strong>
                        <span>P/E, EV/EBITDA, Dividend Yield</span>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 42
    {
        "id": 42,
        "module": "Module 4 · Financial Ratios",
        "title": "Liquidity Ratios: Current Ratio (CR)",
        "subtitle": "Short-term buffer and the classic inventory trap",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Current Ratio: Formula & Benchmarks</h3>
            <p>Measures the ability to cover short-term obligations due within 1 year using short-term liquid assets:</p>
            <div class="formula-box">
                <div class="formula-name">Current Ratio Formula:</div>
                <div class="formula-code">Current Ratio = Current Assets / Current Liabilities</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.7; font-size:0.9rem;">
                <li><strong>Traditional Benchmark:</strong> <strong>2.0 : 1</strong> (or 1.5–2.0x for modern manufacturing).</li>
                <li><strong>Interpretation:</strong> A ratio of 2.0x means the firm possesses ₹2.00 of liquid resources for every ₹1.00 of debt falling due.</li>
                <li><strong>Too High (> 3.0x):</strong> Inefficient management! Cash sits idle or excessive unsaleable inventory is piling up.</li>
                <li><strong>Too Low (< 1.0x):</strong> Liquidity stress; firm relies on incoming cash flow or fresh bank overdrafts to survive.</li>
            </ul>
            <div class="callout callout-warning" style="margin-top:0.75rem;">
                <strong>⚠️ MCQ Trap:</strong> A high Current Ratio does NOT guarantee instant safety if 70% of Current Assets are obsolete inventory or disputed receivables!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Current Ratio Balance Barometer</h4>
                <div style="margin:1rem 0;">
                    <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#64748b; margin-bottom:0.25rem;">
                        <span>&lt; 1.0x (Danger)</span>
                        <span style="font-weight:bold; color:#059669;">1.5x – 2.0x (Healthy Zone)</span>
                        <span>&gt; 3.0x (Idle Assets)</span>
                    </div>
                    <div style="height:16px; background:linear-gradient(to right, #ef4444 0%, #f59e0b 30%, #10b981 50%, #3b82f6 100%); border-radius:8px;"></div>
                </div>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.8rem;">
                    <strong>Worked Numerical:</strong><br>
                    Current Assets = ₹60 Lakhs (Cash ₹10L, AR ₹20L, Inventory ₹30L)<br>
                    Current Liabilities = ₹30 Lakhs<br>
                    <strong>Current Ratio</strong> = 60 / 30 = <strong>2.0x</strong>.
                </div>
            </div>
        """
    },

    # SLIDE 43
    {
        "id": 43,
        "module": "Module 4 · Financial Ratios",
        "title": "Liquidity Ratios: Quick Ratio & Cash Ratio",
        "subtitle": "Stripping out illiquid inventories and prepayments",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Acid Test (Quick) & Super-Quick (Cash) Ratios</h3>
            <p>Inventory cannot be converted to cash immediately without offering deep discounts or waiting for customer orders:</p>
            <div class="formula-box">
                <div class="formula-name">Quick Ratio (Acid Test):</div>
                <div class="formula-code">Quick Ratio = (Current Assets − Inventory) / Current Liabilities</div>
            </div>
            <div class="formula-box" style="margin-top:0.5rem;">
                <div class="formula-name">Cash Ratio:</div>
                <div class="formula-code">Cash Ratio = (Cash & Cash Equivalents + Marketable Securities) / Current Liabilities</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Quick Ratio Benchmark:</strong> <strong>1.0 : 1</strong> is considered prudent.</li>
                <li><strong>Why exclude Inventory?</strong> Inventory requires a buyer, credit terms, and delivery before becoming cash.</li>
                <li><strong>Why exclude Prepaid Expenses?</strong> Prepayments cannot be refunded in cash to pay bank debts.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Liquidity Stripping Hierarchy</h4>
                <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.8rem;">
                    <div style="background:#eff6ff; border:1px solid #93c5fd; padding:0.5rem; border-radius:6px;">
                        <strong>Current Assets:</strong> Cash + AR + Prepaids + Inventory<br>
                        <span style="color:#1d4ed8; font-weight:bold;">Current Ratio = 60 / 30 = 2.0x</span>
                    </div>
                    <div style="background:#fefce8; border:1px solid #fde047; padding:0.5rem; border-radius:6px;">
                        <strong>Quick Assets:</strong> Cash + AR (Drop Inventory ₹30L)<br>
                        <span style="color:#b45309; font-weight:bold;">Quick Ratio = (60 − 30) / 30 = 1.0x</span>
                    </div>
                    <div style="background:#ecfdf5; border:1px solid #6ee7b7; padding:0.5rem; border-radius:6px;">
                        <strong>Cash Assets:</strong> Only Cash ₹10L (Drop AR ₹20L)<br>
                        <span style="color:#047857; font-weight:bold;">Cash Ratio = 10 / 30 = 0.33x</span>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 44
    {
        "id": 44,
        "module": "Module 4 · Financial Ratios",
        "title": "Efficiency Ratios: Inventory Days & Turnover",
        "subtitle": "How many times stock clears and days inventory sits on shelves",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Inventory Turnover & Holding Period</h3>
            <p>Measures how efficiently working capital tied up in warehouses is rotated into actual sales:</p>
            <div class="formula-box">
                <div class="formula-name">Inventory Turnover Ratio:</div>
                <div class="formula-code">Inventory Turnover = Cost of Goods Sold (COGS) / Average Inventory</div>
            </div>
            <div class="formula-box" style="margin-top:0.5rem;">
                <div class="formula-name">Days Sales of Inventory (DSI / Inventory Days):</div>
                <div class="formula-code">Inventory Days = (Average Inventory × 365) / COGS</div>
            </div>
            <div class="callout callout-danger" style="margin-top:0.75rem;">
                <strong>⚠️ MCQ Trap on Denominator:</strong> Always use <strong>COGS</strong> in the denominator (or numerator for days), NOT Sales! Inventory is valued at cost, so comparing it to selling price distorts the turnover with profit margin.
            </div>
            <p style="font-size:0.85rem; margin-top:0.5rem;">
                <strong>Interpretation:</strong> A lower Inventory Days number means stock sells faster, reducing warehousing costs and risk of spoilage or obsolescence.
            </p>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Worked Numerical Example</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.75rem; font-size:0.85rem; line-height:1.7;">
                    <div>• <strong>COGS:</strong> ₹1,200 Lakhs</div>
                    <div>• <strong>Average Inventory:</strong> ₹200 Lakhs</div>
                    <div style="margin-top:0.5rem; padding-top:0.5rem; border-top:1px dashed #cbd5e1;">
                        <strong>Inventory Turnover</strong> = 1,200 / 200 = <strong>6.0 times/year</strong>
                    </div>
                    <div style="margin-top:0.3rem;">
                        <strong>Inventory Days</strong> = (200 × 365) / 1,200 = <strong>60.8 days</strong>
                    </div>
                </div>
                <div style="margin-top:0.6rem; font-size:0.8rem; color:#475569; text-align:center;">
                    Goods sit in the warehouse for ~61 days before being sold.
                </div>
            </div>
        """
    },

    # SLIDE 45
    {
        "id": 45,
        "module": "Module 4 · Financial Ratios",
        "title": "Efficiency Ratios: Receivable Days & Debtor Turnover",
        "subtitle": "How long customers take to settle their credit invoices",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Receivables (Debtor) Days & Collection Period</h3>
            <p>Measures credit management effectiveness and customer payment discipline:</p>
            <div class="formula-box">
                <div class="formula-name">Receivable Turnover:</div>
                <div class="formula-code">Receivable Turnover = Credit Sales / Average Receivables (Debtors)</div>
            </div>
            <div class="formula-box" style="margin-top:0.5rem;">
                <div class="formula-name">Days Sales Outstanding (DSO / Receivable Days):</div>
                <div class="formula-code">Receivable Days = (Average Receivables × 365) / Total (or Credit) Sales</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Benchmark Comparison:</strong> Compare DSO against the company's stated credit terms (e.g., if terms are "Net 30" and DSO is 75 days, credit collection has collapsed).</li>
                <li><strong>Rising DSO Danger:</strong> Indicates aggressive revenue booking, deteriorating customer creditworthiness, or imminent bad debts.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Receivable Collection Numerical</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.75rem; font-size:0.85rem; line-height:1.7;">
                    <div>• <strong>Annual Credit Sales:</strong> ₹3,650 Lakhs</div>
                    <div>• <strong>Trade Receivables:</strong> ₹300 Lakhs</div>
                    <div style="margin-top:0.5rem; padding-top:0.5rem; border-top:1px dashed #cbd5e1;">
                        <strong>Receivable Turnover</strong> = 3,650 / 300 = <strong>12.17x</strong>
                    </div>
                    <div style="margin-top:0.3rem;">
                        <strong>Receivable Days</strong> = (300 × 365) / 3,650 = <strong>30.0 days</strong>
                    </div>
                </div>
                <div style="margin-top:0.6rem; font-size:0.8rem; color:#059669; text-align:center; font-weight:bold;">
                    Clean 30-day collection cycle matching standard corporate terms!
                </div>
            </div>
        """
    },

    # SLIDE 46
    {
        "id": 46,
        "module": "Module 4 · Financial Ratios",
        "title": "Efficiency Ratios: Payable Days & Creditor Turnover",
        "subtitle": "How long the firm delays paying its suppliers for free funding",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Payable (Creditor) Days & Supplier Credit</h3>
            <p>Measures how effectively a firm utilizes interest-free trade credit granted by suppliers:</p>
            <div class="formula-box">
                <div class="formula-name">Payable Turnover:</div>
                <div class="formula-code">Payable Turnover = Annual Purchases (or COGS) / Average Payables</div>
            </div>
            <div class="formula-box" style="margin-top:0.5rem;">
                <div class="formula-name">Days Payables Outstanding (DPO / Payable Days):</div>
                <div class="formula-code">Payable Days = (Average Payables × 365) / Cost of Goods Sold (COGS)</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Longer DPO is good for cash:</strong> Stretches free supplier financing, preserving cash inside the bank account.</li>
                <li><strong>DPO Risk:</strong> If stretched excessively, suppliers may stop shipments, cancel trade discounts, or demand advance cash payments.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Payable Days Numerical</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.75rem; font-size:0.85rem; line-height:1.7;">
                    <div>• <strong>COGS:</strong> ₹1,825 Lakhs</div>
                    <div>• <strong>Trade Payables:</strong> ₹250 Lakhs</div>
                    <div style="margin-top:0.5rem; padding-top:0.5rem; border-top:1px dashed #cbd5e1;">
                        <strong>Payable Days</strong> = (250 × 365) / 1,825 = <strong>50.0 days</strong>
                    </div>
                </div>
                <div style="margin-top:0.6rem; font-size:0.8rem; background:#eff6ff; padding:0.5rem; border-radius:6px; color:#1e40af;">
                    <strong>Insight:</strong> The company enjoys 50 days of free supplier funding before cash leaves the account.
                </div>
            </div>
        """
    },

    # SLIDE 47
    {
        "id": 47,
        "module": "Module 4 · Financial Ratios",
        "title": "Operating Cycle & Cash Conversion Cycle (CCC)",
        "subtitle": "The master arithmetic of working capital efficiency",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Operating Cycle vs Cash Conversion Cycle</h3>
            <p>Tracks the journey of ₹1 from purchasing raw material to receiving cash from customer:</p>
            <div class="formula-box">
                <div class="formula-name">Operating Cycle (Gross):</div>
                <div class="formula-code">Operating Cycle = Inventory Days + Receivable Days</div>
            </div>
            <div class="formula-box" style="margin-top:0.5rem;">
                <div class="formula-name">Cash Conversion Cycle (CCC / Net Cycle):</div>
                <div class="formula-code">Cash Conversion Cycle = Inventory Days + Receivable Days − Payable Days</div>
            </div>
            <div class="callout callout-info" style="margin-top:0.75rem;">
                <strong>Negative Working Capital:</strong> If Payable Days exceeds (Inventory + Receivable Days), CCC is <strong>NEGATIVE</strong> (e.g., Amazon, Walmart, McDonald's). The company is funded completely by suppliers and customers!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Visual Timeline of the CCC</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.8rem;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem;">
                        <span style="color:#d97706; font-weight:bold;">+ Inventory Days (60 d)</span>
                        <span style="color:#2563eb; font-weight:bold;">+ Receivable Days (30 d)</span>
                    </div>
                    <div style="background:#fed7aa; height:12px; border-radius:4px; margin-bottom:0.5rem;"></div>
                    <div style="color:#475569; font-size:0.75rem;">Total Operating Cycle = 60 + 30 = <strong>90 Days</strong></div>
                    <div style="margin-top:0.6rem; display:flex; justify-content:space-between;">
                        <span style="color:#16a34a; font-weight:bold;">− Payable Days (50 d)</span>
                        <span style="color:#dc2626; font-weight:bold;">= CCC (40 Days)</span>
                    </div>
                    <div style="background:#bbf7d0; height:12px; border-radius:4px; margin-bottom:0.3rem;"></div>
                </div>
                <div style="text-align:center; font-weight:bold; color:#1e40af; margin-top:0.5rem; font-size:0.85rem;">
                    Working Capital financing required for exactly 40 days!
                </div>
            </div>
        """
    },

    # SLIDE 48
    {
        "id": 48,
        "module": "Module 4 · Financial Ratios",
        "title": "Solvency & Leverage Ratios: Debt-to-Equity (D/E)",
        "subtitle": "Financial gearing, bankruptcy risk, and capital structure",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Debt-to-Equity (D/E) Ratio</h3>
            <p>Measures the proportion of borrowed funds (debt) compared to owners' capital (equity):</p>
            <div class="formula-box">
                <div class="formula-name">Debt-to-Equity Ratio:</div>
                <div class="formula-code">Debt-to-Equity = Total Debt / Total Shareholders' Equity</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Benchmark:</strong> Generally <strong>&lt; 1.0x to 1.5x</strong> for manufacturing. Capital-heavy utilities/infrastructure may sustain 2.0x.</li>
                <li><strong>High Leverage Benefit:</strong> In boom years, debt magnifies Return on Equity (ROE) because interest is fixed and tax-deductible.</li>
                <li><strong>High Leverage Risk:</strong> In recessions, fixed interest must be paid regardless of revenue, driving over-leveraged firms into liquidation.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Leverage Comparison</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; text-align:center; font-size:0.8rem;">
                    <div style="background:#f0fdf4; border:1px solid #86efac; padding:0.6rem; border-radius:8px;">
                        <strong style="color:#15803d;">Conservative Firm</strong>
                        <div style="margin-top:0.3rem;">Debt: ₹20L | Equity: ₹100L</div>
                        <div style="font-size:1.1rem; font-weight:bold; color:#166534; margin:0.3rem 0;">D/E = 0.20x</div>
                        <div style="font-size:0.75rem; color:#475569;">Pristine solvency; zero default risk</div>
                    </div>
                    <div style="background:#fef2f2; border:1px solid #fca5a5; padding:0.6rem; border-radius:8px;">
                        <strong style="color:#b91c1c;">Aggressive Firm</strong>
                        <div style="margin-top:0.3rem;">Debt: ₹300L | Equity: ₹100L</div>
                        <div style="font-size:1.1rem; font-weight:bold; color:#991b1b; margin:0.3rem 0;">D/E = 3.00x</div>
                        <div style="font-size:0.75rem; color:#475569;">High financial risk; vulnerable to downturns</div>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 49
    {
        "id": 49,
        "module": "Module 4 · Financial Ratios",
        "title": "Coverage Ratios: Interest Coverage Ratio (ICR)",
        "subtitle": "How comfortably operating profit services debt interest",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Interest Coverage Ratio (Times Interest Earned)</h3>
            <p>Evaluates whether operating earnings provide sufficient safety cushion to pay annual debt interest:</p>
            <div class="formula-box">
                <div class="formula-name">Interest Coverage Ratio:</div>
                <div class="formula-code">Interest Coverage = EBIT (Operating Profit) / Interest Expense</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Benchmark:</strong> <strong>&gt; 3.0x</strong> is safe; <strong>&gt; 5.0x</strong> is healthy.</li>
                <li><strong>Danger Threshold:</strong> <strong>&lt; 1.5x</strong> signals distress. If <strong>&lt; 1.0x</strong>, the company does not even earn enough from operations to service its debt!</li>
                <li><strong>Lender Perspective:</strong> Banks will refuse additional debt financing if ICR slips below 2.0x.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Interest Coverage Zones</h4>
                <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.8rem;">
                    <div style="background:#fee2e2; border-left:4px solid #ef4444; padding:0.4rem 0.6rem;">
                        <strong>ICR &lt; 1.5x (Distress):</strong> High default risk. Cannot service interest if sales dip slightly.
                    </div>
                    <div style="background:#fef3c7; border-left:4px solid #f59e0b; padding:0.4rem 0.6rem;">
                        <strong>ICR 1.5x – 3.0x (Moderate):</strong> Vulnerable during economic downturns.
                    </div>
                    <div style="background:#dcfce7; border-left:4px solid #22c55e; padding:0.4rem 0.6rem;">
                        <strong>ICR &gt; 5.0x (Pristine):</strong> Asian Paints = 35.1x! Substantial buffer against rate shocks.
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 50
    {
        "id": 50,
        "module": "Module 4 · Financial Ratios",
        "title": "Profitability Ratios: Gross Margin & Operating Margin",
        "subtitle": "Distinguishing manufacturing markup from operational efficiency",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Gross Profit Margin vs Operating Profit Margin</h3>
            <p>Tracks how much profit remains from each ₹1 of sales after deducting successive expense tiers:</p>
            <div class="formula-box">
                <div class="formula-name">Gross Profit Margin:</div>
                <div class="formula-code">Gross Margin (%) = (Gross Profit / Sales Revenue) × 100</div>
            </div>
            <div class="formula-box" style="margin-top:0.5rem;">
                <div class="formula-name">Operating Profit Margin (EBIT Margin):</div>
                <div class="formula-code">Operating Margin (%) = (EBIT / Sales Revenue) × 100</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Gross Margin</strong> reflects product pricing power, brand strength, and raw material procurement efficiency.</li>
                <li><strong>Operating Margin</strong> incorporates overhead control (admin, sales, marketing, R&D).</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Margin Erosion Cascade</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.8rem; line-height:1.7;">
                    <div>Sales Revenue: ₹100.00 (100.0%)</div>
                    <div style="color:#dc2626;">− COGS: ₹60.00</div>
                    <div style="font-weight:bold; color:#1e40af; border-top:1px dashed #cbd5e1; padding-top:0.2rem;">
                        = Gross Profit: ₹40.00 (40.0% Gross Margin)
                    </div>
                    <div style="color:#dc2626;">− SG&A / Opex: ₹25.00</div>
                    <div style="font-weight:bold; color:#059669; border-top:1px dashed #cbd5e1; padding-top:0.2rem;">
                        = EBIT: ₹15.00 (15.0% Operating Margin)
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 51
    {
        "id": 51,
        "module": "Module 4 · Financial Ratios",
        "title": "Profitability Ratios: Net Profit Margin & EBITDA Margin",
        "subtitle": "Bottom-line owner returns vs pure operating cash margin",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Net Profit Margin & EBITDA Margin</h3>
            <p>Comparing pure operational cash earnings to the final bottom line:</p>
            <div class="formula-box">
                <div class="formula-name">Net Profit Margin (PAT Margin):</div>
                <div class="formula-code">Net Profit Margin (%) = (PAT / Sales Revenue) × 100</div>
            </div>
            <div class="formula-box" style="margin-top:0.5rem;">
                <div class="formula-name">EBITDA Margin:</div>
                <div class="formula-code">EBITDA Margin (%) = (EBITDA / Sales Revenue) × 100</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Why EBITDA?</strong> Earnings Before Interest, Tax, Depreciation, and Amortisation removes accounting policy distortions (SLM vs WDV) and capital structure differences.</li>
                <li><strong>Net Margin reflects everything:</strong> Operations, financing costs, and taxes all impact PAT.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">EBITDA to PAT Bridge</h4>
                <div style="display:flex; flex-direction:column; gap:0.3rem; font-size:0.8rem;">
                    <div style="background:#eff6ff; padding:0.4rem 0.6rem; border-radius:6px; font-weight:bold; color:#1e40af;">
                        EBITDA (Pure Operating Cash Flow Proxy)
                    </div>
                    <div style="text-align:center; font-size:0.75rem; color:#64748b;">↓ Deduct: Depreciation & Amortisation (Non-cash)</div>
                    <div style="background:#f1f5f9; padding:0.4rem 0.6rem; border-radius:6px; font-weight:bold; color:#334155;">
                        EBIT (Operating Profit)
                    </div>
                    <div style="text-align:center; font-size:0.75rem; color:#64748b;">↓ Deduct: Interest & Taxes</div>
                    <div style="background:#ecfdf5; padding:0.4rem 0.6rem; border-radius:6px; font-weight:bold; color:#065f46;">
                        PAT (Net Profit Margin)
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 52
    {
        "id": 52,
        "module": "Module 4 · Financial Ratios",
        "title": "Return on Capital Employed (ROCE)",
        "subtitle": "The true test of management's overall capital efficiency",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Return on Capital Employed (ROCE)</h3>
            <p>Measures how efficiently management generates operating profits from all long-term capital invested:</p>
            <div class="formula-box">
                <div class="formula-name">ROCE Formula:</div>
                <div class="formula-code">ROCE = EBIT / Capital Employed</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:0.6rem; border-radius:6px; margin-top:0.5rem; font-size:0.85rem;">
                <strong>What is Capital Employed?</strong><br>
                • <em>Asset Side:</em> Total Assets − Current Liabilities<br>
                • <em>Liability Side:</em> Shareholders' Equity + Long-Term Debt
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>The Hurdle Rate Rule:</strong> ROCE must be <strong>greater than the Cost of Capital (WACC)</strong> to create economic shareholder value.</li>
                <li><strong>Why EBIT in numerator?</strong> Capital Employed includes both debt and equity; EBIT is the total return before splitting between debt interest and equity profit.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">ROCE Alignment Principle</h4>
                <div style="background:#eff6ff; border:1px solid #93c5fd; border-radius:8px; padding:0.8rem; text-align:center;">
                    <div style="font-size:1.1rem; font-weight:bold; color:#1e40af;">
                        EBIT (Return to All Capital Providers)
                    </div>
                    <div style="border-top:2px solid #3b82f6; margin:0.5rem 2rem;"></div>
                    <div style="font-size:1.1rem; font-weight:bold; color:#1e40af;">
                        Equity + Debt (Total Long-Term Capital)
                    </div>
                </div>
                <div style="text-align:center; font-size:0.8rem; color:#475569; margin-top:0.75rem;">
                    Both numerator and denominator include Debt and Equity! Perfect consistency.
                </div>
            </div>
        """
    }
]

print(f"Loaded {len(slides_36_to_52)} slides in Part 2-A.")
