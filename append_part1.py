# append_part1.py
import slides_data_part1

new_slides = [
    # SLIDE 11
    {
        "id": 11,
        "module": "Module 1 · Accounting Foundations",
        "title": "The Seven Elements of Financial Reporting",
        "subtitle": "How the business universe is categorized",
        "badge": "FRAMEWORK",
        "badge_type": "primary",
        "content_html": """
            <h3>The Building Blocks of Financial Reporting</h3>
            <p>Every single number in corporate accounts belongs to one of seven fundamental elements:</p>
            <ul style="margin-left:1.5rem; line-height:1.7; font-size:0.9rem;">
                <li><strong>1. Assets:</strong> Resources controlled yielding future economic benefit.</li>
                <li><strong>2. Liabilities:</strong> Present obligations arising from past events.</li>
                <li><strong>3. Equity:</strong> Residual interest of owners (Assets − Liabilities).</li>
                <li><strong>4. Income:</strong> Inflows/enhancements of assets from core operations.</li>
                <li><strong>5. Expenses:</strong> Outflows/depletions of assets in generating revenue.</li>
                <li><strong>6. Gains:</strong> Incidental increases in equity (e.g., selling old equipment above book value).</li>
                <li><strong>7. Losses:</strong> Incidental reductions in equity (e.g., fire loss, selling plant at a loss).</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">7 Elements Split by Statement</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem;">
                    <div style="background:#eff6ff; border:1px solid #bfdbfe; padding:0.8rem; border-radius:8px;">
                        <strong style="color:#1d4ed8;">Balance Sheet (Point in Time):</strong>
                        <ul style="font-size:0.85rem; margin-left:1rem; margin-top:0.3rem;">
                            <li>Assets</li>
                            <li>Liabilities</li>
                            <li>Equity</li>
                        </ul>
                    </div>
                    <div style="background:#fefce8; border:1px solid #fef08a; padding:0.8rem; border-radius:8px;">
                        <strong style="color:#a16207;">Income Statement (Period of Time):</strong>
                        <ul style="font-size:0.85rem; margin-left:1rem; margin-top:0.3rem;">
                            <li>Income</li>
                            <li>Expenses</li>
                            <li>Gains</li>
                            <li>Losses</li>
                        </ul>
                    </div>
                </div>
                <div class="callout callout-info" style="margin-top:0.75rem; font-size:0.85rem;">
                    All Income, Expenses, Gains, and Losses flow directly into Equity!
                </div>
            </div>
        """
    },

    # SLIDE 12
    {
        "id": 12,
        "module": "Module 1 · Accounting Foundations",
        "title": "Equity Mechanics: How Equity Moves",
        "subtitle": "The engine connecting the Income Statement to the Balance Sheet",
        "badge": "EQUITY DYNAMICS",
        "badge_type": "primary",
        "content_html": """
            <h3>How Equity Changes Over Time</h3>
            <p>Owners' equity is dynamic. It increases with profits and fresh capital, and decreases with losses and withdrawals:</p>
            <div class="formula-box">
                <div class="formula-name">Movement in Owners' Equity:</div>
                <div class="formula-code">ΔEquity = Fresh Capital + (Income − Expenses) + (Gains − Losses) − Drawings/Dividends</div>
            </div>
            <h4>Entity Forms Comparison:</h4>
            <ul style="margin-left:1.5rem; line-height:1.7;">
                <li><strong>Sole Proprietorship:</strong> Equity = Owner's Capital + Profit − Drawings.</li>
                <li><strong>Corporate Company:</strong> Equity = Share Capital + Retained Earnings + Other Reserves.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Equity Valve Diagram</h4>
                <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.85rem;">
                    <div style="background:#dcfce7; border:1px solid #86efac; padding:0.6rem; border-radius:6px; color:#14532d;">
                        <strong>▲ PUSHES EQUITY UP:</strong><br>
                        • New Capital Infusion<br>
                        • Revenues & Operating Income<br>
                        • Capital Gains on Asset Disposals
                    </div>
                    <div style="background:#fee2e2; border:1px solid #fca5a5; padding:0.6rem; border-radius:6px; color:#7f1d1d;">
                        <strong>▼ PULLS EQUITY DOWN:</strong><br>
                        • Operating Expenses (COGS, Rent, Salaries)<br>
                        • Capital Losses on Asset Write-downs<br>
                        • Owner Drawings (Proprietor) / Dividends (Corporate)
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 13
    {
        "id": 13,
        "module": "Module 1 · Accounting Foundations",
        "title": "Drawings & Dividends: The Classic Exam Trap",
        "subtitle": "Why withdrawing money is NOT an expense",
        "badge": "MCQ EXAM TRAP ⚠️",
        "badge_type": "danger",
        "content_html": """
            <h3>Do NOT Mistake Drawings for Expenses!</h3>
            <p>A perennial exam trap tests whether students classify personal drawings or corporate dividends as expenses.</p>
            <div class="callout callout-danger">
                <strong>🚨 Golden Rule:</strong> Drawings and Dividends are <strong>distributions of equity</strong> to owners, NOT expenses of doing business!
            </div>
            <h4>Slide Case: Rahul's Cafe (Proprietorship):</h4>
            <ul style="margin-left:1.5rem; line-height:1.7;">
                <li>Starts with ₹5,00,000 cash equity.</li>
                <li>Cash expenses: ₹3,00,000 → Cash ₹2L, Equity ₹2L.</li>
                <li>Cash sales: ₹4,00,000 → Cash ₹6L, Equity ₹6L (Profit = ₹1L).</li>
                <li><strong>Drawings for personal use: ₹50,000</strong> → Cash ₹5.5L, Equity ₹5.5L.</li>
            </ul>
            <p style="margin-top:0.5rem; font-size:0.9rem; color:#b91c1c; font-weight:bold;">
                The ₹50,000 drawings NEVER appears on the Income Statement!
            </p>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:#be123c; margin-bottom:1rem;">Income Statement vs Balance Sheet</h4>
                <div style="display:flex; flex-direction:column; gap:0.75rem;">
                    <div style="background:#f1f5f9; padding:0.75rem; border-radius:6px;">
                        <div style="font-weight:bold; color:var(--primary);">Income Statement:</div>
                        <div style="font-size:0.85rem; color:#475569;">Sales ₹4L − Expenses ₹3L = <strong>₹1.0L Profit</strong></div>
                        <small style="color:#64748b;">(Drawings completely excluded!)</small>
                    </div>
                    <div style="background:#f1f5f9; padding:0.75rem; border-radius:6px;">
                        <div style="font-weight:bold; color:var(--primary);">Balance Sheet:</div>
                        <div style="font-size:0.85rem; color:#475569;">
                            Assets: Cash ₹5.5L<br>
                            Liabilities: ₹0<br>
                            Equity: ₹5.0L + ₹1.0L profit − <strong>₹0.5L drawings</strong> = ₹5.5L
                        </div>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 14
    {
        "id": 14,
        "module": "Module 1 · Accounting Foundations",
        "title": "Kirana Store Case: Transaction 1 (Starting Up)",
        "subtitle": "Ravi invests ₹5L and borrows ₹2L",
        "badge": "WORKED CASE",
        "badge_type": "info",
        "content_html": """
            <h3>Step 1: Capital Infusion & Debt</h3>
            <p>Ravi decides to open a neighborhood Kirana grocery store. He invests ₹5,00,000 of his personal savings and borrows ₹2,00,000 from a commercial bank.</p>
            <div class="table-responsive" style="margin-top:1rem;">
                <table class="data-table">
                    <thead>
                        <tr><th>Line</th><th>Cash (Asset)</th><th>Loan (Liab)</th><th>Equity</th></tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Invests ₹5L, borrows ₹2L</td>
                            <td style="color:#15803d; font-weight:bold;">+₹7.0 Lakh</td>
                            <td style="color:#b91c1c; font-weight:bold;">+₹2.0 Lakh</td>
                            <td style="color:#1d4ed8; font-weight:bold;">+₹5.0 Lakh</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="callout callout-success" style="margin-top:1rem;">
                <strong>Equation Check:</strong> Total Assets (₹7.0L Cash) = Liabilities (₹2.0L Loan) + Equity (₹5.0L Ravi's Capital). Equality holds!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Step 1 Balance Sheet</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem;">
                    <div style="background:#dbeafe; padding:1rem; border-radius:8px; text-align:center;">
                        <div style="font-size:0.85rem; color:#1e40af;">CASH (ASSET)</div>
                        <div style="font-size:1.5rem; font-weight:bold; color:#1e3a8a;">₹7,00,000</div>
                    </div>
                    <div style="display:flex; flex-direction:column; gap:0.5rem;">
                        <div style="background:#fee2e2; padding:0.5rem; border-radius:6px; text-align:center;">
                            <div style="font-size:0.75rem; color:#991b1b;">BANK LOAN</div>
                            <div style="font-size:1.1rem; font-weight:bold; color:#7f1d1d;">₹2,00,000</div>
                        </div>
                        <div style="background:#dcfce7; padding:0.5rem; border-radius:6px; text-align:center;">
                            <div style="font-size:0.75rem; color:#166534;">OWNER EQUITY</div>
                            <div style="font-size:1.1rem; font-weight:bold; color:#14532d;">₹5,00,000</div>
                        </div>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 15
    {
        "id": 15,
        "module": "Module 1 · Accounting Foundations",
        "title": "Kirana Store Case: Transaction 2 (Stock Purchase)",
        "subtitle": "Buying ₹3L stock for cash — Asset Substitution",
        "badge": "WORKED CASE",
        "badge_type": "info",
        "content_html": """
            <h3>Step 2: Purchasing Wholesale Merchandise</h3>
            <p>Ravi buys grocery inventory for ₹3,00,000 cash from a wholesale distributor.</p>
            <div class="table-responsive" style="margin-top:1rem;">
                <table class="data-table">
                    <thead>
                        <tr><th>Event</th><th>Cash</th><th>Inventory</th><th>Loan</th><th>Equity</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Initial</td><td>₹7.0L</td><td>—</td><td>₹2.0L</td><td>₹5.0L</td></tr>
                        <tr style="background:#fef3c7; font-weight:bold;">
                            <td>Buy Stock ₹3L</td>
                            <td style="color:#b91c1c;">−₹3.0L</td>
                            <td style="color:#15803d;">+₹3.0L</td>
                            <td>₹2.0L</td>
                            <td>₹5.0L</td>
                        </tr>
                        <tr style="background:#f0fdf4;">
                            <td><strong>New Balance</strong></td>
                            <td><strong>₹4.0L</strong></td>
                            <td><strong>₹3.0L</strong></td>
                            <td><strong>₹2.0L</strong></td>
                            <td><strong>₹5.0L</strong></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="callout callout-info" style="margin-top:1rem;">
                <strong>Key Insight:</strong> Total Assets remain unchanged at ₹7.0 Lakh (₹4L Cash + ₹3L Inventory). This is a pure <em>asset composition swap</em>. Zero impact on equity or profit!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Asset Shift (No Net Change)</h4>
                <div style="display:flex; justify-content:center; align-items:center; gap:1rem;">
                    <div style="background:#fee2e2; padding:1rem; border-radius:8px; text-align:center; width:120px;">
                        <small style="color:#991b1b;">Cash Outflow</small>
                        <div style="font-weight:bold; color:#7f1d1d; font-size:1.1rem;">−₹3,00,000</div>
                    </div>
                    <div style="font-size:1.5rem; color:#94a3b8;">➔</div>
                    <div style="background:#dcfce7; padding:1rem; border-radius:8px; text-align:center; width:120px;">
                        <small style="color:#166534;">Inventory In</small>
                        <div style="font-weight:bold; color:#14532d; font-size:1.1rem;">+₹3,00,000</div>
                    </div>
                </div>
                <div style="text-align:center; margin-top:1.25rem; font-size:0.85rem; color:#475569;">
                    Total Assets still = ₹7,00,000.<br>Liabilities = ₹2,00,000 | Equity = ₹5,00,000.
                </div>
            </div>
        """
    },

    # SLIDE 16
    {
        "id": 16,
        "module": "Module 1 · Accounting Foundations",
        "title": "Kirana Store Case: Transaction 3 (Profitable Sale)",
        "subtitle": "Selling ₹1L stock for ₹1.5L cash",
        "badge": "WORKED CASE",
        "badge_type": "info",
        "content_html": """
            <h3>Step 3: Generating Revenue & Profit</h3>
            <p>Ravi sells grocery items that cost him ₹1,00,000 to customers for ₹1,50,000 cash.</p>
            <div class="table-responsive" style="margin-top:1rem;">
                <table class="data-table">
                    <thead>
                        <tr><th>Line</th><th>Cash</th><th>Inventory</th><th>Loan</th><th>Equity</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Prior</td><td>₹4.0L</td><td>₹3.0L</td><td>₹2.0L</td><td>₹5.0L</td></tr>
                        <tr style="background:#dbeafe; font-weight:bold;">
                            <td>Sale</td>
                            <td style="color:#15803d;">+₹1.5L</td>
                            <td style="color:#b91c1c;">−₹1.0L</td>
                            <td>₹2.0L</td>
                            <td style="color:#15803d;">+₹0.5L (Profit)</td>
                        </tr>
                        <tr style="background:#dcfce7;">
                            <td><strong>Final</strong></td>
                            <td><strong>₹5.5L</strong></td>
                            <td><strong>₹2.0L</strong></td>
                            <td><strong>₹2.0L</strong></td>
                            <td><strong>₹5.5L</strong></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="callout callout-success" style="margin-top:1rem;">
                <strong>Balance Check:</strong> Assets (₹5.5L Cash + ₹2.0L Inventory = ₹7.5L) = Liabilities (₹2.0L Loan) + Equity (₹5.5L). Profit of ₹50,000 raised equity!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Profit Flow to Equity</h4>
                <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:1rem; border-radius:8px;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.4rem; font-size:0.9rem;">
                        <span>Sales Inflow:</span>
                        <span style="font-weight:bold; color:#15803d;">+₹1,50,000</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.4rem; font-size:0.9rem;">
                        <span>Cost of Goods Sold:</span>
                        <span style="font-weight:bold; color:#b91c1c;">−₹1,00,000</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; padding-top:0.4rem; border-top:1px solid #cbd5e1; font-weight:bold;">
                        <span>Net Profit Created:</span>
                        <span style="color:#1d4ed8;">+₹50,000</span>
                    </div>
                </div>
                <div style="text-align:center; margin-top:1rem; font-size:0.85rem; color:#166534; font-weight:bold;">
                    Equity expands from ₹5.0L to ₹5.5L!
                </div>
            </div>
        """
    },

    # SLIDE 17
    {
        "id": 17,
        "module": "Module 1 · Accounting Foundations",
        "title": "Current vs Non-Current Assets",
        "subtitle": "The 12-month / operating cycle line of demarcation",
        "badge": "ASSET TYPES",
        "badge_type": "primary",
        "content_html": """
            <h3>Classifying Assets on the Balance Sheet</h3>
            <p>An asset is classified based on the expected timeframe of its realization or consumption:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-top:1rem;">
                <div style="background:#eff6ff; padding:0.85rem; border-radius:8px; border:1px solid #bfdbfe;">
                    <strong style="color:#1d4ed8;">Current Assets (≤ 12 Months):</strong>
                    <p style="font-size:0.85rem; margin-top:0.3rem;">Realized, sold, or consumed within the operating cycle or roughly 1 year.</p>
                    <ul style="font-size:0.8rem; margin-left:1rem; margin-top:0.3rem;">
                        <li>Cash & Bank balances</li>
                        <li>Trade Receivables (Debtors)</li>
                        <li>Inventories (Raw, WIP, Finished)</li>
                        <li>Prepaid expenses</li>
                    </ul>
                </div>
                <div style="background:#f8fafc; padding:0.85rem; border-radius:8px; border:1px solid #cbd5e1;">
                    <strong style="color:#334155;">Non-Current Assets (> 12 Months):</strong>
                    <p style="font-size:0.85rem; margin-top:0.3rem;">Yield productive economic benefit over a long-term horizon.</p>
                    <ul style="font-size:0.8rem; margin-left:1rem; margin-top:0.3rem;">
                        <li>Property, Plant & Equipment (PPE)</li>
                        <li>Factory Machinery & Vehicles</li>
                        <li>Intangible assets (Patents, Software)</li>
                        <li>Long-term investments</li>
                    </ul>
                </div>
            </div>
            <p style="margin-top:0.75rem; font-size:0.85rem; color:var(--text-muted);">
                <em>Kirana Example:</em> ₹50k cash and ₹3L stock are <strong>current</strong>; the ₹1.2L display freezer is <strong>non-current</strong>.
            </p>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Kirana Asset Classification</h4>
                <div style="display:flex; flex-direction:column; gap:0.6rem; font-size:0.85rem;">
                    <div style="background:#eff6ff; padding:0.6rem; border-radius:6px; display:flex; justify-content:space-between;">
                        <span>Cash in register</span>
                        <span class="badge badge-primary">Current Asset</span>
                    </div>
                    <div style="background:#eff6ff; padding:0.6rem; border-radius:6px; display:flex; justify-content:space-between;">
                        <span>Rice & Dal stock</span>
                        <span class="badge badge-primary">Current Asset</span>
                    </div>
                    <div style="background:#f1f5f9; padding:0.6rem; border-radius:6px; display:flex; justify-content:space-between;">
                        <span>Display Freezer</span>
                        <span class="badge badge-dark">Non-Current Asset</span>
                    </div>
                    <div style="background:#f1f5f9; padding:0.6rem; border-radius:6px; display:flex; justify-content:space-between;">
                        <span>Shop wooden shelves</span>
                        <span class="badge badge-dark">Non-Current Asset</span>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 18
    {
        "id": 18,
        "module": "Module 1 · Accounting Foundations",
        "title": "Current vs Non-Current Liabilities",
        "subtitle": "Short-term operational obligations vs long-term funding",
        "badge": "LIABILITY TYPES",
        "badge_type": "primary",
        "content_html": """
            <h3>Classifying Obligations to Outsiders</h3>
            <p>Liabilities represent legal claims by non-owners that must be settled using company resources:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-top:1rem;">
                <div style="background:#fff1f2; padding:0.85rem; border-radius:8px; border:1px solid #fecdd3;">
                    <strong style="color:#be123c;">Current Liabilities (≤ 12 Months):</strong>
                    <p style="font-size:0.85rem; margin-top:0.3rem;">Due within the operational cycle or normal 12-month window.</p>
                    <ul style="font-size:0.8rem; margin-left:1rem; margin-top:0.3rem;">
                        <li>Accounts Payable (Trade Creditors)</li>
                        <li>Salaries & Wages Payable</li>
                        <li>Taxes Payable (GST, Advance Tax)</li>
                        <li>Short-term bank overdraft</li>
                    </ul>
                </div>
                <div style="background:#f8fafc; padding:0.85rem; border-radius:8px; border:1px solid #cbd5e1;">
                    <strong style="color:#334155;">Non-Current Liabilities (> 12 Months):</strong>
                    <p style="font-size:0.85rem; margin-top:0.3rem;">Maturity extends beyond one year from reporting date.</p>
                    <ul style="font-size:0.8rem; margin-left:1rem; margin-top:0.3rem;">
                        <li>Long-term bank term loans</li>
                        <li>Corporate debentures & bonds</li>
                        <li>Long-term lease obligations</li>
                    </ul>
                </div>
            </div>
            <p style="margin-top:0.75rem; font-size:0.85rem; color:var(--text-muted);">
                <em>Store Example:</em> Supplier bill ₹80,000 is <strong>current</strong>; 5-year bank term loan ₹5L is <strong>non-current</strong>.
            </p>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Maturity Timeline Horizon</h4>
                <div style="position:relative; padding:1.5rem 0.5rem; text-align:center;">
                    <div style="height:4px; background:#cbd5e1; position:relative; margin:1rem 0;">
                        <div style="position:absolute; left:0; top:-6px; width:16px; height:16px; border-radius:50%; background:#1e3a8a;"></div>
                        <div style="position:absolute; left:50%; top:-6px; width:16px; height:16px; border-radius:50%; background:#f59e0b;"></div>
                        <div style="position:absolute; right:0; top:-6px; width:16px; height:16px; border-radius:50%; background:#8b5cf6;"></div>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-size:0.8rem; color:#64748b;">
                        <span>Today</span>
                        <span style="font-weight:bold; color:#b45309;">12 Months Boundary</span>
                        <span>5+ Years</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; margin-top:0.75rem; font-size:0.85rem;">
                        <span style="color:#be123c; font-weight:bold;">Current Liabilities</span>
                        <span style="color:#1e3a8a; font-weight:bold;">Non-Current Liabilities</span>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 19
    {
        "id": 19,
        "module": "Module 1 · Accounting Foundations",
        "title": "Core Assumptions: Business Entity & Going Concern",
        "subtitle": "The foundational bedrock of GAAP financial records",
        "badge": "CORE ASSUMPTIONS",
        "badge_type": "primary",
        "content_html": """
            <h3>Two Foundational Pillars</h3>
            <div style="margin-top:1rem; display:flex; flex-direction:column; gap:1rem;">
                <div class="callout callout-info" style="margin:0;">
                    <h4 style="color:#0369a1;">1. Business Entity Assumption</h4>
                    <p style="font-size:0.88rem;">
                        The business is treated as a separate, distinct legal and financial personality from its owners. Personal assets and expenses of owners are NEVER mixed into the business books.
                    </p>
                    <small><em>Real-life case:</em> Amazon’s financial statements do not report Jeff Bezos's personal yacht or private mansions.</small>
                </div>
                <div class="callout callout-success" style="margin:0;">
                    <h4 style="color:#15803d;">2. Going Concern Assumption</h4>
                    <p style="font-size:0.88rem;">
                        The business is assumed to continue operating indefinitely into the future. It has neither the intention nor necessity to liquidate.
                    </p>
                    <small><em>Real-life case:</em> Commercial baking ovens are reported at cost minus accumulated wear, NOT at their crash distress/scrap auction price!</small>
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Exam Identification Drill</h4>
                <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.75rem; border-radius:6px; font-size:0.85rem; margin-bottom:0.75rem;">
                    <strong>Question:</strong> An accountant values factory machinery at depreciated book value even though second-hand market scrap prices have collapsed by 80%. Why?
                </div>
                <div style="background:#dcfce7; border:1px solid #86efac; padding:0.75rem; border-radius:6px; font-size:0.85rem; color:#14532d;">
                    <strong>Correct Answer:</strong> Going Concern Assumption!<br>
                    (Because the machine will be used in future operations to produce revenue, not sold off as scrap today).
                </div>
            </div>
        """
    },

    # SLIDE 20
    {
        "id": 20,
        "module": "Module 1 · Accounting Foundations",
        "title": "Core Assumptions: Money Measurement, Periodicity & Historical Cost",
        "subtitle": "How accounting restricts and standards its reporting",
        "badge": "CORE ASSUMPTIONS",
        "badge_type": "primary",
        "content_html": """
            <h3>Three Standardising Assumptions</h3>
            <div style="margin-top:0.75rem; display:flex; flex-direction:column; gap:0.75rem; font-size:0.88rem;">
                <div style="background:#f1f5f9; padding:0.75rem; border-radius:6px; border-left:4px solid #3b82f6;">
                    <strong>3. Money Measurement Concept:</strong><br>
                    Only events capable of reliable objective measurement in currency units are recorded. Employee brilliance, brand love, or customer loyalty cannot be an asset line item.
                </div>
                <div style="background:#f1f5f9; padding:0.75rem; border-radius:6px; border-left:4px solid #3b82f6;">
                    <strong>4. Accounting Period (Periodicity):</strong><br>
                    The infinite economic life of an enterprise is sliced into uniform artificial time intervals for reporting performance (e.g., Indian FY: 1st April to 31st March).
                </div>
                <div style="background:#f1f5f9; padding:0.75rem; border-radius:6px; border-left:4px solid #3b82f6;">
                    <strong>5. Historical Cost Principle:</strong><br>
                    Assets are recorded at the original cash acquisition cost. Land purchased 20 years ago for ₹50 Lakh remains on the books at ₹50 Lakh, regardless of current market appreciation.
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card" style="text-align:center;">
                <div style="font-size:3rem; margin-bottom:0.5rem;">📏</div>
                <h4 style="color:var(--secondary); margin-bottom:0.5rem;">Objectivity & Comparability</h4>
                <p style="font-size:0.85rem; color:#475569;">
                    These assumptions sacrifice subjective market valuation in exchange for verifiable, auditable objectivity that external auditors and banks can trust.
                </p>
                <div style="margin-top:1rem; padding:0.75rem; background:#eff6ff; border-radius:6px; font-size:0.8rem; color:#1e40af;">
                    Indian Financial Year Standard: <strong>1 April to 31 March</strong>
                </div>
            </div>
        """
    }
]

# Append into slides_data_part1
slides_data_part1.slides_part1.extend(new_slides)
print(f"Appended slides. Total slides now: {len(slides_data_part1.slides_part1)}")
