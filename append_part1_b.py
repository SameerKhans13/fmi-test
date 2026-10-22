# append_part1_b.py
import slides_data_part1

slides_21_to_35 = [
    # SLIDE 21
    {
        "id": 21,
        "module": "Module 1 · Accounting Foundations",
        "title": "Accrual Concept: Record As & When It Happens",
        "subtitle": "Economic activity dictates recognition, not the movement of physical cash",
        "badge": "DRIVING PRINCIPLES",
        "badge_type": "primary",
        "content_html": """
            <h3>Accrual Accounting vs Cash Accounting</h3>
            <p>Revenues are recorded when earned and expenses when incurred, regardless of when cash changes hands.</p>
            <div class="table-responsive" style="margin-top:0.75rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <thead>
                        <tr><th>Event</th><th>Economic Period</th><th>Cash Period</th><th>Proper Accounting Treatment</th></tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>March Ad Campaign ₹1,00,000</td>
                            <td>March 2026</td>
                            <td>April 2026</td>
                            <td>March expense; ₹1L current liability at 31 March</td>
                        </tr>
                        <tr>
                            <td>March Staff Salary paid 5 April</td>
                            <td>March 2026</td>
                            <td>April 2026</td>
                            <td>March expense; Salaries Payable on Balance Sheet</td>
                        </tr>
                        <tr>
                            <td>Annual Insurance ₹12k paid 1 April</td>
                            <td>12 Months</td>
                            <td>April 2026</td>
                            <td>₹1,000/month expense; remainder is Prepaid Asset</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="callout callout-warning" style="margin-top:0.75rem; font-size:0.85rem;">
                A cash-basis view would distort profits across months. Accrual aligns revenue with actual economic exertion!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Accrual Timeline</h4>
                <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:1rem; font-size:0.85rem;">
                    <div style="color:#1d4ed8; font-weight:bold; margin-bottom:0.3rem;">March 31 (Work Done):</div>
                    <div style="margin-bottom:0.75rem;">Recognize <strong>₹1,00,000 Expense</strong> in March Income Statement. Create <strong>₹1,00,000 Liability</strong> on March 31 Balance Sheet.</div>
                    <div style="color:#15803d; font-weight:bold; margin-bottom:0.3rem;">April 5 (Cash Paid):</div>
                    <div>Cash decreases by ₹1,00,000; Liability extinguished. <strong>April Income Statement = ₹0 Expense!</strong></div>
                </div>
            </div>
        """
    },

    # SLIDE 22
    {
        "id": 22,
        "module": "Module 1 · Accounting Foundations",
        "title": "Matching Principle: Pair Cost with Revenue Earned",
        "subtitle": "Unsold goods are assets, not expenses",
        "badge": "DRIVING PRINCIPLES",
        "badge_type": "primary",
        "content_html": """
            <h3>Slide Case: FashionHub Shirt Retailer</h3>
            <p>FashionHub buys 1,000 shirts at wholesale for ₹1,000 each (Total outlay = ₹10,00,000). During the month, it sells 600 shirts at ₹1,800 each.</p>
            <div class="table-responsive" style="margin-top:0.75rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <thead>
                        <tr><th>Line Item</th><th>Working</th><th>Amount</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Sales Revenue</td><td>600 shirts × ₹1,800</td><td>₹10,80,000</td></tr>
                        <tr><td>Cost of Goods Sold (COGS)</td><td>600 shirts × ₹1,000</td><td style="color:#b91c1c;">₹6,00,000</td></tr>
                        <tr style="background:#dcfce7; font-weight:bold;"><td>Gross Profit</td><td>₹10.8L − ₹6.0L</td><td style="color:#15803d;">₹4,80,000</td></tr>
                        <tr style="background:#eff6ff;"><td>Closing Inventory (Current Asset)</td><td>400 shirts × ₹1,000</td><td style="color:#1e40af;">₹4,00,000</td></tr>
                    </tbody>
                </table>
            </div>
            <div class="callout callout-danger" style="margin-top:0.75rem; font-size:0.85rem;">
                <strong>Fatal Student Error:</strong> Expensing the entire ₹10L purchase immediately would show a fake loss of −₹0.8L and hide ₹4L of valuable unsold inventory!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">1,000 Shirts Purchase Split</h4>
                <div style="display:flex; height:120px; border-radius:8px; overflow:hidden; font-weight:bold; text-align:center;">
                    <div style="width:60%; background:#fed7aa; color:#9a3412; display:flex; flex-direction:column; justify-content:center; padding:0.5rem;">
                        <span>600 SOLD</span>
                        <small>COGS: ₹6,00,000 (Income Statement)</small>
                    </div>
                    <div style="width:40%; background:#bfdbfe; color:#1e40af; display:flex; flex-direction:column; justify-content:center; padding:0.5rem;">
                        <span>400 UNSOLD</span>
                        <small>Inventory: ₹4,00,000 (Balance Sheet)</small>
                    </div>
                </div>
                <div style="margin-top:1rem; font-size:0.85rem; color:#475569; text-align:center;">
                    Only the cost of the 600 shirts that generated revenue is matched!
                </div>
            </div>
        """
    },

    # SLIDE 23
    {
        "id": 23,
        "module": "Module 1 · Accounting Foundations",
        "title": "Realisation Principle: Revenue When It Is Earned",
        "subtitle": "Upfront advance cash is an obligation, not revenue",
        "badge": "DRIVING PRINCIPLES",
        "badge_type": "primary",
        "content_html": """
            <h3>Slide Case: The ₹12,000 Netflix Subscription</h3>
            <p>A customer pays ₹12,000 upfront on 1st April 2025 for an annual Netflix subscription covering 12 months. Service is delivered at ₹1,000 each month.</p>
            <div class="table-responsive" style="margin-top:0.75rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <thead>
                        <tr><th>Reporting Date</th><th>Revenue Recognised So Far</th><th>Unearned Revenue (Current Liability)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>30 June 2025 (3 mos)</td><td>₹3,000</td><td>₹9,000</td></tr>
                        <tr><td>30 September 2025 (6 mos)</td><td>₹6,000</td><td>₹6,000</td></tr>
                        <tr><td>31 March 2026 (12 mos)</td><td>₹12,000</td><td>₹0</td></tr>
                    </tbody>
                </table>
            </div>
            <div class="callout callout-info" style="margin-top:0.75rem; font-size:0.85rem;">
                <strong>Identical Logic:</strong> Airline ticket bookings, educational coaching tuition, and annual enterprise SaaS software licenses.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Unearned Revenue Burn-Down</h4>
                <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.85rem;">
                    <div style="display:flex; justify-content:space-between; align-items:center; background:#eff6ff; padding:0.5rem; border-radius:6px;">
                        <span>Day 1 (1 April):</span>
                        <span style="font-weight:bold; color:#be123c;">₹12,000 Liability (100% Unearned)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center; background:#eff6ff; padding:0.5rem; border-radius:6px;">
                        <span>Month 6 (30 Sept):</span>
                        <span style="font-weight:bold; color:#f59e0b;">₹6,000 Revenue / ₹6,000 Liability</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center; background:#eff6ff; padding:0.5rem; border-radius:6px;">
                        <span>Month 12 (31 March):</span>
                        <span style="font-weight:bold; color:#15803d;">₹12,000 Revenue / ₹0 Liability</span>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 24
    {
        "id": 24,
        "module": "Module 1 · Accounting Foundations",
        "title": "Four Conventions that Guide Judgment",
        "subtitle": "Consistency, Prudence, Full Disclosure & Materiality",
        "badge": "CONVENTIONS",
        "badge_type": "primary",
        "content_html": """
            <h3>The Four Modifying Conventions</h3>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-top:0.75rem; font-size:0.85rem;">
                <div style="background:#eff6ff; padding:0.75rem; border-radius:6px; border-left:3px solid #3b82f6;">
                    <strong>1. Consistency:</strong><br>
                    Keep the same accounting methods year after year. Changing depreciation or inventory formulas every year destroys multi-year comparability.
                </div>
                <div style="background:#fef2f2; padding:0.75rem; border-radius:6px; border-left:3px solid #ef4444;">
                    <strong>2. Prudence (Conservatism):</strong><br>
                    Anticipate no profits, but provide for all probable losses. Never overstate assets or understate liabilities.
                </div>
                <div style="background:#f0fdf4; padding:0.75rem; border-radius:6px; border-left:3px solid #10b981;">
                    <strong>3. Full Disclosure:</strong><br>
                    Disclose all material facts and footnotes necessary for investors to understand the true financial condition.
                </div>
                <div style="background:#fffbeb; padding:0.75rem; border-radius:6px; border-left:3px solid #f59e0b;">
                    <strong>4. Materiality:</strong><br>
                    Information matters only if omitting or misstating it could influence user decisions. (A ₹500 office stapler is expensed immediately).
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card" style="text-align:center;">
                <div style="font-size:2.5rem; margin-bottom:0.5rem;">⚖️</div>
                <h4 style="color:var(--secondary); margin-bottom:0.5rem;">Prudence Rule: Lower of Cost or NRV</h4>
                <p style="font-size:0.85rem; color:#475569;">
                    If inventory cost is ₹1,00,000 but flood damage drops realisable value to ₹70,000, write it down immediately to ₹70,000! If market value rises to ₹1,40,000, keep it at ₹1,00,000 (never record unrealised paper gains).
                </p>
            </div>
        """
    },

    # SLIDE 25
    {
        "id": 25,
        "module": "Module 1 · Accounting Foundations",
        "title": "Reconciling Net Income to Operating Cash Flow",
        "subtitle": "The indirect method step-by-step arithmetic",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Why Net Income Does Not Equal Operating Cash Flow</h3>
            <p>Accrual net profit includes non-cash expenses and reflects credit sales not yet collected. We reconcile using the indirect method:</p>
            <div class="formula-box">
                <div class="formula-name">Indirect Operating Cash Flow (CFO) Formula:</div>
                <div class="formula-code">CFO = PAT + Depreciation − ΔReceivables − ΔInventory + ΔPayables</div>
            </div>
            <div style="margin-top:0.75rem; font-size:0.85rem; display:flex; flex-direction:column; gap:0.35rem;">
                <div>• <strong>Add Depreciation:</strong> Non-cash expense; cash never left the bank.</div>
                <div>• <strong>Subtract Increase in Receivables:</strong> Cash trapped with customers.</div>
                <div>• <strong>Subtract Increase in Inventory:</strong> Cash spent to stock warehouse.</div>
                <div>• <strong>Add Increase in Payables:</strong> Suppliers funded purchases; cash preserved!</div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Slide Worked Reconciliation (₹ Lakh)</h4>
                <div class="table-responsive">
                    <table class="data-table" style="font-size:0.85rem;">
                        <tbody>
                            <tr><td><strong>Start: Net Income (PAT)</strong></td><td style="font-weight:bold;">₹67.5L</td></tr>
                            <tr><td>Add: Depreciation (non-cash)</td><td style="color:#15803d;">+₹20.0L</td></tr>
                            <tr><td>Less: Increase in Receivables</td><td style="color:#b91c1c;">−₹30.0L</td></tr>
                            <tr><td>Less: Increase in Inventory</td><td style="color:#b91c1c;">−₹15.0L</td></tr>
                            <tr><td>Add: Increase in Payables</td><td style="color:#15803d;">+₹10.0L</td></tr>
                            <tr style="background:#e0f2fe; font-weight:bold;"><td><strong>Cash from Operating Activities</strong></td><td style="color:#1d4ed8;">₹52.5L</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        """
    },

    # SLIDE 26
    {
        "id": 26,
        "module": "Module 2 · Asset Accounting & Depreciation",
        "title": "What is Depreciation?",
        "subtitle": "Spreading the acquisition cost across the revenue-earning life",
        "badge": "CONCEPT",
        "badge_type": "primary",
        "content_html": """
            <h3>Depreciation is Allocation, NOT Valuation!</h3>
            <p>Depreciation is the systematic allocation of the depreciable amount of a tangible non-current asset over its useful life (Matching Concept).</p>
            <div class="callout callout-warning">
                <strong>🚨 Common Student Misconception:</strong>
                Depreciation does NOT represent a pile of cash stored in a bank account to buy new machines, nor does it measure current resale market value!
            </div>
            <h4>Why It Matters to Investors:</h4>
            <ul style="margin-left:1.5rem; line-height:1.7;">
                <li>Reduces reported net profit on the Income Statement.</li>
                <li>Creates a tax shield (depreciation is tax-deductible).</li>
                <li>Reduces asset carrying value on the Balance Sheet.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card" style="text-align:center;">
                <h4 style="color:var(--secondary); margin-bottom:1rem;">Cost Allocation Across 5 Years</h4>
                <div style="background:#f1f5f9; padding:0.75rem; border-radius:6px; font-weight:bold; color:#1e3a8a; margin-bottom:0.75rem;">
                    Initial Purchase: ₹10,00,000 (Year 0)
                </div>
                <div style="display:flex; justify-content:space-around; font-size:0.8rem; color:#475569;">
                    <div style="background:#dbeafe; padding:0.5rem; border-radius:4px;">Yr 1: ₹1.8L</div>
                    <div style="background:#dbeafe; padding:0.5rem; border-radius:4px;">Yr 2: ₹1.8L</div>
                    <div style="background:#dbeafe; padding:0.5rem; border-radius:4px;">Yr 3: ₹1.8L</div>
                    <div style="background:#dbeafe; padding:0.5rem; border-radius:4px;">Yr 4: ₹1.8L</div>
                    <div style="background:#dbeafe; padding:0.5rem; border-radius:4px;">Yr 5: ₹1.8L</div>
                </div>
                <div style="margin-top:1rem; font-size:0.85rem; color:#15803d; font-weight:bold;">
                    Matches ₹1.8L yearly wear to yearly revenue!
                </div>
            </div>
        """
    },

    # SLIDE 27
    {
        "id": 27,
        "module": "Module 2 · Asset Accounting & Depreciation",
        "title": "The Four Depreciation Variables",
        "subtitle": "Cost, Residual Value, Useful Life & Depreciable Amount",
        "badge": "FORMULA SETUP",
        "badge_type": "primary",
        "content_html": """
            <h3>The 4 Essential Variables</h3>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-top:1rem; font-size:0.85rem;">
                <div style="background:#eff6ff; padding:0.75rem; border-radius:6px; border:1px solid #bfdbfe;">
                    <strong style="color:#1d4ed8;">1. Historical Cost:</strong><br>
                    Purchase price plus freight, installation, and trial run costs.<br>
                    <em>Slide Example:</em> ₹11,00,000
                </div>
                <div style="background:#fefce8; padding:0.75rem; border-radius:6px; border:1px solid #fef08a;">
                    <strong style="color:#a16207;">2. Residual (Salvage) Value:</strong><br>
                    Expected scrap disposal value at the end of its working life.<br>
                    <em>Slide Example:</em> ₹1,00,000
                </div>
                <div style="background:#f0fdf4; padding:0.75rem; border-radius:6px; border:1px solid #bbf7d0;">
                    <strong style="color:#15803d;">3. Useful Life:</strong><br>
                    Estimated working life in years or output units.<br>
                    <em>Slide Example:</em> 5 Years
                </div>
                <div style="background:#fdf2f8; padding:0.75rem; border-radius:6px; border:1px solid #fbcfe8;">
                    <strong style="color:#be185d;">4. Depreciable Amount:</strong><br>
                    Cost minus Residual Value = Total amount to allocate.<br>
                    <em>Slide Example:</em> ₹11L − ₹1L = <strong>₹10,00,000</strong>
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Depreciable Base Equation</h4>
                <div style="font-family:monospace; font-size:1.1rem; text-align:center; padding:1rem; background:#f8fafc; border:1px dashed #cbd5e1; border-radius:8px;">
                    Depreciable Amount = Cost − Residual Value<br>
                    <span style="color:#16a34a; font-weight:bold;">₹10,00,000 = ₹11,00,000 − ₹1,00,000</span>
                </div>
            </div>
        """
    },

    # SLIDE 28
    {
        "id": 28,
        "module": "Module 2 · Asset Accounting & Depreciation",
        "title": "Straight-Line Method (SLM)",
        "subtitle": "Equal annual depreciation charge across useful life",
        "badge": "FORMULA DRILL",
        "badge_type": "primary",
        "content_html": """
            <h3>Straight-Line Method (SLM) Formula</h3>
            <p>Under SLM, an identical rupee depreciation expense is charged against profits in every single year:</p>
            <div class="formula-box">
                <div class="formula-name">Annual SLM Depreciation:</div>
                <div class="formula-code">Annual Depreciation = (Cost − Residual Value) / Useful Life</div>
            </div>
            <h4>Core Characteristics:</h4>
            <ul style="margin-left:1.5rem; line-height:1.7;">
                <li>Uniform, constant expense on the Income Statement.</li>
                <li>Book value declines at a steady, linear rate.</li>
                <li>Best suited for assets that provide uniform utility over time (buildings, office furniture).</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Linear Book Value Decline</h4>
                <svg viewBox="0 0 300 160" width="100%" height="150">
                    <line x1="40" y1="20" x2="40" y2="130" stroke="#94a3b8" stroke-width="2"/>
                    <line x1="40" y1="130" x2="280" y2="130" stroke="#94a3b8" stroke-width="2"/>
                    <!-- Linear line -->
                    <line x1="40" y1="30" x2="260" y2="115" stroke="#3b82f6" stroke-width="3"/>
                    <circle cx="40" cy="30" r="4" fill="#1e40af"/>
                    <circle cx="260" cy="115" r="4" fill="#1e40af"/>
                    <text x="35" y="25" text-anchor="end" font-size="10" fill="#1e293b">Cost</text>
                    <text x="265" y="115" font-size="10" fill="#1e293b">Salvage</text>
                    <text x="150" y="145" text-anchor="middle" font-size="10" fill="#64748b">Useful Life (Years)</text>
                </svg>
            </div>
        """
    },

    # SLIDE 29
    {
        "id": 29,
        "module": "Module 2 · Asset Accounting & Depreciation",
        "title": "SLM Worked Numerical: The 5-Year Machine",
        "subtitle": "Machine cost ₹10,00,000, residual ₹1,00,000, 5 years",
        "badge": "NUMERICAL DRILL",
        "badge_type": "info",
        "content_html": """
            <h3>Slide Exact Numerical Example</h3>
            <p>Annual Depreciation = <span class="math-expr">(₹10,00,000 − ₹1,00,000) / 5 = ₹1,80,000/year</span>.</p>
            <div class="table-responsive" style="margin-top:0.75rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <thead>
                        <tr><th>Year</th><th>Opening Balance</th><th>Depreciation</th><th>Closing Balance</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Year 1</td><td>₹10,00,000</td><td>₹1,80,000</td><td>₹8,20,000</td></tr>
                        <tr><td>Year 2</td><td>₹8,20,000</td><td>₹1,80,000</td><td>₹6,40,000</td></tr>
                        <tr><td>Year 3</td><td>₹6,40,000</td><td>₹1,80,000</td><td>₹4,60,000</td></tr>
                        <tr><td>Year 4</td><td>₹4,60,000</td><td>₹1,80,000</td><td>₹2,80,000</td></tr>
                        <tr style="background:#dcfce7; font-weight:bold;"><td>Year 5</td><td>₹2,80,000</td><td>₹1,80,000</td><td>₹1,00,000 (Residual)</td></tr>
                    </tbody>
                </table>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <div class="callout callout-success" style="margin:0;">
                    <strong>Exam Quick Verification:</strong>
                    At the end of Year 5, closing book value must exactly equal the ₹1,00,000 expected residual salvage value!
                </div>
            </div>
        """
    },

    # SLIDE 30
    {
        "id": 30,
        "module": "Module 2 · Asset Accounting & Depreciation",
        "title": "Reducing-Balance Method (WDV)",
        "subtitle": "Charge is heaviest in Year 1 and diminishes each year",
        "badge": "METHODS COMPARISON",
        "badge_type": "primary",
        "content_html": """
            <h3>Written Down Value (WDV) Formula</h3>
            <p>Applies a fixed depreciation percentage rate to the <strong>opening book value</strong> of the asset at the beginning of each period:</p>
            <div class="formula-box">
                <div class="formula-name">Annual Reducing-Balance Depreciation:</div>
                <div class="formula-code">Annual Depreciation = Opening Book Value × Depreciation Rate (r)</div>
            </div>
            <h4>Why Use WDV?</h4>
            <ul style="margin-left:1.5rem; line-height:1.7;">
                <li>Assets lose market and productive value fastest in their early years (e.g., brand new cars lose 20% value upon leaving showroom).</li>
                <li>Combines high early depreciation with low early maintenance; as maintenance rises in later years, depreciation falls, keeping total asset cost smooth.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">SLM vs WDV Annual Expense</h4>
                <div style="display:flex; justify-content:space-around; align-items:flex-end; height:120px; border-bottom:2px solid #cbd5e1; padding-bottom:0.5rem;">
                    <div style="text-align:center; font-size:0.75rem;">
                        <div style="height:90px; width:25px; background:#ef4444; margin:0 auto; border-radius:4px;"></div>
                        <span>Yr 1 WDV</span>
                    </div>
                    <div style="text-align:center; font-size:0.75rem;">
                        <div style="height:65px; width:25px; background:#3b82f6; margin:0 auto; border-radius:4px;"></div>
                        <span>Yr 1 SLM</span>
                    </div>
                    <div style="text-align:center; font-size:0.75rem;">
                        <div style="height:40px; width:25px; background:#ef4444; margin:0 auto; border-radius:4px;"></div>
                        <span>Yr 5 WDV</span>
                    </div>
                    <div style="text-align:center; font-size:0.75rem;">
                        <div style="height:65px; width:25px; background:#3b82f6; margin:0 auto; border-radius:4px;"></div>
                        <span>Yr 5 SLM</span>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 31
    {
        "id": 31,
        "module": "Module 2 · Asset Accounting & Depreciation",
        "title": "Reducing-Balance Worked Numerical: Truck Case",
        "subtitle": "Truck cost ₹20,00,000, 25% WDV rate, residual nil",
        "badge": "NUMERICAL DRILL",
        "badge_type": "info",
        "content_html": """
            <h3>Slide 20 Case Walkthrough</h3>
            <p>Truck cost ₹20,00,000 depreciated at 25% per annum on reducing book value:</p>
            <div class="table-responsive" style="margin-top:0.75rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <thead>
                        <tr><th>Year</th><th>Opening Balance</th><th>Depreciation @ 25%</th><th>Closing Balance</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Year 1</td><td>₹20,00,000</td><td style="color:#b91c1c; font-weight:bold;">₹5,00,000</td><td>₹15,00,000</td></tr>
                        <tr><td>Year 2</td><td>₹15,00,000</td><td>₹3,75,000</td><td>₹11,25,000</td></tr>
                        <tr><td>Year 3</td><td>₹11,25,000</td><td>₹2,81,250</td><td>₹8,43,750</td></tr>
                        <tr><td>Year 4</td><td>₹8,43,750</td><td>₹2,10,938</td><td>₹6,32,812</td></tr>
                        <tr><td>Year 5</td><td>₹6,32,812</td><td>₹1,58,203</td><td>₹4,74,609</td></tr>
                    </tbody>
                </table>
            </div>
            <div class="callout callout-info" style="margin-top:0.75rem; font-size:0.85rem;">
                Notice that Year 1 depreciation is ₹5L under WDV, whereas SLM on the same truck would charge ₹4L every year!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <div class="callout callout-warning" style="margin:0;">
                    <strong>Exam Takeaway:</strong>
                    WDV creates a larger tax shield in the early years of an asset's life, boosting early cash flows!
                </div>
            </div>
        """
    },

    # SLIDE 32
    {
        "id": 32,
        "module": "Module 2 · Asset Accounting & Depreciation",
        "title": "Intangible Assets & Amortisation",
        "subtitle": "Identifiable non-monetary assets without physical substance",
        "badge": "INTANGIBLES",
        "badge_type": "primary",
        "content_html": """
            <h3>Intangible Asset Recognition Criteria</h3>
            <p>Identifiable assets with no physical substance controlled by the firm (Patents, Software licenses, Trademarks, Brand franchises).</p>
            <div class="callout callout-info" style="margin-top:0.75rem; font-size:0.85rem;">
                <strong>Recognition Rule:</strong> Recognized ONLY if future economic benefits are probable AND acquisition cost can be measured reliably. (Externally bought: at cost).
            </div>
            <h4>Slide Case: Pharmaceutical Patent</h4>
            <p style="font-size:0.88rem;">
                Patent purchased for ₹10 Crore with a 10-year legal protection life:<br>
                • Amortisation each year (SLM) = <span class="math-expr">₹10 Crore / 10 = ₹1 Crore/year</span>.<br>
                • Carrying book value after 3 years = <span class="math-expr">₹10 Cr − 3(₹1 Cr) = <strong>₹7 Crore</strong></span>.
            </p>
            <div class="callout callout-warning" style="margin-top:0.75rem; font-size:0.85rem;">
                <strong>Goodwill Note:</strong> Internally generated brands or goodwill are NEVER recognized. Goodwill arises ONLY during mergers and acquisitions!
            </div>
        """,
        "visual_html": """
            <div class="visual-card" style="text-align:center;">
                <div style="font-size:3rem; margin-bottom:0.5rem;">📜</div>
                <h4 style="color:var(--secondary); margin-bottom:0.5rem;">Patent Amortisation</h4>
                <div style="background:#f1f5f9; padding:0.75rem; border-radius:6px; font-size:0.85rem;">
                    <div>Purchase Cost: <strong>₹10 Crore</strong></div>
                    <div>Annual Amortisation: <strong>₹1 Crore</strong></div>
                    <div style="margin-top:0.5rem; color:#15803d; font-weight:bold;">Carrying Value Yr 3: ₹7 Crore</div>
                </div>
            </div>
        """
    },

    # SLIDE 33
    {
        "id": 33,
        "module": "Module 2 · Asset Accounting & Depreciation",
        "title": "Long-Term Investments: Strategic vs Financial",
        "subtitle": "Tata Motors and Volkswagen corporate cases",
        "badge": "INVESTMENTS",
        "badge_type": "primary",
        "content_html": """
            <h3>Two Types of Long-Term Investments</h3>
            <p>Non-current investments fall into two broad corporate categories:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-top:0.75rem; font-size:0.85rem;">
                <div style="background:#eff6ff; padding:0.75rem; border-radius:6px; border:1px solid #bfdbfe;">
                    <strong style="color:#1d4ed8;">1. Strategic Investments:</strong><br>
                    Investments in subsidiaries, joint ventures (JVs), and associates to support core supply chains and technology.<br>
                    • <em>Tata Motors (FY25):</em> <strong>₹29,718 Crore</strong> in subsidiaries & JVs.<br>
                    • <em>Volkswagen:</em> €10.0 bn (SAIC-VW 50%, QuantumScape 16%).
                </div>
                <div style="background:#fefce8; padding:0.75rem; border-radius:6px; border:1px solid #fef08a;">
                    <strong style="color:#a16207;">2. Financial Investments:</strong><br>
                    Investments in debt bonds, treasury bills, and passive equity to earn dividends, interest, or capital gains.<br>
                    • <em>Tata Motors (FY25):</em> <strong>₹1,709 Crore</strong> other financial assets.<br>
                    • <em>Total LT Investments:</em> ₹31,427 Crore.
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:1rem;">Tata Motors LT Investment Split</h4>
                <div style="display:flex; height:100px; border-radius:8px; overflow:hidden; font-weight:bold; font-size:0.8rem; text-align:center;">
                    <div style="width:94.5%; background:#3b82f6; color:white; display:flex; flex-direction:column; justify-content:center; padding:0.25rem;">
                        <span>Strategic (94.5%)</span>
                        <small>₹29,718 Cr</small>
                    </div>
                    <div style="width:5.5%; background:#f59e0b; color:white; display:flex; flex-direction:column; justify-content:center; padding:0.25rem;">
                        <span>Fin</span>
                    </div>
                </div>
                <div style="text-align:center; margin-top:0.75rem; font-size:0.85rem; color:#475569;">
                    Total Long-Term Investments = ₹31,427 Crore
                </div>
            </div>
        """
    },

    # SLIDE 34
    {
        "id": 34,
        "module": "Module 3 · Financial Statements Linkage",
        "title": "Three Important Statements & How They Link",
        "subtitle": "Income Statement, Balance Sheet, and Cash Flow Statement",
        "badge": "STATEMENTS LINKAGE",
        "badge_type": "primary",
        "content_html": """
            <h3>The Triad of Corporate Financials</h3>
            <div style="display:flex; flex-direction:column; gap:0.6rem; font-size:0.85rem; margin-top:0.75rem;">
                <div style="background:#eff6ff; padding:0.6rem; border-radius:6px; border-left:4px solid #3b82f6;">
                    <strong>1. Income Statement (Performance):</strong> Revenues − Expenses = Net Profit (PAT) over a period of time.
                </div>
                <div style="background:#ecfeff; padding:0.6rem; border-radius:6px; border-left:4px solid #06b6d4;">
                    <strong>2. Balance Sheet (Position):</strong> Assets = Liabilities + Equity as of one snapshot date.
                </div>
                <div style="background:#f0fdf4; padding:0.6rem; border-radius:6px; border-left:4px solid #10b981;">
                    <strong>3. Cash Flow Statement (Liquidity):</strong> Where cash came from and went across Operating, Investing, and Financing activities.
                </div>
            </div>
            <div class="callout callout-info" style="margin-top:0.75rem; font-size:0.85rem;">
                <strong>How they connect:</strong> Net Profit from the Income Statement flows into Retained Earnings (Equity) on the Balance Sheet. Depreciation reduces profit on the Income Statement but is added back on the Cash Flow Statement!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The Circular Flow</h4>
                <div style="display:flex; justify-content:space-around; align-items:center; text-align:center; font-size:0.8rem; font-weight:bold;">
                    <div style="background:#dbeafe; padding:0.75rem; border-radius:8px; width:80px;">INCOME STMT</div>
                    <div style="color:#94a3b8;">➔ Profit ➔</div>
                    <div style="background:#dcfce7; padding:0.75rem; border-radius:8px; width:80px;">BALANCE SHEET</div>
                </div>
                <div style="text-align:center; margin-top:0.75rem; font-size:0.8rem; color:#64748b;">
                    ▲ Cash Flow Statement reconciles the closing Cash on the Balance Sheet!
                </div>
            </div>
        """
    },

    # SLIDE 35
    {
        "id": 35,
        "module": "Module 3 · Financial Statements Linkage",
        "title": "Income Statement Architecture: Revenue to Operating Profit",
        "subtitle": "Sales, COGS, Gross Profit & Operating Expenses",
        "badge": "P&L ARCHITECTURE",
        "badge_type": "primary",
        "content_html": """
            <h3>Top Half of the Income Statement</h3>
            <p>Understanding the standard line-item progression of corporate profits:</p>
            <div class="table-responsive" style="margin-top:0.75rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <thead>
                        <tr><th>Line Item</th><th>Economic Meaning</th><th>Slide Example (₹ Lakh)</th></tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>Revenue (Sales)</strong></td><td>Total gross proceeds from goods/services</td><td>₹500L</td></tr>
                        <tr><td>Less: <strong>COGS</strong></td><td>Direct costs: raw materials, factory wages</td><td style="color:#b91c1c;">(₹300L)</td></tr>
                        <tr style="background:#dcfce7; font-weight:bold;"><td><strong>Gross Profit</strong></td><td>Profit after direct manufacturing costs</td><td style="color:#15803d;">₹200L (40%)</td></tr>
                        <tr><td>Less: Selling & Admin</td><td>Commissions, ad campaigns, head-office rent</td><td>(₹80L)</td></tr>
                        <tr><td>Less: Depreciation</td><td>Non-cash asset cost allocation</td><td>(₹20L)</td></tr>
                        <tr style="background:#eff6ff; font-weight:bold;"><td><strong>Operating Profit (EBIT)</strong></td><td>Profit generated by the main core business</td><td style="color:#1d4ed8;">₹100L (20%)</td></tr>
                    </tbody>
                </table>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Gross vs Operating Margin</h4>
                <div style="background:#f8fafc; border:1px solid #cbd5e1; padding:0.75rem; border-radius:6px; font-size:0.85rem;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.5rem;">
                        <span>Gross Profit Margin:</span>
                        <span style="font-weight:bold; color:#15803d;">₹200L / ₹500L = 40.0%</span>
                    </div>
                    <div style="display:flex; justify-content:space-between;">
                        <span>Operating Margin (EBIT):</span>
                        <span style="font-weight:bold; color:#1d4ed8;">₹100L / ₹500L = 20.0%</span>
                    </div>
                </div>
            </div>
        """
    }
]

slides_data_part1.slides_part1.extend(slides_21_to_35)
print(f"Appended Part 1-B. Total slides in Part 1 now: {len(slides_data_part1.slides_part1)}")
