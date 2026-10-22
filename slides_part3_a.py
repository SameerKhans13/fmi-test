# slides_part3_a.py
# Slides 71 to 86: Overhead Absorption, CVP / Break-Even Mastery, and Time Value Foundations

slides_71_to_86 = [
    # SLIDE 71
    {
        "id": 71,
        "module": "Module 6 · Management Accounting",
        "title": "Overhead Absorption & Predetermined OAR",
        "subtitle": "How indirect factory costs are allocated to products",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Overhead Absorption Rate (OAR) Mechanics</h3>
            <p>Overheads (indirect rent, machine maintenance, supervisor wages) cannot be traced to specific products. Companies establish a predetermined rate at the start of the year:</p>
            <div class="formula-box">
                <div class="formula-name">Predetermined Overhead Absorption Rate (OAR):</div>
                <div class="formula-code">OAR = Budgeted Factory Overheads / Budgeted Activity Level (Hours or Units)</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Activity Bases commonly used:</strong> Direct Labour Hours (for labour-intensive plants), Machine Hours (for automated robot plants), or Direct Material Cost.</li>
                <li><strong>Applying OAR to a Job:</strong> Absorbed Overhead = Actual Activity Units × Predetermined OAR.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">OAR Calculation Example</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.85rem; line-height:1.7;">
                    <div>• <strong>Budgeted Factory Overheads:</strong> ₹5,00,000</div>
                    <div>• <strong>Budgeted Machine Hours:</strong> 25,000 hours</div>
                    <div style="margin-top:0.4rem; padding-top:0.4rem; border-top:1px dashed #cbd5e1;">
                        <strong>OAR</strong> = 5,00,000 / 25,000 = <strong>₹20 per machine hour</strong>
                    </div>
                </div>
                <div style="margin-top:0.6rem; font-size:0.8rem; color:#475569; text-align:center;">
                    If Job #101 consumes 15 machine hours, it absorbs: 15 × ₹20 = <strong>₹300 overhead</strong>.
                </div>
            </div>
        """
    },

    # SLIDE 72
    {
        "id": 72,
        "module": "Module 6 · Management Accounting",
        "title": "Under-Absorption vs Over-Absorption of Overheads",
        "subtitle": "Closing variance adjustments at year-end",
        "badge": "EXAM TRAP",
        "badge_type": "danger",
        "content_html": """
            <h3>Under-Absorption vs Over-Absorption</h3>
            <p>Because OAR is estimated upfront, actual overheads incurred almost never match absorbed overheads:</p>
            <div class="formula-box">
                <div class="formula-name">Overhead Variance Equation:</div>
                <div class="formula-code">Overhead Variance = Absorbed Overheads − Actual Overheads Incurred</div>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; margin-top:0.75rem; font-size:0.8rem;">
                <div style="background:#fee2e2; border:1px solid #fca5a5; padding:0.6rem; border-radius:8px;">
                    <strong style="color:#991b1b;">Under-Absorbed (Debit P&L)</strong><br>
                    <span>Absorbed Overheads &lt; Actual Overheads</span><br>
                    <span style="font-size:0.75rem; color:#7f1d1d;">Too little cost was assigned to products! Remaining unabsorbed overhead is <strong>debited to P&L, slashing profit</strong>.</span>
                </div>
                <div style="background:#dcfce7; border:1px solid #86efac; padding:0.6rem; border-radius:8px;">
                    <strong style="color:#166534;">Over-Absorbed (Credit P&L)</strong><br>
                    <span>Absorbed Overheads &gt; Actual Overheads</span><br>
                    <span style="font-size:0.75rem; color:#14532d;">Too much cost was assigned to products! Excess absorbed overhead is <strong>credited to P&L, boosting profit</strong>.</span>
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Year-End P&L Impact</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.85rem; line-height:1.7;">
                    <div>• <strong>Actual Factory Overhead Spent:</strong> ₹5,20,000</div>
                    <div>• <strong>Overhead Absorbed (24k hrs × ₹20):</strong> ₹4,80,000</div>
                    <div style="margin-top:0.4rem; padding-top:0.4rem; border-top:1px dashed #cbd5e1; color:#dc2626; font-weight:bold;">
                        = Under-Absorbed: ₹40,000 (Debit to P&L)
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 73
    {
        "id": 73,
        "module": "Module 7 · CVP & Break-Even",
        "title": "Cost-Volume-Profit (CVP): The Unprovided Formulas",
        "subtitle": "Formulas you MUST commit to memory for the exam hall",
        "badge": "MUST MEMORIZE",
        "badge_type": "danger",
        "content_html": """
            <h3>The CVP Secret Weapon</h3>
            <p>While financial ratios are provided on your formula sheet, <strong>CVP and Break-Even formulas are NOT provided</strong>! You must memorize them thoroughly:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <tr><th>Formula Name</th><th>Exact Mathematical Expression</th></tr>
                    <tr><td><strong>Unit Contribution</strong></td><td><code>Selling Price (SP) − Variable Cost per Unit (VC)</code></td></tr>
                    <tr><td><strong>P/V Ratio (Profit-Volume)</strong></td><td><code>Contribution / Sales = (SP − VC) / SP</code></td></tr>
                    <tr><td><strong>Break-Even Point (Units)</strong></td><td><code>Fixed Cost / Unit Contribution</code></td></tr>
                    <tr><td><strong>Break-Even Point (Value ₹)</strong></td><td><code>Fixed Cost / P/V Ratio</code></td></tr>
                    <tr><td><strong>Target Profit (Units)</strong></td><td><code>(Fixed Cost + Target Profit) / Unit Contribution</code></td></tr>
                    <tr><td><strong>Margin of Safety (MoS)</strong></td><td><code>Actual Sales − Break-Even Sales = Profit / P/V Ratio</code></td></tr>
                </table>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The Marginal Costing Flow</h4>
                <div style="background:#eff6ff; border:1px solid #93c5fd; border-radius:8px; padding:0.6rem; font-size:0.85rem; line-height:1.8;">
                    <div style="display:flex; justify-content:space-between;">
                        <span>Sales Revenue (SP × Q)</span>
                        <span style="font-weight:bold;">100%</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; color:#dc2626;">
                        <span>− Total Variable Cost (VC × Q)</span>
                        <span>Variable Ratio</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; border-top:2px solid #3b82f6; padding-top:0.2rem; font-weight:bold; color:#1e40af;">
                        <span>= Total Contribution</span>
                        <span>P/V Ratio</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; color:#dc2626;">
                        <span>− Total Fixed Cost</span>
                        <span>Fixed Amount</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; border-top:2px solid #10b981; padding-top:0.2rem; font-weight:bold; color:#065f46;">
                        <span>= Operating Profit</span>
                        <span>Bottom Line</span>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 74
    {
        "id": 74,
        "module": "Module 7 · CVP & Break-Even",
        "title": "Unit Contribution & The Recovery Mechanism",
        "subtitle": "What each unit sold contributes towards fixed costs",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Unit Contribution: Selling Price Minus Variable Cost</h3>
            <p>Every time you sell one unit, you collect the Selling Price. After paying the unit's direct variable cost, whatever is left over is the <strong>Contribution</strong>:</p>
            <div class="formula-box">
                <div class="formula-name">Unit Contribution:</div>
                <div class="formula-code">Contribution per unit = Selling Price (SP) − Variable Cost per Unit (VC)</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.7; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Why call it 'Contribution'?</strong> Because it <em>contributes</em> towards paying off the fixed overheads (rent, salaries).</li>
                <li>Once fixed overheads are 100% paid off, <strong>every additional rupee of contribution becomes pure 100% profit</strong>!</li>
                <li>If Contribution is negative (SP &lt; VC), stop manufacturing immediately! Every unit sold increases the loss.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Visual Unit Anatomy</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.8rem; font-size:0.85rem;">
                    <div style="font-weight:bold; font-size:1.1rem; color:#1e40af; text-align:center; margin-bottom:0.5rem;">
                        Selling Price = ₹1,000
                    </div>
                    <div style="display:flex; height:28px; border-radius:6px; overflow:hidden; text-align:center; color:#ffffff; font-weight:bold; font-size:0.8rem; line-height:28px;">
                        <div style="background:#ef4444; width:60%;">VC: ₹600 (60%)</div>
                        <div style="background:#10b981; width:40%;">Contribution: ₹400 (40%)</div>
                    </div>
                    <div style="margin-top:0.6rem; font-size:0.8rem; color:#475569; text-align:center;">
                        ₹400 goes towards paying fixed rent.
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 75
    {
        "id": 75,
        "module": "Module 7 · CVP & Break-Even",
        "title": "Profit-Volume (P/V) Ratio (Contribution Margin %)",
        "subtitle": "How many paise of profit are generated per ₹1 of sales",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Profit-Volume (P/V) Ratio</h3>
            <p>The P/V ratio expresses contribution as a percentage of sales revenue:</p>
            <div class="formula-box">
                <div class="formula-name">P/V Ratio Formula:</div>
                <div class="formula-code">P/V Ratio = Contribution / Sales = (SP − VC) / SP = Change in Profit / Change in Sales</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Fundamental Property:</strong> <code>P/V Ratio + Variable Cost Ratio = 100%</code>. If VC ratio is 60%, P/V ratio is automatically 40%!</li>
                <li><strong>Shortcut Exam Formula:</strong> When data for two different periods is given without unit costs:
                    <div style="font-weight:bold; color:#1e40af; margin-top:0.3rem;">P/V Ratio = (Profit Period 2 − Profit Period 1) / (Sales Period 2 − Sales Period 1)</div>
                </li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Two-Period P/V Shortcut</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.8rem; line-height:1.7;">
                    <div>• Year 1: Sales ₹10L | Profit ₹1L</div>
                    <div>• Year 2: Sales ₹15L | Profit ₹3L</div>
                    <div style="margin-top:0.4rem; padding-top:0.4rem; border-top:1px dashed #cbd5e1;">
                        Change in Profit = ₹2L | Change in Sales = ₹5L
                    </div>
                    <div style="font-weight:bold; color:#059669; margin-top:0.3rem;">
                        P/V Ratio = 2,00,000 / 5,00,000 = <strong>40.0%</strong>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 76
    {
        "id": 76,
        "module": "Module 7 · CVP & Break-Even",
        "title": "Break-Even Point (BEP) in Physical Units",
        "subtitle": "How many units must be sold to neither earn a profit nor suffer a loss",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Break-Even Point (Units)</h3>
            <p>At the Break-Even Point, Total Revenue exactly equals Total Cost. Net Profit is exactly ZERO:</p>
            <div class="formula-box">
                <div class="formula-name">Break-Even Units Formula:</div>
                <div class="formula-code">BEP (Units) = Total Fixed Cost / Contribution per Unit = FC / (SP − VC)</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>Logic:</strong> If your monthly factory rent is ₹1,00,000 and each chair sold gives ₹500 of contribution, you must sell exactly 1,00,000 / 500 = <strong>200 chairs</strong> to break even!</li>
                <li>Selling 199 chairs = Net Loss.</li>
                <li>Selling 201 chairs = Net Profit of ₹500.</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The Break-Even Scale</h4>
                <div style="text-align:center; padding:1rem 0;">
                    <div style="font-size:2rem; font-weight:bold; color:#1e40af;">Profit = ₹0</div>
                    <div style="font-size:0.85rem; color:#64748b; margin-top:0.3rem;">Total Revenue = Total Costs</div>
                    <div style="margin-top:0.8rem; background:#eff6ff; border:1px solid #93c5fd; padding:0.6rem; border-radius:8px; font-size:0.8rem;">
                        <strong>FC = ₹1,00,000 | Unit Contrib = ₹500</strong><br>
                        BEP = 1,00,000 / 500 = <strong>200 Units</strong>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 77
    {
        "id": 77,
        "module": "Module 7 · CVP & Break-Even",
        "title": "Break-Even Point (BEP) in Value (Rupees ₹)",
        "subtitle": "How much sales revenue is required to cover all operating costs",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Break-Even Sales Revenue (Value ₹)</h3>
            <p>When questions ask for break-even in Rupees (or for multi-product firms where physical unit counts cannot be added together):</p>
            <div class="formula-box">
                <div class="formula-name">Break-Even Value Formula:</div>
                <div class="formula-code">BEP (Sales ₹) = Fixed Cost / P/V Ratio = BEP (Units) × Selling Price</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; margin-top:0.5rem; font-size:0.85rem;">
                <strong>Worked Numerical:</strong><br>
                • Fixed Costs = ₹12,00,000<br>
                • Selling Price = ₹100 | Variable Cost = ₹60 (P/V Ratio = 40%)<br>
                <strong>BEP (Value ₹)</strong> = 12,00,000 / 0.40 = <strong>₹30,00,000</strong>.<br>
                <em>Check:</em> BEP Units = 12,00,000 / 40 = 30,000 units × ₹100 = ₹30,00,000.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Break-Even Revenue Dial</h4>
                <div style="display:flex; justify-content:center; align-items:center; height:120px;">
                    <div style="background:#ecfdf5; border:3px solid #10b981; border-radius:50%; width:110px; height:110px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
                        <span style="font-size:0.75rem; color:#047857; font-weight:bold;">BEP SALES</span>
                        <span style="font-size:1.1rem; font-weight:bold; color:#065f46;">₹30 Lakh</span>
                    </div>
                </div>
                <div style="text-align:center; font-size:0.8rem; color:#475569;">
                    Sales above ₹30L generate profits at 40% margin!
                </div>
            </div>
        """
    },

    # SLIDE 78
    {
        "id": 78,
        "module": "Module 7 · CVP & Break-Even",
        "title": "Target Profit Analysis: Desired Rupee Income",
        "subtitle": "Determining exact sales required to hit profit targets",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Required Sales for Target Profit</h3>
            <p>To generate a desired profit target, the contribution must cover BOTH the fixed overheads AND the target profit:</p>
            <div class="formula-box">
                <div class="formula-name">Target Profit (Units):</div>
                <div class="formula-code">Required Units = (Fixed Cost + Target Profit) / Unit Contribution</div>
            </div>
            <div class="formula-box" style="margin-top:0.4rem;">
                <div class="formula-name">Target Profit (Sales ₹):</div>
                <div class="formula-code">Required Sales (₹) = (Fixed Cost + Target Profit) / P/V Ratio</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; margin-top:0.5rem; font-size:0.85rem;">
                <strong>Numerical:</strong> FC = ₹24,00,000 | Unit Contrib = ₹800 | Desired Profit = ₹8,00,000<br>
                <strong>Required Units</strong> = (24,00,000 + 8,00,000) / 800 = 32,00,000 / 800 = <strong>4,000 Units</strong>.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Combined Contribution Target</h4>
                <div style="display:flex; flex-direction:column; gap:0.4rem; font-size:0.8rem;">
                    <div style="background:#fee2e2; border:1px solid #fca5a5; padding:0.5rem; border-radius:6px;">
                        <strong>Fixed Costs to Cover:</strong> ₹24,00,000 (3,000 units)
                    </div>
                    <div style="background:#dcfce7; border:1px solid #86efac; padding:0.5rem; border-radius:6px;">
                        <strong>Target Profit Desired:</strong> ₹8,00,000 (1,000 units)
                    </div>
                    <div style="background:#eff6ff; border:2px solid #3b82f6; padding:0.5rem; border-radius:6px; font-weight:bold; color:#1e40af; text-align:center;">
                        Total Required: 4,000 Units (₹80 Lakh Sales)
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 79
    {
        "id": 79,
        "module": "Module 7 · CVP & Break-Even",
        "title": "Margin of Safety (MoS): The Cushion Against Loss",
        "subtitle": "How far sales can collapse before the company bleeds money",
        "badge": "MUST MEMORIZE",
        "badge_type": "primary",
        "content_html": """
            <h3>Margin of Safety (MoS)</h3>
            <p>The Margin of Safety measures the gap between actual (or budgeted) sales and the break-even sales volume:</p>
            <div class="formula-box">
                <div class="formula-name">Margin of Safety (MoS ₹):</div>
                <div class="formula-code">MoS = Actual Sales − Break-Even Sales = Profit / P/V Ratio</div>
            </div>
            <div class="formula-box" style="margin-top:0.4rem;">
                <div class="formula-name">Margin of Safety Percentage (MoS %):</div>
                <div class="formula-code">MoS % = (MoS Sales / Actual Sales) × 100 = Profit / Total Contribution</div>
            </div>
            <div class="callout callout-success" style="margin-top:0.75rem;">
                <strong>Exam Rule:</strong> A high MoS (e.g. 40%) means business sales can plunge by 40% before the company suffers an operating loss!
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Visual Margin of Safety Cushion</h4>
                <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:0.6rem;">
                    <div style="display:flex; justify-content:space-between; font-size:0.8rem; margin-bottom:0.3rem;">
                        <span style="color:#dc2626; font-weight:bold;">BEP: ₹60L (75%)</span>
                        <span style="color:#059669; font-weight:bold;">MoS: ₹20L (25%)</span>
                    </div>
                    <div style="display:flex; height:20px; border-radius:6px; overflow:hidden;">
                        <div style="background:#f87171; width:75%;"></div>
                        <div style="background:#34d399; width:25%;"></div>
                    </div>
                    <div style="text-align:center; font-size:0.75rem; color:#475569; margin-top:0.4rem;">
                        Total Actual Sales = ₹80 Lakhs
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 80
    {
        "id": 80,
        "module": "Module 7 · CVP & Break-Even",
        "title": "ClassicShoes Case Study: Base Parameters",
        "subtitle": "The foundational lecture case tested repeatedly in exams",
        "badge": "WORKED NUMERICAL",
        "badge_type": "primary",
        "content_html": """
            <h3>ClassicShoes Manufacturing: Baseline Model</h3>
            <p>From the speed-run lecture case: ClassicShoes manufactures premium handmade leather footwear:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <tr><th>Parameter</th><th>Value</th><th>Unit</th></tr>
                    <tr><td><strong>Selling Price per Pair (SP)</strong></td><td>₹2,000</td><td>per pair</td></tr>
                    <tr><td><strong>Variable Cost per Pair (VC)</strong></td><td>₹1,200</td><td>per pair</td></tr>
                    <tr><td><strong>Annual Fixed Overheads (FC)</strong></td><td>₹24,00,000</td><td>annual</td></tr>
                    <tr><td><strong>Current Production & Sales</strong></td><td>4,000 pairs</td><td>annual</td></tr>
                </table>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; margin-top:0.5rem; font-size:0.85rem; line-height:1.7;">
                • <strong>Unit Contribution:</strong> 2,000 − 1,200 = <strong>₹800 per pair</strong>.<br>
                • <strong>P/V Ratio:</strong> 800 / 2,000 = <strong>40.0%</strong>.<br>
                • <strong>Break-Even Volume:</strong> 24,00,000 / 800 = <strong>3,000 pairs</strong> (₹60,00,000).<br>
                • <strong>Actual Profit at 4,000 pairs:</strong> (4,000 × 800) − 24,00,000 = <strong>₹8,00,000</strong>.<br>
                • <strong>MoS:</strong> 4,000 − 3,000 = 1,000 pairs = <strong>25.0%</strong>.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">ClassicShoes Base Dashboard</h4>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.4rem; text-align:center; font-size:0.8rem;">
                    <div style="background:#eff6ff; padding:0.5rem; border-radius:6px;">
                        <span style="color:#64748b;">BEP Pairs</span><br>
                        <strong style="font-size:1.1rem; color:#1e40af;">3,000</strong>
                    </div>
                    <div style="background:#ecfdf5; padding:0.5rem; border-radius:6px;">
                        <span style="color:#64748b;">Actual Profit</span><br>
                        <strong style="font-size:1.1rem; color:#065f46;">₹8 Lakh</strong>
                    </div>
                    <div style="background:#fefce8; padding:0.5rem; border-radius:6px;">
                        <span style="color:#64748b;">P/V Ratio</span><br>
                        <strong style="font-size:1.1rem; color:#854d0e;">40%</strong>
                    </div>
                    <div style="background:#faf5ff; padding:0.5rem; border-radius:6px;">
                        <span style="color:#64748b;">Margin of Safety</span><br>
                        <strong style="font-size:1.1rem; color:#6b21a8;">25%</strong>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 81
    {
        "id": 81,
        "module": "Module 7 · CVP & Break-Even",
        "title": "ClassicShoes Price Cut Shock: The 10% Disaster",
        "subtitle": "Why cutting price by 10% spikes break-even volume by +33.3%",
        "badge": "EXAM TRAP",
        "badge_type": "danger",
        "content_html": """
            <h3>The Deadly Impact of Price Cuts</h3>
            <p>ClassicShoes cuts price by 10% to combat competition. Watch the catastrophic arithmetic chain:</p>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.85rem;">
                    <tr><th>Metric</th><th>Before Price Cut</th><th>After 10% Cut</th><th>Change</th></tr>
                    <tr><td>Selling Price (SP)</td><td>₹2,000</td><td>₹1,800</td><td>−10.0%</td></tr>
                    <tr><td>Variable Cost (VC)</td><td>₹1,200</td><td>₹1,200</td><td>0% (Unchanged)</td></tr>
                    <tr><td><strong>Unit Contribution</strong></td><td><strong>₹800</strong></td><td><strong>₹600</strong></td><td><strong style="color:#dc2626;">−25.0%!</strong></td></tr>
                    <tr><td><strong>BEP (Units)</strong></td><td>24L / 800 = <strong>3,000</strong></td><td>24L / 600 = <strong>4,000</strong></td><td><strong style="color:#dc2626;">+33.3%!</strong></td></tr>
                </table>
            </div>
            <div class="callout callout-danger" style="margin-top:0.75rem;">
                <strong>🚨 Crucial Intuition:</strong> Because variable costs are sticky, the entire 10% price reduction hits unit contribution directly! To earn the same ₹8 Lakhs profit, ClassicShoes would now need to sell <strong>5,333 pairs</strong> (+33% volume expansion!).
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Break-Even Surge</h4>
                <div style="background:#fee2e2; border:2px solid #ef4444; border-radius:8px; padding:0.8rem; text-align:center;">
                    <div style="font-size:1.4rem; font-weight:bold; color:#991b1b;">BEP: 3,000 ➔ 4,000 Pairs</div>
                    <div style="font-size:0.85rem; color:#7f1d1d; margin-top:0.3rem;">+1,000 Extra Pairs Just to Break Even!</div>
                    <div style="margin-top:0.6rem; background:#ffffff; border-radius:6px; padding:0.4rem; font-size:0.8rem; color:#b91c1c;">
                        All current 4,000 volume produces ₹0 profit!
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 82
    {
        "id": 82,
        "module": "Module 7 · CVP & Break-Even",
        "title": "Multi-Product CVP & Sales Mix: Cloud Kitchen Case",
        "subtitle": "Weighted average P/V ratio across different margin menu items",
        "badge": "MULTI-PRODUCT",
        "badge_type": "primary",
        "content_html": """
            <h3>Multi-Product Break-Even Analysis</h3>
            <p>Real businesses sell multiple products with different profit margins. We compute a <strong>Weighted Average P/V Ratio</strong> based on sales mix:</p>
            <div class="formula-box">
                <div class="formula-name">Weighted Average P/V Ratio:</div>
                <div class="formula-code">Weighted P/V = Σ (P/V Ratio of Product i × Sales Mix Weight of Product i)</div>
            </div>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.8rem;">
                    <tr><th>Menu Item</th><th>Sales Mix %</th><th>P/V Ratio</th><th>Weighted Contribution</th></tr>
                    <tr><td>Burgers</td><td>50%</td><td>30%</td><td>0.50 × 0.30 = 0.150 (15.0%)</td></tr>
                    <tr><td>Beverages & Fries</td><td>50%</td><td>70%</td><td>0.50 × 0.70 = 0.350 (35.0%)</td></tr>
                    <tr><td><strong>Blended Total</strong></td><td><strong>100%</strong></td><td>—</td><td><strong>Weighted P/V = 50.0%</strong></td></tr>
                </table>
            </div>
            <p style="font-size:0.85rem; margin-top:0.5rem;">
                If Fixed Costs are ₹10 Lakhs, Total Break-Even Sales = 10,00,000 / 0.50 = <strong>₹20 Lakhs</strong>.
            </p>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Sales Mix Shift Trap</h4>
                <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px; padding:0.6rem; font-size:0.8rem;">
                    <strong>If beverage sales drop from 50% to 20%:</strong><br>
                    • Blended P/V collapses from 50% to 38%<br>
                    • Break-even sales spike from ₹20L to ₹26.3L!<br>
                    <span style="color:#dc2626; font-weight:bold;">Total revenue can stay flat while profits plunge!</span>
                </div>
            </div>
        """
    },

    # SLIDE 83
    {
        "id": 83,
        "module": "Module 8 · Time Value of Money",
        "title": "Time Value of Money (TVM): Why Cash Has Time Bias",
        "subtitle": "The three fundamental drivers of time preference",
        "badge": "TVM FOUNDATION",
        "badge_type": "primary",
        "content_html": """
            <h3>Why ₹1 Today is Worth More than ₹1 Tomorrow</h3>
            <p>The entire universe of corporate finance, valuation, and capital budgeting is built on the principle that money has time value:</p>
            <div style="display:flex; flex-direction:column; gap:0.5rem; margin-top:0.75rem; font-size:0.85rem;">
                <div style="background:#f8fafc; border-left:4px solid #3b82f6; padding:0.5rem;">
                    <strong>1. Reinvestment Opportunity:</strong> ₹1 today can be invested in a bank deposit or govt bond to earn interest, yielding more than ₹1 in future.
                </div>
                <div style="background:#f8fafc; border-left:4px solid #ef4444; padding:0.5rem;">
                    <strong>2. Inflation Risk:</strong> General price inflation erodes purchasing power over time. ₹100 buys fewer goods next year than today.
                </div>
                <div style="background:#f8fafc; border-left:4px solid #f59e0b; padding:0.5rem;">
                    <strong>3. Uncertainty & Default Risk:</strong> The future is uncertain. A promised rupee tomorrow carries credit risk and counterparty default risk.
                </div>
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">The Time Preference Bridge</h4>
                <div style="display:flex; justify-content:space-around; align-items:center; text-align:center; padding:1rem 0;">
                    <div style="background:#ecfdf5; border:2px solid #10b981; border-radius:8px; padding:0.75rem; width:40%;">
                        <div style="font-size:1.6rem;">💵</div>
                        <div style="font-weight:bold; color:#065f46;">₹1 Today</div>
                        <div style="font-size:0.75rem; color:#047857;">Certain & Investable</div>
                    </div>
                    <div style="font-size:1.2rem; font-weight:bold; color:#3b82f6;">&gt;</div>
                    <div style="background:#fef2f2; border:2px solid #ef4444; border-radius:8px; padding:0.75rem; width:40%;">
                        <div style="font-size:1.6rem;">⏳</div>
                        <div style="font-weight:bold; color:#991b1b;">₹1 in 1 Year</div>
                        <div style="font-size:0.75rem; color:#7f1d1d;">Uncertain & Eroded</div>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 84
    {
        "id": 84,
        "module": "Module 8 · Time Value of Money",
        "title": "Compounding & Future Value (FV): Forward Motion",
        "subtitle": "Earning interest on interest over multi-year horizons",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Future Value (Compounding)</h3>
            <p>Compounding moves money FORWARD in time by reinvesting interest earned:</p>
            <div class="formula-box">
                <div class="formula-name">Future Value Formula:</div>
                <div class="formula-code">FV = PV × (1 + r)^n</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>PV:</strong> Present Value (Principal amount invested today).</li>
                <li><strong>r:</strong> Interest / discount rate per period.</li>
                <li><strong>n:</strong> Number of compounding periods.</li>
                <li><strong>Intra-Year Compounding:</strong> If compounded semi-annually (twice a year): rate becomes <code>r / 2</code> and periods become <code>n × 2</code>. Compounding more frequently increases FV!</li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Single Cash Flow Compounding</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.85rem; line-height:1.7;">
                    <div>• <strong>Invest:</strong> ₹10,000 today @ 10% for 3 years</div>
                    <div style="margin-top:0.4rem; padding-top:0.4rem; border-top:1px dashed #cbd5e1;">
                        Year 1: 10,000 × 1.10 = ₹11,000<br>
                        Year 2: 11,000 × 1.10 = ₹12,100<br>
                        Year 3: 12,100 × 1.10 = <strong>₹13,310</strong>
                    </div>
                    <div style="font-weight:bold; color:#1e40af; margin-top:0.3rem;">
                        FV = 10,000 × (1.10)³ = ₹13,310
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 85
    {
        "id": 85,
        "module": "Module 8 · Time Value of Money",
        "title": "Discounting & Present Value (PV): Backward Motion",
        "subtitle": "Bringing future cash flows back to today's purchasing power",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>Present Value (Discounting)</h3>
            <p>Discounting is the exact mathematical inverse of compounding, moving money BACKWARD to time zero:</p>
            <div class="formula-box">
                <div class="formula-name">Present Value Formula:</div>
                <div class="formula-code">PV = FV / (1 + r)^n = FV × PVIF(r, n)</div>
            </div>
            <ul style="margin-left:1.5rem; line-height:1.6; font-size:0.85rem; margin-top:0.5rem;">
                <li><strong>PV Factor / Discount Factor:</strong> <code>1 / (1 + r)^n</code>. Always less than 1.0 for positive interest rates!</li>
                <li><strong>Crucial Exam Behavior:</strong>
                    <br>• As discount rate <code>r</code> rises, PV <strong>falls</strong>.
                    <br>• As time horizon <code>n</code> lengthens, PV <strong>falls</strong>.
                </li>
            </ul>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Discount Factor Decay</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:0.6rem; font-size:0.8rem; line-height:1.7;">
                    <div>Present value of ₹1,000 received at 10% interest:</div>
                    <div style="display:flex; justify-content:space-between; margin-top:0.4rem;">
                        <span>In 1 Year:</span>
                        <strong style="color:#1e40af;">₹909 (Factor 0.909)</strong>
                    </div>
                    <div style="display:flex; justify-content:space-between;">
                        <span>In 2 Years:</span>
                        <strong style="color:#1e40af;">₹826 (Factor 0.826)</strong>
                    </div>
                    <div style="display:flex; justify-content:space-between;">
                        <span>In 3 Years:</span>
                        <strong style="color:#1e40af;">₹751 (Factor 0.751)</strong>
                    </div>
                </div>
            </div>
        """
    },

    # SLIDE 86
    {
        "id": 86,
        "module": "Module 8 · Time Value of Money",
        "title": "The Rule of 72: Instant Mental Math for Doubling",
        "subtitle": "How to double your money without touching a calculator",
        "badge": "FORMULA GIVEN",
        "badge_type": "info",
        "content_html": """
            <h3>The Famous Rule of 72</h3>
            <p>A fast, accurate mental approximation to calculate how many years it takes for an investment to double at compound interest:</p>
            <div class="formula-box">
                <div class="formula-name">Rule of 72 Formula:</div>
                <div class="formula-code">Years to Double ≈ 72 / Annual Interest Rate (%)</div>
            </div>
            <div class="table-responsive" style="margin-top:0.5rem;">
                <table class="data-table" style="font-size:0.8rem;">
                    <tr><th>Interest Rate (r%)</th><th>Calculation</th><th>Years to Double Money</th></tr>
                    <tr><td>6.0% p.a.</td><td>72 / 6</td><td><strong>12.0 Years</strong></td></tr>
                    <tr><td>8.0% p.a.</td><td>72 / 8</td><td><strong>9.0 Years</strong></td></tr>
                    <tr><td>9.0% p.a.</td><td>72 / 9</td><td><strong>8.0 Years</strong></td></tr>
                    <tr><td>12.0% p.a.</td><td>72 / 12</td><td><strong>6.0 Years</strong></td></tr>
                    <tr><td>18.0% p.a.</td><td>72 / 18</td><td><strong>4.0 Years</strong></td></tr>
                </table>
            </div>
            <div class="callout callout-info" style="margin-top:0.5rem;">
                <strong>Exam Tip:</strong> Do NOT convert percentage to decimal in the denominator! Use whole number 8 for 8%, not 0.08.
            </div>
        """,
        "visual_html": """
            <div class="visual-card">
                <h4 style="text-align:center; color:var(--secondary); margin-bottom:0.75rem;">Doubling Speedometer</h4>
                <div style="background:#eff6ff; border:1px solid #93c5fd; border-radius:8px; padding:0.8rem; text-align:center;">
                    <div style="font-size:1.8rem; font-weight:bold; color:#1e40af;">72 ÷ 12% = 6 Yrs</div>
                    <div style="font-size:0.8rem; color:#1e3a8a; margin-top:0.4rem;">
                        At 12% returns, ₹1 Lakh becomes ₹2 Lakhs in 6 years, and ₹4 Lakhs in 12 years!
                    </div>
                </div>
            </div>
        """
    }
]

print(f"Loaded {len(slides_71_to_86)} slides in Part 3-A.")
