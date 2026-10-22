# slides_part2_b.py
# Slides 53 to 70: DuPont Analysis, Valuation, Asian Paints Case Study, and Cost Accounting

slides_53_to_70 = [
    # SLIDE 53
    {
        "id": 53,
        "module": "Module 4 · Financial Ratios",
        "title": "Return on Equity (ROE) & Shareholder Wealth",
        "subtitle": "The ultimate bottom-line benchmark and its leverage trap",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Return on Equity (ROE)</h3>
            <p>Measures how many rupees of net profit management generates for every ₹100 of shareholders' net worth:</p>
            <div class="formula-box">
                <div class="formula-name">Return on Equity Formula:</div>
                <div class="formula-code">ROE = PAT (Net Income) / Shareholders' Equity</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>The Shareholder Standard:</strong> High sustained ROE (> 15–20%) is the hallmark of great compounder companies.</li>
                <li><strong>The Dangerous Trap:</strong> ROE can be artificially boosted by taking on massive, dangerous debt! When Equity shrinks relative to Total Assets, ROE explodes upwards even if operating efficiency is deteriorating.</li>
            </ul>
            <div class="callout callout-warning" style="margin-top:0.75rem;">
                <strong>⚠️ Why DuPont Analysis is essential:</strong> The 3-step DuPont identity breaks ROE apart to reveal whether high returns come from good margins, high turnover, or just dangerous leverage.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">ROE Distortion Risk</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; text-align:center; font-size:0.8rem;">
                    <div style="background:#eff6ff; border:1px solid #bfdbfe; padding:0.6rem; border-radius:8px;">
                        <strong style="color:#1d4ed8;">Firm A (Zero Debt)</strong>
                        <div style="margin-top:0.3rem;">PAT: ₹15L | Equity: ₹100L</div>
                        <div style="font-size:1.1rem; font-weight:bold; color:#1e40af; margin:0.3rem 0;">ROE = 15%</div>
                        <div style="font-size:0.75rem; color:#475569;">100% genuine operational return</div>
                    </div>
                    <div style="background:#fef2f2; border:1px solid #fecdd3; padding:0.6rem; border-radius:8px;">
                        <strong style="color:#b91c1c;">Firm B (90% Debt Funded)</strong>
                        <div style="margin-top:0.3rem;">PAT: ₹5L | Equity: ₹10L</div>
                        <div style="font-size:1.1rem; font-weight:bold; color:#991b1b; margin:0.3rem 0;">ROE = 50%!</div>
                        <div style="font-size:0.75rem; color:#b91c1c; font-weight:bold;">Massive bankruptcy risk!</div>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 54
    {
        "id": 54,
        "module": "Module 4 · Financial Ratios",
        "title": "The 3-Step DuPont Identity: Mathematical Breakdown",
        "subtitle": "Margin × Turnover × Financial Leverage",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>The DuPont 3-Way Decomposition</h3>
            <p>DuPont decomposes ROE into three intuitive drivers by multiplying and dividing by Sales and Total Assets:</p>
            <div class="formula-box">
                <div class="formula-name">The 3-Step DuPont Identity:</div>
                <div class="formula-code">ROE = (PAT / Sales) × (Sales / Total Assets) × (Total Assets / Equity)</div>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.4rem; margin-top:0.75rem; text-align:center; font-size:0.8rem;">
                <div style="background:#ecfdf5; border:1px solid #a7f3d0; padding:0.5rem; border-radius:6px;">
                    <strong style="color:#065f46;">1. Net Profit Margin</strong><br>
                    <span>(PAT / Sales)</span><br>
                    <span style="font-size:0.75rem; color:#047857;">Pricing power & cost control</span>
                </div>
                <div style="background:#eff6ff; border:1px solid #bfdbfe; padding:0.5rem; border-radius:6px;">
                    <strong style="color:#1e40af;">2. Asset Turnover</strong><br>
                    <span>(Sales / Total Assets)</span><br>
                    <span style="font-size:0.75rem; color:#1d4ed8;">Volume & asset utilization</span>
                </div>
                <div style="background:#faf5ff; border:1px solid #e9d5ff; padding:0.5rem; border-radius:6px;">
                    <strong style="color:#6b21a8;">3. Equity Multiplier</strong><br>
                    <span>(Assets / Equity)</span><br>
                    <span style="font-size:0.75rem; color:#581c87;">Financial leverage (1 + D/E)</span>
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">DuPont Mathematical Cancellation</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.8rem; text-align:center; font-family:monospace; font-size:0.95rem;">
                    ROE = <span style="color:#059669;">(PAT / <strike style="color:#94a3b8;">Sales</strike>)</span> × 
                    <span style="color:#2563eb;">(<strike style="color:#94a3b8;">Sales</strike> / <strike style="color:#64748b;">Assets</strike>)</span> × 
                    <span style="color:#7c3aed;">(<strike style="color:#64748b;">Assets</strike> / Equity)</span>
                </div>
                <div style="text-align:center; margin-top:0.75rem; font-size:0.85rem; font-weight:bold; color:#1e40af;">
                    Sales & Assets cancel out perfectly to leave: PAT / Equity!
                </div>
            </div>
        """
    },

    # SLIDE 55
    {
        "id": 55,
        "module": "Module 4 · Financial Ratios",
        "title": "DuPont Strategic Diagnostics: 3 Business Models",
        "subtitle": "How different industries achieve superior return on equity",
        "badge": "STRATEGY",
        "badge_type": "primary",
        "content_html": """
            <h3>Three Distinct Paths to 20% ROE</h3>
            <p>Every industry achieves its ROE through a fundamentally different combination of the 3 DuPont levers:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.8rem;">
                    <tr><th>Business Model</th><th>Net Margin</th><th>Asset Turnover</th><th>Leverage</th><th>Resulting ROE</th></tr>
                    <tr><td><strong>1. High-Margin Luxury / Tech</strong> (Apple, Rolex, Titan)</td><td><strong style="color:#059669;">25.0%</strong> (High)</td><td>0.80x (Low)</td><td>1.00x (No debt)</td><td><strong>20.0%</strong></td></tr>
                    <tr><td><strong>2. High-Turnover Retail</strong> (D-Mart, Walmart, Costco)</td><td>3.0% (Razor-thin)</td><td><strong style="color:#2563eb;">5.00x</strong> (Blazing)</td><td>1.33x (Low debt)</td><td><strong>20.0%</strong></td></tr>
                    <tr><td><strong>3. High-Leverage Banking</strong> (HDFC Bank, SBI)</td><td>15.0% (Moderate)</td><td>0.15x (Slow)</td><td><strong style="color:#dc2626;">8.90x</strong> (High debt)</td><td><strong>20.0%</strong></td></tr>
                </table>
            </div>
            <div class="callout callout-info" style="margin-top:0.75rem;">
                <strong>Exam Rule:</strong> High turnover offsets low margins; high margin offsets low turnover.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The Three ROE Engines</h4>
                <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.8rem;">
                    <div style="background:#eff6ff; padding:0.5rem; border-radius:6px; border-left:4px solid #3b82f6;">
                        <strong>Apple / Pharma:</strong> Premium pricing power (Margin Driven)
                    </div>
                    <div style="background:#ecfdf5; padding:0.5rem; border-radius:6px; border-left:4px solid #10b981;">
                        <strong>D-Mart / Supermarkets:</strong> Rapid inventory velocity (Turnover Driven)
                    </div>
                    <div style="background:#fef2f2; padding:0.5rem; border-radius:6px; border-left:4px solid #ef4444;">
                        <strong>Commercial Banks:</strong> Customer deposits as debt (Leverage Driven)
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 56
    {
        "id": 56,
        "module": "Module 4 · Financial Ratios",
        "title": "Valuation Multiples: P/E, Dividend Yield & Payout",
        "subtitle": "Connecting market stock prices to fundamental accounting metrics",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Market Valuation Multiples</h3>
            <p>How stock market investors price earnings and cash distributions:</p>
            <div class="formula-box">
                <div class="formula-name">Price-to-Earnings (P/E) Ratio:</div>
                <div class="formula-code">P/E = Market Price per Share / Earnings per Share (EPS)</div>
            </div>
            <div class="formula-box" style="margin-top:0.4rem;">
                <div class="formula-name">Dividend Yield:</div>
                <div class="formula-code">Dividend Yield (%) = (Dividend per Share / Market Price per Share) × 100</div>
            </div>
            <div class="formula-box" style="margin-top:0.4rem;">
                <div class="formula-name">Dividend Payout Ratio:</div>
                <div class="formula-code">Payout Ratio (%) = (Total Dividends / PAT) = (DPS / EPS) × 100</div>
            </div>
            <p style="font-size:0.85rem; margin-top:0.5rem;">
                <strong>Retention Ratio (Ploughback):</strong> 100% − Payout Ratio. What portion of profits is retained to fund future growth.
            </p>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Valuation Numerical</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.8rem; line-height:1.7;">
                    <div>• <strong>Market Price per share:</strong> ₹500</div>
                    <div>• <strong>EPS:</strong> ₹25 | <strong>DPS:</strong> ₹10</div>
                    <div style="margin-top:0.4rem; padding-top:0.4rem; border-top:1px dashed #cbd5e1;">
                        <strong>P/E Ratio</strong> = 500 / 25 = <strong>20.0x</strong>
                    </div>
                    <div>
                        <strong>Dividend Yield</strong> = (10 / 500) × 100 = <strong>2.0%</strong>
                    </div>
                    <div>
                        <strong>Payout Ratio</strong> = (10 / 25) × 100 = <strong>40.0%</strong> (Retention = 60%)
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 57
    {
        "id": 57,
        "module": "Module 4 · Financial Ratios",
        "title": "Enterprise Value (EV) & The Capital-Neutral Multiple",
        "subtitle": "Why EV is superior to Market Cap for acquisitions",
        "badge": "VALUATION",
        "badge_type": "primary",
        "content_html": """
            <h3>Enterprise Value (EV) Architecture</h3>
            <p>If you bought 100% of a company today, you would have to buy out the equity AND repay all its lenders, but you would get to keep all the cash in the bank:</p>
            <div class="formula-box">
                <div class="formula-name">Enterprise Value Formula:</div>
                <div class="formula-code">EV = Market Capitalization + Total Debt − Cash & Cash Equivalents</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Why subtract cash?</strong> Cash in the bank can immediately be used to pay off existing debt.</li>
                <li><strong>Net Debt:</strong> Total Debt − Cash. If Cash > Debt, Net Debt is negative!</li>
                <li><strong>EV / EBITDA Multiple:</strong> Measures takeover price against operating cash generation, completely independent of how much debt or equity is used.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Enterprise Value Building Blocks</h4>
                <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.8rem;">
                    <div style="background:#eff6ff; padding:0.5rem; border-radius:6px; border:1px solid #93c5fd;">
                        <strong>+ Market Capitalization:</strong> Value of all equity shares
                    </div>
                    <div style="background:#fee2e2; padding:0.5rem; border-radius:6px; border:1px solid #fca5a5;">
                        <strong>+ Total Debt:</strong> Bank loans & debentures to settle
                    </div>
                    <div style="background:#dcfce7; padding:0.5rem; border-radius:6px; border:1px solid #86efac;">
                        <strong>− Cash in Bank:</strong> Available to offset debt immediately
                    </div>
                    <div style="background:#faf5ff; padding:0.5rem; border-radius:6px; font-weight:bold; color:#6b21a8; text-align:center;">
                        = Enterprise Value (True Takeover Cost)
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 58
    {
        "id": 58,
        "module": "Module 5 · Corporate Case Study",
        "title": "Asian Paints FY25 Profile & Income Statement",
        "subtitle": "Real-world financial analysis from the speed-run lecture",
        "badge": "CASE STUDY",
        "badge_type": "success",
        "content_html": """
            <h3>Asian Paints Standalone FY25 Income Statement</h3>
            <p>Asian Paints represents India's premier decorative paints manufacturer. Lecture data reveals exact audited figures:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.8rem;">
                    <tr><th>Line Item</th><th>Amount (₹ Crores)</th><th>% of Revenue</th></tr>
                    <tr><td><strong>Revenue from Operations</strong></td><td><strong>₹29,552.65 cr</strong></td><td>100.0%</td></tr>
                    <tr><td><strong>Cost of Goods Sold (COGS)</strong></td><td>₹17,340.54 cr</td><td>58.7%</td></tr>
                    <tr><td><strong>Gross Profit</strong></td><td><strong>₹12,212.11 cr</strong></td><td><strong>41.3%</strong></td></tr>
                    <tr><td>Operating Expenses & Other Costs</td><td>₹7,166.74 cr</td><td>24.2%</td></tr>
                    <tr><td><strong>Operating Profit (EBIT)</strong></td><td><strong>₹5,045.37 cr</strong></td><td><strong>17.1%</strong></td></tr>
                    <tr><td>Finance Costs (Interest)</td><td>₹143.68 cr</td><td>0.5%</td></tr>
                    <tr><td>Tax Expense</td><td>₹1,313.62 cr</td><td>4.5%</td></tr>
                    <tr><td><strong>Net Profit (PAT)</strong></td><td><strong>₹3,588.07 cr</strong></td><td><strong>12.1%</strong></td></tr>
                </table>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">FY25 Margin Profile</h4>
                <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.8rem;">
                    <div style="background:#eff6ff; padding:0.5rem; border-radius:6px;">
                        <strong>Gross Margin: 41.3%</strong><br>
                        Exceptional pricing power over crude oil derivative raw materials.
                    </div>
                    <div style="background:#f0fdf4; padding:0.5rem; border-radius:6px;">
                        <strong>Operating Margin (EBIT): 17.1%</strong><br>
                        Tight logistics and direct-to-dealer network with zero wholesalers.
                    </div>
                    <div style="background:#faf5ff; padding:0.5rem; border-radius:6px;">
                        <strong>Net Margin (PAT): 12.1%</strong><br>
                        Healthy double-digit bottom line conversion.
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 59
    {
        "id": 59,
        "module": "Module 5 · Corporate Case Study",
        "title": "Asian Paints Balance Sheet & Capital Structure",
        "subtitle": "Pristine fortress balance sheet with negligible debt",
        "badge": "CASE STUDY",
        "badge_type": "success",
        "content_html": """
            <h3>Asian Paints Balance Sheet Metrics</h3>
            <p>The balance sheet reveals the financial strength that underpins decades of steady shareholder wealth creation:</p>
            <ul style="margin-left:1.5rem; line-height:1.7; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Shareholders' Net Worth (Equity):</strong> ~₹19,000 Crores (Funded almost entirely by accumulated retained earnings over 50 years).</li>
                <li><strong>Total Debt:</strong> Only ~₹1,100 Crores (Tiny short-term working capital borrowings).</li>
                <li><strong>Total Assets:</strong> ~₹20,500 Crores.</li>
                <li><strong>Cash & Liquid Mutual Funds:</strong> ~₹1,800 Crores.</li>
            </ul>
            <div class="callout callout-success" style="margin-top:0.75rem;">
                <strong>Fortress Financial Position:</strong> Cash (₹1,800 cr) > Debt (₹1,100 cr). Asian Paints is a <strong>Net-Cash</strong> company! It has zero net debt.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Capital Structure Breakdown</h4>
                <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:0.75rem;">
                    <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:0.3rem;">
                        <span style="font-weight:bold; color:#1e40af;">Shareholders' Equity: 94.5%</span>
                        <span style="font-weight:bold; color:#dc2626;">Debt: 5.5%</span>
                    </div>
                    <div style="display:flex; height:20px; border-radius:6px; overflow:hidden;">
                        <div style="background:#3b82f6; width:94.5%;"></div>
                        <div style="background:#ef4444; width:5.5%;"></div>
                    </div>
                </div>
                <div style="text-align:center; margin-top:0.75rem; font-size:0.8rem; color:#475569;">
                    Funded 94.5% by owners' retained profits!
                </div>
            </div>
        """
    },

    # SLIDE 60
    {
        "id": 60,
        "module": "Module 5 · Corporate Case Study",
        "title": "Asian Paints Liquidity: CR 1.87x vs Quick 0.89x",
        "subtitle": "The inventory heavy nature of the paint manufacturing industry",
        "badge": "EXAM TRAP",
        "badge_type": "danger",
        "content_html": """
            <h3>The Asian Paints Liquidity Dichotomy</h3>
            <p>Exam questions love asking why a blue-chip titan has a Quick Ratio below 1.0x:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; margin-top:0.5rem; text-align:center;">
                <div style="background:#eff6ff; border:1px solid #93c5fd; padding:0.6rem; border-radius:8px;">
                    <strong style="color:#1d4ed8;">Current Ratio</strong>
                    <div style="font-size:1.4rem; font-weight:bold; color:#1e40af; margin:0.3rem 0;">1.87x</div>
                    <div style="font-size:0.75rem; color:#64748b;">Healthy short-term buffer</div>
                </div>
                <div style="background:#fefce8; border:1px solid #fde047; padding:0.6rem; border-radius:8px;">
                    <strong style="color:#b45309;">Quick Ratio</strong>
                    <div style="font-size:1.4rem; font-weight:bold; color:#92400e; margin:0.3rem 0;">0.89x</div>
                    <div style="font-size:0.75rem; color:#64748b;">Below 1.0x standard!</div>
                </div>
            </div>
            <div class="callout callout-warning" style="margin-top:0.75rem;">
                <strong>🔍 Why is Quick Ratio &lt; 1.0x?</strong><br>
                Paint companies must hold substantial raw materials (titanium dioxide, solvents) and thousands of finished paint tint variants in warehouses. <strong>Inventory accounts for > 50% of Current Assets</strong>!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Liquidity Stripping in Paint</h4>
                <div style="font-size:0.8rem; line-height:1.7; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem;">
                    <div>• <strong>Current Assets:</strong> ~₹7,500 cr</div>
                    <div style="color:#dc2626;">• <strong>Less Inventory:</strong> ~₹3,900 cr (52% of CA!)</div>
                    <div style="border-top:1px dashed #cbd5e1; padding-top:0.3rem;">• <strong>Quick Assets:</strong> ~₹3,600 cr</div>
                    <div>• <strong>Current Liabilities:</strong> ~₹4,010 cr</div>
                    <div style="font-weight:bold; color:#b45309; margin-top:0.3rem;">
                        Quick Ratio = 3,600 / 4,010 = <strong>0.89x</strong>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 61
    {
        "id": 61,
        "module": "Module 5 · Corporate Case Study",
        "title": "Asian Paints Solvency: D/E 0.06x & ICR 35.1x",
        "subtitle": "Proof of exceptional debt servicing capabilities",
        "badge": "SOLVENCY",
        "badge_type": "success",
        "content_html": """
            <h3>Solvency Ratios for Asian Paints</h3>
            <p>Exam questions highlighting bankruptcy risk can be instantly dismissed for Asian Paints:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <tr><th>Solvency Ratio</th><th>Formula Value</th><th>Asian Paints FY25</th><th>Benchmark</th></tr>
                    <tr><td><strong>Debt-to-Equity</strong></td><td>Debt / Equity</td><td>1,100 / 19,000 = <strong>0.06x</strong></td><td>&lt; 1.0x</td></tr>
                    <tr><td><strong>Interest Coverage</strong></td><td>EBIT / Interest</td><td>5,045.37 / 143.68 = <strong>35.1x</strong></td><td>&gt; 3.0x</td></tr>
                </table>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Interest Coverage of 35.1x</strong> means Asian Paints earns 35 times more operating profit than needed to service all lender interest!</li>
                <li>Operating profits would have to plunge by <strong>97.2%</strong> before the company struggled to pay annual interest.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Interest Safety Margin</h4>
                <div style="text-align:center; padding:0.5rem;">
                    <div style="font-size:2rem; font-weight:bold; color:#059669;">35.1x</div>
                    <div style="font-size:0.85rem; color:#047857; font-weight:bold;">Times Interest Earned</div>
                    <div style="margin-top:0.8rem; background:#ecfdf5; border:1px solid #6ee7b7; padding:0.6rem; border-radius:8px; font-size:0.8rem; color:#065f46;">
                        Even in severe macroeconomic crises, debt default probability is virtually ZERO.
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 62
    {
        "id": 62,
        "module": "Module 5 · Corporate Case Study",
        "title": "Asian Paints DuPont Breakdown: Dissecting 18.9% ROE",
        "subtitle": "How 12.1% Margin × 1.44 Turnover × 1.08 Leverage = 18.9% ROE",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Asian Paints FY25 DuPont Identity</h3>
            <p>Plugging Asian Paints' audited figures into the 3-step DuPont identity reveals pure operational excellence:</p>
            <div class="formula-box">
                <div class="formula-name">Audited DuPont Components:</div>
                <div class="formula-code">ROE = 12.14% (Margin) × 1.441 (Asset Turnover) × 1.079 (Leverage) = 18.88%</div>
            </div>
            <div style="display:flex; flex-direction:column; gap:0.4rem; margin-top:0.75rem; font-size:0.85rem;">
                <div>• <strong>Net Profit Margin (12.14%):</strong> Solid pricing power and premium product mix.</div>
                <div>• <strong>Asset Turnover (1.44x):</strong> Rotates total assets almost 1.5 times per year via automated plants.</div>
                <div>• <strong>Equity Multiplier (1.08x):</strong> Negligible leverage! Assets are only 1.08x Equity (almost 1.0x).</div>
            </div>
            <div class="callout callout-success" style="margin-top:0.75rem;">
                <strong>Key Takeaway:</strong> Unlike banks or distressed companies, Asian Paints' 18.9% ROE is <strong>100% genuine operational quality</strong>, not financial leverage engineering!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">DuPont 3-Step Chain</h4>
                <div style="display:flex; justify-content:center; align-items:center; gap:0.4rem; font-size:0.85rem; font-weight:bold; flex-wrap:wrap;">
                    <div style="background:#eff6ff; border:1px solid #93c5fd; padding:0.4rem 0.6rem; border-radius:6px; color:#1e40af;">
                        12.1%<br><span style="font-size:0.7rem; font-weight:normal;">Net Margin</span>
                    </div>
                    <span>×</span>
                    <div style="background:#ecfdf5; border:1px solid #86efac; padding:0.4rem 0.6rem; border-radius:6px; color:#166534;">
                        1.44x<br><span style="font-size:0.7rem; font-weight:normal;">Turnover</span>
                    </div>
                    <span>×</span>
                    <div style="background:#fefce8; border:1px solid #fde047; padding:0.4rem 0.6rem; border-radius:6px; color:#854d0e;">
                        1.08x<br><span style="font-size:0.7rem; font-weight:normal;">Leverage</span>
                    </div>
                    <span>=</span>
                    <div style="background:#faf5ff; border:2px solid #a855f7; padding:0.4rem 0.6rem; border-radius:6px; color:#6b21a8; font-size:1rem;">
                        18.9%<br><span style="font-size:0.7rem; font-weight:normal;">ROE</span>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 63
    {
        "id": 63,
        "module": "Module 5 · Corporate Case Study",
        "title": "Asian Paints Summary: Exam MCQ Takeaways",
        "subtitle": "5 guaranteed test angles based on the corporate case",
        "badge": "EXAM RECAP",
        "badge_type": "primary",
        "content_html": """
            <h3>Top 5 Exam Takeaways from Asian Paints Case</h3>
            <div style="display:flex; flex-direction:column; gap:0.5rem; margin-top:0.75rem; font-size:0.85rem;">
                <div style="background:#f8fafc; border-left:4px solid #3b82f6; padding:0.5rem;">
                    <strong>1. Quick Ratio &lt; 1.0x is NOT always fatal:</strong> For paint companies, heavy inventory explains the difference between CR 1.87x and Quick 0.89x.
                </div>
                <div style="background:#f8fafc; border-left:4px solid #10b981; padding:0.5rem;">
                    <strong>2. Net Cash Status:</strong> When Cash & Investments exceed Total Debt, financial distress risk is essentially zero.
                </div>
                <div style="background:#f8fafc; border-left:4px solid #f59e0b; padding:0.5rem;">
                    <strong>3. Super-High Coverage:</strong> Interest coverage of 35x represents virtually unbreakable debt solvency.
                </div>
                <div style="background:#f8fafc; border-left:4px solid #8b5cf6; padding:0.5rem;">
                    <strong>4. Clean DuPont Quality:</strong> A low Equity Multiplier (~1.08) proves high ROE is driven by margins and asset turnover, not high borrowing.
                </div>
                <div style="background:#f8fafc; border-left:4px solid #ef4444; padding:0.5rem;">
                    <strong>5. Direct-to-Dealer Efficiency:</strong> Eliminating wholesale intermediaries drives both high Gross Margin (41%) and rapid debtor turnaround.
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <div style="text-align:center; padding:1.5rem 0.5rem;">
                    <div style="font-size:3rem; margin-bottom:0.5rem;">🎯</div>
                    <h4 style="color:#1e40af; font-size:1.1rem; margin-bottom:0.5rem;">Case Study Mastered!</h4>
                    <p style="color:#64748b; font-size:0.85rem;">You now know the exact numbers and diagnostic logic tested in the Speed-Run lectures.</p>
                </div>
            </div>
        """
    },

    # SLIDE 64
    {
        "id": 64,
        "module": "Module 6 · Management Accounting",
        "title": "Management Accounting vs Financial Accounting",
        "subtitle": "Internal decision-making vs external statutory reporting",
        "badge": "THEORY",
        "badge_type": "primary",
        "content_html": """
            <h3>Financial Accounting vs Management Accounting</h3>
            <p>Session 6 introduces internal cost management for operational and pricing decisions:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.8rem;">
                    <tr><th>Dimension</th><th>Financial Accounting</th><th>Management Accounting</th></tr>
                    <tr><td><strong>Target Audience</strong></td><td>External (Shareholders, Banks, Tax)</td><td>Internal (CEOs, Plant Managers, Foremen)</td></tr>
                    <tr><td><strong>Time Orientation</strong></td><td>Historical (Past year/quarter performance)</td><td>Future-oriented (Budgets, Forecasts, CVP)</td></tr>
                    <tr><td><strong>Statutory Rules</strong></td><td>Mandatory compliance with GAAP / Ind AS</td><td>Zero statutory format; flexible to need</td></tr>
                    <tr><td><strong>Reporting Frequency</strong></td><td>Quarterly / Annually (Fixed)</td><td>Daily, Weekly, Monthly, On-Demand</td></tr>
                    <tr><td><strong>Precision</strong></td><td>To the exact Rupee / Paise</td><td>Estimates and projections acceptable</td></tr>
                </table>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Two Divergent Focus Areas</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; text-align:center; font-size:0.8rem;">
                    <div style="background:#eff6ff; border:1px solid #bfdbfe; padding:0.6rem; border-radius:8px;">
                        <div style="font-size:1.5rem;">🏛️</div>
                        <strong style="color:#1d4ed8;">Financial Acc.</strong>
                        <div style="font-size:0.75rem; color:#475569; margin-top:0.3rem;">Backward Looking<br>External Compliance<br>Audited Reports</div>
                    </div>
                    <div style="background:#ecfdf5; border:1px solid #a7f3d0; padding:0.6rem; border-radius:8px;">
                        <div style="font-size:1.5rem;">🧭</div>
                        <strong style="color:#065f46;">Management Acc.</strong>
                        <div style="font-size:0.75rem; color:#475569; margin-top:0.3rem;">Forward Looking<br>Internal Decisions<br>Pricing & Budgets</div>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 65
    {
        "id": 65,
        "module": "Module 6 · Management Accounting",
        "title": "Cost Classification: By Traceability",
        "subtitle": "Direct costs (Prime Cost) vs Indirect costs (Overheads)",
        "badge": "COST CONCEPTS",
        "badge_type": "primary",
        "content_html": """
            <h3>Traceability: Direct vs Indirect Costs</h3>
            <p>Every rupee spent in a factory is either directly traceable to a specific finished product or shared across the facility:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-top:0.75rem;">
                <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:8px; padding:0.6rem;">
                    <h4 style="color:#166534; font-size:0.9rem; margin-bottom:0.3rem;">Direct Costs (Prime Cost)</h4>
                    <p style="font-size:0.8rem; line-height:1.5; color:#334155;">Physically and economically traceable to a specific single unit of output.</p>
                    <ul style="font-size:0.75rem; margin-left:1rem; line-height:1.5;">
                        <li><strong>Direct Materials:</strong> Leather in shoes, wood in table, steel in car.</li>
                        <li><strong>Direct Labour:</strong> Assembly-line worker, carpenter wages.</li>
                    </ul>
                </div>
                <div style="background:#fffbeb; border:1px solid #fde68a; border-radius:8px; padding:0.6rem;">
                    <h4 style="color:#92400e; font-size:0.9rem; margin-bottom:0.3rem;">Indirect Costs (Overheads)</h4>
                    <p style="font-size:0.8rem; line-height:1.5; color:#334155;">Shared expenses supporting overall production; cannot be traced to 1 unit.</p>
                    <ul style="font-size:0.75rem; margin-left:1rem; line-height:1.5;">
                        <li><strong>Indirect Materials:</strong> Machine lubricant, cleaning supplies.</li>
                        <li><strong>Indirect Labour:</strong> Factory security guard, supervisor salary.</li>
                        <li><strong>Indirect Expenses:</strong> Factory rent, electricity, depreciation.</li>
                    </ul>
                </div>
            </div>
            <div style="margin-top:0.75rem; font-size:0.85rem; font-weight:bold; color:#1e40af; text-align:center;">
                Prime Cost = Direct Materials + Direct Labour + Direct Expenses
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Manufacturing Cost Pyramids</h4>
                <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.8rem;">
                    <div style="background:#ecfdf5; border:1px solid #86efac; padding:0.5rem; border-radius:6px;">
                        <strong>Prime Cost:</strong> Direct Material + Direct Labour
                    </div>
                    <div style="text-align:center; color:#64748b; font-size:0.75rem;">+ Factory Overheads</div>
                    <div style="background:#eff6ff; border:1px solid #93c5fd; padding:0.5rem; border-radius:6px;">
                        <strong>Factory / Works Cost:</strong> Prime Cost + Production Overheads
                    </div>
                    <div style="text-align:center; color:#64748b; font-size:0.75rem;">+ Admin & Selling Overheads</div>
                    <div style="background:#faf5ff; border:1px solid #d8b4fe; padding:0.5rem; border-radius:6px;">
                        <strong>Total Cost of Sales:</strong> Factory Cost + Commercial Overheads
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 66
    {
        "id": 66,
        "module": "Module 6 · Management Accounting",
        "title": "Cost Classification: By Behavior",
        "subtitle": "Fixed, Variable, and Semi-Variable cost dynamics",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Cost Behavior with Production Volume</h3>
            <p>How total cost and per-unit cost react when production volume changes:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.8rem;">
                    <tr><th>Cost Category</th><th>Behavior in TOTAL</th><th>Behavior PER UNIT</th><th>Example</th></tr>
                    <tr><td><strong>Variable Cost (VC)</strong></td><td>Increases proportionally with volume</td><td><strong style="color:#059669;">CONSTANT</strong> per unit</td><td>Direct raw materials, packaging</td></tr>
                    <tr><td><strong>Fixed Cost (FC)</strong></td><td><strong style="color:#2563eb;">CONSTANT</strong> in total (within relevant range)</td><td>Decreases as volume rises (Economies of scale)</td><td>Factory rent, plant manager salary</td></tr>
                    <tr><td><strong>Semi-Variable Cost</strong></td><td>Contains both fixed base + variable usage</td><td>Decreases per unit, but not to zero</td><td>Electricity bill (meter rent + unit charge)</td></tr>
                </table>
            </div>
            <div class="callout callout-warning" style="margin-top:0.75rem;">
                <strong>⚠️ MCQ Exam Trap:</strong> "Fixed costs per unit are fixed." — <strong>FALSE!</strong> Fixed cost in total is fixed; fixed cost per unit <em>falls</em> as volume increases!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Cost Behavior Curves</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; text-align:center; font-size:0.8rem;">
                    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:0.5rem; border-radius:6px;">
                        <strong>Total Variable Cost</strong>
                        <div style="height:60px; display:flex; align-items:flex-end; padding:0.3rem;">
                            <div style="height:2px; width:100%; background:#2563eb; transform:rotate(-25deg); transform-origin:bottom left;"></div>
                        </div>
                        <span style="font-size:0.7rem; color:#64748b;">Straight upward diagonal</span>
                    </div>
                    <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:0.5rem; border-radius:6px;">
                        <strong>Total Fixed Cost</strong>
                        <div style="height:60px; display:flex; align-items:center; padding:0.3rem;">
                            <div style="height:2px; width:100%; background:#dc2626;"></div>
                        </div>
                        <span style="font-size:0.7rem; color:#64748b;">Horizontal flat line</span>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 67
    {
        "id": 67,
        "module": "Module 6 · Management Accounting",
        "title": "The High-Low Method: Separating Mixed Costs",
        "subtitle": "Step-by-step arithmetic to extract fixed and variable components",
        "badge": "WORKED NUMERICAL",
        "badge_type": "primary",
        "content_html": """
            <h3>Splitting Semi-Variable Costs: The High-Low Method</h3>
            <p>When an expense contains both fixed and variable elements, compare the highest and lowest activity points:</p>
            <div class="formula-box">
                <div class="formula-name">Step 1: Variable Cost per Unit:</div>
                <div class="formula-code">VC per unit = (Cost at Highest Activity − Cost at Lowest Activity) / (Highest Activity − Lowest Activity)</div>
            </div>
            <div class="formula-box" style="margin-top:0.4rem;">
                <div class="formula-name">Step 2: Total Fixed Cost:</div>
                <div class="formula-code">Fixed Cost = Total Cost − (VC per unit × Activity Units)</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; margin-top:0.5rem; font-size:0.85rem;">
                <strong>Numerical Example:</strong><br>
                • High: 10,000 units → Cost = ₹90,000<br>
                • Low: 4,000 units → Cost = ₹54,000<br>
                <strong>VC/unit</strong> = (90,000 − 54,000) / (10,000 − 4,000) = 36,000 / 6,000 = <strong>₹6 per unit</strong>.<br>
                <strong>Fixed Cost</strong> = 90,000 − (6 × 10,000) = <strong>₹30,000</strong>.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Prediction Equation</h4>
                <div style="background:#eff6ff; border:1px solid #93c5fd; border-radius:8px; padding:0.8rem; text-align:center;">
                    <div style="font-size:1.1rem; font-weight:bold; color:#1e40af;">
                        Total Cost = ₹30,000 + ₹6 × (Units)
                    </div>
                </div>
                <div style="margin-top:0.75rem; font-size:0.8rem; color:#475569; text-align:center;">
                    Now you can predict total cost at ANY production level (e.g. at 8,000 units = 30k + 48k = ₹78,000).
                </div>
            </div>
        """
    },

    # SLIDE 68
    {
        "id": 68,
        "module": "Module 6 · Management Accounting",
        "title": "Relevant Costs: Sunk Costs (Always Ignore!)",
        "subtitle": "Cost already incurred that cannot be changed by any future choice",
        "badge": "EXAM TRAP",
        "badge_type": "danger",
        "content_html": """
            <h3>The Sunk Cost Rule for Decision-Making</h3>
            <p>A sunk cost is an expenditure that has already occurred in the past and cannot be recovered or altered by any decision made today or tomorrow:</p>
            <div class="callout callout-danger" style="margin-top:0.75rem;">
                <strong>🚨 The Golden Rule:</strong> Sunk costs are <strong>IRRELEVANT</strong> to all managerial decisions! Always eliminate them completely from project evaluations, pricing decisions, or continuation choices.
            </div>
            <h4>Classic Sunk Cost Examples in Exam MCQs:</h4>
            <ul style="margin-left:1.5rem; line-height:1.7; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Market Survey Fees:</strong> Spent ₹5 Lakhs last month surveying consumer interest for a new drink. Irrelevant to whether we launch or cancel!</li>
                <li><strong>Past R&D Expenditure:</strong> ₹50 Lakhs spent over 2 years developing a prototype. That ₹50L is gone forever.</li>
                <li><strong>Book Value of Existing Machinery:</strong> Historical depreciated book value is irrelevant; only current scrap salvage value matters.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Sunk Cost Fallacy Filter</h4>
                <div style="background:#fee2e2; border:2px dashed #ef4444; border-radius:8px; padding:1rem; text-align:center;">
                    <div style="font-size:2rem; margin-bottom:0.3rem;">🛑</div>
                    <div style="font-weight:bold; color:#991b1b; font-size:1rem;">PAST MONEY SPENT</div>
                    <div style="font-size:0.8rem; color:#7f1d1d; margin-top:0.3rem;">R&D, Old Studies, Past Capex</div>
                    <div style="margin-top:0.6rem; background:#ffffff; border-radius:6px; padding:0.4rem; font-weight:bold; color:#dc2626; font-size:0.85rem;">
                        DO NOT INCLUDE IN FUTURE DECISIONS!
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 69
    {
        "id": 69,
        "module": "Module 6 · Management Accounting",
        "title": "Relevant Costs: Opportunity Costs & Incremental Flows",
        "subtitle": "The benefit forgone from the next best alternative",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Opportunity Cost: The Hidden Cost</h3>
            <p>Opportunity cost represents the lost economic benefit from giving up the next best alternative use of a scarce resource:</p>
            <div class="callout callout-success" style="margin-top:0.75rem;">
                <strong>🚨 The Golden Rule:</strong> Opportunity costs <strong>MUST ALWAYS BE INCLUDED</strong> as an expense in financial decision-making and capital budgeting!
            </div>
            <h4>Classic Opportunity Cost Cases:</h4>
            <ul style="margin-left:1.5rem; line-height:1.7; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Using an Owned Warehouse:</strong> If a firm uses its own building for a new project, it pays ₹0 out of pocket. BUT it gives up ₹10 Lakhs/year in rental income from an outside tenant. <strong>Opportunity cost = ₹10L/year</strong>!</li>
                <li><strong>Owner's Own Time:</strong> Rahul quits a ₹12 Lakhs salary job to open a cafe. The ₹12L forgone salary is an opportunity cost of running the cafe.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Opportunity Cost Decision Path</h4>
                <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.8rem;">
                    <div style="background:#eff6ff; border:1px solid #93c5fd; padding:0.5rem; border-radius:6px;">
                        <strong>Choice A: Use Warehouse for Project</strong><br>
                        Generates project revenue, but loses rental income.
                    </div>
                    <div style="text-align:center; font-size:0.75rem; color:#64748b;">vs Next Best Forgone Alternative</div>
                    <div style="background:#fefce8; border:1px solid #fde047; padding:0.5rem; border-radius:6px;">
                        <strong>Choice B: Rent Warehouse to Third Party</strong><br>
                        Earn ₹10 Lakhs/year risk-free rent.
                    </div>
                    <div style="background:#f0fdf4; border:1px solid #86efac; padding:0.4rem; border-radius:6px; font-weight:bold; color:#166534; text-align:center;">
                        Project must cover the ₹10L rent forgone to be viable!
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 70
    {
        "id": 70,
        "module": "Module 6 · Management Accounting",
        "title": "Committed vs Discretionary Fixed Costs",
        "subtitle": "Short-term management flexibility and spending freezes",
        "badge": "COST CONCEPTS",
        "badge_type": "primary",
        "content_html": """
            <h3>Committed vs Discretionary Fixed Costs</h3>
            <p>Not all fixed costs can be cut when an economic downturn strikes:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-top:0.75rem;">
                <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:0.6rem;">
                    <h4 style="color:#1e40af; font-size:0.9rem; margin-bottom:0.3rem;">Committed Fixed Costs</h4>
                    <p style="font-size:0.8rem; line-height:1.5; color:#334155;">Arise from long-term legal, organizational, or capital investment obligations.</p>
                    <ul style="font-size:0.75rem; margin-left:1rem; line-height:1.5;">
                        <li>Depreciation on buildings & plant.</li>
                        <li>Non-cancellable 10-year factory lease.</li>
                        <li>Property taxes and insurance.</li>
                    </ul>
                    <div style="font-size:0.75rem; color:#dc2626; font-weight:bold; margin-top:0.3rem;">Cannot be cut without disrupting survival!</div>
                </div>
                <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:0.6rem;">
                    <h4 style="color:#059669; font-size:0.9rem; margin-bottom:0.3rem;">Discretionary Fixed Costs</h4>
                    <p style="font-size:0.8rem; line-height:1.5; color:#334155;">Arise from annual budgeting decisions; can be altered or frozen in the short term.</p>
                    <ul style="font-size:0.75rem; margin-left:1rem; line-height:1.5;">
                        <li>Advertising & brand marketing.</li>
                        <li>Employee training programs.</li>
                        <li>Discretionary research & development.</li>
                    </ul>
                    <div style="font-size:0.75rem; color:#16a34a; font-weight:bold; margin-top:0.3rem;">Can be frozen instantly during a cash crunch!</div>
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Crisis Budgeting Flexibility</h4>
                <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.8rem;">
                    <div style="background:#fee2e2; padding:0.5rem; border-radius:6px; border-left:4px solid #ef4444;">
                        <strong>Rigid (Committed):</strong> Lease, Factory Depreciation, Senior Staff
                    </div>
                    <div style="background:#dcfce7; padding:0.5rem; border-radius:6px; border-left:4px solid #22c55e;">
                        <strong>Flexible (Discretionary):</strong> Ad campaigns, Travel, External consultants
                    </div>
                </div>
                <div style="text-align:center; margin-top:0.75rem; font-size:0.8rem; color:#475569;">
                    During crises, firms immediately freeze discretionary costs to preserve cash.
                </div>
            </div>
        """
    }
]

print(f"Loaded {len(slides_53_to_70)} slides in Part 2-B.")
