# slides_part3_b.py
# Slides 87 to 102: Annuities, Capital Budgeting, CAPM, Derivatives, and Exam Master Checklist

slides_87_to_102 = [
    # SLIDE 87
    {
        "id": 87,
        "module": "Module 8 · Time Value of Money",
        "title": "Ordinary Annuity: Cash Flows at Period-End",
        "subtitle": "Equal periodic cash flows occurring at the end of each period",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Ordinary Annuity Mechanics</h3>
            <p>An annuity is a series of equal cash payments made at fixed, regular intervals. For an <strong>Ordinary Annuity</strong>, cash flows occur at the <strong>END</strong> of each period (e.g. loan EMIs, bond coupons):</p>
            <div class="formula-box">
                <div class="formula-name">Present Value of Ordinary Annuity (PVIFA):</div>
                <div class="formula-code">PV = PMT × [ (1 − (1 + r)^−n) / r ] = PMT × PVIFA(r, n)</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Shortcut with PV Table:</strong> In exams, <code>PVIFA(r, n)</code> is simply the sum of individual PV discount factors across all n years!</li>
                <li><strong>Example:</strong> If 1-yr factor is 0.893, 2-yr is 0.797, 3-yr is 0.712, then 3-yr PVIFA @ 12% = 0.893 + 0.797 + 0.712 = <strong>2.402</strong>.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Ordinary Annuity Stream</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.8rem; line-height:1.7;">
                    <div>Receive ₹10,000 at the end of Year 1, 2, and 3 @ 10%:</div>
                    <div style="display:flex; justify-content:space-between; margin-top:0.3rem;">
                        <span>End of Yr 1: ₹10,000 × 0.909</span>
                        <strong>= ₹9,090</strong>
                    </div>
                    <div style="display:flex; justify-content:space-between;">
                        <span>End of Yr 2: ₹10,000 × 0.826</span>
                        <strong>= ₹8,260</strong>
                    </div>
                    <div style="display:flex; justify-content:space-between;">
                        <span>End of Yr 3: ₹10,000 × 0.751</span>
                        <strong>= ₹7,510</strong>
                    </div>
                    <div style="border-top:1px dashed #cbd5e1; margin-top:0.4rem; padding-top:0.4rem; font-weight:bold; color:#1e40af;">
                        Total PV = ₹10,000 × 2.487 = ₹24,870
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 88
    {
        "id": 88,
        "module": "Module 8 · Time Value of Money",
        "title": "Annuity Due: Upfront Payments (The (1+r) Trap)",
        "subtitle": "Why beginning-of-period cash flows are worth more",
        "badge": "EXAM TRAP",
        "badge_type": "danger",
        "content_html": """
            <h3>Annuity Due: Immediate Upfront Cash Flows</h3>
            <p>In an <strong>Annuity Due</strong>, cash flows occur at the <strong>BEGINNING</strong> of each period (e.g. apartment rent, equipment lease):</p>
            <div class="formula-box">
                <div class="formula-name">Annuity Due Relationship:</div>
                <div class="formula-code">PV of Annuity Due = PV of Ordinary Annuity × (1 + r)</div>
            </div>
            <div class="callout callout-warning" style="margin-top:0.75rem;">
                <strong>⚠️ Why is Annuity Due worth more?</strong> Every single payment arrives exactly 1 period earlier, so every cash flow has 1 less period of discounting (earns 1 additional period of compounding interest)!
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; margin-top:0.5rem; font-size:0.85rem;">
                <strong>Numerical Quick Check:</strong> If Ordinary Annuity PV = ₹24,870 @ 10%, then:<br>
                <strong>Annuity Due PV</strong> = 24,870 × (1 + 0.10) = <strong>₹27,357</strong>.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Timeline Comparison</h4>
                <div style="display:flex; flex-direction:column; gap:0.5rem; font-size:0.8rem;">
                    <div style="background:#eff6ff; border:1px solid #93c5fd; padding:0.5rem; border-radius:6px;">
                        <strong>Ordinary Annuity:</strong> Payments at t=1, t=2, t=3<br>
                        <span style="color:#64748b; font-size:0.75rem;">First payment discounted by 1 full year</span>
                    </div>
                    <div style="background:#fefce8; border:1px solid #fde047; padding:0.5rem; border-radius:6px;">
                        <strong>Annuity Due:</strong> Payments at t=0, t=1, t=2<br>
                        <span style="color:#b45309; font-weight:bold; font-size:0.75rem;">Payment at t=0 has ZERO discounting! (Full face value)</span>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 89
    {
        "id": 89,
        "module": "Module 8 · Time Value of Money",
        "title": "Level Perpetuity: Infinite Constant Cash Flows",
        "subtitle": "Valuing consols, endowments, and perpetual preferred shares",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Level Perpetuity Formula</h3>
            <p>A perpetuity is an infinite series of equal cash payments that continues forever (n → ∞):</p>
            <div class="formula-box">
                <div class="formula-name">Present Value of Level Perpetuity:</div>
                <div class="formula-code">PV = Cash Flow (C) / Discount Rate (r)</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>No Complex Math Needed:</strong> As time goes to infinity, the annuity formula simplifies to just dividing by <code>r</code>!</li>
                <li><strong>Classic Example:</strong> A scholarship pays ₹50,000 every year forever. If the endowment earns 8% p.a., what donation is required today?
                    <div style="font-weight:bold; color:#1e40af; margin-top:0.3rem;">PV = 50,000 / 0.08 = ₹6,25,000.</div>
                </li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Perpetuity Arithmetic</h4>
                <div style="background:#ecfdf5; border:1px solid #86efac; border-radius:8px; padding:0.8rem; text-align:center;">
                    <div style="font-size:1.8rem; font-weight:bold; color:#065f46;">PV = C ÷ r</div>
                    <div style="font-size:0.85rem; color:#047857; margin-top:0.3rem;">
                        ₹60,000 / 0.10 = <strong>₹6,00,000</strong>
                    </div>
                    <div style="font-size:0.75rem; color:#475569; margin-top:0.5rem;">
                        ₹6 Lakhs in bank earning 10% generates ₹60k interest every year forever without touching principal!
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 90
    {
        "id": 90,
        "module": "Module 8 · Time Value of Money",
        "title": "Growing Perpetuity: The Gordon Growth Model",
        "subtitle": "Valuing cash flows that expand at constant growth rate g",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Growing Perpetuity (Gordon Model)</h3>
            <p>When cash flows do not stay flat but grow at a constant annual percentage rate <code>g</code> forever:</p>
            <div class="formula-box">
                <div class="formula-name">Present Value of Growing Perpetuity:</div>
                <div class="formula-code">PV = Cash Flow in Period 1 (CF₁) / (r − g)</div>
            </div>
            <div class="callout callout-danger" style="margin-top:0.75rem;">
                <strong>⚠️ Strict Mathematical Condition:</strong> Discount rate <code>r</code> <strong>MUST be strictly greater than</strong> growth rate <code>g</code> (r &gt; g). If g ≥ r, the formula explodes to infinity and becomes mathematically invalid!
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; margin-top:0.5rem; font-size:0.85rem;">
                <strong>Numerical:</strong> Next year dividend CF₁ = ₹10. Required return r = 12%. Constant dividend growth g = 7%.<br>
                <strong>Stock Value (PV)</strong> = 10 / (0.12 − 0.07) = 10 / 0.05 = <strong>₹200 per share</strong>.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Growing Stream Dynamics</h4>
                <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.8rem;">
                    <div style="background:#eff6ff; padding:0.5rem; border-radius:6px;">
                        <strong>Level Perpetuity:</strong> Denominator is <code>r</code>
                    </div>
                    <div style="background:#ecfdf5; padding:0.5rem; border-radius:6px;">
                        <strong>Growing Perpetuity:</strong> Denominator shrinks to <code>(r − g)</code>
                    </div>
                    <div style="background:#fef2f2; padding:0.5rem; border-radius:6px; color:#b91c1c; font-weight:bold; text-align:center;">
                        Smaller denominator = Much higher valuation!
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 91
    {
        "id": 91,
        "module": "Module 9 · Capital Budgeting",
        "title": "Capital Budgeting: The Long-Term Decision Framework",
        "subtitle": "Committing multi-crore capital today for multi-year cash returns",
        "badge": "CAPITAL BUDGETING",
        "badge_type": "primary",
        "content_html": """
            <h3>What is Capital Budgeting?</h3>
            <p>Capital budgeting is the process of planning and evaluating major long-term capital investments (building factories, buying machinery, launching product lines):</p>
            <ul style="margin-left:1.5rem; line-height:1.7; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Massive Capital Commitment:</strong> Mistakes cannot be easily reversed without massive losses.</li>
                <li><strong>Cash Flows, NOT Accounting Profits:</strong> Decisions must evaluate actual after-tax cash flows (PAT + Depreciation).</li>
                <li><strong>Incremental Analysis:</strong> Evaluate only the additional cash inflows and outflows generated directly by the project.</li>
            </ul>
            <div class="callout callout-info" style="margin-top:0.75rem;">
                <strong>Four Core Appraisal Techniques:</strong> 1. Net Present Value (NPV), 2. Internal Rate of Return (IRR), 3. Payback Period (PB), 4. Profitability Index (PI).
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The Investment Pipeline</h4>
                <div style="display:flex; justify-content:space-around; align-items:center; text-align:center; padding:1rem 0;">
                    <div style="background:#fee2e2; border:2px solid #ef4444; border-radius:8px; padding:0.6rem; width:40%;">
                        <div style="font-weight:bold; color:#991b1b;">Time 0</div>
                        <div style="font-size:0.8rem; color:#7f1d1d;">Outflow (Capex)</div>
                        <div style="font-size:0.75rem; color:#475569;">−₹80 Lakhs</div>
                    </div>
                    <div style="font-size:1.5rem; color:#94a3b8;">➔</div>
                    <div style="background:#dcfce7; border:2px solid #22c55e; border-radius:8px; padding:0.6rem; width:40%;">
                        <div style="font-weight:bold; color:#166534;">Years 1 to 5</div>
                        <div style="font-size:0.8rem; color:#14532d;">Inflows (Cash)</div>
                        <div style="font-size:0.75rem; color:#475569;">+₹25L / year</div>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 92
    {
        "id": 92,
        "module": "Module 9 · Capital Budgeting",
        "title": "Net Present Value (NPV): The Rupee Wealth Gold Standard",
        "subtitle": "Why NPV is the single best capital budgeting decision rule",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Net Present Value (NPV)</h3>
            <p>NPV measures the exact net additions to shareholder rupee wealth created by a project, discounted at the cost of capital <code>r</code>:</p>
            <div class="formula-box">
                <div class="formula-name">Net Present Value Formula:</div>
                <div class="formula-code">NPV = Present Value of Cash Inflows − Initial Cash Outlay</div>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; margin-top:0.75rem; font-size:0.85rem;">
                <div style="background:#dcfce7; border:1px solid #86efac; padding:0.5rem; border-radius:6px;">
                    <strong style="color:#166534;">Accept if NPV &gt; 0</strong><br>
                    Project earns more than the hurdle rate. Adds direct rupee wealth to equity owners!
                </div>
                <div style="background:#fee2e2; border:1px solid #fca5a5; padding:0.5rem; border-radius:6px;">
                    <strong style="color:#991b1b;">Reject if NPV &lt; 0</strong><br>
                    Project earns less than the required return. Destroys shareholder wealth!
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">NPV Wealth Creation</h4>
                <div style="background:#eff6ff; border:1px solid #93c5fd; border-radius:8px; padding:0.8rem; text-align:center;">
                    <div style="font-size:1.1rem; font-weight:bold; color:#1e40af;">
                        NPV = Σ [ CFt / (1 + r)^t ] − Initial Investment
                    </div>
                </div>
                <div style="margin-top:0.75rem; font-size:0.8rem; color:#475569; text-align:center;">
                    Considers all cash flows, incorporates time value of money, and directly measures shareholder wealth creation!
                </div>
            </div>
        """
    },

    # SLIDE 93
    {
        "id": 93,
        "module": "Module 9 · Capital Budgeting",
        "title": "Bharat AutoParts Numerical: The 5-Year Machinery Case",
        "subtitle": "Step-by-step arithmetic without scientific calculators",
        "badge": "WORKED NUMERICAL",
        "badge_type": "primary",
        "content_html": """
            <h3>Bharat AutoParts Worked Numerical</h3>
            <p>From the speed-run lecture: Bharat AutoParts evaluates an automated CNC stamping machine:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <tr><th>Parameter</th><th>Value</th><th>Exam Context</th></tr>
                    <tr><td>Initial Outlay (Capex at t=0)</td><td>₹80 Lakhs</td><td>Immediate cash outflow</td></tr>
                    <tr><td>Annual Cash Inflows (Years 1 to 5)</td><td>₹25 Lakhs per year</td><td>Constant annuity for 5 years</td></tr>
                    <tr><td>Cost of Capital (Discount Rate r)</td><td>12.0%</td><td>Hurdle rate</td></tr>
                    <tr><td>PVIFA Table Factor (12%, 5 years)</td><td><strong>3.6048</strong></td><td>Given on exam formula sheet</td></tr>
                </table>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; margin-top:0.5rem; font-size:0.85rem; line-height:1.7;">
                1. <strong>PV of Cash Inflows:</strong> 25 Lakhs × 3.6048 = <strong>₹90.12 Lakhs</strong>.<br>
                2. <strong>Net Present Value (NPV):</strong> 90.12 − 80.00 = <strong>+₹10.12 Lakhs</strong>.<br>
                3. <strong>Decision:</strong> <strong>ACCEPT!</strong> Machine adds ₹10.12 Lakhs of direct shareholder wealth.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Bharat Auto Balance</h4>
                <div style="display:flex; justify-content:space-around; align-items:center; text-align:center; padding:0.5rem 0;">
                    <div style="background:#eff6ff; border:1px solid #93c5fd; padding:0.6rem; border-radius:8px; width:45%;">
                        <div style="font-size:0.75rem; color:#64748b;">PV of Inflows</div>
                        <div style="font-size:1.1rem; font-weight:bold; color:#1e40af;">₹90.12L</div>
                    </div>
                    <div style="font-size:1.2rem; font-weight:bold; color:#dc2626;">−</div>
                    <div style="background:#fee2e2; border:1px solid #fca5a5; padding:0.6rem; border-radius:8px; width:45%;">
                        <div style="font-size:0.75rem; color:#64748b;">Cost of Machine</div>
                        <div style="font-size:1.1rem; font-weight:bold; color:#991b1b;">₹80.00L</div>
                    </div>
                </div>
                <div style="text-align:center; margin-top:0.6rem; font-weight:bold; color:#059669; font-size:1rem;">
                    NPV = +₹10.12 Lakhs (Accept!)
                </div>
            </div>
        """
    },

    # SLIDE 94
    {
        "id": 94,
        "module": "Module 9 · Capital Budgeting",
        "title": "Internal Rate of Return (IRR): The Breakeven Rate",
        "subtitle": "The discount rate where NPV equals exactly ZERO",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Internal Rate of Return (IRR)</h3>
            <p>The IRR is the project's internal yield—the discount rate that makes Present Value of Inflows equal to Initial Outlay (NPV = 0):</p>
            <div class="formula-box">
                <div class="formula-name">IRR Definition:</div>
                <div class="formula-code">At Discount Rate = IRR ➔ NPV = 0</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Decision Rule:</strong> Accept if <strong>IRR &gt; Cost of Capital (r)</strong>.</li>
                <li><strong>Linear Interpolation Shortcut (if asked):</strong>
                    <div style="font-weight:bold; color:#1e40af; margin-top:0.3rem;">IRR ≈ r_L + [ NPV_L / (NPV_L − NPV_H) ] × (r_H − r_L)</div>
                </li>
                <li>For Bharat AutoParts: IRR is approximately <strong>17.0%</strong>. Since 17% &gt; 12% cost of capital, project is acceptable!</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The NPV Profile Curve</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.8rem; line-height:1.7;">
                    <div>• At r = 0%: NPV = +₹45 Lakhs (Undiscounted)</div>
                    <div>• At r = 12%: NPV = +₹10.12 Lakhs (Cost of capital)</div>
                    <div style="color:#059669; font-weight:bold;">• At r = 17%: NPV = ₹0 ➔ IRR is 17%!</div>
                    <div style="color:#dc2626;">• At r = 20%: NPV = −₹5.2 Lakhs (Negative)</div>
                </div>
            </div>
        """
    },

    # SLIDE 95
    {
        "id": 95,
        "module": "Module 9 · Capital Budgeting",
        "title": "NPV vs IRR Conflict: Mutually Exclusive Projects",
        "subtitle": "Why you must ALWAYS follow NPV and ignore IRR in conflicts",
        "badge": "EXAM TRAP",
        "badge_type": "danger",
        "content_html": """
            <h3>The Classical NPV vs IRR Conflict</h3>
            <p>When choosing between mutually exclusive projects (can only pick one), NPV and IRR often give conflicting advice:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.8rem;">
                    <tr><th>Project</th><th>Initial Outlay</th><th>NPV (₹ Wealth)</th><th>IRR (%)</th><th>Which Metric Wins?</th></tr>
                    <tr><td><strong>Project Solar Farm</strong></td><td>₹100 Lakhs</td><td><strong style="color:#059669;">+₹30 Lakhs</strong></td><td>18.0%</td><td><strong>NPV Champion</strong></td></tr>
                    <tr><td><strong>Project LED Lighting</strong></td><td>₹10 Lakhs</td><td>+₹5 Lakhs</td><td><strong style="color:#dc2626;">40.0%</strong></td><td>IRR Champion</td></tr>
                </table>
            </div>
            <div class="callout callout-danger" style="margin-top:0.75rem;">
                <strong>🚨 The Golden Exam Rule: ALWAYS CHOOSE NPV!</strong><br>
                Why? You cannot deposit percentages in a bank account! Project Solar adds <strong>₹30 Lakhs</strong> of absolute rupee wealth to owners, whereas LED lighting adds only <strong>₹5 Lakhs</strong>. IRR is scale-blind!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The Scale Flaw of IRR</h4>
                <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.8rem;">
                    <div style="background:#fee2e2; padding:0.5rem; border-radius:6px;">
                        <strong>100% Return on ₹10</strong> = Earn ₹10 Profit
                    </div>
                    <div style="text-align:center; font-weight:bold; color:#64748b;">vs</div>
                    <div style="background:#dcfce7; padding:0.5rem; border-radius:6px;">
                        <strong>20% Return on ₹1,00,000</strong> = Earn ₹20,000 Profit!
                    </div>
                </div>
                <div style="text-align:center; margin-top:0.6rem; font-size:0.8rem; font-weight:bold; color:#1e40af;">
                    NPV accounts for scale; IRR ignores it completely.
                </div>
            </div>
        """
    },

    # SLIDE 96
    {
        "id": 96,
        "module": "Module 9 · Capital Budgeting",
        "title": "Payback Period: Recovery Time & Major Flaws",
        "subtitle": "How fast the initial cash outlay is recovered",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Payback Period (PB)</h3>
            <p>Measures the exact number of years required to recover the initial cash outlay from incoming cash flows:</p>
            <div class="formula-box">
                <div class="formula-name">Equal Cash Flows Payback Formula:</div>
                <div class="formula-code">Payback Period = Initial Investment / Annual Cash Inflow</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Bharat Auto:</strong> Outlay = ₹80L, Annual Inflow = ₹25L ➔ Payback = 80 / 25 = <strong>3.2 Years</strong>.</li>
                <li><strong>Two Fatal Shortcomings (Guaranteed MCQ):</strong>
                    <br>1. <strong>Ignores Time Value of Money:</strong> Treats ₹25L in Year 5 the same as ₹25L in Year 1.
                    <br>2. <strong>Ignores all cash flows after payback:</strong> A project that yields ₹100 Crores in Year 6 is rejected if payback cutoff is 3 years!
                </li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Payback Timeline</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.8rem; line-height:1.7;">
                    <div>Outlay: −₹80 Lakhs</div>
                    <div>Yr 1: +₹25L (Balance: −₹55L)</div>
                    <div>Yr 2: +₹25L (Balance: −₹30L)</div>
                    <div>Yr 3: +₹25L (Balance: −₹5L)</div>
                    <div style="font-weight:bold; color:#059669;">
                        Yr 4: 5 / 25 = 0.2 Yrs ➔ Total = <strong>3.2 Years</strong>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 97
    {
        "id": 97,
        "module": "Module 9 · Capital Budgeting",
        "title": "Profitability Index (PI) & Capital Rationing",
        "subtitle": "Ranking projects when investment budget is strictly capped",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Profitability Index (Benefit-Cost Ratio)</h3>
            <p>Measures the present value of cash inflows generated per ₹1 of initial investment:</p>
            <div class="formula-box">
                <div class="formula-name">Profitability Index Formula:</div>
                <div class="formula-code">PI = Present Value of Inflows / Initial Outlay = (NPV + Outlay) / Outlay</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Acceptance Rule:</strong> Accept if <strong>PI &gt; 1.0</strong> (matches NPV &gt; 0).</li>
                <li><strong>Bharat AutoParts PI:</strong> 90.12 / 80.00 = <strong>1.13</strong>.</li>
                <li><strong>When to use PI instead of NPV?</strong> When the firm faces <strong>Capital Rationing</strong> (e.g. only ₹50 Crores total budget). Ranking by highest PI maximizes total NPV within a fixed capital budget!</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Bang for the Buck</h4>
                <div style="background:#eff6ff; border:1px solid #93c5fd; border-radius:8px; padding:0.8rem; text-align:center;">
                    <div style="font-size:1.8rem; font-weight:bold; color:#1e40af;">PI = 1.13</div>
                    <div style="font-size:0.85rem; color:#1e3a8a; margin-top:0.3rem;">
                        Every ₹1.00 invested returns ₹1.13 in present value.
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 98
    {
        "id": 98,
        "module": "Module 9 · Capital Budgeting",
        "title": "Capital Budgeting Master Summary & Decision Matrix",
        "subtitle": "Side-by-side comparison across all 4 appraisal methods",
        "badge": "MASTER MATRIX",
        "badge_type": "primary",
        "content_html": """
            <h3>Appraisal Techniques Comparison</h3>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.75rem;">
                    <tr><th>Method</th><th>Formula / Metric</th><th>Accept Rule</th><th>Reinvestment Assumption</th><th>Primary Weakness</th></tr>
                    <tr><td><strong>NPV</strong></td><td>PV Inflows − Outlay</td><td>NPV &gt; 0</td><td><strong>Cost of Capital (r)</strong> (Realistic)</td><td>Scale-sensitive</td></tr>
                    <tr><td><strong>IRR</strong></td><td>Discount rate where NPV = 0</td><td>IRR &gt; r</td><td><strong>At IRR rate</strong> (Unrealistic)</td><td>Ignores scale; multiple roots</td></tr>
                    <tr><td><strong>Payback</strong></td><td>Years to recover outlay</td><td>PB &lt; Cutoff</td><td>None (No TVM)</td><td>Ignores post-payback cash flows</td></tr>
                    <tr><td><strong>PI</strong></td><td>PV Inflows / Outlay</td><td>PI &gt; 1.0</td><td>Cost of Capital (r)</td><td>Cannot pick between mutually exclusive without scale adjustment</td></tr>
                </table>
            </div>
            <div class="callout callout-info" style="margin-top:0.5rem;">
                <strong>Exam Guaranteed Question:</strong> What rate does NPV assume cash flows are reinvested at? ➔ <strong>The Cost of Capital</strong>!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The Undisputed King</h4>
                <div style="background:#ecfdf5; border:2px solid #10b981; border-radius:8px; padding:1rem; text-align:center;">
                    <div style="font-size:2rem;">👑</div>
                    <div style="font-weight:bold; color:#065f46; font-size:1.1rem;">NPV ALWAYS WINS</div>
                    <div style="font-size:0.8rem; color:#047857; margin-top:0.4rem;">
                        Measures absolute wealth added to shareholders' pockets in hard rupees.
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 99
    {
        "id": 99,
        "module": "Module 10 · CAPM & Derivatives",
        "title": "Cost of Equity & CAPM: The Risk-Return Formula",
        "subtitle": "How investors price market risk (Beta)",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Capital Asset Pricing Model (CAPM)</h3>
            <p>From Session 9: CAPM calculates the required rate of return for equity investors based on systematic market risk:</p>
            <div class="formula-box">
                <div class="formula-name">CAPM Cost of Equity Formula:</div>
                <div class="formula-code">Ke = Rf + β × (Rm − Rf)</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Rf (Risk-Free Rate):</strong> Yield on sovereign government bonds (e.g. 6.0%).</li>
                <li><strong>Rm:</strong> Expected return on the broad stock market (e.g. Nifty 50 = 14.0%).</li>
                <li><strong>(Rm − Rf):</strong> <strong>Equity Risk Premium (ERP)</strong> = The extra reward demanded for taking equity risk (14% − 6% = 8.0%).</li>
                <li><strong>β (Beta):</strong> Volatility sensitivity relative to the market index.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">CAPM Worked Numerical</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.85rem; line-height:1.7;">
                    <div>• <strong>Rf:</strong> 6.0% | <strong>Rm:</strong> 14.0%</div>
                    <div>• <strong>Beta (β):</strong> 1.25</div>
                    <div style="margin-top:0.4rem; padding-top:0.4rem; border-top:1px dashed #cbd5e1;">
                        ERP = 14.0% − 6.0% = <strong>8.0%</strong>
                    </div>
                    <div style="font-weight:bold; color:#1e40af; margin-top:0.3rem;">
                        Ke = 6.0% + 1.25 × (8.0%) = 6.0% + 10.0% = <strong>16.0%</strong>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 100
    {
        "id": 100,
        "module": "Module 10 · CAPM & Derivatives",
        "title": "Beta & Jensen's Alpha: Risk & Outperformance",
        "subtitle": "Systematic volatility vs manager skill",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Interpreting Beta (β) & Jensen's Alpha (α)</h3>
            <p>Beta measures systematic market risk that cannot be eliminated by diversification:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.8rem;">
                    <tr><th>Beta Value</th><th>Classification</th><th>Interpretation</th><th>Sector Examples</th></tr>
                    <tr><td><strong>β = 1.0</strong></td><td>Average Market Risk</td><td>Moves 1-to-1 with Nifty 50</td><td>Index ETFs</td></tr>
                    <tr><td><strong>β &gt; 1.0</strong></td><td>Aggressive / Cyclical</td><td>Amplifies market swings (high volatility)</td><td>Real Estate, Metals, Auto</td></tr>
                    <tr><td><strong>β &lt; 1.0</strong></td><td>Defensive</td><td>Resists market crashes (low volatility)</td><td>FMCG, Pharma, Utilities</td></tr>
                </table>
            </div>
            <div class="formula-box" style="margin-top:0.5rem;">
                <div class="formula-name">Jensen's Alpha Formula:</div>
                <div class="formula-code">Alpha (α) = Actual Realized Return − CAPM Required Return</div>
            </div>
            <p style="font-size:0.85rem; margin-top:0.4rem;">
                <strong>Positive Alpha (+α)</strong> means fund manager outperformed risk expectations (true skill).
            </p>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Alpha Numerical</h4>
                <div style="background:#ecfdf5; border:1px solid #86efac; border-radius:8px; padding:0.6rem; font-size:0.8rem; line-height:1.7;">
                    <div>• CAPM Required Return: 16.0%</div>
                    <div>• Fund Actual Return: 19.5%</div>
                    <div style="font-weight:bold; color:#065f46; border-top:1px dashed #cbd5e1; margin-top:0.3rem; padding-top:0.3rem;">
                        Jensen's Alpha (α) = 19.5% − 16.0% = <strong>+3.5%</strong>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 101
    {
        "id": 101,
        "module": "Module 10 · CAPM & Derivatives",
        "title": "Financial Derivatives: Forwards vs Futures",
        "subtitle": "Strictly theoretical comparison for exam hall MCQs",
        "badge": "THEORY ONLY",
        "badge_type": "primary",
        "content_html": """
            <h3>Forwards vs Futures Contracts</h3>
            <p>From Sessions 13–14: No complex derivative math is tested. Focus strictly on institutional differences:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.8rem;">
                    <tr><th>Feature</th><th>Forward Contract</th><th>Futures Contract</th></tr>
                    <tr><td><strong>Trading Venue</strong></td><td>Over-the-Counter (OTC, private bank deal)</td><td>Organized Exchange (NSE, BSE, CME)</td></tr>
                    <tr><td><strong>Contract Terms</strong></td><td>Fully customized (any date, size, commodity)</td><td>Strictly standardized (fixed lots & expiry dates)</td></tr>
                    <tr><td><strong>Default / Credit Risk</strong></td><td><strong style="color:#dc2626;">High Counterparty Risk</strong> (party may default)</td><td><strong style="color:#059669;">Zero Default Risk</strong> (Guaranteed by Clearinghouse)</td></tr>
                    <tr><td><strong>Settlement Method</strong></td><td>Settled in single lump sum on maturity date</td><td>Daily Mark-to-Market (MTM) margin settlement</td></tr>
                    <tr><td><strong>Liquidity</strong></td><td>Low (difficult to exit early)</td><td>High (liquid secondary trading anytime)</td></tr>
                </table>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Clearinghouse Novation</h4>
                <div style="background:#eff6ff; border:1px solid #93c5fd; border-radius:8px; padding:0.6rem; text-align:center; font-size:0.8rem;">
                    <div style="display:flex; justify-content:space-around; align-items:center;">
                        <span style="font-weight:bold;">Buyer</span>
                        <span>➔</span>
                        <span style="background:#3b82f6; color:#ffffff; padding:0.3rem 0.5rem; border-radius:4px; font-weight:bold;">Clearinghouse</span>
                        <span>➔</span>
                        <span style="font-weight:bold;">Seller</span>
                    </div>
                    <div style="margin-top:0.5rem; color:#1e3a8a;">
                        The Clearinghouse becomes the buyer to every seller and seller to every buyer, eliminating counterparty default!
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 102
    {
        "id": 102,
        "module": "Module 10 · CAPM & Derivatives",
        "title": "Options Demystified & 100/100 Exam Hall Final Checklist",
        "subtitle": "Calls, Puts, Asymmetric Payoffs & The Golden Rules",
        "badge": "FINAL CHECKLIST",
        "badge_type": "success",
        "content_html": """
            <h3>Options Foundations & Exam Hall Checklist</h3>
            <p>An option gives the buyer the <strong>RIGHT, but NOT the obligation</strong> to transact:</p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; margin-top:0.5rem; font-size:0.8rem;">
                <div style="background:#ecfdf5; border:1px solid #86efac; padding:0.5rem; border-radius:6px;">
                    <strong style="color:#166534;">Call Option (Right to BUY)</strong><br>
                    • Bullish view (Expect price to rise).<br>
                    • Buyer max loss = <strong>Premium paid</strong>.<br>
                    • Buyer max gain = <strong>Unlimited</strong>.
                </div>
                <div style="background:#fee2e2; border:1px solid #fca5a5; padding:0.5rem; border-radius:6px;">
                    <strong style="color:#991b1b;">Put Option (Right to SELL)</strong><br>
                    • Bearish view (Protective put for insurance).<br>
                    • Buyer max loss = <strong>Premium paid</strong>.<br>
                    • Buyer max gain = Down to Strike price (if stock hits 0).
                </div>
            </div>
            <div style="background:#f8fafc; border-left:4px solid #10b981; padding:0.6rem; margin-top:0.75rem; font-size:0.85rem;">
                <strong>🎓 5 Final Rules for 100/100:</strong><br>
                1. <em>Drawings & Dividends:</em> Never an expense on P&L (Direct equity reduction).<br>
                2. <em>CVP Formulas:</em> Memorize BEP = FC / Unit Contribution (Not on formula sheet!).<br>
                3. <em>NPV vs IRR:</em> In mutual exclusivity, ALWAYS pick highest NPV.<br>
                4. <em>Sunk Costs:</em> Past spent money is 100% irrelevant to decisions.<br>
                5. <em>Time Management:</em> 40 MCQs in 120 mins = 3 mins/question. Sweep theory first!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <div style="text-align:center; padding:1.5rem 0.5rem;">
                    <div style="font-size:3.5rem; margin-bottom:0.5rem;">🏆</div>
                    <h3 style="color:#059669; font-size:1.4rem; margin-bottom:0.3rem;">Masterclass Completed!</h3>
                    <p style="color:#475569; font-size:0.85rem;">You have covered all 102 slides spanning Sessions 1–16.</p>
                    <div style="margin-top:1rem; display:inline-block; background:#dcfce7; border:2px solid #22c55e; border-radius:8px; padding:0.5rem 1rem; font-weight:bold; color:#166534; font-size:0.9rem;">
                        Target: 100/100 in FMI Final Exam
                    </div>
                </div>
            </div>
        """
    }
]

print(f"Loaded {len(slides_87_to_102)} slides in Part 3-B.")
